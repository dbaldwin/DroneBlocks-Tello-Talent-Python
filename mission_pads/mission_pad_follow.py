from droneblocks.DroneBlocksContextManager import DroneBlocksContextManager
import time
import math

"""
With Motors off, walk the RoboMaster Tello Talent over mission pads to see 
the mission pad ID detected and displayed.

Usage:

python -m droneblocks.tello_script_runner --handler mission_pad_follow --tello-web

"""

# Maximum speed sent to send_rc_control
MAX_SPEED = 1.5

# If the distance to the target is less than the minimum then just set to zero to keep Tello close
MIN_DISTANCE = 10

# If we exceed the max distance from the pad let's stop tracking
MAX_DISTANCE = 100

def init(tello, params):
    # enable mission pad detection downward camera only
    tello.enable_mission_pads() # default is direction 0
    tello.set_mission_pad_detection_direction(0) # optional but here for clarity
    tello.clear_display()
    tello.set_top_led(r=255, g=0, b=0)

    return None


def handler(tello, frame, params):
    mid = tello.get_mission_pad_id()

    # Pad detected
    if 1 <= mid <= 8:

        # then we have detected a mission pad
        tello.set_top_led(r=0, g=255, b=0)
        tello.display_character(mid)

        x = tello.get_mission_pad_distance_x()
        y = tello.get_mission_pad_distance_y()
        z = tello.get_mission_pad_distance_z()

        # Distance from drone to pad in 2d space, we'll handle altitude differently
        distance_to_pad_center = math.sqrt(x ** 2 + y ** 2)

        # Set the x/y speeds
        f_b_speed = int((MAX_SPEED * x) / 2) * -1 # Need to invert this
        l_r_speed = int((MAX_SPEED * y) / 2)
        u_d_speed = 0

        # Try to maintain a reasonable altitude above the pad
        if z < 80:
            u_d_speed = 30
        elif z > 120:
            u_d_speed = -30

        # If we're in the distance range then don't move
        # If we're outside the distance range then don't move
        if abs(distance_to_pad_center) <= MIN_DISTANCE or abs(distance_to_pad_center) > MAX_DISTANCE:
           f_b_speed = 0
           l_r_speed = 0
           u_d_speed = 0

        # For debugging purposes
        print(f'pad: {pad_id}, dist center: {distance_to_pad_center}, x dist: {pad_x_dist}, y dist: {pad_y_dist}, z dist: {pad_z_dist}')

        # Send the control inputs to Tello
        tello.send_rc_control(l_r_speed, f_b_speed, u_d_speed, 0)

    # No pad detected
    else:
        tello.send_rc_control(0, 0, 0, 0)
        tello.display_character("X")
        tello.set_top_led(r=255, g=0, b=0)

    return

def stop(tello, params):
    """
    Called when the script runner is exiting.

    :param tello: Reference to the DJITelloPy Tello object.
    :type tello: Tello
    :param fly_flag: True - the fly flag was specified and the Tello will take off. False - the Tello will NOT
                        be instructed to take off
    :type fly_flag:  bool
    :return: None
    :rtype:
    """
    tello.display_smile()
    time.sleep(2)
    tello.clear_everything()

if __name__ == '__main__':
    with DroneBlocksContextManager(start_tello_web=False) as db_tello:
        main(db_tello)