#this file contains the constant values (ids, etc) associated with the robot

#map of can ids
can_ids = {
    #left side drivetrain motors
    "left1": 8,
    "left2": 1,
    "left3": 2,

    #right side drivetrain motors
    "right1": 3,
    "right2": 4,
    "right3": 5,

    "pcm": 0
}

#map of pcm connectors
pcm = {
    "gearbox": 0,
    "end_effector": 2,
    "ramp": 3,
    "arm": 1
}

#map of ds4 buttons and axes
ds4 = {
    "square": 1,
    "cross": 2,
    "circle": 3,
    "triangle": 4,
    "l_click": 11,
    "r_click": 12,
    "options": 10,
    "share": 9,
    "l1": 5,
    "l2_button": 7,
    "r1": 6,
    "r2_button": 8,
    "l-y_axis": 1,
    "l-x_axis": 0,
    "r-y_axis": 5,
    "r-x_axis": 2,
    "l2_axis": 3,
    "r2_axis": 4,
    "touchpad_button": 14
}

#k values for tape following pid system
k = {
    "p": .1,
    "i": .1,
    "d": .1,
    "f": .1
}

#constants for the tape following pid system
pid = {
    "speed": .2,
    "setpoint": 25,
    "input_range": [0, 51],
    "output_range": .2
}

#map of color patterns for the blinkin
blinkin = {
    "bluechase": 0.01,
    "defaultgradient": 0.41,
    "forest": -0.91,
    "strobered": -.11,
    "bpm": .43,
    "green": .77,
    "hotpink": .57,
    "rorange": .63
}
