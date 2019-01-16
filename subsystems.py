import wpilib
from wpilib.command.subsystem import Subsystem
import ctre
import robot_map
import math
import commands


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


    def followJoystick(self, joystick):
        left_output  = math.pow(joystick.getY(XboxController.Hand.kLeft ), 3)
        right_output = math.pow(joystick.getY(XboxController.Hand.kRight), 3)

        factor = .4

        if   joystick.getBumper(XboxController.Hand.kLeft):
            factor += .3
        elif joystick.getBumper(XboxController.Hand.kRight):
            factor += .3

        setSpeed(left_output * factor, right_output * factor)

    def setSpeed(left, right):
        self.left1.set(ctre.TalonSRX.ControlMode.PercentOutput, limit(left))
        self.left2.set(ctre.TalonSRX.ControlMode.PercentOutput, limit(left))
        self.left3.set(ctre.TalonSRX.ControlMode.PercentOutput, limit(left))

        self.right1.set(ctre.TalonSRX.ControlMode.PercentOutput, limit(right))
        self.right2.set(ctre.TalonSRX.ControlMode.PercentOutput, limit(right))
        self.right3.set(ctre.TalonSRX.ControlMode.PercentOutput, limit(right))

    def limit(speed):
        if(speed > 1.0):
            return 1.0
        elif(speed < -1.0):
            return -1.0
        return speed

    def initDefaultCommand(self):
        self.setDefaultCommand(commands.drivetrain.FollowJoystick) #needs default command




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

def initSubsystems(): #creates the subsystem global variables
    global arm, grabber, drivetrain, ramp
    arm = Arm()
    grabber = Grabber()
    drivetrain = Drivetrain()
    ramp = Ramp()
