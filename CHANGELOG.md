# Changelog

All notable changes to Mini Multimeter are documented in this file.

The project follows semantic versioning for stable releases. Earlier development history remains available in Git; `v1.0.0` is the first formal release milestone.

## [1.0.0] - 2026-10-18

### Added

- Bare-metal STM32F103C8T6 firmware for resistance and capacitance measurement.
- PWM frequency and duty-cycle capture using timer input capture.
- Programmable PWM generation from 1 Hz to 100 kHz.
- LCD1602 user interface with non-blocking state-machine workflows.
- Layered `Application -> Services -> Drivers -> Infrastructure -> Platform` architecture.
- Versioned internal-Flash settings with CRC-32 validation and read-back verification.
- USART1 diagnostics and centralized runtime error history.
- Focused technical documentation for hardware, measurement, runtime behavior, validation, and build/flash workflow.
- Reproducible release packaging for flash-only Intel HEX and raw BIN images.

### Validation

- Frequency measurement documented from 100 Hz to 100 kHz with less than 1% error.
- Duty-cycle measurement documented from 10% to 90% with less than 1% error.
- Resistance and capacitance paths include hardware validation tables and documented project limitations.
- Checked build reports 0 errors and 0 warnings with an approximately 30.5 KB Flash image.

### Release artifacts

- `mini-multimeter-v1.0.0.hex` — Intel HEX image for STM32 Flash.
- `mini-multimeter-v1.0.0.bin` — raw Flash image, base address `0x08000000`.
- `SHA256SUMS` — SHA-256 checksums for both firmware images.

See [docs/releases/v1.0.0.md](docs/releases/v1.0.0.md) for release notes and verification details.
