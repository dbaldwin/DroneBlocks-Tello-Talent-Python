import random
import time

"""
usage: 
cd top_led

python -m droneblocks.tello_script_runner --handler alternate_top_led_user_script

python -m droneblocks.tello_script_runner --handler alternate_top_led_user_script --tello-web

python -m droneblocks.tello_script_runner --handler alternate_top_led_user_script --show-original-video --tello-web

python -m droneblocks.tello_script_runner --handler alternate_top_led_user_script --show-original-video --fly


"""


def init(tello, params):
    tello.turn_motor_on()


def handler(tello, frame, params):
    r1 = random.randint(0,100)
    g1 = random.randint(0,100)
    b1 = random.randint(0,100)

    r2 = random.randint(0,100)
    g2 = random.randint(0,100)
    b2 = random.randint(0,100)

    freq = random.randint(0,10)

    tello.alternate_top_led(r1=r1, g1=g1, b1=b1, r2=r2, g2=g2, b2=b2, freq=freq)
    time.sleep(3)


def stop(tello, params):
    try:
        tello.turn_motor_off()
    finally:
        tello.clear_everything()
