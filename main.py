"""
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Project 1 for Aerial Robotics:
Path following and error analysis. The drone will perform two shapes, a square and a figure 8, and then land. the paths
will be run multiple times at varying speeds and analyzed for optimal settings.


designed by: Colby Howell
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
"""


# Drone setup
from codrone_edu.drone import *
drone = Drone()
drone.pair()

# Functions

# Function to streamline battery check
def battery_check():
    battery = drone.get_battery()
    if battery > 75: # turns green to show good battery
        drone.set_drone_LED(0,255,0,100)
        print('battery ready!')
    elif battery > 50: # turns yellow to indicate charging is need
        drone.set_drone_LED(255,255,0,100)
        print('battery getting low!')
    else: #  turns red to warn operator to charge before using
        drone.set_drone_LED(255,0,0,100)
        print('Battery too low! Charge!')
        drone.close()


# Square movement
def square(pitch_speed, yaw_speed, dur):
    for x in range(0,4,1): # performs these movements four times to create a circle
        drone.set_pitch(pitch_speed) # forward
        drone.move(dur)
        drone.set_pitch(0)
        drone.hover(0.5)
        drone.set_yaw(yaw_speed) # turn
        drone.move(dur)
        drone.set_yaw(0)
        drone.hover(0.5)


def circle(pitch_speed, yaw_speed, delay):
    drone.set_pitch(pitch_speed) # Circle 1
    drone.set_yaw(yaw_speed)
    drone.move(delay)
    drone.set_yaw(0)
    drone.set_pitch(0)
    drone.hover(1)

def go_to_height(desired_height):
    curr_height = drone.get_height()
    if curr_height > desired_height:
        while (curr_height > desired_height):
            drone.set_throttle(-20)
            drone.move(0.1)
            curr_height = drone.get_height()
    elif curr_height < desired_height:
        while (curr_height < desired_height):
            drone.set_throttle(20)
            drone.move(0.1)
            curr_height = drone.get_height()
    else:
        drone.set_throttle(0)
        pass




#///////////////////////////////////////////////////////////////////////////
# code start
# Working Variables
circle_Pitch = 30
circle_Yaw = 70
square_Pitch = 25
square_Yaw = 65
square_duration = 1
circle_duration = 4

# five runs of the two shapes, at each of these 10 height parameters: 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150
height_param = 140


battery_check()
#drone.land()
drone.takeoff()

# Setting the height parameter for testing
go_to_height(height_param)
drone.set_drone_LED(0, 0, 100, 200) # Set to blue to visually show code began

drone.hover(1)
circle(circle_Pitch, circle_Yaw, circle_duration)
square(square_Pitch, square_Yaw, square_duration)

# end drone movements
drone.land()
drone.close()

