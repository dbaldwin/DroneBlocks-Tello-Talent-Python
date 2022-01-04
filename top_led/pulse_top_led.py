from droneblocks.DroneBlocksTello import DroneBlocksTello
import time

# Source Virtual Environment
# MacOS:  source venv/bin/activate
# Windows: venv\Scripts\activate.bat
"""
Usage:

cd top_led
python pulse_top_led.py
"""


def main(droneblocks_tello):
    battery_level = droneblocks_tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")

    print("Pulse Top LED Red with frequency of 1Hz")
    rtn = droneblocks_tello.send_command_with_return("EXT led br 1.0 255 0 0")
    print(rtn)
    time.sleep(3)

    print("Pulse LED Green")
    rtn = droneblocks_tello.pulse_top_led(r=0, g=255, b=0, freq=1.0)
    print(rtn)
    time.sleep(3)

    print("Set LED to Yellow")
    rtn = droneblocks_tello.pulse_top_led(r=255, g=255, b=0, freq=1.0)
    print(rtn)
    time.sleep(3)

    for x in range(1, 25, 5):
        freq = x / 10
        print(f"Pulse LED Blue at frequency: {freq}")
        droneblocks_tello.pulse_top_led(r=0, g=0, b=255, freq=freq)
        time.sleep(5)

    print("Set LED to OFF")
    rtn = droneblocks_tello.set_top_led(r=0, b=0, g=0)
    print(rtn)


if __name__ == '__main__':
    print("Create Tello object")
    db_tello = DroneBlocksTello()
    try:
        print("Connect to Tello Drone")
        db_tello.connect()

        print("Turn motor to stay cool")
        db_tello.turn_motor_on()

        main(db_tello)

    finally:
        db_tello.turn_motor_off()
