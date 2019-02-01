import wpilib
import commandbased
import ctre
import oi
import subsystems
import navx
import networktables
import robot_map


class Melody(commandbased.CommandBasedRobot):

    def robotInit(self):
        subsystems.Subsystems.initSubsystems()
        oi.initOI()
        #self.navx = navx.ahrs.AHRS.create_spi()
        self.compressor = wpilib.Compressor(robot_map.pcm["compressor"])


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
