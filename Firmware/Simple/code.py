print("Starting")

import board
import supervisor
import board
import digitalio
import storage
import usb_cdc
import usb_hid

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

from kmk.modules.layers import Layers

from kmk.extensions.media_keys import MediaKeys


keyboard = KMKKeyboard()

keyboard.modules.append(Layers())

keyboard.extensions.append(MediaKeys())

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

LOWER = KC.MO(1)
RAISE = KC.MO(2)

# Cols
keyboard.col_pins = (board.GP27, board.GP10, board.GP20, board.GP19, board.GP18, board.GP17, board.GP16, board.GP15, board.GP14, board.GP13, board.GP12, board.GP11)
# Rows
keyboard.row_pins = (board.GP0, board.GP1, board.GP28, board.GP26)
# Diode Direction
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Keymap
keyboard.keymap = [
    [  #QWERTY
        KC.ESC,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.BSPC,
        KC.TAB,  KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.LBRC,
        KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.UP,   KC.ENT ,
        KC.LCTL, KC.LGUI, KC.RALT, KC.TO(3),LOWER,   KC.SPC,  KC.SPC,  RAISE,   KC.SLSH, KC.LEFT, KC.DOWN, KC.RGHT
    ],
    [  #LOWER
        KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.DEL,
        KC.CAPS, KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.EQL, KC.UNDS,  KC.QUOT, KC.BSLS, KC.RBRC,
        KC.LSFT, KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,  KC.NUHS, KC.NUBS, KC.PGUP, KC.PGDN, _______,
        KC.PSCR, XXXXXXX, KC.LALT, _______, _______, _______, _______, _______, _______, XXXXXXX, XXXXXXX, XXXXXXX
    ],
    [  #RAISE
        KC.TILD, KC.EXLM, KC.AT,   KC.HASH, KC.DLR,  KC.PERC, KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN, KC.BSPC,
        KC.CAPS, KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.MINS, KC.PLUS, KC.LCBR, KC.RCBR, KC.PIPE,
        KC.LSFT, KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,  _______, KC.HOME, KC.END,  KC.VOLU, _______,
        _______, _______, KC.RALT, _______, _______, _______, _______, _______, KC.MUTE, KC.MNXT, KC.VOLD, KC.MPLY
    ],
    [  #NUM
        KC.ESC,  XXXXXXX, KC.UP,   XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.PSCR, KC.P7,  KC.P8,   KC.P9,   KC.SLSH,
        KC.BSPC, KC.LEFT, KC.DOWN, KC.RGHT, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.P4,  KC.P5,   KC.P6,   KC.RBRC,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.P1,  KC.P2,   KC.P3,   KC.ENT ,
        XXXXXXX, XXXXXXX, KC.LALT, KC.TO(0),XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.P0,  KC.DOT,  KC.RCBR, KC.AMPR
    ]
]



if __name__ == '__main__':
    keyboard.go()


