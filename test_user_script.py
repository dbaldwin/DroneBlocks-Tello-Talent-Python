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

def handler(tello, frame, params):
    global command_issued

    mid = tello.get_mission_pad_id()
    if mid > 0:
        print(mid)
        tello.display_character(mid)
        tello.set_top_led(r=0, g=255, b=0)
    else:
        tello.set_top_led(r=255, g=0, b=0)

    time.sleep(5)

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
