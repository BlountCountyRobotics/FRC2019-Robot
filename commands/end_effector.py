import wpilib
from wpilib.command import InstantCommand
from wpilib.command import Scheduler
import commands.lights



class Toggle(InstantCommand):

    def __init__(self):
        super().__init__("Toggle")
        self.requires(self.getRobot().end_effector)

    def initialize(self):
        pass

    def execute(self):
        self.getRobot().end_effector.set(not self.getRobot().end_effector.get())
        Scheduler.getInstance().add(commands.lights.FlashColor("green", .2))
