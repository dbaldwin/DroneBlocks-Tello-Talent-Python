from droneblocks.DroneBlocksTello import DroneBlocksTello
import time

if __name__ == '__main__':
    print("Create DroneBlocks Tello object")
    db_tello = DroneBlocksTello()

    print("Connect to Tello Drone")
    db_tello.connect()

    battery_level = db_tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")

    print("Pulse Top LED raw command")
    rtn = db_tello.send_command_with_return("EXT led 255 0 0")
    print(rtn)
    time.sleep(3)

    print("Set LED to Green")
    rtn = db_tello.set_top_led(r=0, g=255, b=0)
    print(rtn)
    time.sleep(3)

    print("Set LED to Blue")
    rtn = db_tello.set_top_led(r=0, g=0, b=255)
    print(rtn)
    time.sleep(3)

    print("Set LED to Purple")
    rtn = db_tello.set_top_led(r=130, g=130, b=189)
    print(rtn)
    time.sleep(3)

    print("Set LED to Yellow")
    rtn = db_tello.set_top_led(r=243, g=171, b=105)
    print(rtn)
    time.sleep(3)

    print("Set LED to OFF")
    rtn = db_tello.set_top_led(r=0, g=0, b=0)
    print(rtn)


