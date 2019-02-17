import wpilib
from wpilib.command import Command
from wpilib.command import InstantCommand
import commands.color

class Toggle(InstantCommand):

    def __init__(self):
        super().__init__("Toggle")
        self.requires(self.getRobot().ramp)

    def initialize(self):
        pass

    def execute(self):
        self.getRobot().ramp.set(not self.getRobot().ramp.get())
        self.getRobot().blinkin.setCurrentCommand(commands.color.SetColor("bluechase"))
