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

    tello.turn_motor_off()
