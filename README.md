# Happy Keyboard
A 40% (47 keys) ortholinear keyboard built around the Raspberry Pi Pico and KMK firmware (powered by Python). A low-cost design with a sandwich case.

No reset button or unplugging is needed to update the keymap. Just edit `code.py` with any text editor, save, and you are done.
The code lives in a "flash drive" partition on the Pico, so you can edit the keymap on the go without DFU or any other dev tool.

![Happy Keyboard](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/Photos/keyboard.png)

## Features
- Raspberry Pi Pico. Low cost and widely available.
- 2U space bar.
- Dual switch footprint. Supports direct soldering or Kailh hotswap sockets.
- SMD diodes.
- Programmable with [KMK Firmware](https://github.com/KMKfw/kmk_firmware "KMK Firmware"). Requires [CircuitPython](https://circuitpython.org/board/vcc_gnd_yd_rp2040/ "CircuitPython") to run.
- Assembled with M3 standoffs and screws.
- Designed in KiCad.

## Part List
- 1x RP2040 in the form of a Raspberry Pi Pico. I chose a [version with USB-C](https://es.aliexpress.com/item/1005003371056277.html?spm=a2g0o.order_list.order_list_main.11.2e83194dM0664U&gatewayAdapt=glo2esp "black version with USB C").
- 47x 1N4148 SOD-123 diodes.
- 47x [mechanical switches](https://es.aliexpress.com/item/1005002378701948.html?spm=a2g0o.order_list.order_list_main.5.4b24194d63C1ud&gatewayAdapt=glo2esp "brown Outemu switches") (Cherry MX type).
- Keycaps. I chose white keycaps with a [pink theme](https://es.aliexpress.com/item/1005005120762702.html?spm=a2g0o.order_list.order_list_main.17.2e83194dM0664U&gatewayAdapt=glo2esp "pink theme").
- Optional: [Kailh hotswap sockets](https://es.aliexpress.com/item/4001051840976.html?spm=a2g0o.cart.0.0.76d27a9dWyhGyQ&mp=1&gatewayAdapt=glo2esp "Kailh Hotswap sockets").

## Enclosure
- Aluminium or acrylic. Bottom: 3 mm. Plate: 1.5 mm.
- 6x M3x8 mm standoffs.
- 6x M3x6 mm screws.
- 6x M3x4 mm screws.

## Layers
My keyboard layout is Spanish. These are my keycode layers.

Four layers come pre-programmed.
Edit Firmware/[code.py](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Firmware/code.py) to suit your needs.

### Layer 0
![L0](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/keycodes/Layer0.png)
### Layer 1
![L1](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/keycodes/Layer1.png)
### Layer 2
![L2](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/keycodes/Layer2.png)
### Layer 3
![L3](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/keycodes/Layer3.png)

## More Photos
![Exploded view](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/Photos/Despliegue.jpg)
![Switches](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/Photos/BrownSwitches.jpg)
![Keycaps](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/Photos/KeycapsLetters.jpg)
![USB-C](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/Photos/USBC.jpg)
![RP2040](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/Photos/RP2040.jpg)
![Front PCB](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/Photos/FrontPCB.jpg)
![Back PCB](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/Photos/BackPCB.jpg)

## Build your own [here](https://www.pcbway.com/project/shareproject/Happy_Keyboard_47_keys_Planck_Type_a725bc7f.html).
