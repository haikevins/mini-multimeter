# Contributing to Mini Multimeter

Thank you for taking the time to improve `mini-multimeter`.

`mini-multimeter` is an educational embedded-firmware project for the STM32F103C8T6. Contributions should preserve the distinction between implemented firmware behavior, documented validation results, and future ideas. Do not claim hardware validation, measurement accuracy, or toolchain results that were not actually verified.

## Before you start

- Read the project overview in `README.md` and the technical documentation under `docs/`.
- Read `ARCHITECTURE.md` before changing module boundaries, ownership, runtime flow, or dependency direction.
- Keep changes focused. Avoid mixing firmware behavior changes, documentation cleanup, build-system changes, and unrelated refactors in one pull request.
- Do not commit generated Keil output from `MDK/Objects/` or `MDK/Listings/`.
- Preserve the existing layered boundaries unless a change explicitly proposes and justifies a different design.

## Build and validation

The checked project configuration is:

```text
MDK/mini-multimeter.uvprojx
```

The reference firmware build uses Keil µVision with Arm Compiler 6.

For changes that affect firmware code, drivers, startup, interrupt behavior, Flash persistence, timers, ADC behavior, GPIO, or board-facing logic:

1. build the affected firmware configuration cleanly;
2. report the actual compiler result;
3. perform the relevant target or hardware validation;
4. document any limitation that was not exercised.

A successful host-side check or documentation review is not a substitute for physical STM32 validation when hardware-facing behavior changes.

For documentation-only changes, at minimum run:

```bash
git diff --check
```

If documentation changes build commands, measurement claims, supported ranges, release instructions, memory layout, or hardware behavior, verify those statements against the current project before submitting.

## Release artifacts

Release images are derived from the linked AXF using:

```bash
python3 scripts/release/package_firmware.py \
  --axf MDK/Objects/mini-multimeter.axf \
  --version <version> \
  --output-dir <output-directory>
```

The script packages only STM32 Flash-addressed loadable segments and generates:

```text
mini-multimeter-<version>.hex
mini-multimeter-<version>.bin
SHA256SUMS
```

Do not commit generated release images into the source tree unless the repository policy changes explicitly.

## Change expectations

A good change should:

- compile cleanly under the validation path it affects;
- avoid suppressing warnings without justification;
- preserve runtime, interrupt, state-machine, and ownership invariants;
- update documentation when public behavior, hardware assumptions, configuration, or limitations change;
- keep measured project validation separate from calibrated-instrument claims;
- avoid unrelated generated files and editor or IDE user-state files.

## Commit and pull request style

Use concise commit subjects with a clear area, for example:

```text
fix(measurement): reject invalid resistance samples
feat(driver): add timer capture guard
docs: clarify capacitance validation limits
build(keil): update release output configuration
```

A pull request should explain:

1. what changed and why;
2. which firmware or documentation area is affected;
3. which build or validation steps were actually run;
4. whether physical hardware was exercised;
5. any known limitations or follow-up work.

## Firmware and hardware claims

This project is a learning and portfolio project, not a calibrated laboratory instrument.

Do not present project validation results as guaranteed metrology specifications. If a contribution changes measurement behavior, document the test setup, tested range, observed error, and relevant hardware conditions.

## Reporting security issues

Do not publish exploit details, sensitive device information, secrets, or proof-of-concept material for a suspected security issue in a public issue.

Follow `SECURITY.md` instead.
