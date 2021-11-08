import time
import random

time_to_switch_colors = 0


def init(tello, fly_flag=False):
    """

    :param tello: Reference to the DJITelloPy Tello object.
    :type tello: Tello
    :param fly_flag: True - the fly flag was specified and the Tello will take off. False - the Tello will NOT
                        be instructed to take off
    :type fly_flag:  bool
    :return: None or Map of Keyboard Mappings
    :rtype:
    """
    global time_to_switch_colors

    tello.clear_everything()
    tello.pulse_top_led(r=0, g=255, b=0, freq=1.0)
    time_to_switch_colors = time.time() + 5

    return None


def handler(tello, frame, fly_flag=False):
    """

    :param tello: Reference to the DJITelloPy Tello object.
    :type tello: Tello
    :param frame: image
    :type frame:
    :param fly_flag: True - the fly flag was specified and the Tello will take off. False - the Tello will NOT
                        be instructed to take off
    :type fly_flag:  bool
    :return: None
    :rtype:
    """
    global time_to_switch_colors

    if time.time() > time_to_switch_colors:
        tello.set_top_led(r=random.randint(0, 255), g=random.randint(0, 255), b=random.randint(0, 255))
        time_to_switch_colors = time.time() + 2

    return


def stop(tello, fly_flag=False):
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
