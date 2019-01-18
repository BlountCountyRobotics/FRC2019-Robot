from wpilib.command import InstantCommand
import robot

class ToggleCompressor(InstantCommand):

    def __init__(self):
        super().__init__("ToggleCompressor")


    def initialize(self):
        pass

    def execute(self):
        if robot.compressor.enabled():
            stop()
        else:
            start()
