from droneblocks.DroneBlocksContextManager import DroneBlocksContextManager
from droneblocks.DroneBlocksTello import DroneBlocksTello
import time
import logging

"""

"""


sleep_time = 1


def test_top_led(db_tello: DroneBlocksTello):

    db_tello.set_top_led(r=255, g=0, b=0)
    time.sleep(sleep_time)
    db_tello.set_top_led(r=0, g=255, b=0)
    time.sleep(sleep_time)
    db_tello.set_top_led(r=0, g=0, b=255)
    time.sleep(sleep_time)
    db_tello.alternate_top_led(r1=0, g1=255, b1=0, r2=0, g2=0, b2=255, freq=2.5)
    time.sleep(sleep_time)
    db_tello.pulse_top_led(r=255, g=0, b=255, freq=2.5)
    time.sleep(sleep_time*2)

def test_matrxi_led(db_tello: DroneBlocksTello):
    db_tello.clear_everything()
    time.sleep(sleep_time)

    db_tello.display_smile(display_color=DroneBlocksTello.PURPLE)
    time.sleep(sleep_time)
    db_tello.display_smile(display_color=DroneBlocksTello.RED)
    time.sleep(sleep_time)
    db_tello.display_smile(display_color=DroneBlocksTello.BLUE)
    time.sleep(sleep_time)

    db_tello.display_sad(display_color=DroneBlocksTello.PURPLE)
    time.sleep(sleep_time)
    db_tello.display_sad(display_color=DroneBlocksTello.RED)
    time.sleep(sleep_time)
    db_tello.display_sad(display_color=DroneBlocksTello.BLUE)
    time.sleep(sleep_time)

    db_tello.display_heart(display_color=DroneBlocksTello.PURPLE)
    time.sleep(sleep_time)
    db_tello.display_heart(display_color=DroneBlocksTello.RED)
    time.sleep(sleep_time)
    db_tello.display_heart(display_color=DroneBlocksTello.BLUE)
    time.sleep(sleep_time)

    db_tello.display_up_arrow(display_color=DroneBlocksTello.PURPLE)
    time.sleep(sleep_time)
    db_tello.display_up_arrow(display_color=DroneBlocksTello.RED)
    time.sleep(sleep_time)
    db_tello.display_up_arrow(display_color=DroneBlocksTello.BLUE)
    time.sleep(sleep_time)

    db_tello.display_down_arrow(display_color=DroneBlocksTello.PURPLE)
    time.sleep(sleep_time)
    db_tello.display_down_arrow(display_color=DroneBlocksTello.RED)
    time.sleep(sleep_time)
    db_tello.display_down_arrow(display_color=DroneBlocksTello.BLUE)
    time.sleep(sleep_time)

    db_tello.display_left_arrow(display_color=DroneBlocksTello.PURPLE)
    time.sleep(sleep_time)
    db_tello.display_left_arrow(display_color=DroneBlocksTello.RED)
    time.sleep(sleep_time)
    db_tello.display_left_arrow(display_color=DroneBlocksTello.BLUE)
    time.sleep(sleep_time)

    db_tello.display_right_arrow(display_color=DroneBlocksTello.PURPLE)
    time.sleep(sleep_time)
    db_tello.display_right_arrow(display_color=DroneBlocksTello.RED)
    time.sleep(sleep_time)
    db_tello.display_right_arrow(display_color=DroneBlocksTello.BLUE)
    time.sleep(sleep_time)

def main(droneblocks_tello: DroneBlocksTello):
    droneblocks_tello.LOGGER.setLevel(logging.INFO)
    test_top_led(droneblocks_tello)
    time.sleep(2)
    test_matrxi_led(droneblocks_tello)
    time.sleep(1)

    droneblocks_tello.clear_everything()



if __name__ == '__main__':
    with DroneBlocksContextManager(start_tello_web=False, ignore_tello_talent_methods=False, motor_on=True) as db_tello:
        main(db_tello)
