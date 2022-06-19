from droneblocks.DroneBlocksContextManager import DroneBlocksContextManager
from droneblocks.DroneBlocksTello import DroneBlocksTello
import time

"""
Challenge 2 Solution

Usage:

python challenge_2_script.py

"""

import logging


def main(droneblocks_tello: DroneBlocksTello):
    droneblocks_tello.LOGGER.setLevel(logging.INFO)
    print("Clear display and intialize top LED")
    # Display a smiley face on the matrix display!
    droneblocks_tello.display_smile(display_color=DroneBlocksTello.PURPLE)
    droneblocks_tello.set_top_led(r=255, g=0, b=0)
    time.sleep(1)

    battery_level = droneblocks_tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")
    time.sleep(1)

    print("Start Challenge 2 ")
    droneblocks_tello.takeoff()

    time.sleep(2)
    print("fly_forward 1")
    droneblocks_tello.set_top_led(r=0, g=255, b=0)
    droneblocks_tello.fly_forward(30, 'in')
    droneblocks_tello.set_top_led(r=255, g=0, b=0)

    time.sleep(1)
    print("ccw1")
    droneblocks_tello.rotate_counter_clockwise(90)

    time.sleep(1)
    print("fly_forward 2")
    droneblocks_tello.set_top_led(r=0, g=255, b=0)
    droneblocks_tello.fly_forward(30, 'in')
    droneblocks_tello.set_top_led(r=255, g=0, b=0)

    time.sleep(1)
    print("ccw2")
    droneblocks_tello.rotate_counter_clockwise(90)

    time.sleep(1)
    print("fly_forward 3")
    droneblocks_tello.set_top_led(r=0, g=255, b=0)
    droneblocks_tello.fly_forward(30, 'in')
    droneblocks_tello.set_top_led(r=255, g=0, b=0)

    time.sleep(1)
    print("ccw3")
    droneblocks_tello.rotate_counter_clockwise(90)

    time.sleep(1)
    print("fly_forward4")
    droneblocks_tello.set_top_led(r=0, g=255, b=0)
    droneblocks_tello.fly_forward(30, 'in')
    droneblocks_tello.set_top_led(r=255, g=0, b=0)

    time.sleep(1)
    print("ccw4")
    droneblocks_tello.rotate_counter_clockwise(90)

    time.sleep(1)
    print("land")
    droneblocks_tello.alternate_top_led(r1=200, g1=0, b1=0, r2=0, g2=0, b2=255)
    time.sleep(2)

    droneblocks_tello.clear_everything()
    time.sleep(1)

    droneblocks_tello.land()


if __name__ == '__main__':
    with DroneBlocksContextManager(start_tello_web=False) as db_tello:
        main(db_tello)
