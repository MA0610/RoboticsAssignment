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

FORWARD_SPEED = 50
MAX_DIFF = 800
MAX_SENSOR = 500


# TEST
while(True):
    sensors = bot.get_sensors()
    left = max(sensors.light_bumper_left, sensors.light_bumper_center_left, sensors.light_bumper_front_left)
    right = max(sensors.light_bumper_right, sensors.light_bumper_center_right, sensors.light_bumper_front_right)

    print(f"Left: {left}, Right: {right}")
    
    if left > right:
        adjust = int((left / MAX_SENSOR) * MAX_DIFF)
        print(f"Right adjust: {adjust}")
        bot.drive_direct(FORWARD_SPEED - adjust, FORWARD_SPEED + adjust)
    elif right > left:
        adjust = int((right / MAX_SENSOR) * MAX_DIFF)
        print(f"Left adjust: {adjust}")
        bot.drive_direct(FORWARD_SPEED + adjust, FORWARD_SPEED - adjust)
    else:
        print("Straight")
        bot.drive_direct(FORWARD_SPEED, FORWARD_SPEED)

    time.sleep(0.05)
#


# sensors = bot.get_sensors()

# x = True

# l = False
# r = False

# while(x): 
#     sensors = bot.get_sensors()
#     # print("Bumper left: "+sensors.light_bumper_left+ "| Bumper center left: " + sensors.light_bumper_center_left + "| Bumper front left: "+sensors.light_bumper_front_left)
    

#     if(sensors.light_bumper_center_left>400):
#         bot.drive_stop()
#         l = True

#     if(sensors.light_bumper_center_right>400):
#         bot.drive_stop()
#         r = True
    
#     while (l):
#         bot.drive_direct(-50,50)
#         print(sensors.light_bumper_center_left)
#         if(sensors.light_bumper_center_left<200):
#             bot.drive_stop()
#             bot.drive_direct(100,100)

#             l = False

#     while (r):
#         bot.drive_direct(100,-100)
#         if(sensors.light_bumper_center_right<200):
#             bot.drive_stop()
#             bot.drive_direct(100,100)

#             r = False





# bot.drive_direct(100, 100)
# time.sleep(1)
# bot.drive_direct(200,-200) # inputs for motors are +/- 500 max
# time.sleep(2)
# bot.drive_stop()
#


# bot.start() #added this after to get sound

# sensors = bot.get_sensors()
# for i in range(100): 
#     sensors = bot.get_sensors()
#     print(sensors.light_bumper_left)

bot.stop() # Should play a low note


