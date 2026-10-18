# Validation and Limitations

Recorded project-level validation results together with the current limitations and explicitly identified future improvements.

## Validation Results

The following tables are the measurement results documented for this project. They represent the project validation data, not a calibrated metrology specification.

### Frequency measurement

| Test input | Measured result | Documented error |
|---:|---:|---:|
| 100 Hz | 99 – 101 Hz | < 1% |
| 500 Hz | 496 – 504 Hz | < 1% |
| 1 kHz | 0.99 – 1.01 kHz | < 1% |
| 5 kHz | 4.95 – 5.05 kHz | < 1% |
| 10 kHz | 9.9 – 10.1 kHz | < 1% |
| 20 kHz | 19.8 – 20.2 kHz | < 1% |
| 50 kHz | 49.5 – 50.5 kHz | < 1% |
| 100 kHz | 99 – 101 kHz | < 1% |

### Duty-cycle measurement

| Test input | Measured result | Documented error |
|---:|---:|---:|
| 10% | 9.9 – 10.1% | < 1% |
| 20% | 19.8 – 20.2% | < 1% |
| 30% | 29.7 – 30.3% | < 1% |
| 40% | 39.6 – 40.4% | < 1% |
| 50% | 49.5 – 50.5% | < 1% |
| 60% | 59.4 – 60.6% | < 1% |
| 70% | 69.3 – 70.7% | < 1% |
| 80% | 79.2 – 80.8% | < 1% |
| 90% | 89.1 – 90.9% | < 1% |

### Capacitance measurement

| Test component | Measured result | Documented error |
|---:|---:|---:|
| 100 nF | 90 – 115 nF | ~15% |
| 220 nF | 200 – 250 nF | ~14% |
| 470 nF | 430 – 520 nF | ~11% |
| 1 µF | 0.9 – 1.1 µF | ~10% |
| 2.2 µF | 2.0 – 2.45 µF | ~11% |
| 4.7 µF | 4.3 – 5.2 µF | ~11% |
| 10 µF | 9.5 – 10.8 µF | ~8% |
| 22 µF | 20 – 25 µF | ~13% |
| 47 µF | 43 – 52 µF | ~11% |
| 100 µF | 95 – 110 µF | ~10% |
| 220 µF | 205 – 245 µF | ~11% |
| 470 µF | 440 – 520 µF | ~11% |
| 1000 µF | 930 – 1120 µF | ~12% |

### Resistance measurement

| Test component | Measured result | Documented error |
|---:|---:|---:|
| 100 Ω | 96 – 104 Ω | ~4% |
| 220 Ω | 213 – 228 Ω | ~3% |
| 330 Ω | 320 – 342 Ω | ~3% |
| 470 Ω | 455 – 488 Ω | ~4% |
| 1 kΩ | 0.98 – 1.02 kΩ | ~2% |
| 2.2 kΩ | 2.15 – 2.25 kΩ | ~2% |
| 4.7 kΩ | 4.58 – 4.82 kΩ | ~3% |
| 10 kΩ | 9.8 – 10.3 kΩ | ~3% |
| 22 kΩ | 21.3 – 22.8 kΩ | ~4% |
| 47 kΩ | 45.5 – 49.0 kΩ | ~4% |
| 100 kΩ | 96 – 105 kΩ | ~5% |
| 220 kΩ | 210 – 235 kΩ | ~7% |
| 470 kΩ | 445 – 510 kΩ | ~8% |
| 1 MΩ | 0.92 – 1.10 MΩ | ~10% |

---


## Limitations and Future Improvements

### Current limitations

- Resistance accuracy depends on Vcc/Vref accuracy, reference-resistor tolerance, contact resistance, and ADC noise.
- The resistor network has no hardware auto-ranging.
- Very large resistances become electrically close to an open socket and can intentionally be classified as `No Resistor`.
- Capacitance accuracy depends on the 20 kΩ timing resistor, ADC thresholds, GPIO behavior, and the 1 ms SysTick timing resolution.
- Very small capacitors may cross the timing window too quickly and be classified as `No Capacitor`.
- PWM capture range is chosen from an expected frequency, not automatically discovered from an arbitrary external input.
- PWM output search is designed to find an acceptable `<1%` frequency solution, not exhaustively optimize every possible PSC/ARR pair.
- LCD1602 is limited to two 16-character rows.
- Configuration uses one Flash page; corruption is detected but there is no redundant power-fail-safe copy.
- UART RX collects input until `!`, but no application command protocol is currently built on top of that buffer.
- The project is intended for learning and embedded development, not calibrated laboratory measurement.

### Good next improvements

- Hardware resistance auto-ranging.
- Multiple capacitor timing resistors / auto-ranging.
- Calibrated Vref or measured supply compensation.
- Per-range calibration coefficients stored in Flash.
- Automatic PWM input range discovery.
- DMA-based ADC acquisition for experiments with higher sample throughput.
- Dual-slot or journaled Flash configuration for stronger power-fail recovery.
- Structured UART command/telemetry protocol.
- Host-side logging and plotting utility.
- Automated hardware-in-the-loop tests for PWM loopback, buttons, LCD, ADC thresholds, and Flash recovery.
- Dedicated schematic/PCB documentation tied directly to the firmware pin map.

---
