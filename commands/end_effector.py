from wpilib.command import InstantCommand, Scheduler
import commands.lights, wpilib



class Toggle(InstantCommand):

    def __init__(self):
        super().__init__("Toggle")
        self.requires(self.getRobot().end_effector)

    def initialize(self):
        pass

    def execute(self):
        self.getRobot().end_effector.set(not self.getRobot().end_effector.get())
        Scheduler.getInstance().add(commands.lights.FlashColor("green", .2))
