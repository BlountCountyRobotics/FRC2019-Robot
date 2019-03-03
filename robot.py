from wpilib.command import Subsystem, Scheduler, Command
import wpilib, commandbased, ctre, wpilib.buttons, subsystems, networktables, robot_map, commands.ramp, commands.other, commands.lights, commands.end_effector, commands.arm, commands.drivetrain

class Melody(commandbased.CommandBasedRobot):
    def robotInit(self):
        #add getRobot methods to Command and Subsystem
        #allows commands and subsystems to access the instance
        Command.getRobot = lambda x=0: self
        Subsystem.getRobot = lambda x=0: self

        #initialize subsystems
        self.initSubsystems()

        #initialize joysticks and buttons
        self.initOI()

        #initialize networktables connection
        self.initNetworkTables()

    def autonomousInit(self):
        #Set exploratory color during autonomous
        Scheduler.getInstance().add(commands.lights.SetColor("forest"))
        self.blinkin.setDefaultCommand(commands.lights.SetColor("forest"))

    def autonomousPeriodic(self):
        #put SD values during the match
        super().autonomousPeriodic()
        self.smart_dashboard.putString("Gearing:", "Low" if self.drivetrain.getGearing() else "High")
        self.smart_dashboard.putString("Compressor:", "Enabled" if self.compressor.enabled() else "Disabled")
        self.smart_dashboard.putString("End Effector:", "Closed" if self.end_effector.get() else "Grabbing")

    def teleopInit(self):
        #Set default gradient during teleop
        Scheduler.getInstance().add(commands.lights.SetColor("defaultgradient"))
        self.blinkin.setDefaultCommand(commands.lights.SetColor("defaultgradient"))

    def teleopPeriodic(self):
        #put SD values during the match
        super().teleopPeriodic()
        self.smart_dashboard.putString("Gearing:", "High" if self.drivetrain.getGearing() else "Low")
        self.smart_dashboard.putString("Compressor:", "Enabled" if self.compressor.enabled() else "Disabled")
        self.smart_dashboard.putString("End Effector:", "Closed" if self.end_effector.get() else "Grabbing")

    def disabledInit(self):
        #set red strobing lights if robot disables
        Scheduler.getInstance().add(commands.lights.SetColor("strobered"))
        self.blinkin.setDefaultCommand(commands.lights.SetColor("strobered"))

    def initSubsystems(self):
        #initialize subsystems; run at robot startup
        self.arm = subsystems.Arm()
        self.end_effector = subsystems.EndEffector()
        self.drivetrain = subsystems.Drivetrain()
        self.ramp = subsystems.Ramp()
        self.blinkin = subsystems.Lights()
        self.compressor = wpilib.Compressor()

    def initNetworkTables(self):
        #allows for smartdashboard and offboard vision communication
        networktables.NetworkTables.initialize()
        self.smart_dashboard = networktables.NetworkTables.getTable("SmartDashboard")

    def initOI(self):
        #initialize joysticks
        self.controller = wpilib.Joystick(0)
        self.button_board = wpilib.Joystick(1)

        #initialize buttons and assign commands to those buttons
        #wpilib.buttons.JoystickButton(self.controller, robot_map.ds4["options"]).toggleWhenPressed(commands.drivetrain.StopDriving())
        wpilib.buttons.JoystickButton(self.controller, robot_map.ds4["share"]).whenPressed(commands.other.ToggleCompressor())
        wpilib.buttons.JoystickButton(self.controller, robot_map.ds4["r1"]).whenPressed(commands.end_effector.Toggle())
        wpilib.buttons.JoystickButton(self.controller, robot_map.ds4["square"]).whenPressed(commands.ramp.Deploy())
        wpilib.buttons.JoystickButton(self.controller, robot_map.ds4["triangle"]).whenPressed(commands.arm.Toggle())

if __name__ == '__main__':
    wpilib.run(Melody)
