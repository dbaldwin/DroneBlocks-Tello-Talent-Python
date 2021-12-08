from droneblocks.DroneBlocksTello import DroneBlocksTello
from droneblocks.DroneBlocksContextManager import DroneBlocksContextManager
import time


def main(droneblocks_tello):
    battery_level = droneblocks_tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")

    droneblocks_tello.send_command_with_return(f"EXT mled s p a")
    time.sleep(3)

    droneblocks_tello.send_command_with_return(f"EXT mled s b A")
    time.sleep(3)

    droneblocks_tello.send_command_with_return(f"EXT mled s r heart")
    time.sleep(3)

    droneblocks_tello.display_character('d', DroneBlocksTello.PURPLE)
    time.sleep(3)

    droneblocks_tello.display_character('D', DroneBlocksTello.BLUE)
    time.sleep(3)

    droneblocks_tello.display_character('3', DroneBlocksTello.RED)
    time.sleep(3)

    droneblocks_tello.display_heart(DroneBlocksTello.RED)
    time.sleep(3)

    droneblocks_tello.clear_everything()


if __name__ == '__main__':
    with DroneBlocksContextManager(motor_on=True) as db_tello:
        main(delattr())
