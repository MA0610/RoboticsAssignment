
import time
from pycreate2 import Create2
port = "COM3" # TODO: Where is your serial port?
bot = Create2(port)
bot.sleep_timer = 1.5 # Mine had trouble with the default 0.5
bot.start() # Should play a high note
bot.safe() # Should play a click

time.sleep(1) #########
#h

bot.drive_direct(100,100)

FORWARD_SPEED = 100
MAX_DIFF = 100
MAX_SENSOR = 500


# TEST
while(True):
    sensors = bot.get_sensors()
    left = sensors.light_bumper_center_left
    right = sensors.light_bumper_center_right

    print(f"Left: {left}, Right: {right}")
    
    if left > right:
        adjust = int((left / MAX_SENSOR) * MAX_DIFF)
        print(f"Right adjust: {adjust}")
        bot.drive_direct(FORWARD_SPEED - adjust, FORWARD_SPEED + adjust)
    elif right > left:
        adjust = int((right / MAX_SENSOR) * MAX_DIFF)
        print(f"Right adjust: {adjust}")
        bot.drive_direct(FORWARD_SPEED - adjust, FORWARD_SPEED + adjust)