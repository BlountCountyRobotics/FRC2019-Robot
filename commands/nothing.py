import wpilib
from wpilib.command import Command

class Nothing(Command):

    def __init__(self, subsystem):
        super().__init__("Nothing")
        self.requires(subsystem)

    def initialize(self):
        pass

    def execute(self):
        pass
