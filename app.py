# coding: utf-8

import keyboard
import time

keyboard.add_hotkey('1', lambda: keyboard.write('foobar'))

duration = 10   # 10 min
time.sleep(duration * 60)
