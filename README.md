# Python Input Library

A library for simulating mouse and keyboard usage in python using pynput

## Installation

Use [pip](https://pip.pypa.io/en/stable/) to install the needed packages

```bash
pip install pynput
```

## Usage

1. Download the files
2. Drop in the files for the part of the lib you want to use
3. Import the files like this
```python
import Mouse
import Keyboard
```

## Functions

### Mouse
* __Mouse.GetPos()__ returns the current mouse position
* __Mouse.SetPos(int x, int y)__ sets mouse position to position given
* __Mouse.Move(int x, int y)__ moved the mouse relative to the current position
* __Mouse.Scroll(int x, int y)__ scrolls the mouse relative to current position
* __Mouse.LeftClick()__ clicks the left mouse button
* __Mouse.LeftMultiClick(int clicks)__ clicks the left mouse button for the specified clicks
* __Mouse.LeftPress()__ presses down the left mouse button
* __Mouse.LeftRelease()__ releases the left mouse button
* __Mouse.RightClick()__ clicks the right mouse button
* __Mouse.RightMultiClick(int clicks)__ clicks the right mouse button for the specified clicks
* __Mouse.RightPress()__ presses down the right mouse button
* __Mouse.RightRelease()__ releases the right mouse button
* __Mouse.MiddleClick()__ clicks the middle mouse button
* __Mouse.MiddleMultiClick(int clicks)__ clicks the middle mouse button for the specified clicks
* __Mouse.MiddlePress()__ presses down the middle mouse button
* __Mouse.MiddleRelease()__ releases the middle mouse button

### Keyboard
#### Keycodes for other keys like space can be found [here](https://pynput.readthedocs.io/en/latest/keyboard.html#pynput.keyboard.Key)
* __Keyboard.Press(string key)__ presses down the passed in key
* __Keyboard.Release(string key)__ releases the passed in key
* __Keyboard.Click(string key)__ clicks the passed in key
* __Keyboard.Type(string text)__ types the text that you pass in

## Contributions
Please feel free to make a pull request if you wish to try to improve the Library