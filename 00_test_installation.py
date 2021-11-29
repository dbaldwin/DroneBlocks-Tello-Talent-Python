from droneblocks.DroneBlocksTello import DroneBlocksTello
import cv2
import droneblocks

if __name__ == '__main__':
    print(f"DroneBlocks Util Version: {droneblocks.__version__}")
    db_tello = DroneBlocksTello()
    print(f"OpenCV Version: {cv2.__version__}")
    print("Your installation worked!")