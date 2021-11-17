from droneblocks.tello_keyboard_mapper import UP, DOWN, LEFT, RIGHT
import time


def init(tello, params):
    tello.display_heart()
    return None


def handler(tello, frame, params):
    if params:
        last_key = params['last_key_pressed']
        if last_key is not None:
            print(last_key)
            if last_key == UP:
                tello.display_up_arrow()
            elif last_key == DOWN:
                tello.display_down_arrow()
            elif last_key == LEFT:
                tello.display_left_arrow()
            elif last_key == RIGHT:
                tello.display_right_arrow()
            else:
                tello.display_question_mark()
        else:
            tello.clear_display()

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
