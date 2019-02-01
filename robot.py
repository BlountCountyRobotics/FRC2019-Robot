import wpilib
import commandbased
import ctre
import oi
from wpilib.command import Command
import subsystems
import navx
import networktables
import robot_map

class Melody(commandbased.CommandBasedRobot):
    def robotInit(self):
        Command.getRobot = lambda x=0: self

        self.arm = subsystems.Arm()
        self.grabber = subsystems.Grabber()
        self.drivetrain = subsystems.Drivetrain()
        self.ramp = subsystems.Ramp()

        oi.initOI()
        #self.navx = navx.ahrs.AHRS.create_spi()
        self.compressor = wpilib.Compressor()



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
