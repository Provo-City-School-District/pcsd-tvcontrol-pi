from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtCore import Qt
import sys
from time import sleep
import os

os.environ['DISPLAY'] = ':0'

def clickMethod1():
    print ("Epson ON")
    os.system('echo "pwr on" > /dev/ttyUSB0')
    sleep(.01)


def clickMethod2():
    print ("Epson OFF")
    os.system('echo "source 30" > /dev/ttyUSB0')
    sleep(3)
    os.system('echo "pwr off" > /dev/ttyUSB0')
    sleep(.5)


def clickMethod3():
    print ("Epson Apple TV")
    os.system('echo "pwr on" > /dev/ttyUSB0')
    sleep(.01)
    os.system('echo "source 30" > /dev/ttyUSB0')
    sleep(.01)


def clickMethod4():
    print ("Epson HDMI")
    os.system('echo "pwr on" > /dev/ttyUSB0')
    sleep(.01)
    os.system('echo "source a0" > /dev/ttyUSB0')
    sleep(.01)


def clickMethod5():
    print ("Epson Volume Up")
    os.system('echo "vol inc" > /dev/ttyUSB0')
    sleep(.01)


def clickMethod6():
    print ("Epson Volume Down")
    os.system('echo "vol dec" > /dev/ttyUSB0')
    sleep(.01)


stylesheet = """
    QMainWindow {
        background-image: url("background.png"); 
        background-repeat: no-repeat; 
        background-position: center;
    }
"""

app = QApplication([])
app.setStyleSheet(stylesheet)
win = QMainWindow()
win.setWindowTitle("Test")
win.resize(800,480)
win.move(0,0)
win.setWindowFlag(Qt.FramelessWindowHint)

label = QLabel("Built by Chad Duncan", win)
label.move(20,0)

button1 = QPushButton(win)
button1.move(71,44) #edge, top
button1.resize(160,160)
button1.clicked.connect(clickMethod1)
button1.setStyleSheet("background-image : url(onbutton.png); border: none;")


button2 = QPushButton(win)
button2.move(71,270) #edge, top
button2.resize(160,160)
button2.clicked.connect(clickMethod2)
button2.setStyleSheet("background-image : url(offbutton.png); border: none;")

button3 = QPushButton(win)
button3.move(324,44) #(edge, top)
button3.resize(160,160)
button3.clicked.connect(clickMethod3)
button3.setStyleSheet("background-image : url(appletvbutton.png); border: none;")

button4 = QPushButton(win)
button4.move(324,270) #(edge, top)
button4.resize(160,160)
button4.clicked.connect(clickMethod4)
button4.setStyleSheet("background-image : url(hdmibutton.png); border: none;")

button5 = QPushButton(win)
button5.move(578,44) #(edge, top)
button5.resize(160,160)
button5.setAutoRepeat(True)
button5.setAutoRepeatDelay(500)
button5.setAutoRepeatInterval(500)
button5.clicked.connect(clickMethod5)
button5.setStyleSheet("background-image : url(volumeupbutton.png); border: none;")

button6 = QPushButton(win)
button6.move(578,270) #(edge, top)
button6.resize(160,160)
button6.setAutoRepeat(True)
button6.setAutoRepeatDelay(500)
button6.setAutoRepeatInterval(500)
button6.clicked.connect(clickMethod6)
button6.setStyleSheet("background-image : url(volumedownbutton.png); border: none;")


win.show()

sys.exit(app.exec_())
