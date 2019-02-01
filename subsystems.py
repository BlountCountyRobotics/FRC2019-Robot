import wpilib
from wpilib.command.subsystem import Subsystem
import ctre
import robot_map
import math
from commands.drivetrain import FollowJoystick


class Arm(Subsystem):

    def __init__(self):
        super().__init__("Arm")
        self.arm_motor = ctre.TalonSRX(robot_map.can_ids["arm"])



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

        self.left_solenoid = wpilib.Solenoid(robot_map.can_ids["pcm"],
                                             robot_map.solenoids["left_gearbox"])
        self.right_solenoid = wpilib.Solenoid(robot_map.can_ids["pcm"],
                                              robot_map.solenoids["right_gearbox"])

        self.useFactor = True

    #use xbox controller to feed motor output
    def followJoystick(self, joystick):
        #cube joystick input for better curve
        left_output  = math.pow(joystick.getRawAxis(robot_map.ds4["l-y_axis"]), 3)
        right_output = math.pow(joystick.getRawAxis(robot_map.ds4["r-y_axis"]), 3)

        if useFactor:
            #create factor for easier driving at slow speeds
            factor = .4

            #if bumpers are pressed, increase factor
            if   joystick.getBumper(XboxController.Hand.kLeft):
                factor += .3
            elif joystick.getBumper(XboxController.Hand.kRight):
                factor += .3

            setSpeed(left_output * factor, right_output * factor)
        else:
            setSpeed(left_output, right_output)


    def setSpeed(left, right):
        self.left1.set(ctre.TalonSRX.ControlMode.PercentOutput, limit(left))
        self.left2.set(ctre.TalonSRX.ControlMode.PercentOutput, limit(left))
        self.left3.set(ctre.TalonSRX.ControlMode.PercentOutput, limit(left))

        self.right1.set(ctre.TalonSRX.ControlMode.PercentOutput, limit(right))
        self.right2.set(ctre.TalonSRX.ControlMode.PercentOutput, limit(right))
        self.right3.set(ctre.TalonSRX.ControlMode.PercentOutput, limit(right))

    #limit percent output from -1.0 to 1.0
    def limit(speed):
        if(speed > 1.0):
            return 1.0
        elif(speed < -1.0):
            return -1.0
        return speed

    def toggleGearing():
        setGearing(not getGearing())

    def setHighGearing():
        if getGearing() == False:
            setGearing(True)

    def setLowGearing():
        if getGearing() == True:
            setGearing(False)

    def getGearing():
        #if they are both the same, then return just one of them
        if self.left_solenoid.get() and self.right_solenoid.get():
            return self.left_solenoid.get()
        else:
            #otherwise, return current gearing as high (to be safe)
            return True

    #set both gearbox gearings at the same time
    def setGearing(input):
        self.left_solenoid.set(input)
        self.right_solenoid.set(input)

    def initDefaultCommand(self):
        self.setDefaultCommand(FollowJoystick()) #needs default command




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
