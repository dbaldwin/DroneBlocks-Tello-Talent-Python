import time
import cv2

"""

Example user script showing how to process the Tello video frame in the user handler script, and showing
the processing on the tello video frame while also showing the original video frame is that option is
selected. 

Usage: 
cd examples

# Show both video windows
python -m droneblocks.tello_script_runner --handler video_feed_user_script --show-original-video --display-video --tello-web

# Show only the User Tello Video updated in the user script
python -m droneblocks.tello_script_runner --handler video_feed_user_script --display-video

# Show only the original Tello Video
python -m droneblocks.tello_script_runner --handler video_feed_user_script --show-original-video


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
    try:
        tello.turn_motor_on()
    except:
        pass

    return None

counter = 0
t1 = time.time()

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
    global t1, counter
    if time.time() > t1+2:
        t1 = time.time()
        counter += 1
    if frame is not None:
        cv2.putText(frame, f"Count: {counter}", (int(frame.shape[1]/2), int(frame.shape[0]/2)), cv2.FONT_HERSHEY_SIMPLEX, 1,
                (255, 0, 0), 2, cv2.LINE_AA)  #

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
    try:
        tello.turn_motor_off()
    except:
        pass
