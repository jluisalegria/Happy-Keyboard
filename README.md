# Happy Keyboard
A 40% (47 keys) ortholinear keyboard using the Raspberry pi Pico and KMK firmware (powered by python). Low cost design, with sandwich case.  
  
No reset button or disconnect is necesary to update the keymap. Only edit the code.py with any text editor, save the changes and that's it.
The code lives on a "flash-drive" space in the Pico. Edit the keymap on the go without DFU or other Devtool.

![Happy Keyboard](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/Photos/keyboard.png)

## Features
- Raspberry Pi Pico. Low cost and high availability.
- 2U space button.
- Dual switch footprint. Support direct solder or Kailh hostswap socket.
- SMD diodes.
- Programmable with [KMK Firmware](https://github.com/KMKfw/kmk_firmware "KMK Firmware"). Require [Circuitpython](https://circuitpython.org/board/vcc_gnd_yd_rp2040/ "Circuitpython") to run.
- Assembly with M3 standoffs and screws. 
- Design with Kicad.

## Part List
- 1x RP2040 in the form of the Raspberry Pi Pico. I select a [version with USB-C](https://es.aliexpress.com/item/1005003371056277.html?spm=a2g0o.order_list.order_list_main.11.2e83194dM0664U&gatewayAdapt=glo2esp "black version with USB C").
- 47x 1N4148 SOD-123
- 47x [Mechanical switches](https://es.aliexpress.com/item/1005002378701948.html?spm=a2g0o.order_list.order_list_main.5.4b24194d63C1ud&gatewayAdapt=glo2esp "brown Outemu switches") (Cherry MX type).
- Keycaps. I select white keycaps with [pink theme](https://es.aliexpress.com/item/1005005120762702.html?spm=a2g0o.order_list.order_list_main.17.2e83194dM0664U&gatewayAdapt=glo2esp "pink theme").
- Optional [Kailh Hotswap sockets](https://es.aliexpress.com/item/4001051840976.html?spm=a2g0o.cart.0.0.76d27a9dWyhGyQ&mp=1&gatewayAdapt=glo2esp "Kailh Hotswap sockets").

## Enclosure
- Aluminium or Acrylic. Bottom: 3 mm. Plate: 1.5 mm.
- 6x M3X8 mm. standoffs.
- 6x M3X6 mm. Screws.
- 6x M3X4 mm. screws.

## Layers
My keyboard language is Spanish. Here my keycode layers.

Pre-programed 4 layers.
Edit the Firmware/[code.py](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Firmware/code.py) as you prefer.

### Layer 0
![L0](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/keycodes/Layer0.png)
### Layer 1
![L1](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/keycodes/Layer1.png)
### Layer 2
![L2](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/keycodes/Layer2.png)
### Layer 3
![L3](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/keycodes/Layer3.png)

## More Photos
![Despliegue](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/Photos/Despliegue.jpg)
![switches](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/Photos/BrownSwitches.jpg)
![Keycaps](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/Photos/KeycapsLetters.jpg)
![USBC](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/Photos/USBC.jpg)
![RP2040](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/Photos/RP2040.jpg)
![FPCB](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/Photos/FrontPCB.jpg)
![BPCB](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/Photos/BackPCB.jpg)

## Make your own [here](https://www.pcbway.com/project/shareproject/Happy_Keyboard_47_keys_Planck_Type_a725bc7f.html).
