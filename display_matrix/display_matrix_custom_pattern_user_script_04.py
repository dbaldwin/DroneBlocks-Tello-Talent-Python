from droneblocksutils.exceptions import LandException
from display_matrix_custom_pattern_03 import main

"""
usage: 
cd top_led

python -m droneblocks.tello_script_runner --handler display_matrix_custom_pattern_user_script_03

python -m droneblocks.tello_script_runner --handler display_matrix_custom_pattern_user_script_03 --show-original-video

python -m droneblocks.tello_script_runner --handler display_matrix_custom_pattern_user_script_03 --show-original-video --fly


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

    if params['fly_flag'] == False:
        # Turn the motor on to keep the Tello cool
        tello.turn_motor_on()

    return None

main_called_flag = False
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
    global main_called_flag

    if not main_called_flag:
        main(tello)
        main_called_flag = True
    # raise LandException()

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
    if params['fly_flag'] == False:
        # if we are not flying, then turn the motors off
        tello.turn_motor_off()
