import wpilib
from wpilib.command.subsystem import Subsystem
import ctre
import robot_map
import math
import commands.drivetrain
import commands.end_effector


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

    def setSpeed(self, left, right):
        self.left1.set(ctre.ControlMode.PercentOutput, self.limit(left))
        self.left2.set(ctre.ControlMode.PercentOutput, self.limit(left))
        self.left3.set(ctre.ControlMode.PercentOutput, self.limit(left))

        self.right1.set(ctre.ControlMode.PercentOutput, self.limit(-right))
        self.right2.set(ctre.ControlMode.PercentOutput, self.limit(-right))
        self.right3.set(ctre.ControlMode.PercentOutput, self.limit(-right))



    #use xbox controller to feed motor output
    def followJoystick(self, joystick):
        #cube joystick input for better curve
        left_output  = math.pow(joystick.getRawAxis(robot_map.ds4["l-y_axis"]), 3)
        right_output = math.pow(joystick.getRawAxis(robot_map.ds4["r-y_axis"]), 3)

        #create factor for easier driving at slow speeds
        factor = .4

        #if bumpers are pressed, increase factor
        if   joystick.getRawButton(robot_map.ds4["l1"]):
            factor += .3
        if joystick.getRawButton(robot_map.ds4["r1"]):
            factor += .3

        self.setSpeed(left_output * factor, right_output * factor)

    #limit percent output from -1.0 to 1.0
    def limit(self, speed):
        if(speed > 1.0):
            return 1.0
        elif(speed < -1.0):
            return -1.0
        return speed

    def toggleGearing(self):
        setGearing(not getGearing())

    def setHighGearing(self):
        if getGearing() == False:
            setGearing(True)

    def setLowGearing(self):
        if getGearing() == True:
            setGearing(False)

    def getGearing(self):
        return self.solenoid.get()
    #set both gearbox gearings at the same time
    def setGearing(self, input):
        self.solenoid.set(input)

    def initDefaultCommand(self):
        self.setDefaultCommand(commands.drivetrain.FollowJoystick()) #needs default command




class EndEffector(Subsystem):

    def __init__(self):
        super().__init__("EndEffector")
        self.end_effector = wpilib.Solenoid(robot_map.can_ids["pcm"], robot_map.pcm["end_effector"])

    def set(self, input):
        self.end_effector.set(input)

    def get(self):
        return self.end_effector.get()

    def initDefaultCommand(self):
        self.setDefaultCommand(commands.end_effector.Nothing()) 





class Ramp(Subsystem):

    def __init__(self):
        super().__init__("Ramp")
        self.ramp_motor = ctre.TalonSRX(robot_map.can_ids["ramp"])


    def initDefaultCommand(self):
        self.setDefaultCommand(None) #needs default command
