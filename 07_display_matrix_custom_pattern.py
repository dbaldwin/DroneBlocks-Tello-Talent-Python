from droneblocks.DroneBlocksTello import DroneBlocksTello
import time

if __name__ == '__main__':
    print("Create Tello object")
    db_tello = DroneBlocksTello()

    print("Connect to Tello Drone")
    db_tello.connect()

    battery_level = db_tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")

    # Use the DroneBlocks TT Pattern Generator to design a pattern and use the generated string here
    # This pattern is from the lecture showing the work UP
    image_string = "b00b0000b00b0000b00b0000bbbb00000000pppp0000p00p0000pppp0000p000"

    db_tello.display_image(image_string)
    time.sleep(3)

    # change all purple colors to red.
    image_string = db_tello.change_image_color(image_string, from_color=DroneBlocksTello.PURPLE, to_color=DroneBlocksTello.RED)
    db_tello.display_image(image_string)
    time.sleep(3)

    db_tello.clear_everything()


