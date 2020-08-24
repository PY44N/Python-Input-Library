from pynput.keyboard import Key, Controller


keyboard = Controller()


def Press(key):
    keyboard.press(key)


def Release(key):
    keyboard.release(key)


def Click(key):
    keyboard.press(key)
    keyboard.release(key)


def Type(txt):
    keyboard.type(txt)
