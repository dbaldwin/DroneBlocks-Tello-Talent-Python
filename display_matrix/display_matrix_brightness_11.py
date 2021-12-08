from droneblocks.DroneBlocksTello import DroneBlocksTello
from droneblocks.DroneBlocksContextManager import DroneBlocksContextManager
import time


def main(droneblocks_tello):
    battery_level = droneblocks_tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")

    droneblocks_tello.display_heart(DroneBlocksTello.RED)
    time.sleep(3)
    brightness_levels = [50, 100, 150, 200, 255]
    for brightness_level in brightness_levels:
        droneblocks_tello.send_command_with_return(f"EXT mled sl {brightness_level}")
        time.sleep(3)

    for brightness_level in brightness_levels:
        droneblocks_tello.set_display_brightness(brightness_level)
        time.sleep(3)

    droneblocks_tello.clear_everything()


if __name__ == '__main__':
    with DroneBlocksContextManager(motor_on=True) as db_tello:
        main(db_tello)
