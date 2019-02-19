from wpilib.command import Command, Scheduler
import robot, robot_map, subsystems, commands.lights

#default command to drive the drivetrain
class FollowJoystick(Command):
    def __init__(self):
        super().__init__("FollowJoystick")
        self.requires(self.getRobot().drivetrain)

    def initialize(self):
        pass

    def execute(self):
        self.getRobot().drivetrain.followJoystick(self.getRobot().controller)

        #if touchpad button is pressed, invert gearing
        if self.getRobot().controller.getRawButtonPressed(robot_map.ds4["l1"]):
            self.getRobot().drivetrain.setGearing(not self.getRobot().drivetrain.getGearing())

            #flash hotpink for .2 seconds when the gearing switches
            Scheduler.getInstance().add(commands.lights.FlashColor("hotpink", .2))

#stop driving but keep feeding the motor 0.0 output
class StopDriving(Command):
    def __init__(self):
        super().__init__("StopDriving")
        self.requires(self.getRobot().drivetrain)

    def initialize(self):
        pass

    def execute(self):
        self.getRobot().drivetrain.setSpeed(0.0, 0.0)
