from droneblocks.DroneBlocksTello import DroneBlocksTello
import time

if __name__ == '__main__':
    print("Create Tello object")
    db_tello = DroneBlocksTello()

    print("Connect to Tello Drone")
    db_tello.connect()

    battery_level = db_tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")

    print("Pulse Top LED Red (raw command)")
    rtn = db_tello.send_command_with_return("EXT led br 1.0 255 0 0")
    print(rtn)
    time.sleep(3)

    print("Pulse LED Green")
    rtn = db_tello.pulse_top_led(r=0, g=255, b=0, freq=1.0)
    print(rtn)
    time.sleep(3)

    print("Pulse LED Blue")
    rtn = db_tello.pulse_top_led(r=0, g=0, b=255, freq=1.0)
    print(rtn)
    time.sleep(3)

    print("Set LED to Purple")
    rtn = db_tello.pulse_top_led(r=130, g=130, b=189, freq=1.0)
    print(rtn)
    time.sleep(3)

    print("Set LED to Yellow")
    rtn = db_tello.pulse_top_led(r=243, g=171, b=105, freq=1.0)
    print(rtn)
    time.sleep(3)

    for x in range(1, 25, 5):
        freq = x/10
        print(f"Pulse LED Blue at frequency: {freq}")
        db_tello.pulse_top_led(r=0, g=0, b=255, freq=freq)
        time.sleep(5)

    print("Set LED to OFF")
    rtn = db_tello.set_top_led(r=0, b=0, g=0)
    print(rtn)


