import time
from droneblocks.DroneBlocksTello import DroneBlocksTello

"""
Challenge:
Write a user script that will change the top LED based on the height of the Tello.

usage: python -m droneblocks.tello_script_runner --handler challenge_1_user_script --tello-web
"""

lower_threshold = 60
upper_threshold = lower_threshold + 25


def init(tello, params):
    tello.display_sad(display_color=DroneBlocksTello.RED)
    tello.set_top_led(r=255, g=0, b=0)
    time.sleep(1)

    battery_level = tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")
    time.sleep(1)

    return None


def handler(tello, frame, params):
    height = tello.get_height()
    print(height)
    if height < lower_threshold:
        tello.set_top_led(r=255, g=0, b=0)
        tello.display_sad(display_color=DroneBlocksTello.RED)
    elif lower_threshold <= height < upper_threshold:
        tello.set_top_led(r=0, g=255, b=0)
        tello.display_up_arrow(display_color=DroneBlocksTello.PURPLE)
    elif height >= upper_threshold:
        tello.set_top_led(r=0, g=0, b=255)
        tello.display_smile(display_color=DroneBlocksTello.BLUE)

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
    tello.clear_everything()
