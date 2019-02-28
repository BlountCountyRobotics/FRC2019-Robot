from wpilib.command import Subsystem, Scheduler, Command
import wpilib, commandbased, ctre, wpilib.buttons, subsystems, networktables, robot_map, commands.ramp, commands.lights, commands.end_effector, commands.arm, commands.compressor, commands.drivetrain

class Melody(commandbased.CommandBasedRobot):
    def robotInit(self):
        #add getRobot methods to Command and Subsystem
        #allows commands and subsystems to access this robot
        Command.getRobot = lambda x=0: self
        Subsystem.getRobot = lambda x=0: self

        #initialize subsystems
        self.initSubsystems()

        #initialize joysticks and buttons
        self.initOI()

        #initialize networktables connection
        self.initNetworkTables()

    def autonomousInit(self):
        Scheduler.getInstance().add(commands.lights.SetColor("forest"))
        self.blinkin.setDefaultCommand(commands.lights.SetColor("forest"))

    def teleopInit(self):
        Scheduler.getInstance().add(commands.lights.SetColor("defaultgradient"))
        self.blinkin.setDefaultCommand(commands.lights.SetColor("defaultgradient"))

    def teleopPeriodic(self):
        super().teleopPeriodic()
        self.smart_dashboard.putString("Gearing:", "High" if self.drivetrain.getGearing() else "Low")
        self.smart_dashboard.putString("Compressor:", "Enabled" if self.compressor.get() else "Disabled")
        self.smart_dashboard.putString("End Effector:", "Closed" if self.end_effector.get() else "Grabbing")

    def disabledInit(self):
        #Scheduler.getInstance().add(commands.lights.SetColor("strobered"))
        pass

    def initSubsystems(self):
        #initialize subsystems; run at robot startup
        self.arm = subsystems.Arm()
        self.end_effector = subsystems.EndEffector()
        self.drivetrain = subsystems.Drivetrain()
        self.ramp = subsystems.Ramp()
        self.blinkin = subsystems.Lights()
        self.compressor = subsystems.Compressor()

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
        wpilib.buttons.JoystickButton(self.controller, robot_map.ds4["share"]).whenPressed(commands.compressor.ToggleCompressor())
        wpilib.buttons.JoystickButton(self.controller, robot_map.ds4["r1"]).whenPressed(commands.end_effector.Toggle())
        wpilib.buttons.JoystickButton(self.controller, robot_map.ds4["square"]).whenPressed(commands.ramp.Deploy())
        wpilib.buttons.JoystickButton(self.controller, robot_map.ds4["triangle"]).whenPressed(commands.arm.Toggle())


if __name__ == '__main__':
    wpilib.run(Melody)
