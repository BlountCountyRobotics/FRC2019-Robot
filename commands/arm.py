import wpilib
from wpilib.command import InstantCommand



class Toggle(InstantCommand): #should only be used to drop the arm

    def __init__(self):
        super().__init__("Toggle")
        self.requires(self.getRobot().end_effector)

    def initialize(self):
        pass

    def execute(self):
        self.getRobot().arm.set(not self.getRobot().arm.get())
