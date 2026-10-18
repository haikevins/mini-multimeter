# Build, Flash, and Repository Guide

Toolchain, build and flashing workflow, current footprint, repository layout, important entry points, and primary references.

## Build, Flash, and Project Footprint

### Toolchain represented by the checked-in build

The repository contains a Keil µVision project at:

```text
MDK/mini-multimeter.uvprojx
```

The current checked-in build log records:

```text
ARM.CMSIS pack             6.3.0
CMSIS Core component       6.2.0
Keil STM32F1xx DFP         2.4.1
STM32F1 StdPeriph drivers  3.6.0
Compiler project mode      Arm Compiler 6
Target device              STM32F103C8
```

### Build

1. Open `MDK/mini-multimeter.uvprojx` in Keil µVision.
2. Verify the target device is `STM32F103C8`.
3. Verify the project include path contains:

```text
..\Application
..\Services
..\Drivers
..\Infrastructure
..\Platform
```

4. Build or **Rebuild all target files**.
5. Check that the linker still reserves the final 1 KB Flash page for configuration.

### Flash and run

1. Connect ST-Link to the STM32 board.
2. Build the firmware.
3. Program the target from µVision.
4. Reset the MCU.
5. Verify:
   - LCD backpack is discovered.
   - The 2-second splash appears.
   - Main menu follows.
   - UART boot log appears if a serial terminal is connected at 9600 8-N-1.

### Current build footprint

The checked-in build log reports:

```text
Code     = 28882 bytes
RO-data  = 1454 bytes
RW-data  = 164 bytes
ZI-data  = 2204 bytes

Total RO size             = 30336 bytes
Total RW size             = 2368 bytes
Total ROM size            = 30500 bytes
Build result              = 0 errors, 0 warnings
```

The application link region is `0xFC00` bytes rather than the full 64 KB because the last 1 KB is reserved for persistent settings.

---


## Repository Structure

```text
mini-multimeter/
├── Application/
│   ├── main.c
│   ├── app_controller.c/.h
│   ├── ui_controller.c/.h
│   ├── ui_view.c/.h
│   └── ui_formatter.c/.h
│
├── Services/
│   ├── config_service.c/.h
│   ├── measurement_service.c/.h
│   └── signal_generator_service.c/.h
│
├── Drivers/
│   ├── adc_driver.c/.h
│   ├── button_driver.c/.h
│   ├── capacitor_charge_driver.c/.h
│   ├── flash_storage_driver.c/.h
│   ├── lcd1602_driver.c/.h
│   ├── pwm_capture_driver.c/.h
│   └── pwm_output_driver.c/.h
│
├── Infrastructure/
│   ├── debug_logger.c/.h
│   └── error_manager.c/.h
│
├── Platform/
│   ├── platform_init.c/.h
│   ├── system_time.c/.h
│   └── uart_port.c/.h
│
├── Demo/
│   └── demo.mp4
│
├── MDK/
│   ├── mini-multimeter.uvprojx
│   ├── RTE/
│   ├── Objects/
│   └── Listings/
│
├── ARCHITECTURE.md
├── LICENSE
└── README.md
```

### Important entry points

| File | Why it matters |
|---|---|
| `Application/main.c` | Minimal firmware entry point |
| `Application/app_controller.c` | Initialization order and super-loop orchestration |
| `Application/ui_controller.c` | Main menu/UI FSM and per-state resource requests |
| `Services/measurement_service.c` | Core R/C/frequency/duty algorithms and measurement statuses |
| `Services/signal_generator_service.c` | PWM PSC/ARR/CCR calculation |
| `Drivers/adc_driver.c` | Interrupt-driven ADC batching |
| `Drivers/pwm_capture_driver.c` | Multi-timer PWM input capture |
| `Drivers/flash_storage_driver.c` | Versioned/CRC Flash persistence |
| `Infrastructure/error_manager.c` | Error history/coalescing |
| `ARCHITECTURE.md` | Additional architecture notes and old-to-new module mapping |

---


## References

The firmware behavior and peripheral configuration are best understood together with the original vendor documentation:

- [STMicroelectronics — STM32F103 documentation](https://www.st.com/en/microcontrollers-microprocessors/stm32f103/documentation.html)
- [STMicroelectronics — RM0008: STM32F101xx/102xx/103xx/105xx/107xx Reference Manual](https://www.st.com/resource/en/reference_manual/cd00171190-stm32f101xx-stm32f102xx-stm32f103xx-advanced-arm-based-32-bit-mcus-stmicroelectronics.pdf)
- [STMicroelectronics — STM32F1 Series Documentation](https://www.st.com/en/microcontrollers-microprocessors/stm32f1-series/documentation.html)
- [Arm — CMSIS documentation](https://arm-software.github.io/CMSIS_6/latest/General/index.html)
- [Keil — µVision documentation](https://www.keil.com/support/man/docs/uv4/)

The checked-in Keil project additionally records the exact CMSIS/STM32F1 pack versions used by the current build in `MDK/Objects/mini-multimeter.build_log.htm`.

---
