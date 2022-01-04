from droneblocksutils.exceptions import LandException
from pulse_top_led import main

"""
usage: 
cd top_led
python -m droneblocks.tello_script_runner --handler pulse_top_led_user_script

python -m droneblocks.tello_script_runner --handler pulse_top_led_user_script --show-original-video


"""


def init(tello, params):
    # Turn the motor on to keep the Tello cool
    tello.turn_motor_on()


def handler(tello, frame, params):
    main(tello)
    raise LandException()


def stop(tello, params):
    tello.turn_motor_off()
