# Thanks to Tirthak for saving my time to code!!!

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.mouse_keys import MouseKeys

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D1, board.D2, board.D3, board.D4)
keyboard.row_pins = (board.D7, board.D8, board.D9)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.modules.append(encoder_handler)

encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.D10, board.D11),)
encoder_handler.map = ((KC.VOLD, KC.VOLU))

KC_SNIP = KC.MACRO_TAP(
    KC.LGUI(KC.LSHIFT(KC.S))
)

keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(MouseKeys())

keyboard.keymap = [

    [
        KC.MPRV,   KC.MPLY,  KC.MNXT, KC.MUTE, 
        KC.LEFT, KC.RIGHT, KC.UP, KC.DOWN,
        KC.BRID,  KC.BRIU, KC.CALCULATOR, KC_SNIP
    ]
]

display = Display(
    display=SSD1306(sda=board.D5, scl=board.D6),
    entries=[
        TextEntry(text='Keybie here!!! Sleep at 11pm lol!!'),
    ],
    height=80,
)
keyboard.extensions.append(display)


if __name__ == '__main__':
    keyboard.go()