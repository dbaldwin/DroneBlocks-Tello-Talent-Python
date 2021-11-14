from droneblocks.DroneBlocksTello import DroneBlocksTello
import time

if __name__ == '__main__':
    print("Create Tello object")
    db_tello = DroneBlocksTello()

    print("Connect to Tello Drone")
    db_tello.connect()

    battery_level = db_tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")

    db_tello.send_command_with_return(f"EXT mled s p a")
    time.sleep(3)

    db_tello.send_command_with_return(f"EXT mled s b A")
    time.sleep(3)

    db_tello.send_command_with_return(f"EXT mled s r heart")
    time.sleep(3)

    db_tello.display_character('d', DroneBlocksTello.PURPLE)
    time.sleep(3)

    db_tello.display_character('D', DroneBlocksTello.BLUE)
    time.sleep(3)

    db_tello.display_heart(DroneBlocksTello.RED)
    time.sleep(3)

    db_tello.clear_everything()
