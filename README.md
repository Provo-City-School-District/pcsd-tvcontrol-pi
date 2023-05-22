# pcsd-tvcontrol-pi
This is a Python program designed to control projectors using a Raspberry Pi with a touchscreen. It can also be adapted to work with other devices connected to projectors or TVs. Additionally, it can be modified to control TVs with CEC capabilities.

## Build Environment (Recommended)
Please note that you may need to modify the commands below based on your specific device. Different operating systems have varying default installation methods, so replace "python" with "python3" and "pip" with "pip3" if necessary.

Clone <br>
```git clone https://github.com/Provo-City-School-District/pcsd-tvcontrol-pi.git``` <br>
<br>
Change to the repository directory: <br>
```cd pcsd-tvcontrol-pi``` <br>
<br>
Create a virtual environment: <br>
```python3 -m venv env``` <br>
<br>
Activate the virtual environment: <br>
macOS/Linux <br>
```source env/bin/activate``` <br>
Windows: <br>
```.\env\Scripts\activate``` <br>
<br>
Install dependencies if not already installed:<br>
```pip install -r requirements.txt``` <br>

## Starting from Crontab
Open the crontab file:<br>
```crontab -e``` <br>
<br>
running with a start script with crontab so that the program executes at startup. Remember, if you're using a vevn to call that python<br>
```@reboot sleep 15 && cd /home/pi/pcsd-tvcontrol-pi/ && /bin/python3 /home/pi/pcsd-tvcontrol-pi/touch.py >> /home/pi/cron.log 2>&1``` <br>

## ScreenSaver (optional) 
If desired, you can install Xscreensaver: <br>
```sudo apt install xscreensaver xscreensaver-data xscreensaver-data-extra -y``` <br>

## Optional Installations
### Linux
To further enhance the program, you can consider the following optional installations: <br>
<br>
Unclutter: Removes mouse display when not in use. <br>
```sudo apt install unclutter -y``` <br>
Xdotool: Allows automation and simulation of keyboard and mouse input. <br>
```sudo apt install xdotool -y``` <br>


## Optimization Changes

- Eliminated the need for the `time` module by using other parts of PyQt.
- Used a dictionary to store button configurations, reducing code duplication.
- Created a signal mapper for button clicks to simplify the code and eliminate the need for separate functions for each button.
- Moved the UI configuration code into a separate function for better code organization and readability.
- Uses venv ti insure proper modules
