import wpilib
from wpilib.command import Command
from wpilib.command import InstantCommand

class Nothing(Command):

    def __init__(self):
        super().__init__("Nothing")
        self.requires(self.getRobot().end_effector)

    def initialize(self):
        pass

    def execute(self):
        pass


class Toggle(InstantCommand):

    def __init__(self):
        super().__init__("Toggle")
        self.requires(self.getRobot().end_effector)

    def initialize(self):
        pass

    def execute(self):
        self.getRobot().end_effector.set(not self.getRobot().end_effector.get())