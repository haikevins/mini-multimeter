# Security Policy

## Project scope

`mini-multimeter` is an educational embedded-firmware and portfolio project for the STM32F103C8T6. It is not safety-certified, security-certified, production-qualified, or a calibrated metrology product. No security response SLA is guaranteed.

Security reports are still welcome, especially for issues involving memory safety, unsafe interrupt or peripheral behavior, Flash configuration integrity, release-image integrity, or documentation that could lead users to make incorrect security or safety assumptions.

## Supported code

Security fixes are considered on a best-effort basis for:

- the current `main` branch; and
- the latest published release.

Older snapshots, historical commits, and superseded releases are not maintained as supported security branches unless explicitly stated otherwise.

## Reporting a vulnerability

Please do not disclose exploit details, proof-of-concept code, secrets, or sensitive device information in a public GitHub issue.

Preferred reporting path:

1. Use GitHub private vulnerability reporting or a private security advisory for this repository when available under the **Security** tab.
2. If private reporting is unavailable, open a minimal public issue that contains no vulnerability details and asks the maintainer for a private contact channel.

Include, when possible:

- affected commit or release;
- affected hardware and configuration;
- a concise impact description;
- reproduction conditions without publishing sensitive material;
- whether physical hardware is required to reproduce the issue;
- relevant debugger, fault, register, or Flash-state evidence.

## Security and safety boundaries

This project does not provide or claim:

- secure boot;
- cryptographic firmware authentication;
- hardware isolation or memory protection beyond the target MCU's configured behavior;
- resistance to malicious physical access;
- electrical safety certification;
- calibrated measurement guarantees;
- production security hardening.

A successful build, static check, or host-side tool result does not establish target security, electrical safety, timing safety, or measurement accuracy.

Any claim tied to STM32 behavior should be supported by target-specific evidence rather than inferred from desktop tooling alone.

## Release integrity

Published firmware releases should provide SHA-256 checksums for downloadable firmware images.

Users should verify release artifacts with:

```bash
sha256sum -c SHA256SUMS
```

Report any checksum mismatch, unexpected release asset, or suspected tampering through the private reporting path above.
