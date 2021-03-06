from djitellopy import Tello
from DroneBlocksTello import DroneBlocksTello
import time
import random

if __name__ == '__main__':

    print("Create Tello object")
    tello = Tello()
    db_tello = DroneBlocksTello()

    print("Connect to Tello Drone")
    tello.connect()

    battery_level = tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")

    for _ in range(0,10):
        tello.send_command_with_return(f"EXT led bl 1 {random.randint(1,255)} {random.randint(1,255)} {random.randint(1,255)} {random.randint(1,255)} {random.randint(1,255)} {random.randint(1,255)}")
        time.sleep(4)

    time.sleep(1)
    db_tello.blink_led_color(255, 0, 0, 0, 0, 255, 0.5)