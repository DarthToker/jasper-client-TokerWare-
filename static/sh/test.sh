#! /bin/sh
# /home/pi/fullscreen.sh

sleep 5s;

# this does the same job as pressing the F11 key to force Kiosk mode
xte "key F11" -x:0 &
