from droneblocks.DroneBlocksTello import DroneBlocksTello

"""
* Tello class vs Script

"""

if __name__ == '__main__':

    print("Create Tello object")
    tello = DroneBlocksTello()

    print("Connect to Tello Drone")
    tello.connect()

    tello.land()
