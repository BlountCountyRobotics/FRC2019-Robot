import wpilib
from wpilib.command.subsystem import Subsystem
import ctre
import robot_map



class Arm(Subsystem):

    def __init__(self):
        super().__init__("Arm")
        super.arm_motor = ctre.TalonSRX(robot_map.can_ids["arm"])



    def initDefaultCommand(self):
        self.setDefaultCommand(None) #needs default command




class Drivetrain(Subsystem):



    def __init__(self):
        super().__init__("Drivetrain")
        self.left1 = ctre.TalonSRX(robot_map.can_ids["left1"])
        self.left2 = ctre.TalonSRX(robot_map.can_ids["left2"])
        self.left3 = ctre.TalonSRX(robot_map.can_ids["left3"])

        self.right1 = ctre.TalonSRX(robot_map.can_ids["right1"])
        self.right2 = ctre.TalonSRX(robot_map.can_ids["right2"])
        self.right3 = ctre.TalonSRX(robot_map.can_ids["right3"])




    def initDefaultCommand(self):
        self.setDefaultCommand(None) #needs default command




class Grabber(Subsystem):

    def __init__(self):
        super().__init__("Grabber")
        self.grabber_motor = ctre.TalonSRX(robot_map.can_ids["grabber"])



    def initDefaultCommand(self):
        self.setDefaultCommand(None) #needs default command





class Ramp(Subsystem):

    def __init__(self):
        super().__init__("Ramp")
        self.ramp_motor = ctre.TalonSRX(robot_map.can_ids["ramp"])


    def initDefaultCommand(self):
        self.setDefaultCommand(None) #needs default command



#global variables used to access the main instance of each subsystem
arm = None
grabber = None
drivetrain = None
ramp = None

def InitSubsystems(): #creates the subsystem global variables
    global arm, grabber, drivetrain, ramp
    arm = Arm()
    grabber = Grabber()
    drivetrain = Drivetrain()
    ramp = Ramp()
