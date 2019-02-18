from wpilib.command.subsystem import Subsystem
import wpilib.interfaces, wpilib, commands.drivetrain, commands.lights, ctre, robot_map, math

class Arm(Subsystem):
    def __init__(self):
        super().__init__("Arm")
        self.arm = wpilib.Solenoid(robot_map.can_ids["pcm"], robot_map.pcm["arm"])

    #get state of pistons that hold the arm open (true=drop, false=hold)
    def get(self):
        return self.arm.get()

    #set state of pistons that hold the arm
    def set(self, input):
        self.arm.set(input)

    def initDefaultCommand(self):
        pass



class Drivetrain(Subsystem, wpilib.interfaces.PIDSource, wpilib.interfaces.PIDOutput):
    def __init__(self):
        #run subsystem constructor
        super().__init__("Drivetrain")

        #initialize motors
        self.left1 = ctre.TalonSRX(robot_map.can_ids["left1"])
        self.left2 = ctre.TalonSRX(robot_map.can_ids["left2"])
        self.left3 = ctre.TalonSRX(robot_map.can_ids["left3"])

        self.right1 = ctre.TalonSRX(robot_map.can_ids["right1"])
        self.right2 = ctre.TalonSRX(robot_map.can_ids["right2"])
        self.right3 = ctre.TalonSRX(robot_map.can_ids["right3"])

        #initialize the solenoid to shift gearing
        self.solenoid = wpilib.Solenoid(robot_map.can_ids["pcm"], robot_map.pcm["gearbox"])

        #initialize pid variables
        self.pid_command_names = ["FollowTape"]
        self.pid_controller = wpilib.PIDController(robot_map.k["p"], robot_map.k["i"], robot_map.k["d"], robot_map.k["f"], source=self, output=self)
        self.pid_controller.onTarget = self.onTarget
        self.pid_controller.disable()


    #set speed for the left and right sides of the robot
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

    #toggle the gearing of the gearbox
    def toggleGearing(self):
        setGearing(not getGearing())

    #set gearbox to high gearing
    def setHighGearing(self):
        if getGearing() == False:
            setGearing(True)

    #set gearbox to low gearing
    def setLowGearing(self):
        if getGearing() == True:
            setGearing(False)

    #get gearing as bool (true=high, false=low)
    def getGearing(self):
        return self.solenoid.get()

    #set both gearbox gearings at the same time
    def setGearing(self, input):
        self.solenoid.set(input)

    #start pid system to follow tape
    def start_pid(self):
        self.pid_controller.enable()

    #stop pid system (return to operator control)
    def stop_pid(self):
        self.pid_controller.disable()

    def initDefaultCommand(self):
        self.setDefaultCommand(commands.drivetrain.FollowJoystick())

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

    #set end effector state
    def get(self):
        return self.end_effector.get()

    #get end effector state (true=open, false=closed)
    def set(self, input):
        self.end_effector.set(input)

    def initDefaultCommand(self):
        pass





class Ramp(Subsystem):
    def __init__(self):
        super().__init__("Ramp")
        self.solenoid = wpilib.Solenoid(robot_map.can_ids["pcm"], robot_map.pcm["ramp"])

    #get ramp state (true=extended)
    def get(self):
        return self.solenoid.get()

    #set ramp state
    def set(self, input):
        self.solenoid.set(input)

    def initDefaultCommand(self):
        pass

class Lights(Subsystem):
    def __init__(self):
        super().__init__("Lights")
        self.blinkin = wpilib.Spark(0)

    #get the current output to the blinkin
    #(check output to table on blinkin user guide)
    def get(self):
        return self.blinkin.get()

    #set color, see colors available on robot_map.blinkin
    def set(self, input):
        self.blinkin.set(input)

    def initDefaultCommand(self):
        self.setDefaultCommand(commands.lights.SetColor("defaultgradient")) #needs default command
