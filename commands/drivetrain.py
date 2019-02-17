from wpilib.command import Command, Scheduler
import commands.lights
import subsystems
import robot
import robot_map


class FollowJoystick(Command):

    def __init__(self):
        super().__init__("FollowJoystick")
        self.requires(self.getRobot().drivetrain)

    def initialize(self):
        pass

    def execute(self):
        self.getRobot().drivetrain.followJoystick(self.getRobot().controller)
        #if touchpad button is pressed, invert gearing
        if self.getRobot().controller.getRawButtonPressed(robot_map.ds4["l_click"]):
            self.getRobot().drivetrain.setGearing(not self.getRobot().drivetrain.getGearing())
            Scheduler.getInstance().add(commands.lights.FlashColor("hotpink", .2))



class StopDriving(Command):

    def __init__(self):
        super().__init__("StopDriving")
        self.requires(self.getRobot().drivetrain)

    def initialize(self):
        pass

    def execute(self):
        self.getRobot().drivetrain.setSpeed(0.0, 0.0)
