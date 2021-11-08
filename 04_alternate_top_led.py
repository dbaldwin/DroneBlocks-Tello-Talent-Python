from droneblocks.DroneBlocksTello import DroneBlocksTello
import time

if __name__ == '__main__':
    print("Create Tello object")
    db_tello = DroneBlocksTello()

    print("Connect to Tello Drone")
    db_tello.connect()

    battery_level = db_tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")

    print("Alternate Top LED between red and blue (raw command)")
    rtn = db_tello.send_command_with_return("EXT led bl 1.0 255 0 0 0 0 255")
    print(rtn)
    time.sleep(3)

    print("Alternate Top LED")
    rtn = db_tello.alternate_top_led(r1=0, g1=255, b1=0, r2=255, g2=0, b2=255, freq=1.0)
    print(rtn)
    time.sleep(3)

    for x in range(1, 30, 5):
        freq = x/10
        print(f"Pulse LED Blue at frequency: {freq}")
        db_tello.alternate_top_led(r1=0, g1=255, b1=0, r2=255, g2=0, b2=255, freq=freq)
        time.sleep(5)


    print("Set LED to OFF")
    rtn = db_tello.set_top_led(r=0, b=0, g=0)
    print(rtn)


