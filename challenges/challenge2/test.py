from droneblocks.DroneBlocksTello import DroneBlocksTello
import logging
import time

if __name__ == '__main__':
    db_tello = DroneBlocksTello()

    db_tello.LOGGER.setLevel(logging.INFO)

    db_tello.connect()

    print("Start Challenge 2 ")
    db_tello.takeoff()
    print("DONE")

    time.sleep(5)
    print("ff1")
    db_tello.fly_forward(30, 'in')
    print("DONE")

    time.sleep(1)
    print("ccw1")
    db_tello.rotate_counter_clockwise(90)
    print("DONE")

    time.sleep(1)
    print("ff2")
    db_tello.fly_forward(30, 'in')
    print("DONE")

    time.sleep(1)
    print("ccw2")
    db_tello.rotate_counter_clockwise(90)
    print("DONE")

    time.sleep(1)
    print("ff3")
    db_tello.fly_forward(30, 'in')
    print("DONE")

    time.sleep(1)
    print("ccw3")
    db_tello.rotate_counter_clockwise(90)
    print("DONE")

    time.sleep(1)
    print("ff4")
    db_tello.fly_forward(30, 'in')
    print("DONE")

    time.sleep(1)
    print("ccw4")
    db_tello.rotate_counter_clockwise(90)
    print("DONE")

    time.sleep(1)
    print("land")
    time.sleep(2)
    db_tello.land()
    print("DONE")
