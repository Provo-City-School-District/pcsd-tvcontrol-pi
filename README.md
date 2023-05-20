# pcsd-tvcontrol-pi
python program to control projectors using a raspberry pi with a touchscreen. could be implimented to any device that is connected to a projector or TV though. could be modified to control TV with CEC capabilities

## build environment (Recommended)
be aware that you might need to modify the commands mentioned below, replacing "python" with "python3" and "pip" with "pip3" depending on your device, as different operating systems have varying default installation methods.

Clone \\
```git clone https://github.com/Provo-City-School-District/pcsd-tvcontrol-pi.git``` \\
Change to the repository directory: \\
```cd pcsd-tvcontrol-pi``` \\
Create a virtual environment: \\
```python3 -m venv env``` \\
Activate \\
Mac/Linux \\
```source env/bin/activate``` \\
On Windows: \\
```.\env\Scripts\activate``` \\
install dependencies if not already installed \\
```pip install -r requirements.txt``` \\

## start from crontab
running with a start script with crontab so that the program executes at startup. \\
```@reboot sleep 15 && /home/pi/pcsd-tvcontrol-pi/start.sh``` \\

## ScreenSaver (optional) 
### Xscreensaver Installation
```sudo apt install xscreensaver xscreensaver-data xscreensaver-data-extra -y``` \\

## optional installations
### Linux
unclutter - removes mouse display while not in use \\
```sudo apt install unclutter -y``` \\
xdotool - allows you to automate and simulate keyboard and mouse input \\
```sudo apt install xdotool -y``` \\
