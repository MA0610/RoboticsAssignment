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


    print(f"Left: {left}, Right: {right}")

    # Follow (switching both left/right and +/-)
    if left < right:
        left_adjust = int((left / MAX_SENSOR) * MAX_DIFF * -1)
        right_adjust = int((left / MAX_SENSOR) * MAX_DIFF)
        print(f"Right adjust: {adjust}")
        bot.drive_direct(FORWARD_SPEED + left_adjust, FORWARD_SPEED + right_adjust)
    elif right < left:
        adjust = int((right / MAX_SENSOR) * MAX_DIFF)
        print(f"Left adjust: {adjust}")
        bot.drive_direct(FORWARD_SPEED - adjust, FORWARD_SPEED + adjust)
    else:
        print("Straight")
        bot.drive_direct(FORWARD_SPEED, FORWARD_SPEED)

    # Follow (switching (+ => -))
    # This worked better than switching signs. When object is in dead center it tends to jerk around.
    # if left > right:
    #     adjust = int((left / MAX_SENSOR) * MAX_DIFF)
    #     print(f"Right adjust: {adjust}")
    #     bot.drive_direct(FORWARD_SPEED + adjust, FORWARD_SPEED - adjust)
    # elif right > left:
    #     adjust = int((right / MAX_SENSOR) * MAX_DIFF)
    #     print(f"Left adjust: {adjust}")
    #     bot.drive_direct(FORWARD_SPEED - adjust, FORWARD_SPEED + adjust)
    # else:
    #     print("Straight")
    #     bot.drive_direct(FORWARD_SPEED, FORWARD_SPEED)
    
    # Follow (switching left > right to left < right etc)
    # This worked but was a bit janky didn't move as strong.
    # if left < right:
    #     adjust = int((left / MAX_SENSOR) * MAX_DIFF)
    #     print(f"Right adjust: {adjust}")
    #     bot.drive_direct(FORWARD_SPEED - adjust, FORWARD_SPEED + adjust)
    # elif right < left:
    #     adjust = int((right / MAX_SENSOR) * MAX_DIFF)
    #     print(f"Left adjust: {adjust}")
    #     bot.drive_direct(FORWARD_SPEED + adjust, FORWARD_SPEED - adjust)
    # else:
    #     print("Straight")
    #     bot.drive_direct(FORWARD_SPEED, FORWARD_SPEED)

    time.sleep(0.05)
#

