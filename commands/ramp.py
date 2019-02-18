from wpilib.command import InstantCommand, Scheduler, Command
import commands.lights, wpilib


#toggle the ramp state
class Toggle(InstantCommand):
    def __init__(self):
        super().__init__("Toggle")
        self.requires(self.getRobot().ramp)

    def initialize(self):
        pass

    def execute(self):
        #toggle state
        self.getRobot().ramp.set(not self.getRobot().ramp.get())

        #change the color of the blinkins to a "chase" pattern
        Scheduler.getInstance().add(commands.lights.SetColor("bluechase"))
