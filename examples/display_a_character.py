from droneblocks.DroneBlocksContextManager import DroneBlocksContextManager
import time

"""
Usage:
cd examples

python display_a_character.py

"""


def main(droneblocks_tello):
    droneblocks_tello.display_character("@")
    time.sleep(3)

    droneblocks_tello.display_character("%")
    time.sleep(3)

    droneblocks_tello.display_character("#")
    time.sleep(3)

    droneblocks_tello.display_character("?")
    time.sleep(3)

    droneblocks_tello.display_character(">")
    time.sleep(3)

    droneblocks_tello.display_character("<")
    time.sleep(3)

if __name__ == '__main__':
    print("Create DroneBlocksContextManager")
    with DroneBlocksContextManager(motor_on=True) as db_tello:
        main(db_tello)
