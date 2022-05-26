from droneblocks.DroneBlocksContextManager import DroneBlocksContextManager
from droneblocks.DroneBlocksTello import DroneBlocksTello
import time

"""
Challenge 1 Solution

Usage:

python challenge_1_script.py

"""


def main(droneblocks_tello):
    # lower_threshold - lower threshold between red and green led
    lower_threshold = 60

    # upper_threshold - upper threshold between green and blue led
    upper_threshold = lower_threshold + 25

    print("Clear display and intialize top LED")
    # Display a sad face on the matrix display!
    droneblocks_tello.display_sad(display_color=DroneBlocksTello.RED)
    droneblocks_tello.set_top_led(r=255, g=0, b=0)
    time.sleep(1)

    battery_level = droneblocks_tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")
    time.sleep(1)

    print("Start detecting height")
    while True:
        height = droneblocks_tello.get_height()
        print(height)
        if height < lower_threshold:
            droneblocks_tello.set_top_led(r=255, g=0, b=0)
            droneblocks_tello.display_sad(display_color=DroneBlocksTello.RED)
        elif lower_threshold <= height < upper_threshold:
            droneblocks_tello.set_top_led(r=0, g=255, b=0)
            droneblocks_tello.display_up_arrow(display_color=DroneBlocksTello.PURPLE)
        elif height >= upper_threshold:
            droneblocks_tello.set_top_led(r=0, g=0, b=255)
            droneblocks_tello.display_smile(display_color=DroneBlocksTello.BLUE)

        # sleep for a second so we do not overwhelm
        # the RMTT with too many requests
        time.sleep(1)


if __name__ == '__main__':
    with DroneBlocksContextManager(start_tello_web=True) as db_tello:
        main(db_tello)
