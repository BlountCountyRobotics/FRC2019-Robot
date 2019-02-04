import wpilib
from wpilib.command.subsystem import Subsystem
import ctre
import robot_map
import math
import commands.drivetrain


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

        self.solenoid = wpilib.Solenoid(robot_map.can_ids["pcm"], robot_map.pcm["gearbox"])
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
        self.left1.set(ctre.ControlMode.PercentOutput, limit(left))
        self.left2.set(ctre.ControlMode.PercentOutput, limit(left))
        self.left3.set(ctre.ControlMode.PercentOutput, limit(left))

        self.right1.set(ctre.ControlMode.PercentOutput, limit(right))
        self.right2.set(ctre.ControlMode.PercentOutput, limit(right))
        self.right3.set(ctre.ControlMode.PercentOutput, limit(right))

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

        return self.solenoid.get()
    #set both gearbox gearings at the same time
    def setGearing(input):
        self.solenoid.set(input)

    def initDefaultCommand(self):
        self.setDefaultCommand(commands.drivetrain.FollowJoystick()) #needs default command




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
