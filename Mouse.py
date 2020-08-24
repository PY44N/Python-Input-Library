from pynput.mouse import Button, Controller as MouseController


mouse = MouseController()


def GetPos():
    return mouse.position


def SetPos(x, y):
    mouse.position = (x, y)


# Moves relative to current mouse pos
def Move(x, y):
    mouse.move(x, y)


def LeftClick():
    mouse.click(Button.left, 1)


def LeftMultiClick(clicks):
    mouse.click(Button.left, clicks)


def LeftPress():
    mouse.press(Button.left)


def LeftRelease():
    mouse.release(Button.left)


def RightClick():
    mouse.click(Button.right, 1)


def RightMultiClick(clicks):
    mouse.click(Button.right, clicks)


def RightPress():
    mouse.press(Button.right)


def RightRelease():
    mouse.release(Button.right)


def MiddleClick():
    mouse.click(Button.middle, 1)


def MiddleMultiClick(clicks):
    mouse.click(Button.middle, clicks)


def MiddlePress():
    mouse.press(Button.middle)


def MiddleRelease():
    mouse.release(Button.middle)


def Scroll(x, y):
    mouse.scroll(x, y)
