from wpilib.command import Command
import subsystems
import oi

class FollowJoystick(Command):

    def __init__(self):
        super().__init__("FollowJoystick")
        self.requires(subsystems.drivetrain)

    def initialize(self):
        pass

    def execute(self):
        subsystems.drivetrain.followJoystick(oi.controller)
        if oi.controller.getPOV() == 0:
            subsystems.drivetrain.setHighGearing()
        if oi.controller.getPOV() == 180:
            subsystems.drivetrain.setLowGearing()
