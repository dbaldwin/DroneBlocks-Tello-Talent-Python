from droneblocks.DroneBlocksTello import DroneBlocksTello
import time
from djitellopy import Tello

"""
* Tello class vs Script

"""

if __name__ == '__main__':

    print("Create Tello object")
    tello = DroneBlocksTello()

    print("Connect to Tello Drone")
    tello.connect()

    battery_level = tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")

    print("Takeoff!")
    tello.takeoff()

    print("Sleep for 5 seconds")
    time.sleep(5)

    print("landing")
    tello.land()
    print("touchdown.... goodbye")
