from droneblocks.DroneBlocksTello import DroneBlocksTello
import cv2
import droneblocks

"""
Usage

python 00_test_installation.py

"""

if __name__ == '__main__':
    print(f"DroneBlocks Util Version: {droneblocks.__version__}")
    db_tello = DroneBlocksTello()
    db_tello.display_smile()
    print(f"OpenCV Version: {cv2.__version__}")
    db_tello.connect()
    sdk_version = db_tello.query_sdk_version()
    print(f"Tello SDK Version: {sdk_version}")
    print("Your installation worked!")
    db_tello.clear_everything()