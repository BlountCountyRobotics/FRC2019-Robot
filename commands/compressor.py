from wpilib.command import InstantCommand, Command
import robot, robot_map

#toggle the compressor state
class ToggleCompressor(Command):
    def __init__(self):
        super().__init__("ToggleCompressor")
        self.state = not self.getRobot().compressor.get()
        self.requires(self.getRobot().compressor)

    def initialize(self):
        pass

    def execute(self):
        self.getRobot().compressor.set(self.state)

#set the compressor state
class SetCompressor(Command):
    def __init__(self, state):
        super().__init__("ToggleCompressor")
        self.state = state
        self.requires(self.getRobot().compressor)

    def initialize(self):
        pass

    def execute(self):
        self.getRobot().compressor.set(self.state)
