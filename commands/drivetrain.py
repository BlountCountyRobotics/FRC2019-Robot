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
