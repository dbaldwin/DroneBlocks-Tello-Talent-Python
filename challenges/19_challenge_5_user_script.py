import time
from droneblocksutils.exceptions import LandException
"""
Challenge:
Detect a mission pad and fly to the mission pad.  Once at the mission pad, issue a
LandException to land the Tello on the mission pad

usage: 
python -m droneblocks.tello_script_runner --handler 18_challenge_4_user_script --fly

"""


def init(tello, params):
    tello.enable_mission_pads() # default is direction 0
    tello.set_mission_pad_detection_direction(0) # optional but here for clarity
    tello.clear_display()
    return None

command_issued = False
def handler(tello, frame, params):
    global command_issued

    mid = tello.get_mission_pad_id()
    if mid > 0:
        print(mid)
        tello.display_character(mid)
        x = tello.get_mission_pad_distance_x()
        y = tello.get_mission_pad_distance_y()
        z = tello.get_mission_pad_distance_z()
        print(f"{x},{y},{z}")
        if not command_issued:
            tello.set_top_led(r=0, g=255, b=0)
            tello.go_xyz_speed_mid(21,21, 90, 30, mid)
            command_issued = True
        if abs(x) <= 25 and abs(y) <= 25:
            raise LandException()
    else:
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
    time.sleep(1)

    tello.clear_everything()
