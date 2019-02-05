import wpilib
import commandbased
import ctre
from wpilib.command import Command
import wpilib.buttons
import subsystems
import networktables
import robot_map
import commands.drivetrain
import commands.other

class Melody(commandbased.CommandBasedRobot):
    def robotInit(self):
        Command.getRobot = lambda x=0: self

        #self.arm = subsystems.Arm()
        #self.grabber = subsystems.Grabber()
        self.drivetrain = subsystems.Drivetrain()
        #self.ramp = subsystems.Ramp()

        self.initOI()
        #self.navx = navx.ahrs.AHRS.create_spi()
        self.compressor = wpilib.Compressor()



    def autonomousInit(self):
        pass

    def teleopInit(self):
        pass

    def initOI(self):
        self.controller = wpilib.Joystick(0)
        self.button_board = wpilib.Joystick(1)

        wpilib.buttons.JoystickButton(self.controller, robot_map.ds4["options"]).toggleWhenPressed(commands.drivetrain.StopDriving())
        wpilib.buttons.JoystickButton(self.controller, robot_map.ds4["share"]).whenPressed(commands.other.ToggleCompressor())



if __name__ == '__main__':
    wpilib.run(Melody)
