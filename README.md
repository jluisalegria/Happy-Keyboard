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
- Optional RGB underglow, driven by a WS2812B strip.
- Assembled with M3 standoffs and screws.
- Designed in KiCad.

## Part List
- 1x RP2040 in the form of a Raspberry Pi Pico. I chose a [version with USB-C](https://es.aliexpress.com/item/1005003371056277.html?spm=a2g0o.order_list.order_list_main.11.2e83194dM0664U&gatewayAdapt=glo2esp "black version with USB C").
- 47x 1N4148 SOD-123 diodes.
- 47x [mechanical switches](https://es.aliexpress.com/item/1005002378701948.html?spm=a2g0o.order_list.order_list_main.5.4b24194d63C1ud&gatewayAdapt=glo2esp "brown Outemu switches") (Cherry MX type).
- Keycaps. I chose white keycaps with a [pink theme](https://es.aliexpress.com/item/1005005120762702.html?spm=a2g0o.order_list.order_list_main.17.2e83194dM0664U&gatewayAdapt=glo2esp "pink theme").
- Optional: 24x WS2812B LEDs (a 5 V addressable strip) for the underglow. See [RGB Lighting](#rgb-lighting).
- Optional: [Kailh hotswap sockets](https://es.aliexpress.com/item/4001051840976.html?spm=a2g0o.cart.0.0.76d27a9dWyhGyQ&mp=1&gatewayAdapt=glo2esp "Kailh Hotswap sockets").

## Enclosure
- Aluminium or acrylic. Bottom: 3 mm. Plate: 1.5 mm.
- 6x M3x8 mm standoffs.
- 6x M3x6 mm screws.
- 6x M3x4 mm screws.

## Firmware
Two variants are included. Pick one and copy the contents of its folder to the
Pico's `CIRCUITPY` drive:

- **[Simple](Firmware/Simple)** - the plain keyboard, no lighting.
- **[With Led](Firmware/With%20Led)** - adds the RGB underglow, with the lighting
  controls mapped to the NUM layer.

Both share the same matrix and the same four layers.

## Layers
My keyboard layout is Spanish. These are my keycode layers.

Four layers come pre-programmed: QWERTY, LOWER, RAISE and NUM. To remap a key,
open `code.py` in any text editor and replace a keycode in the `keyboard.keymap`
matrix. Each row of the matrix is a physical row of the keyboard, read left to
right, so the positions match the images below:

```python
keyboard.keymap = [
    [  #QWERTY
        KC.ESC,  KC.Q,    KC.W,    ...   # top row, starting at the top-left key
```

Save the file and the keyboard reboots with the new keymap. The full list of
keycodes is in the [KMK documentation](https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/keycodes.md "KMK keycodes").

### Layer 0
![L0](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/keycodes/Layer0.png)
### Layer 1
![L1](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/keycodes/Layer1.png)
### Layer 2
![L2](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/keycodes/Layer2.png)
### Layer 3
![L3](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/keycodes/Layer3.png)

## RGB Lighting
The **With Led** firmware drives a chain of **24 addressable LEDs** as underglow.

Use a 5 V **WS2812B** strip (also sold as "NeoPixel"), which is what the
`neopixel` driver behind KMK's RGB extension speaks. A 60 LED/m strip cut to 24
LEDs fits the board.

The strip sticks to the underside of the PCB with its own adhesive backing.
There is no LED connector on the board, so run three jumper wires and solder
them directly to the Pico:

| Strip | Pico |
| --- | --- |
| DIN (data in) | GP23 |
| +5V | VBUS (pin 40) |
| GND | any GND pin |

### How many LEDs can USB power?
A WS2812B draws up to 60 mA at full white, and the Pico itself needs around
50 mA. A USB 2.0 port supplies 500 mA in total, so the strip has roughly 400 mA
to work with once some headroom is left.

What matters is the LED count multiplied by the brightness, not either one
alone. These combinations all land near that 400 mA budget and are safe on any
port:

| LEDs | `val_limit` | Peak draw |
| --- | --- | --- |
| **24** | **64** (25%) | ~360 mA |
| 12 | 128 (50%) | ~360 mA |
| 7 | 255 (100%) | ~420 mA |

The shipped firmware uses the first row - the full 24 LEDs, capped at 25%
brightness. That is bright enough for underglow and leaves the port well inside
spec. `val_limit` is a hard ceiling: the brightness keys on the NUM layer cannot
push past it.

Going above this budget will not damage anything, but the port will current-limit
and the keyboard will disconnect or reboot mid-use. Raise `val_limit` only if you
power the board from something other than the USB host.

Both values live on one line in `code.py`, along with the data pin:

```python
rgb = RGB(pixel_pin=board.GP23, num_pixels=24, val_limit=64, ...)
```

The lighting controls (on/off, hue, saturation, brightness and the animation
modes) live on the NUM layer - see the Layer 3 image above.

## More Photos
![Exploded view](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/Photos/Despliegue.jpg)
![Switches](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/Photos/BrownSwitches.jpg)
![Keycaps](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/Photos/KeycapsLetters.jpg)
![USB-C](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/Photos/USBC.jpg)
![RP2040](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/Photos/RP2040.jpg)
![Front PCB](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/Photos/FrontPCB.jpg)
![Back PCB](https://github.com/jluisalegria/Happy-Keyboard/blob/master/Images/Photos/BackPCB.jpg)

## Build your own [here](https://www.pcbway.com/project/shareproject/Happy_Keyboard_47_keys_Planck_Type_a725bc7f.html).
