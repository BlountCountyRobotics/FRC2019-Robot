from wpilib.joystick import Joystick
from wpilib import XboxController
from wpilib.buttons import JoystickButton
from commands.drivetrain import StopDriving
from commands.other import ToggleCompressor


button_board = None
controller = None



def initOI():
    global button_board, controller

    controller = XboxController(0)
    button_board = Joystick(1)

    JoystickButton(controller, XboxController.Button.kStart).toggleWhenPressed(StopDriving())
    JoystickButton(controller, XboxController.Button.kBack).whenPressed(ToggleCompressor())
