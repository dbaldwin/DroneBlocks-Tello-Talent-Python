from droneblocks.DroneBlocksContextManager import DroneBlocksContextManager
from droneblocks.DroneBlocksTello import DroneBlocksTello
import time
import logging

"""
Challenge 4 Solution

Usage:

python challenge_4_script.py

"""
sleep_time = 2

# python -m droneblocks.tt_matrix_generator
image_string = "p000000p0p0000p000pbbp0000bppb0000brrb0000rbbr000r0000r0r000000r"


def fly_leg_of_journey(droneblocks_tello, x, mid1, mid2):
    print(f"GO {mid1} -> {mid2}")
    droneblocks_tello.display_image(image_string)
    droneblocks_tello.set_top_led(r=0, g=255, b=0)
    time.sleep(sleep_time/2)
    droneblocks_tello.go_xyz_speed_yaw_mid(x=x, y=0, z=60, speed=30, yaw=0, mid1=mid1, mid2=mid2)
    print(f"DONE {mid1} -> {mid2}")
    droneblocks_tello.set_top_led(r=255, g=0, b=0)
    mid = droneblocks_tello.get_mission_pad_id()
    droneblocks_tello.display_character(mid)
    time.sleep(sleep_time)


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

    print("Start Challenge 4 ")
    droneblocks_tello.takeoff()

    time.sleep(sleep_time * 2)

    # show the current mission pad id
    mid = droneblocks_tello.get_mission_pad_id()
    droneblocks_tello.display_character(mid)
    time.sleep(sleep_time)

    for i in range(1, 3):  # repeat the loop twice
        print(f"GO Trip {i} !!!!!!!!!!!!!!!!!!!!!!!!!")
        fly_leg_of_journey(droneblocks_tello, 125, 4, 2)

        fly_leg_of_journey(droneblocks_tello, 150, 2, 5)

        fly_leg_of_journey(droneblocks_tello, 125, 5, 3)

        fly_leg_of_journey(droneblocks_tello, 150, 3, 4)

    time.sleep(sleep_time * 2)

    print("land")
    droneblocks_tello.alternate_top_led(r1=200, g1=0, b1=0, r2=0, g2=0, b2=255)
    time.sleep(sleep_time)

    droneblocks_tello.clear_everything()
    time.sleep(1)

    droneblocks_tello.land()


if __name__ == '__main__':
    with DroneBlocksContextManager(start_tello_web=True) as db_tello:
        main(db_tello)
