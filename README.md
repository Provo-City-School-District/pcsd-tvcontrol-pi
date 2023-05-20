# pcsd-tvcontrol-pi
python program to control projectors using a raspberry pi with a touchscreen. could be implimented to any device that is connected to a projector or TV though. could be modified to control TV with CEC capabilities

## build environment (Recommended)
be aware that you might need to modify the commands mentioned below, replacing "python" with "python3" and "pip" with "pip3" depending on your device, as different operating systems have varying default installation methods.

Clone <br>
```git clone https://github.com/Provo-City-School-District/pcsd-tvcontrol-pi.git``` <br>
<br>
Change to the repository directory: <br>
```cd pcsd-tvcontrol-pi``` <br>
<br>
Create a virtual environment: <br>
```python3 -m venv env``` <br>
<br>
Activate <br>
Mac/Linux <br>
```source env/bin/activate``` <br>
On Windows: <br>
```.\env\Scripts\activate``` <br>
<br>
install dependencies if not already installed <br>
```pip install -r requirements.txt``` <br>

## start from crontab
running with a start script with crontab so that the program executes at startup. <br>
```@reboot sleep 15 && /home/pi/pcsd-tvcontrol-pi/start.sh``` <br>

## ScreenSaver (optional) 
### Xscreensaver Installation
```sudo apt install xscreensaver xscreensaver-data xscreensaver-data-extra -y``` <br>

## optional installations
### Linux
unclutter - removes mouse display while not in use <br>
```sudo apt install unclutter -y``` <br>
xdotool - allows you to automate and simulate keyboard and mouse input <br>
```sudo apt install xdotool -y``` <br>
