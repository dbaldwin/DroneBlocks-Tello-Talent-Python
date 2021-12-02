from droneblocks.DroneBlocksTello import DroneBlocksTello
import time

if __name__ == '__main__':

    print("Create Tello object")
    tello = DroneBlocksTello()

    print("Connect to Tello Drone")
    tello.connect()

    # enable mission pad detection downward camera only
    tello.enable_mission_pads() # default is direction 0, or down
    tello.set_mission_pad_detection_direction(0)

    print("Clear display")
    tello.clear_display()

    battery_level = tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")

    try:
        while True:
            mid = tello.get_mission_pad_id()
            if mid < 0:
                mid = 0
            print(mid)
            tello.display_character(mid)
            x = tello.get_mission_pad_distance_x()
            y = tello.get_mission_pad_distance_y()
            z = tello.get_mission_pad_distance_z()
            print(f"{x},{y},{z}")
            time.sleep(1)
    finally:
        tello.clear_display()
