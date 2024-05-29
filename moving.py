import event
import time
import cyberpi
import mbot2
import mbuild
import random

# initialize variables
moving_list_list = []
Count = 10
#text size
small = 10
middle = 40
big = 80

#list of speeds for run
slow = 25
middem = 50
fast = 100
SuperFast = 150



HelpList = '''To use the code.
You can use the JoyStick to move the robot.
To reset the robot press the B button.
'''

# List of colors for the forward and start function
StartColor = 'green green green green green'
ForwardColor = 'red red green red red'
BackwardColor = 'red red yellow red red'
RightColor = 'red red red green green'
LeftColor = 'green green red red red'

# Plays sound
play = cyberpi.audio.play_drum

# var for the print function
output = cyberpi.display.show_label

# Tell the user what the battery % is
battery = output(str('Stationary ') + "Battery: " + str(cyberpi.get_battery()) + '%', 16, "center", index=0)

# var of the motor
move = mbot2

# On start tell the user that the robot is Stationary and what the battery % is
@event.start
def on_start():
    global StartColor, battery
    cyberpi.led.show(StartColor)
    battery

# If A is pressed, tell the user how the program works
@event.is_press('a')
def help():
    global HelpList
    output(HelpList, 10, index=0)

# Resetting the robot
@event.is_press('b')
def RESET_PRESSED():
    output("RESETTING", big,"center", index=0)
    cyberpi.led.play('flash_orange ')
    cyberpi.restart()
    play('side-stick', 0.25)


# Move the robot forward
@event.is_press('up')
def UP():
    global ForwardColor
    cyberpi.led.show(ForwardColor)
    while True:
        if (mbuild.ultrasonic2.get(1) >= 300):
            output("Moving forward", 24, "center", index=0)
            move.forward(fast)
        else:
            if mbuild.ultrasonic2.get(1) <= 50:
                move.turn(90)
            else:
                output("Moving forward", 24, "center", index=0)
                move.forward(fast)


# Move the robot backwards
@event.is_press('down')
def DOWN():
    global Count, BackwardColor
    cyberpi.led.show(BackwardColor)
    for count in range(Count, 0, -1):
        # tells the user that the robot is moving backward X amount of time
        output("Moving Backwards\n" + str(count), 24, "center", index=0)
        move.backward(50, 1)
    output("Moving Backwards [Complete]", 12, "center", index=0)

@event.is_press('left')
def LEFT():
    global LeftColor
    cyberpi.led.show(LeftColor)
    output("Moving Left", 24, "center", index=0)
    move.turn_left(90, 1)
    time.sleep(1)
    output("Stationary", 16, "center", index=0)

@event.is_press('right')
def RIGHT():
    global RightColor
    cyberpi.led.show(RightColor)
    output("Moving Right", 24, "center", index=0)
    move.turn_right(90, 1)
    time.sleep(1)
    output("Stationary", 16, "center", index=0)
