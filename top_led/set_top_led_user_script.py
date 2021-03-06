from droneblocksutils.exceptions import LandException
from set_top_led import main

"""
usage: 
cd top_led
python -m droneblocks.tello_script_runner --handler set_top_led_user_script

"""


def init(tello, params):
    """
    Called once at the beginning of the script.  Allows for initialization of the user script.
    :param tello:
    :type tello:
    :param params:
    :type params:
    :return:
    :rtype:
    """
    # Turn the motor on to keep the Tello cool
    tello.turn_motor_on()

    return None


def handler(tello, frame, params):
    """
    Called continually during the execution of the user script.

    :param tello:
    :type tello:
    :param frame:
    :type frame:
    :param params:
    :type params:
    :return:
    :rtype:
    """
    main(tello)
    raise LandException()


def stop(tello, params):
    """
    Called when the script runner is exiting.

    :param tello: Reference to the DJITelloPy Tello object.
    :type tello: Tello
    :param params:
    :type params: dictionary
    :return: None
    :rtype:
    """
    tello.turn_motor_off()
