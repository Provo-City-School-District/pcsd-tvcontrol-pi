from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtCore import Qt, QSignalMapper, QTimer, QEventLoop
import sys
import os
import subprocess
import threading
# import cv2
# import dbus
import picamera
import picamera.array
import numpy as np

os.environ['DISPLAY'] = ':0'

def delay(seconds):
    loop = QEventLoop()
    QTimer.singleShot(int(seconds * 1000), loop.quit)
    loop.exec_()

def handleButton(index):
    if index == 1:
        print("Epson ON")
        os.system('echo "pwr on" > /dev/ttyUSB0')
        delay(0.01)
    elif index == 2:
        print("Epson OFF")
        os.system('echo "source 30" > /dev/ttyUSB0')
        delay(3)
        os.system('echo "pwr off" > /dev/ttyUSB0')
        delay(0.5)
    elif index == 3:
        print("Epson Apple TV")
        os.system('echo "pwr on" > /dev/ttyUSB0')
        delay(0.01)
        os.system('echo "source 30" > /dev/ttyUSB0')
        delay(0.01)
    elif index == 4:
        print("Epson HDMI")
        os.system('echo "pwr on" > /dev/ttyUSB0')
        delay(0.01)
        os.system('echo "source a0" > /dev/ttyUSB0')
        delay(0.01)
    elif index == 5:
        print("Epson Volume Up")
        os.system('echo "vol inc" > /dev/ttyUSB0')
        delay(0.01)
    elif index == 6:
        print("Epson Volume Down")
        os.system('echo "vol dec" > /dev/ttyUSB0')
        delay(0.01)

def configureUI(win):
    buttonConfigs = {
        1: {"pos": (71, 44), "size": (160, 160), "image": "images/onbutton.png"},
        2: {"pos": (71, 270), "size": (160, 160), "image": "images/offbutton.png"},
        3: {"pos": (324, 44), "size": (160, 160), "image": "images/appletvbutton.png"},
        4: {"pos": (324, 270), "size": (160, 160), "image": "images/hdmibutton.png"},
        5: {"pos": (578, 44), "size": (160, 160), "image": "images/volumeupbutton.png"},
        6: {"pos": (578, 270), "size": (160, 160), "image": "images/volumedownbutton.png"}
    }

    signalMapper = QSignalMapper(win)
    signalMapper.mapped.connect(handleButton)

    for index, config in buttonConfigs.items():
        button = QPushButton(win)
        button.move(*config["pos"])
        button.resize(*config["size"])
        button.clicked.connect(signalMapper.map)
        signalMapper.setMapping(button, index)
        button.setStyleSheet(f"background-image: url({config['image']}); border: none;")

    win.show()

def preventScreensaver():
    subprocess.run(["xdotool", "mousemove", "1", "1"])


def disableScreensaver():
    print('motion detected')
    subprocess.run(['xset', 's', 'off'])
    preventScreensaver()


# def detectMotion():
#     # Your motion detection logic goes here
#     preventScreensaver()





def detectMotion():
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.framerate = 24

        # Initialize previous frame
        prev_frame = np.empty((480, 640, 3), dtype=np.uint8)

        while True:
            current_frame = np.empty((480, 640, 3), dtype=np.uint8)
            camera.capture(current_frame, 'rgb', use_video_port=True)

            # Calculate the absolute difference between the current frame and the previous frame
            frame_diff = np.abs(prev_frame.astype(np.int16) - current_frame.astype(np.int16)).astype(np.uint8)

            # Convert the frame difference to grayscale
            gray_diff = np.mean(frame_diff, axis=2)

            # Apply thresholding to get the binary image
            threshold = gray_diff > 30

            # Check if any significant change (motion detected)
            motion_detected = np.sum(threshold) > 100  # Adjust the threshold as per your requirements

            if motion_detected:
                disableScreensaver()

            prev_frame = current_frame







def main():
    app = QApplication([])
    app.setOverrideCursor(Qt.BlankCursor)

    stylesheet = """
        QMainWindow {
            background-image: url("images/background.png");
            background-repeat: no-repeat;
            background-position: center;
        }
    """
    app.setStyleSheet(stylesheet)

    win = QMainWindow()
    win.setWindowTitle("Built by Chad Duncan")
    win.resize(800, 480)
    win.move(0, 0)
    win.setWindowFlag(Qt.FramelessWindowHint)

    configureUI(win)

    # Create and start the motion detection thread
    motion_thread = threading.Thread(target=detectMotion)
    motion_thread.start()

    # Create and start the screensaver prevention thread
    screensaver_thread = threading.Thread(target=preventScreensaver)
    screensaver_thread.start()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
