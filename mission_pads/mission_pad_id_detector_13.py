from droneblocks.DroneBlocksContextManager import DroneBlocksContextManager
import time

"""
Usage:

python mission_pad_id_detector_13.py

"""

def main(droneblocks_tello):
    # enable mission pad detection downward camera only
    droneblocks_tello.enable_mission_pads()  # default is direction 0, or down
    droneblocks_tello.set_mission_pad_detection_direction(0)

    print("Clear display")
    droneblocks_tello.clear_display()

    battery_level = droneblocks_tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")

    try:
        while True:
            mid = droneblocks_tello.get_mission_pad_id()
            if mid < 0:
                mid = 0
            print(mid)
            droneblocks_tello.display_character(mid)
            x = droneblocks_tello.get_mission_pad_distance_x()
            y = droneblocks_tello.get_mission_pad_distance_y()
            z = droneblocks_tello.get_mission_pad_distance_z()
            print(f"{x},{y},{z}")
            time.sleep(1)
    finally:
        droneblocks_tello.clear_display()


if __name__ == '__main__':
    with DroneBlocksContextManager(start_tello_web=True) as db_tello:
        main(db_tello)
