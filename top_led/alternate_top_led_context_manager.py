from droneblocks.DroneBlocksContextManager import DroneBlocksContextManager
from alternate_top_led import main as alternate_main

"""
Usage:

python alternate_top_led_context_manager.py

"""


def main(droneblocks_tello):
    alternate_main(droneblocks_tello)


if __name__ == '__main__':
    with DroneBlocksContextManager(motor_on=True) as db_tello:
        main(db_tello)
