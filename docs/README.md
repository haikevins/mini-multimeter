# Documentation

This directory contains the detailed technical documentation for Mini Multimeter. The root `README.md` is retained unchanged during the documentation split so the technical content can be reviewed before the portfolio landing page is simplified in a later commit.

## Technical guides

- [Architecture](../ARCHITECTURE.md) — layering, dependency rules, runtime flows, UI responsibility split, and persistent settings flow.
- [Hardware and Pin Mapping](hardware.md) — hardware inventory, pin assignments, functional signal paths, and clock assumptions.
- [Measurement and Signal Generation](measurement.md) — resistance, capacitance, PWM capture, sequential measurement, and PWM output algorithms.
- [Runtime, UI, Persistence, and Diagnostics](runtime.md) — boot/runtime behavior, UI state machines, Flash persistence, diagnostics, and design trade-offs.
- [Validation and Limitations](validation.md) — recorded measurement validation, project limitations, and future improvements.
- [Build, Flash, and Repository Guide](build-and-flash.md) — Keil toolchain, build/flash workflow, footprint, repository layout, and references.

## Scope

This documentation re-organizes material already present in the project README. It does not modify firmware source code, measurement behavior, hardware configuration, or runtime logic.
