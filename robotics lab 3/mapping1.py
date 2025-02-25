import time
from math import sin, cos, radians
import matplotlib.pyplot as plt
from pycreate2 import Create2

def test_movement(bot):

    print("Starting test movement...")
    # Move forward
    bot.drive_direct(50, 50)
    time.sleep(2)
    # Stop
    bot.drive_direct(0, 0)
    time.sleep(1)
    # Rotate in place (left wheel forward, right wheel backward)
    bot.drive_direct(50, -50)
    time.sleep(1)
    # Stop
    bot.drive_direct(0, 0)
    time.sleep(1)
    print("Test movement complete.\n")

port = "COM7"
bot = Create2(port)
bot.sleep_timer = 1.5
bot.start()
bot.safe()

time.sleep(1)  # Let the robot settle

# Perform test movement to verify motion
test_movement(bot)


x, y, theta = 0.0, 0.0, 0.0
path = [(x, y)]  # List to record positions over time

# Parameters for the Braitenberg behavior
FORWARD_SPEED = 30    # Lower speed for safety
MAX_DIFF = 400        # Reduced maximum adjustment
MAX_SENSOR = 500

# Helper function to clamp values within a specified range
def clamp(val, min_val, max_val):
    return max(min(val, max_val), min_val)

try:
    while True:
        sensors = bot.get_sensors()

        # Safely read light bumper sensor values; if missing, skip this cycle
        try:
            left = max(sensors.light_bumper_left,
                       sensors.light_bumper_center_left,
                       sensors.light_bumper_front_left)
            right = max(sensors.light_bumper_right,
                        sensors.light_bumper_center_right,
                        sensors.light_bumper_front_right)
        except AttributeError:
            print("Error reading bumper sensors. Skipping this cycle.")
            time.sleep(0.05)
            continue

        try:
            d = sensors.distance  # Distance trave in mm)
            a = sensors.angle     # Angle turned (in degrees)
        except AttributeError:
            d, a = 0, 0


        if abs(d) > 1000 or abs(a) > 90:
            print("Odometry reading out of range. Skipping update.")
            d, a = 0, 0


        a_rad = radians(a)
        theta_mid = theta + a_rad / 2
        x += d * cos(theta_mid)
        y += d * sin(theta_mid)
        theta += a_rad
        path.append((x, y))

        print(f"Pose: x={x:.2f}, y={y:.2f}, theta={theta:.2f}")
        print(f"Light Sensors: Left = {left}, Right = {right}")

        if left < right:
            left_adjust = int(clamp((left / MAX_SENSOR) * MAX_DIFF, -MAX_DIFF, MAX_DIFF))
            right_adjust = int(clamp((left / MAX_SENSOR) * MAX_DIFF, -MAX_DIFF, MAX_DIFF))
            left_adjust = -left_adjust
            left_speed = clamp(FORWARD_SPEED + left_adjust, -100, 100)
            right_speed = clamp(FORWARD_SPEED + right_adjust, -100, 100)
            bot.drive_direct(left_speed, right_speed)
            print(f"Adjustments: left_speed={left_speed}, right_speed={right_speed}")
        elif right < left:
            adjust = int(clamp((right / MAX_SENSOR) * MAX_DIFF, -MAX_DIFF, MAX_DIFF))
            left_speed = clamp(FORWARD_SPEED - adjust, -100, 100)
            right_speed = clamp(FORWARD_SPEED + adjust, -100, 100)
            bot.drive_direct(left_speed, right_speed)
            print(f"Adjustment: left_speed={left_speed}, right_speed={right_speed}")
        else:
            print("Going straight")
            bot.drive_direct(FORWARD_SPEED, FORWARD_SPEED)

        time.sleep(0.05)

except KeyboardInterrupt:
    print("KeyboardInterrupt detected. Exiting loop.")
except Exception as e:
    print("Unexpected error:", e)
finally:
    try:
        # Stop the robot safely
        bot.drive_direct(0, 0)
        print("Robot stopped safely.")
    except Exception as e:
        print("Error while stopping the robot:", e)

    if len(path) > 0:
        xs, ys = zip(*path)
        plt.figure()
        plt.plot(xs, ys, marker='o', linestyle='-')
        plt.xlabel("X Position (mm)")
        plt.ylabel("Y Position (mm)")
        plt.title("Robot Path Map")
        plt.axis('equal')
        plt.grid(True)
        plt.show()
    else:
        print("No path recorded.")




