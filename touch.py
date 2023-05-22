from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtCore import Qt, QSignalMapper, QTimer, QEventLoop
import sys
import os

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
    # label = QLabel("Built by Chad Duncan", win)
    # label.move(20, 0)

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


stylesheet = """
    QMainWindow {
        background-image: url("images/background.png");
        background-repeat: no-repeat;
        background-position: center;
    }
"""

app = QApplication([])
app.setStyleSheet(stylesheet)
win = QMainWindow()
win.setWindowTitle("Built by Chad Duncan")
win.resize(800, 480)
win.move(0, 0)
win.setWindowFlag(Qt.FramelessWindowHint)

configureUI(win)

sys.exit(app.exec_())
