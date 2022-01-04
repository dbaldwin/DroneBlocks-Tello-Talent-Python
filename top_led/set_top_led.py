from droneblocks.DroneBlocksTello import DroneBlocksTello
import time

"""
Usage:

python set_top_led.py

"""


def main(droneblocks_tello):
    battery_level = droneblocks_tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")

    print("Pulse Top LED raw command")
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
    rtn = droneblocks_tello.set_top_led(r=255, g=0, b=255)
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

        main(db_tello)
    finally:
        db_tello.turn_motor_off()
