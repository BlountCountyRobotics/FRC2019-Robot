import wpilib
import commandbased

import ctre
import subsystems
import oi


class Melody(commandbased.CommandBasedRobot):

    def robotInit(self):
        subsystems.initSubsystems()
        oi.initOI()

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        pass

if __name__ == '__main__':
    wpilib.run(Melody)
