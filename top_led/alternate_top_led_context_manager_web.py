from droneblocks.DroneBlocksContextManager import DroneBlocksContextManager
import time

# Source Virtual Environment
# MacOS:  source venv/bin/activate
# Windows: venv\Scripts\activate.bat
"""
Usage:

cd top_led
python alternate_top_led_context_manager_web.py

"""


def main(droneblocks_tello):
    print("Alternate Top LED at a freq of 1.0")
    rtn = droneblocks_tello.alternate_top_led(r1=10, g1=0, b1=0, r2=0, g2=0, b2=10, freq=1.0)
    print(rtn)
    time.sleep(300)  # sleep for 5 minutes so we can use the web application


if __name__ == '__main__':
    print("Create Tello object")
    with DroneBlocksContextManager(motor_on=True, start_tello_web=True) as db_tello:
        # only setting brightness to better recording
        db_tello.set_display_brightness(10)
        main(db_tello)
