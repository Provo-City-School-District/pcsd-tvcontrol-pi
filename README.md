# pcsd-tvcontrol-pi
python program to control projectors. could be modified to control TV with CEC capabilities

## start from crontab
running with a start script with crontab so that the program executes at startup
```@reboot sleep 15 && /home/pi/pcsd-tvcontrol-pi/start.sh```

## xscreensaver configuration
```sudo apt install xscreensaver xscreensaver-data xscreensaver-data-extra -y```

## optional installations
unclutter - removes mouse display while not in use
```sudo apt install unclutter -y```

xdotool - 
```sudo apt install xdotool -y```
