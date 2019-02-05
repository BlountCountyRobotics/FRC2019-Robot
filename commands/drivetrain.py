from wpilib.command import Command
import subsystems
import oi
import robot
import robot_map

class FollowJoystick(Command):

    def __init__(self):
        super().__init__("FollowJoystick")
        self.requires(self.getRobot().drivetrain)

    def initialize(self):
        pass

    def execute(self):
        self.getRobot().drivetrain.followJoystick(oi.controller)
        print("x")
        #if touchpad button is pressed, invert gearing
        if oi.controller.getRawButtonPressed(robot_map.ds4["l_click"]):
            self.getRobot().drivetrain.setGearing(not self.getRobot().drivetrain.getGearing())


class StopDriving(Command):

    def __init__(self):
        super().__init__("StopDriving")
        self.requires(self.getRobot().drivetrain)

    def initialize(self):
        pass

    def execute(self):
        self.getRobot().drivetrain.setSpeed(0.0, 0.0)
