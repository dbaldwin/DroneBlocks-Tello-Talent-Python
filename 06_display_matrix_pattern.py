from droneblocks.DroneBlocksTello import DroneBlocksTello
import time

if __name__ == '__main__':
    print("Create Tello object")
    db_tello = DroneBlocksTello()

    print("Connect to Tello Drone")
    db_tello.connect()

    battery_level = db_tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")

    db_tello.display_heart()
    time.sleep(3)

    db_tello.display_up_arrow()
    time.sleep(3)

    db_tello.display_up_arrow(display_color=DroneBlocksTello.PURPLE)
    time.sleep(3)

    db_tello.display_up_arrow(display_color=DroneBlocksTello.RED)
    time.sleep(3)

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

    db_tello.clear_everything()


