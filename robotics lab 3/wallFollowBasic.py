import time
from pycreate2 import Create2
port = "COM3" # TODO: Where is your serial port?
bot = Create2(port)
bot.sleep_timer = 1.5 # Mine had trouble with the default 0.5
bot.start() # Should play a high note
bot.safe() # Should play a click

time.sleep(1) #########
#

bot.drive_direct(100,100)

FORWARD_SPEED = 50
MAX_DIFF = 800
MAX_SENSOR = 500


# TEST
while(True):
    sensors = bot.get_sensors()
    left = max(sensors.light_bumper_left, sensors.light_bumper_center_left, sensors.light_bumper_front_left)
    right = max(sensors.light_bumper_right, sensors.light_bumper_center_right, sensors.light_bumper_front_right)


    # print(f"Left: {left}, Right: {right}")



    if(left > 400):
        bot.drive_direct(100,-100)
    
    if(left < 150):
        bot.drive_direct(100,100)


    # if(sensors.light_bumper_front_left > 300):
    #     bot.drive_direct(100,-100)
    
    # if(sensors.light_bumper_center_left < 200):
    #     bot.drive_direct(100,100)
    

    # time.sleep(0.05)
#

