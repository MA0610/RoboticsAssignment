import time
from pycreate2 import Create2

port = "COM3"  # TODO: Set your serial port correctly
bot = Create2(port)
bot.sleep_timer = 1.5
bot.start()          
bot.safe()        

time.sleep(1)

FORWARD_SPEED = 50
MAX_DIFF = 800
MAX_SENSOR = 500

while True:
    sensors = bot.get_sensors()
    left = max(sensors.light_bumper_left, sensors.light_bumper_center_left, sensors.light_bumper_front_left)
    right = max(sensors.light_bumper_right, sensors.light_bumper_center_right, sensors.light_bumper_front_right)

    sensor_val = left if left < right else right
    adjust = int((sensor_val / MAX_SENSOR) * MAX_DIFF)

    sign = 1 if left < right else (-1 if right < left else 0)

    left_adjust = sign * adjust
    right_adjust = -left_adjust

    bot.drive_direct(FORWARD_SPEED + left_adjust, FORWARD_SPEED + right_adjust)

    print(f"Left: {left}, Right: {right}, Adjust: {adjust}, Sign: {sign}")
    time.sleep(0.1)