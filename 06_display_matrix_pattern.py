from droneblocks.DroneBlocksTello import DroneBlocksTello
import time

if __name__ == '__main__':
    print("Create Tello object")
    db_tello = DroneBlocksTello()

    print("Connect to Tello Drone")
    db_tello.connect()

    battery_level = db_tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")

    # Use the Tello SDK 3.0 API to display pattern
    # display a blue 'up' arrow
    db_tello.send_command_with_return("EXT mled g 000bb00000bbbb000bbbbbb0000bb000000bb000000bb000000bb000000bb000")
    time.sleep(5)

    # display blue 'up' arrow using the DroneBlocks Tello method
    db_tello.display_up_arrow()
    time.sleep(3)

    # change the color of the arrow from blue to purple
    db_tello.display_up_arrow(display_color=DroneBlocksTello.PURPLE)
    time.sleep(3)

    # change the color of the arrow to red
    db_tello.display_up_arrow(display_color=DroneBlocksTello.RED)
    time.sleep(3)

    # display a down arrow
    db_tello.display_down_arrow()
    time.sleep(3)

    db_tello.display_down_arrow(display_color=DroneBlocksTello.PURPLE)
    time.sleep(3)

    db_tello.display_down_arrow(display_color=DroneBlocksTello.RED)
    time.sleep(3)

    db_tello.display_left_arrow()
    time.sleep(3)

    db_tello.display_left_arrow(display_color=DroneBlocksTello.PURPLE)
    time.sleep(3)

    db_tello.display_left_arrow(display_color=DroneBlocksTello.RED)
    time.sleep(3)

    db_tello.display_right_arrow()
    time.sleep(3)

    db_tello.display_right_arrow(display_color=DroneBlocksTello.PURPLE)
    time.sleep(3)

    db_tello.display_right_arrow(display_color=DroneBlocksTello.RED)
    time.sleep(3)

    db_tello.display_heart()
    time.sleep(3)


    db_tello.clear_everything()


