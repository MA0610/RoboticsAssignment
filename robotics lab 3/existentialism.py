import time
from pycreate2 import Create2
from pylab import *
port = "COM3" # TODO: Where is your serial port?
bot = Create2(port)
bot.sleep_timer = 1.5 # Mine had trouble with the default 0.5
bot.start() # Should play a high note
bot.safe() # Should play a click

time.sleep(1) #########
#h

bot.drive_direct(100,100)

FORWARD_SPEED = 100
MAX_DIFF = 800
MAX_SENSOR = 500

while(True):
    sensors = bot.get_sensors()
    left = max(sensors.light_bumper_left, sensors.light_bumper_center_left, sensors.light_bumper_front_left)
    right = max(sensors.light_bumper_right, sensors.light_bumper_center_right, sensors.light_bumper_front_right)


    print(f"Left: {left}, Right: {right}")
    if left == sensors.light_bumper_center_left :
        bot.drive_direct(FORWARD_SPEED - 15, FORWARD_SPEED)
    else :
        left_adjust = int((left / MAX_SENSOR) * MAX_DIFF)
        right_adjust = int((right / MAX_SENSOR) * MAX_DIFF)
        print(f"Right adjust: {right_adjust}")
        print(f"Left adjust: {left_adjust}") 
        bot.drive_direct(FORWARD_SPEED - left_adjust, FORWARD_SPEED - right_adjust)

bot.stop()