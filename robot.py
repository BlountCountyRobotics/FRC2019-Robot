from wpilib.command import Subsystem, Scheduler, Command
import wpilib, commandbased, ctre, wpilib.buttons, subsystems, networktables, robot_map, commands.ramp, commands.lights, commands.end_effector, commands.arm, commands.other, commands.drivetrain

class Melody(commandbased.CommandBasedRobot):
    def robotInit(self):
        #add getRobot methods to Command and Subsystem
        #allows commands and subsystems to access this robot
        Command.getRobot = lambda x=0: self
        Subsystem.getRobot = lambda x=0: self

        #initialize subsystems
        self.arm = subsystems.Arm()
        self.end_effector = subsystems.EndEffector()
        self.drivetrain = subsystems.Drivetrain()
        self.ramp = subsystems.Ramp()
        self.blinkin = subsystems.Lights()

        #create non-subsystem objects
        self.compressor = wpilib.Compressor()

        #initialize joysticks and buttons
        self.initOI()

        #initialize networktables connection
        #allows for smartdashboard and offboard vision communication
        networktables.NetworkTables.initialize()
        self.smart_dashboard = networktables.NetworkTables.getTable("SmartDashboard")

    def autonomousInit(self):
        Scheduler.getInstance().add(commands.lights.SetColor("forest"))
        self.blinkin.setDefaultCommand(commands.lights.SetColor("forest"))

    def teleopInit(self):
        Scheduler.getInstance().add(commands.lights.SetColor("defaultgradient"))
        self.blinkin.setDefaultCommand(commands.lights.SetColor("defaultgradient"))

    def disabledInit(self):
        #Scheduler.getInstance().add(commands.lights.SetColor("strobered"))
        pass

    def initOI(self):
        #initialize joysticks
        self.controller = wpilib.Joystick(0)
        self.button_board = wpilib.Joystick(1)

        #initialize buttons and assign commands to those buttons
        #wpilib.buttons.JoystickButton(self.controller, robot_map.ds4["options"]).toggleWhenPressed(commands.drivetrain.StopDriving())
        wpilib.buttons.JoystickButton(self.controller, robot_map.ds4["share"]).whenPressed(commands.other.ToggleCompressor())
        wpilib.buttons.JoystickButton(self.controller, robot_map.ds4["cross"]).whenPressed(commands.end_effector.Toggle())
        wpilib.buttons.JoystickButton(self.controller, robot_map.ds4["square"]).whenPressed(commands.ramp.Deploy())
        wpilib.buttons.JoystickButton(self.controller, robot_map.ds4["triangle"]).whenPressed(commands.arm.Toggle())


if __name__ == '__main__':
    wpilib.run(Melody)
