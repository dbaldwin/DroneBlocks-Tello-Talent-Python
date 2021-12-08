from droneblocks.DroneBlocksTello import DroneBlocksTello
from droneblocks.DroneBlocksContextManager import DroneBlocksContextManager
import time


def main(droneblocks_tello):
    battery_level = droneblocks_tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")

    smile_face = DroneBlocksTello.smile_image

    # Scroll Pattern with SDK API to scroll text message from right to left
    droneblocks_tello.send_command_with_return(f"EXT mled l g 2.5 {smile_face}")
    time.sleep(20)

    # Use DroneBlocksTello API to scroll text message from right to left
    purple_smile = droneblocks_tello.change_image_color(smile_face, from_color=DroneBlocksTello.BLUE,
                                                        to_color=DroneBlocksTello.PURPLE)
    droneblocks_tello.scroll_image(image_string=purple_smile,
                                   scroll_dir=DroneBlocksTello.LEFT,
                                   rate=2.5)

    time.sleep(20)

    # Scroll Up
    droneblocks_tello.scroll_image(image_string=smile_face,
                                   scroll_dir=DroneBlocksTello.UP,
                                   rate=2.5)
    time.sleep(20)

    # Scroll Down
    down_arrow = DroneBlocksTello.down_arrow_image
    droneblocks_tello.scroll_image(image_string=down_arrow,
                                   scroll_dir=DroneBlocksTello.DOWN,
                                   rate=2.5)

    time.sleep(20)

    droneblocks_tello.clear_everything()


if __name__ == '__main__':
    with DroneBlocksContextManager(motor_on=True) as db_tello:
        main(db_tello)
