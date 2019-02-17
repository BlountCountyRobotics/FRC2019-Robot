from wpilib.command import TimedCommand
from wpilib.command import Command
import robot
import robot_map

class SetColor(Command):
    def __init__(self, color):
        super().__init__("SetColor")
        self.requires(self.getRobot().blinkin)
        self.color = color

    def initialize(self):
        pass

    def execute(self):
        self.getRobot().blinkin.set(robot_map.blinkin[self.color])


class FlashColor(TimedCommand):
    def __init__(self, color, timeout):
        super().__init__("SetColor", timeout)
        self.requires(self.getRobot().blinkin)
        self.color = color

    def initialize(self):
        pass

    def execute(self):
        self.getRobot().blinkin.set(robot_map.blinkin[self.color])
