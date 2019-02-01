from wpilib.joystick import Joystick
from wpilib import XboxController
from wpilib.buttons import JoystickButton
import commands.drivetrain
import commands.other
import robot_map

button_board = None
controller = None



def initOI():
    global button_board, controller

    controller = Joystick(0)
    button_board = Joystick(1)

    JoystickButton(controller, robot_map.ds4["options"]).toggleWhenPressed(commands.drivetrain.StopDriving())
    JoystickButton(controller, robot_map.ds4["share"]).whenPressed(commands.other.ToggleCompressor())
