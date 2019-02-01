from wpilib.joystick import Joystick
from wpilib import XboxController
from wpilib.buttons import JoystickButton
from commands.drivetrain import StopDriving
from commands.other import ToggleCompressor
import robot_map

button_board = None
controller = None



def initOI():
    global button_board, controller

    controller = Joystick(0)
    button_board = Joystick(1)

    JoystickButton(controller, robot_map.ds4["options"]).toggleWhenPressed(StopDriving())
    JoystickButton(controller, robot_map.ds4["share"]).whenPressed(ToggleCompressor())
