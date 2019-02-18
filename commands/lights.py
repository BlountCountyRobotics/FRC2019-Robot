from wpilib.command import TimedCommand, Command
import robot, robot_map

#set the blinkin to an inputted color/pattern
class SetColor(Command):
    def __init__(self, color):
        super().__init__("SetColor")
        self.requires(self.getRobot().blinkin)
        self.color = color

    def initialize(self):
        pass

    def execute(self):
        self.getRobot().blinkin.set(robot_map.blinkin[self.color])

#flash an inputted color/pattern for a designated amount of time
class FlashColor(TimedCommand):
    def __init__(self, color, timeout):
        super().__init__("SetColor", timeout)
        self.requires(self.getRobot().blinkin)
        self.color = color

    def initialize(self):
        pass

    def execute(self):
        self.getRobot().blinkin.set(robot_map.blinkin[self.color])
