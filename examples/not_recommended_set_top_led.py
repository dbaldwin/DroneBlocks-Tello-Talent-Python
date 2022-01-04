from droneblocks.DroneBlocksTello import DroneBlocksTello
import time

"""
Usage:
python not_recommeded_set_top_led.py
"""

print("Create DroneBlocks Tello object")
db_tello = DroneBlocksTello()

print("Connect to Tello Drone")
db_tello.connect()

print("Turn motor to stay cool")
db_tello.turn_motor_on()

battery_level = db_tello.get_battery()
print(f"Battery Life Percentage: {battery_level}")

print("Set LED to Green")
rtn = db_tello.set_top_led(r=0, g=255, b=0)
print(rtn)
time.sleep(3)

print("Set LED to OFF")
rtn = db_tello.set_top_led(r=0, g=0, b=0)
print(rtn)

db_tello.turn_motor_off()
