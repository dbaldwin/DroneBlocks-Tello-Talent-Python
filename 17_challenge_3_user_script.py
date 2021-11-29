import time
from droneblocks.tello_keyboard_mapper import UP, DOWN, LEFT, RIGHT

"""
usage: 
python -m droneblocks.tello_script_runner --display-unknown-keyvalue

python -m droneblocks.tello_script_runner --handler 17_challenge_3_user_script --fly
"""


def init(tello, params):
    tello.clear_display()
    time.sleep(0.25)
    tello.scroll_string("Hello Pat")
    return None


def handler(tello, frame, params):
    if 'last_key_pressed' in params:
        if params['last_key_pressed'] == 112:
            height = tello.get_height()
            print(height)
            tello.scroll_string(f"{height}")

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
