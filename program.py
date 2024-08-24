# https://www.instructables.com/DIY-Macro-Keyboard-Using-a-Raspberry-PI-Pico/ helped a lot
# https://github.com/adafruit/Adafruit_CircuitPython_HID
# https://circuitpython.org/board/raspberry_pi_pico_w/

import board, digitalio, time, usb_hid, .private
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS


keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

button = digitalio.DigitalInOut(board.GP14)
button.switch_to_input(pull=digitalio.Pull.DOWN)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    if button.value:
        layout.write(private.ENTRY_STRING)
    time.sleep(0.1)
