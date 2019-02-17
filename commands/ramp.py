import wpilib
from wpilib.command import Command
from wpilib.command import InstantCommand
from wpilib.command import Scheduler
import commands.lights

class Toggle(InstantCommand):

    def __init__(self):
        super().__init__("Toggle")
        self.requires(self.getRobot().ramp)

    def initialize(self):
        pass

    def execute(self):
        self.getRobot().ramp.set(not self.getRobot().ramp.get())
        Scheduler.getInstance().add(commands.lights.SetColor("bluechase"))
