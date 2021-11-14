from droneblocks.DroneBlocksTello import DroneBlocksTello
import time

if __name__ == '__main__':
    print("Create Tello object")
    db_tello = DroneBlocksTello()

    print("Connect to Tello Drone")
    db_tello.connect()

    battery_level = db_tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")

    db_tello.display_heart(DroneBlocksTello.RED)
    time.sleep(3)
    brightness_levels = [50, 100, 150, 200, 255]
    for brightness_level in brightness_levels:
        db_tello.send_command_with_return(f"EXT mled sl {brightness_level}")
        time.sleep(3)

    for brightness_level in brightness_levels:
        db_tello.set_display_brightness(brightness_level)
        time.sleep(3)

    db_tello.clear_everything()
