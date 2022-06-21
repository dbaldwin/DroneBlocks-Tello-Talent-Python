from droneblocks.DroneBlocksContextManager import DroneBlocksContextManager
from droneblocks.DroneBlocksTello import DroneBlocksTello
import time
import logging

"""
Challenge 3 Solution

Usage:

python challenge_3_script.py

"""
sleep_time = 1


def main(droneblocks_tello: DroneBlocksTello):
    droneblocks_tello.LOGGER.setLevel(logging.INFO)

    print("Enable mission pads")
    droneblocks_tello.enable_mission_pads()

    print("Initialize LED and Display")
    droneblocks_tello.display_smile(display_color=DroneBlocksTello.PURPLE)
    droneblocks_tello.set_top_led(r=255, g=0, b=0)
    time.sleep(sleep_time)

    battery_level = droneblocks_tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")
    time.sleep(sleep_time)

    print("Start Challenge 3 ")
    droneblocks_tello.takeoff()

    time.sleep(sleep_time * 2)

    # show the current mission pad id
    mid = droneblocks_tello.get_mission_pad_id()
    droneblocks_tello.display_character(mid)
    time.sleep(1)

    print("fly_forward 1")
    droneblocks_tello.clear_display()
    droneblocks_tello.set_top_led(r=0, g=255, b=0)
    droneblocks_tello.fly_forward(30, 'in')
    droneblocks_tello.set_top_led(r=255, g=0, b=0)
    mid = droneblocks_tello.get_mission_pad_id()
    droneblocks_tello.display_character(mid)

    time.sleep(sleep_time)
    print("ccw1")
    droneblocks_tello.rotate_counter_clockwise(90)

    time.sleep(sleep_time)
    print("fly_forward 2")
    droneblocks_tello.clear_display()
    droneblocks_tello.set_top_led(r=0, g=255, b=0)
    droneblocks_tello.fly_forward(30, 'in')
    droneblocks_tello.set_top_led(r=255, g=0, b=0)
    mid = droneblocks_tello.get_mission_pad_id()
    droneblocks_tello.display_character(mid)

    time.sleep(sleep_time)
    print("ccw2")
    droneblocks_tello.rotate_counter_clockwise(90)

    time.sleep(sleep_time)
    print("fly_forward 3")
    droneblocks_tello.clear_display()
    droneblocks_tello.set_top_led(r=0, g=255, b=0)
    droneblocks_tello.fly_forward(30, 'in')
    droneblocks_tello.set_top_led(r=255, g=0, b=0)
    mid = droneblocks_tello.get_mission_pad_id()
    droneblocks_tello.display_character(mid)

    time.sleep(sleep_time)
    print("ccw3")
    droneblocks_tello.rotate_counter_clockwise(90)

    time.sleep(sleep_time)
    print("fly_forward 4")
    droneblocks_tello.clear_display()
    droneblocks_tello.set_top_led(r=0, g=255, b=0)
    droneblocks_tello.fly_forward(30, 'in')
    droneblocks_tello.set_top_led(r=255, g=0, b=0)
    mid = droneblocks_tello.get_mission_pad_id()
    droneblocks_tello.display_character(mid)

    time.sleep(sleep_time)
    print("ccw4")
    droneblocks_tello.rotate_counter_clockwise(90)

    time.sleep(sleep_time)
    print("land")
    droneblocks_tello.alternate_top_led(r1=200, g1=0, b1=0, r2=0, g2=0, b2=255)
    time.sleep(sleep_time * 2)

    droneblocks_tello.clear_everything()
    time.sleep(1)

    droneblocks_tello.land()


if __name__ == '__main__':
    with DroneBlocksContextManager(start_tello_web=False) as db_tello:
        main(db_tello)
