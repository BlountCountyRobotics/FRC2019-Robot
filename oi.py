from wpilib.joystick import Joystick
from wpilib import XboxController
from wpilib.buttons import JoystickButton


button_board = None
controller = None

def InitOI():
    global button_board, controller

    controller = XboxController(0)
    button_board = Joystick(1)
