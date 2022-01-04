import time
from droneblocks.tello_keyboard_mapper import UP, DOWN, LEFT, RIGHT

"""
usage: 
Challenge:
Write a user script that will display an UP,DOWN,LEFT,RIGHT arrow in response to keyboard commands.
If the key pressed is not recognized, display a question mark.

python -m droneblocks.tello_script_runner --handler 16_challenge_2_user_script --fly
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
    # start out by clearing the display
    tello.clear_display()
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
    if 'last_key_pressed' in params:
        if params['last_key_pressed'] == UP:
            tello.display_up_arrow()
        elif params['last_key_pressed'] == DOWN:
            tello.display_down_arrow()
        elif params['last_key_pressed'] == LEFT:
            # remember LEFT is from the Tello perspective so if you are looking at the Tello
            # it will move to your right
            tello.display_right_arrow()
        elif params['last_key_pressed'] == RIGHT:
            # remember RIGHT is from the Tello perspective so if you are looking at the Tello
            # it will move to your left
            tello.display_left_arrow()
        else:
            tello.display_question_mark()
    else:
        tello.display_question_mark()

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
