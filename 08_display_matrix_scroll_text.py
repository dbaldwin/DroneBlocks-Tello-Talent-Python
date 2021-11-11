from droneblocks.DroneBlocksTello import DroneBlocksTello
import time

if __name__ == '__main__':
    print("Create Tello object")
    db_tello = DroneBlocksTello()

    print("Connect to Tello Drone")
    db_tello.connect()

    battery_level = db_tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")

    # maximum is 70 characters
    # Scroll Text with SDK API to scroll text message from right to left
    db_tello.send_command_with_return(f"EXT mled l p 2.5 Hello From DroneBlocks")
    time.sleep(20)

    # Use DroneBlocksTello API to scroll text message from right to left
    scrolling_text = "Hello From DroneBlocks"
    db_tello.scroll_string(message=scrolling_text, scroll_dir=DroneBlocksTello.LEFT,
                           display_color=DroneBlocksTello.RED,
                           rate=2.5)

    time.sleep(20)

    # Scroll Up
    db_tello.scroll_string(message=scrolling_text, scroll_dir=DroneBlocksTello.UP,
                           display_color=DroneBlocksTello.BLUE,
                           rate=2.5)


    time.sleep(20)


    db_tello.clear_everything()


