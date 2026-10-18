#!/usr/bin/env python3
"""Create flash-only BIN/HEX release images from a Keil/Arm ELF AXF.

The script reads PT_LOAD segments whose *physical* addresses are in the
configured STM32 Flash range, creates a contiguous raw BIN with 0xFF-filled
gaps, converts that BIN to Intel HEX with GNU objcopy, and writes
SHA256SUMS.
"""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import shutil
import struct
import subprocess
import sys

ELF_MAGIC = b"\x7fELF"
ELFCLASS32 = 1
ELFDATA2LSB = 1
EM_ARM = 40
PT_LOAD = 1
DEFAULT_FLASH_START = 0x08000000
DEFAULT_FLASH_END = 0x08100000


def parse_int(value: str) -> int:
    try:
        return int(value, 0)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"invalid integer: {value}") from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Package flash-only STM32 BIN/HEX images from an AXF."
    )
    parser.add_argument("--axf", required=True, type=Path, help="Input AXF/ELF file")
    parser.add_argument("--version", required=True, help="Release version, e.g. 1.0.0")
    parser.add_argument(
        "--output-dir", required=True, type=Path, help="Directory for release assets"
    )
    parser.add_argument(
        "--flash-start",
        type=parse_int,
        default=DEFAULT_FLASH_START,
        help="First accepted Flash physical address (default: 0x08000000)",
    )
    parser.add_argument(
        "--flash-end",
        type=parse_int,
        default=DEFAULT_FLASH_END,
        help="Exclusive Flash physical-address limit (default: 0x08100000)",
    )
    return parser.parse_args()


def flash_segments(axf_path: Path, flash_start: int, flash_end: int):
    data = axf_path.read_bytes()

    if data[:4] != ELF_MAGIC:
        raise ValueError("input is not an ELF file")
    if data[4] != ELFCLASS32 or data[5] != ELFDATA2LSB:
        raise ValueError("expected a 32-bit little-endian ELF")

    machine = struct.unpack_from("<H", data, 18)[0]
    if machine != EM_ARM:
        raise ValueError(f"expected ARM ELF (e_machine={EM_ARM}), got {machine}")

    phoff = struct.unpack_from("<I", data, 28)[0]
    phentsize = struct.unpack_from("<H", data, 42)[0]
    phnum = struct.unpack_from("<H", data, 44)[0]

    segments: list[tuple[int, int, bytes]] = []

    for index in range(phnum):
        off = phoff + index * phentsize
        if off + 32 > len(data):
            raise ValueError("program header extends beyond ELF file")

        (
            p_type,
            p_offset,
            _p_vaddr,
            p_paddr,
            p_filesz,
            _p_memsz,
            _p_flags,
            _p_align,
        ) = struct.unpack_from("<IIIIIIII", data, off)

        if p_type != PT_LOAD or p_filesz == 0:
            continue
        if not (flash_start <= p_paddr < flash_end):
            continue
        if p_paddr + p_filesz > flash_end:
            raise ValueError(
                f"Flash segment 0x{p_paddr:08X}+0x{p_filesz:X} exceeds Flash limit"
            )
        if p_offset + p_filesz > len(data):
            raise ValueError("loadable segment extends beyond ELF file")

        segments.append((p_paddr, p_filesz, data[p_offset : p_offset + p_filesz]))

    if not segments:
        raise ValueError("no loadable Flash segments found")

    return sorted(segments, key=lambda item: item[0])


def build_binary(segments: list[tuple[int, int, bytes]]) -> tuple[int, int, bytes]:
    base = min(address for address, _size, _payload in segments)
    end = max(address + size for address, size, _payload in segments)
    image = bytearray([0xFF]) * (end - base)

    for address, size, payload in segments:
        start = address - base
        stop = start + size
        existing = image[start:stop]
        if any(byte != 0xFF for byte in existing):
            raise ValueError(f"overlapping Flash segments near 0x{address:08X}")
        image[start:stop] = payload

    return base, end, bytes(image)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    args = parse_args()

    if args.flash_start >= args.flash_end:
        print("ERROR: --flash-start must be below --flash-end", file=sys.stderr)
        return 2

    objcopy = shutil.which("arm-none-eabi-objcopy") or shutil.which("objcopy")
    if objcopy is None:
        print("ERROR: arm-none-eabi-objcopy or GNU objcopy is required", file=sys.stderr)
        return 2

    if not args.axf.is_file():
        print(f"ERROR: AXF not found: {args.axf}", file=sys.stderr)
        return 2

    try:
        segments = flash_segments(args.axf, args.flash_start, args.flash_end)
        base, end, image = build_binary(segments)
    except (OSError, ValueError, struct.error) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    output_dir = args.output_dir.expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    stem = f"mini-multimeter-v{args.version}"
    bin_path = output_dir / f"{stem}.bin"
    hex_path = output_dir / f"{stem}.hex"
    sums_path = output_dir / "SHA256SUMS"

    bin_path.write_bytes(image)

    subprocess.run(
        [
            objcopy,
            "-I",
            "binary",
            "-O",
            "ihex",
            "--change-addresses",
            f"0x{base:08X}",
            str(bin_path),
            str(hex_path),
        ],
        check=True,
    )

    entries = [(hex_path, sha256(hex_path)), (bin_path, sha256(bin_path))]
    sums_path.write_text(
        "".join(f"{digest}  {path.name}\n" for path, digest in entries),
        encoding="ascii",
    )

    print(f"Flash base : 0x{base:08X}")
    print(f"Flash end  : 0x{end:08X}")
    print(f"Image size : {len(image)} bytes")
    print(f"BIN        : {bin_path}")
    print(f"HEX        : {hex_path}")
    print(f"SHA256SUMS : {sums_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
