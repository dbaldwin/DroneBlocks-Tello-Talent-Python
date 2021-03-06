from droneblocks.DroneBlocksTello import DroneBlocksTello
import time

# Source Virtual Environment
# MacOS:  source venv/bin/activate
# Windows: venv\Scripts\activate.bat
"""
Usage:

cd top_led
python set_top_led.py
"""

def main(droneblocks_tello):
    battery_level = droneblocks_tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")

    print("Set Top LED to red.")
    rtn = droneblocks_tello.send_command_with_return("EXT led 255 0 0")
    print(rtn)
    time.sleep(3)

    print("Set LED to Green")
    rtn = droneblocks_tello.set_top_led(r=0, g=255, b=0)
    print(rtn)
    time.sleep(3)

    print("Set LED to Blue")
    rtn = droneblocks_tello.set_top_led(r=0, g=0, b=255)
    print(rtn)
    time.sleep(3)

    print("Set LED to Yellow")
    rtn = droneblocks_tello.set_top_led(r=255, g=255, b=0)
    print(rtn)
    time.sleep(3)

    print("Set LED to OFF")
    rtn = droneblocks_tello.set_top_led(r=0, g=0, b=0)
    print(rtn)


if __name__ == '__main__':
    print("Create DroneBlocks Tello object")
    db_tello = DroneBlocksTello()
    try:
        print("Connect to Tello Drone")
        db_tello.connect()

        print("Turn motor to stay cool")
        db_tello.turn_motor_on()

        # only setting brightness to better recording
        db_tello.set_display_brightness(10)

        print("Call the main function")
        main(db_tello)
    finally:
        print("Turn motors off")
        db_tello.turn_motor_off()

    print("Done")
