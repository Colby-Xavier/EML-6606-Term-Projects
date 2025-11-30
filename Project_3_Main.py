from codrone_edu.drone import *
import time

def go_to_height(desired_height):
    # This function takes the current height and incrementally moves towards the desired height until reached.
    curr_height = drone.get_height()
    if curr_height > desired_height:
        while curr_height > desired_height:
            drone.set_throttle(-20)
            drone.move(0.1)
            curr_height = drone.get_height()
        drone.set_throttle(0)
    elif curr_height < desired_height:
        while curr_height < desired_height:
            drone.set_throttle(20)
            drone.move(0.1)
            curr_height = drone.get_height()
        drone.set_throttle(0)
    else:
        drone.set_throttle(0)


drone = Drone()
drone.pair()

speed = 10


drone.takeoff()
go_to_height(9*2.5)
time.sleep(0.05)
distance = 20
thresh = 20
end_time = time.time() + 30
count = 0

while time.time() < end_time: # While we have gone less than the time limit
    if drone.get_front_range() >= distance + thresh: # Look for
        drone.sendControl(0, speed, 0, 0)
        time.sleep(0.005) # ensures theres time to start moving
    else:
        drone.hover(1)
        if count < 2: # Ensures that the drone take the correct amount of turns
            drone.turn_left(90)
            print('left')
            count = count + 1
        else: break
        # elif count < 3:
        #     drone.turn_right(90)
        #     print('right')
        #     count = count + 1
        # if count >= 3:
        #     break
drone.land()
drone.close()
