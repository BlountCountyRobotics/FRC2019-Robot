from wpilib.command import Command
import subsystems
import oi
import robot

class FollowJoystick(Command):

    def __init__(self):
        super().__init__("FollowJoystick")
        self.requires(self.getRobot().drivetrain)

    def initialize(self):
        pass

    def execute(self):
        self.getRobot().drivetrain.followJoystick(oi.controller)

        #if touchpad button is pressed, invert gearing
        if oi.controller.getRawButtonPressed("touchpad_button"):
            robot.Melody.subsystems.setGearing(
                not robot.drivetrain.getGearing())

class StopDriving(Command):

    def __init__(self):
        super().__init__("StopDriving")
        self.requires(self.getRobot().drivetrain)

    def initialize(self):
        pass

    def execute(self):
        self.getRobot().drivetrain.setSpeed(0.0, 0.0)
