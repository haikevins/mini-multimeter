# Documentation

This directory contains the detailed technical documentation for Mini Multimeter. The root `README.md` is the portfolio-oriented landing page; the documents here preserve the deeper implementation, validation, and release details.

## Technical guides

- [Architecture](../ARCHITECTURE.md) — layering, dependency rules, runtime flows, UI responsibility split, and persistent settings flow.
- [Hardware and Pin Mapping](hardware.md) — hardware inventory, pin assignments, functional signal paths, and clock assumptions.
- [Measurement and Signal Generation](measurement.md) — resistance, capacitance, PWM capture, sequential measurement, and PWM output algorithms.
- [Runtime, UI, Persistence, and Diagnostics](runtime.md) — boot/runtime behavior, UI state machines, Flash persistence, diagnostics, and design trade-offs.
- [Validation and Limitations](validation.md) — recorded measurement validation, project limitations, and future improvements.
- [Build, Flash, and Repository Guide](build-and-flash.md) — Keil toolchain, build/flash workflow, footprint, repository layout, and references.

## Releases

- [v1.0.0 release notes](releases/v1.0.0.md) — first formal stable release, build evidence, firmware artifacts, checksums, and Ubuntu packaging workflow.
- [Changelog](../CHANGELOG.md) — stable release history.

## Scope

The documentation describes the behavior and validation of the checked-in firmware. Release-preparation changes are kept separate from firmware source changes so published artifacts can be traced back to the existing linked image.
