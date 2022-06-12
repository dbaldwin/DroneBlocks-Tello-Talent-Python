from droneblocks.DroneBlocksTello import DroneBlocksTello
import time

"""

Usage:

python land.py

"""

if __name__ == '__main__':

    tello = DroneBlocksTello()

    print("Connect to Tello Drone")
    tello.connect()

    print("landing")
    tello.land()
    print("touchdown.... goodbye")
