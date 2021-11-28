import time
from droneblocks.tello_keyboard_mapper import UP, DOWN, LEFT, RIGHT

"""
usage: 
python -m droneblocks.tello_script_runner --handler 16_challenge_2_user_script --fly
"""


def init(tello, params):
    tello.clear_display()
    return None


def handler(tello, frame, params):
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
