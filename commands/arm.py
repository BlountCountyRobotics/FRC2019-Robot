from wpilib.command import InstantCommand, Scheduler
import commands.lights, wpilib

#toggles and drops the arm
class Toggle(InstantCommand):
    def __init__(self):
        super().__init__("Toggle")
        self.requires(self.getRobot().arm)

    def initialize(self):
        pass

    def execute(self):
        self.getRobot().arm.set(not self.getRobot().arm.get())
        Scheduler.getInstance().add(commands.lights.FlashColor("rorange", .2))
