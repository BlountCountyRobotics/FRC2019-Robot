from wpilib.command import Command
import subsystems
import oi

class FollowJoystick(Command):

    def __init__(self):
        super().__init__("FollowJoystick")
        self.requires(subsystems.Subsystems.drivetrain)

    def initialize(self):
        pass

    def execute(self):
        subsystems.Subsystems.drivetrain.followJoystick(oi.controller)

        #if touchpad button is pressed, invert gearing
        if oi.controller.getRawButtonPressed("touchpad_button"):
            subsystems.Subsystems.drivetrain.setGearing(
                not subsystems.Subsystems.drivetrain.getGearing())

class StopDriving(Command):

    def __init__(self):
        super().__init__("StopDriving")
        self.requires(subsystems.Subsystems.drivetrain)

    def initialize(self):
        pass

    def execute(self):
        subsystems.Subsystems.drivetrain.setSpeed(0.0, 0.0)
