from droneblocks.DroneBlocksContextManager import DroneBlocksContextManager
from droneblocks.DroneBlocksTello import DroneBlocksTello
import time


def main(droneblocks_tello):
    battery_level = droneblocks_tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")

    # Use the DroneBlocks TT Pattern Generator to design a pattern and use the generated string here
    # This pattern is from the lecture showing the word UP
    image_string = "b00b0000b00b0000b00b0000bbbb00000000pppp0000p00p0000pppp0000p000"

    print("Display word UP")
    droneblocks_tello.display_image(image_string)
    time.sleep(3)

    print("change all purple colors to red.")
    image_string = droneblocks_tello.change_image_color(image_string, from_color=DroneBlocksTello.PURPLE,
                                                        to_color=DroneBlocksTello.RED)
    droneblocks_tello.display_image(image_string)
    time.sleep(3)

    droneblocks_tello.clear_everything()


if __name__ == '__main__':
    with DroneBlocksContextManager(motor_on=True) as db_tello:
        main(db_tello)
