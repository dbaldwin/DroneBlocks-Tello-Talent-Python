import time

"""
usage: python -m droneblocks.tello_script_runner --handler 15_top_led_challenge_user_script --fly
"""

base_height = 60

def init(tello, params):
    tello.clear_display()
    return None


def handler(tello, frame, params):
    height = tello.get_height()
    print(height)
    if height < base_height:
        tello.set_top_led(r=255, g=0, b=0)
    elif base_height <= height < base_height+25:
        tello.set_top_led(r=0, g=255, b=0)
    elif height >= base_height+25:
        tello.set_top_led(r=0, g=0, b=255)
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
