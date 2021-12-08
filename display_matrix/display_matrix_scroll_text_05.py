from droneblocks.DroneBlocksTello import DroneBlocksTello
from droneblocks.DroneBlocksContextManager import DroneBlocksContextManager
import time


def main(droneblocks_tello):
    battery_level = droneblocks_tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")

    # maximum is 70 characters
    # Scroll Text with SDK API to scroll text message from right to left
    print("Print message using SDK API")
    droneblocks_tello.send_command_with_return(f"EXT mled l p 2.5 Hello From DroneBlocks")
    time.sleep(20)

    print("Use DroneBlocksTello API to scroll text message from right to left")
    scrolling_text = "Hello From DroneBlocks"
    droneblocks_tello.scroll_string(message=scrolling_text, scroll_dir=DroneBlocksTello.LEFT,
                                    display_color=DroneBlocksTello.RED,
                                    rate=2.5)

    time.sleep(20)

    # Scroll Up
    print("Use DroneBlocksTello API to scroll text message up")
    droneblocks_tello.scroll_string(message=scrolling_text, scroll_dir=DroneBlocksTello.UP,
                                    display_color=DroneBlocksTello.BLUE,
                                    rate=2.5)

    time.sleep(20)

    droneblocks_tello.clear_everything()


if __name__ == '__main__':
    with DroneBlocksContextManager(motor_on=True) as db_tello:
        main(db_tello)
