import time

"""
user script that will detect a mission pad and print the mission pad id, and display the 
mission pad id on the 8x8 matrix display.  It will also print out the x,y,z distance from
the Tello to the mission pad.

Usage:

python -m droneblocks.tello_script_runner --handler mission_pad_user_script_14 --tello-web

python -m droneblocks.tello_script_runner --handler mission_pad_user_script_14 --tello-web --display-video

"""


def init(tello, params):
    # enable mission pad detection downward camera only
    tello.enable_mission_pads() # default is direction 0
    tello.set_mission_pad_detection_direction(0) # optional but here for clarity
    tello.clear_display()
    tello.set_top_led(r=255, g=0, b=0)
    tello.set_display_brightness(5)


    return None


def handler(tello, frame, params):
    mid = tello.get_mission_pad_id()
    if 1 <= mid <= 8:
        # then we have detected a mission pad
        tello.set_top_led(r=0, g=255, b=0)
        print(mid)
        tello.display_character(mid)
        x = tello.get_mission_pad_distance_x()
        y = tello.get_mission_pad_distance_y()
        z = tello.get_mission_pad_distance_z()
        print(f"{x},{y},{z}")
    else:
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
