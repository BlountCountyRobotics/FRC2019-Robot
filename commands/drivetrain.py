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

        if oi.controller.getPOV() == 0: #if d-pad is pressed upward, set gearing to high
            subsystems.drivetrain.setHighGearing()
        if oi.controller.getPOV() == 180: #if d-pad is pressed downward, set gearing to low
            subsystems.drivetrain.setLowGearing()
