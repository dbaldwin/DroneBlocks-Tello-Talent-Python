from droneblocks.DroneBlocksContextManager import DroneBlocksContextManager
from droneblocks.DroneBlocksTello import DroneBlocksTello
import time

"""
Usage:

Connect to Robomaster Tello Talent WiFi (RMTT-??????)

cd display_matrix

python display_matrix_pattern_01.py

"""

def main(droneblocks_tello):
    battery_level = droneblocks_tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")

    # Use the Tello SDK 3.0 API to display pattern
    # display a blue 'up' arrow
    print("Display blue UP arrow using Tello SDK")
    droneblocks_tello.send_command_with_return("EXT mled g 000bb00000bbbb000bbbbbb0000bb000000bb000000bb000000bb000000bb000")
    time.sleep(5)

    print("display blue 'up' arrow using the DroneBlocks Tello method")
    droneblocks_tello.display_up_arrow()
    time.sleep(3)

    print("change the color of the arrow from blue to purple")
    droneblocks_tello.display_up_arrow(display_color=DroneBlocksTello.PURPLE)
    time.sleep(3)

    print("change the color of the arrow to red")
    droneblocks_tello.display_up_arrow(display_color=DroneBlocksTello.RED)
    time.sleep(3)

    print("display a down arrow")
    droneblocks_tello.display_down_arrow()
    time.sleep(3)

    print("change the color or down arrow to purple")
    droneblocks_tello.display_down_arrow(display_color=DroneBlocksTello.PURPLE)
    time.sleep(3)

    print("change the color or down arrow to red")
    droneblocks_tello.display_down_arrow(display_color=DroneBlocksTello.RED)
    time.sleep(3)

    print("display a 'left' arror")
    droneblocks_tello.display_left_arrow()
    time.sleep(3)

    print("change color of left arrow to purple")
    droneblocks_tello.display_left_arrow(display_color=DroneBlocksTello.PURPLE)
    time.sleep(3)

    print("change color of left arrow to red")
    droneblocks_tello.display_left_arrow(display_color=DroneBlocksTello.RED)
    time.sleep(3)

    print("display a 'right' arror")
    droneblocks_tello.display_right_arrow()
    time.sleep(3)

    print("change color of right arrow to purple")
    droneblocks_tello.display_right_arrow(display_color=DroneBlocksTello.PURPLE)
    time.sleep(3)

    print("change color of right arrow to red")
    droneblocks_tello.display_right_arrow(display_color=DroneBlocksTello.RED)
    time.sleep(3)

    print("display heart")
    droneblocks_tello.display_heart()
    time.sleep(3)

    print("clear display")
    droneblocks_tello.clear_everything()


if __name__ == '__main__':
    with DroneBlocksContextManager(motor_on=True) as db_tello:
        main(db_tello)
