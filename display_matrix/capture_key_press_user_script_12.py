from droneblocks.tello_keyboard_mapper import UP, DOWN, LEFT, RIGHT
import time

"""
Using the keyboard commands UP, DOWN, LEFT, RIGHT capture the key press and update the 
matrix display.

Usage:
cd display_matrix

python -m droneblocks.tello_script_runner --handler capture_key_press_user_script


"""


def init(tello, params):
    if params['fly_flag'] == False:
        # Turn the motor on to keep the Tello cool
        tello.turn_motor_on()

    tello.display_heart()
    time.sleep(1)

    return None


def handler(tello, frame, params):
    if params:
        last_key = params['last_key_pressed']
        if last_key is not None:
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

    if params['fly_flag'] == False:
        # if we are not flying, then turn the motors off
        tello.turn_motor_off()

    tello.clear_everything()
