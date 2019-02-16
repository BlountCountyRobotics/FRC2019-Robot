from wpilib.command import InstantCommand
from wpilib.command import Command
import robot
import robot_map

class ToggleCompressor(InstantCommand):

    def __init__(self):
        super().__init__("ToggleCompressor")


    def initialize(self):
        pass

    def execute(self):
        if self.getRobot().compressor.enabled():
            self.getRobot().compressor.stop()
        else:
            self.getRobot().compressor.start()

class StartLeds(Command):

    def __init__(self):
        super().__init__("StartLeds")
        self.requires(self.getRobot().blinkin)

    def initialize(self):
        pass

    def execute(self):
        if self.getRobot().isRamp:
            self.getRobot().blinkin.set(robot_map.blinkin["bluechase"])
        else:
            self.getRobot().blinkin.set(robot_map.blinkin["defaultgradient"])
