from droneblocks.DroneBlocksContextManager import DroneBlocksContextManager
import time

"""
With Motors off, walk the RoboMaster Tello Talent over mission pads to see the mission pad ID
detected and displayed.
Usage:

python mission_pad_id_detector_13.py

"""


def main(droneblocks_tello):
    # enable mission pad detection downward camera only
    print("Enable mission pads....")
    droneblocks_tello.enable_mission_pads()  # default is direction 0, or down
    droneblocks_tello.set_mission_pad_detection_direction(0)
    time.sleep(2)

    print("Clear display")
    droneblocks_tello.clear_display()
    time.sleep(2)

    battery_level = droneblocks_tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")
    time.sleep(2)

    # set the top led to RED to indicate we have not found a mission pad
    droneblocks_tello.set_top_led(r=255, g=0, b=0)

    print("Start detecting mission pads...")
    try:
        while True:
            mid = droneblocks_tello.get_mission_pad_id()
            if 1 <= mid <= 8:
                # then we have detected a mission pad
                # set top led to GREEN to indicate we found a mission pad
                droneblocks_tello.set_top_led(r=0, g=255, b=0)
                print(mid)
                droneblocks_tello.display_character(mid)
                x = droneblocks_tello.get_mission_pad_distance_x()
                y = droneblocks_tello.get_mission_pad_distance_y()
                z = droneblocks_tello.get_mission_pad_distance_z()
                print(f"{x},{y},{z}")
            else:
                # we did not detect a mission pad id
                droneblocks_tello.display_character("X")
                droneblocks_tello.set_top_led(r=255, g=0, b=0)

            time.sleep(1)

    finally:
        droneblocks_tello.clear_display()


if __name__ == '__main__':
    with DroneBlocksContextManager(start_tello_web=False) as db_tello:
        main(db_tello)
