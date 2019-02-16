import wpilib
from wpilib.command import InstantCommand



class Toggle(InstantCommand): #should only be used to drop the arm; we could add a timeout for this if we wanted to prevent re-actuating this solenoid

    def __init__(self):
        super().__init__("Toggle")
        self.requires(self.getRobot().arm)

    def initialize(self):
        pass

    def execute(self):
        self.getRobot().arm.set(not self.getRobot().arm.get())
