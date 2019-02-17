import wpilib
import wpilib.interfaces
from wpilib.command.subsystem import Subsystem
import ctre
import robot_map
import math
import commands.lights
import commands.drivetrain
import commands.nothing

class Arm(Subsystem):

    def __init__(self):
        super().__init__("Arm")
        self.arm = wpilib.Solenoid(robot_map.can_ids["pcm"], robot_map.pcm["arm"])

    def get(self):
        return self.arm.get()

    def set(self, input):
        self.arm.set(input)

    def initDefaultCommand(self):
        self.setDefaultCommand(commands.nothing.Nothing(self)) #needs default command




class Drivetrain(Subsystem, wpilib.interfaces.PIDSource, wpilib.interfaces.PIDOutput):

    def __init__(self):
        super().__init__("Drivetrain")
        self.left1 = ctre.TalonSRX(robot_map.can_ids["left1"])
        self.left2 = ctre.TalonSRX(robot_map.can_ids["left2"])
        self.left3 = ctre.TalonSRX(robot_map.can_ids["left3"])

        self.right1 = ctre.TalonSRX(robot_map.can_ids["right1"])
        self.right2 = ctre.TalonSRX(robot_map.can_ids["right2"])
        self.right3 = ctre.TalonSRX(robot_map.can_ids["right3"])

        self.solenoid = wpilib.Solenoid(robot_map.can_ids["pcm"], robot_map.pcm["gearbox"])

        self.pid_command_names = ["FollowTape"]

        self.pid_controller = wpilib.PIDController(robot_map.k["p"], robot_map.k["i"], robot_map.k["d"], robot_map.k["f"], source=self, output=self)
        self.pid_controller.onTarget = self.onTarget
        self.pid_controller.disable()



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
        if joystick.getRawButton(robot_map.ds4["l1"]):
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

    def start_pid(self):
        self.pid_controller.enable()

    def stop_pid(self):
        self.pid_controller.disable()

    def initDefaultCommand(self):
        self.setDefaultCommand(commands.drivetrain.FollowJoystick()) #needs default command

    #PIDSource overrides:
    def getPIDSourceType(self):
        return PIDSourceType.kRate

    def pidGet(self):
        return getRobot().smart_dashboard.getNumber("visionError", 0)

    #PIDOutput override:
    def pidWrite(self, output):
        #if current command is controlling the DT via pid
        if self.getCurrentCommandName() in self.pid_command_names:
            self.setSpeed(robot_map.k["speed"] - output, robot_map.k["speed"] + output)

    #PIDBase ovveride:
    def onTarget(self):
        return False






class EndEffector(Subsystem):

    def __init__(self):
        super().__init__("EndEffector")
        self.end_effector = wpilib.Solenoid(robot_map.can_ids["pcm"], robot_map.pcm["end_effector"])

    def get(self):
        return self.end_effector.get()

    def set(self, input):
        self.end_effector.set(input)

    def initDefaultCommand(self):
        self.setDefaultCommand(commands.nothing.Nothing(self))





class Ramp(Subsystem):

    def __init__(self):
        super().__init__("Ramp")
        self.solenoid = wpilib.Solenoid(robot_map.can_ids["pcm"], robot_map.pcm["ramp"])

    def get(self):
        return self.solenoid.get()

    def set(self, input):
        self.solenoid.set(input)

    def initDefaultCommand(self):
        self.setDefaultCommand(commands.nothing.Nothing(self)) #needs default command

class Lights(Subsystem):

    def __init__(self):
        super().__init__("Lights")
        self.blinkin1 = wpilib.Spark(0)
        self.blinkin2 = wpilib.Spark(1)
        self.blinkin = wpilib.SpeedControllerGroup(self.blinkin1, self.blinkin2)

    def get(self):
        return self.blinkin.get()

    def set(self, input):
        self.blinkin.set(input)

    def initDefaultCommand(self):
        self.setDefaultCommand(commands.lights.SetColor("defaultgradient")) #needs default command
