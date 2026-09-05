WHEEL_RADIUS=0.045
WHEEL_BASE=0.30
import math
from controller import Robot

robot = Robot()
camera=robot.getDevice('camera')
imu= robot.getDevice('imu')
lidar=robot.getDevice('lidar')
left_motor = robot.getDevice('LEFT_WHEEL_MOTOR')
right_motor = robot.getDevice('RIGHT_WHEEL_MOTOR')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
timestep = int(robot.getBasicTimeStep())
x=0.0
y=0.0
theta=0.0
last_left=0.0
last_right=0.0
left_encoder = robot.getDevice('LEFT_WHEEL sensor')
right_encoder = robot.getDevice('RIGHT_WHEEL sensor')
camera.enable(timestep)
imu.enable(timestep)
lidar.enable(timestep)
left_encoder.enable(timestep)
right_encoder.enable(timestep)

while robot.step(timestep) != -1:
    print(left_encoder.getValue(), right_encoder.getValue())
    roll, pitch, yaw= imu.getRollPitchYaw()
    print(yaw)
    scan= lidar.getRangeImage()
    closest= min(scan)
    #print(closest)
    image=camera.getImage()
    width=camera.getWidth()
    height=camera.getHeight()
    print(width, height)
    center_x = width // 2
    center_y = height // 2
    r = camera.imageGetRed(image, width, center_x, center_y)
    g = camera.imageGetGreen(image, width, center_x, center_y)
    b = camera.imageGetBlue(image, width, center_x, center_y)
    left_now= left_encoder.getValue()
    right_now= right_encoder.getValue()
    delta_left= left_now - last_left
    delta_right= right_now - last_right
    last_left=left_now
    last_right=right_now
    dist_left = delta_left * WHEEL_RADIUS
    dist_right = delta_right * WHEEL_RADIUS
    distance= (dist_left + dist_right)/2
    delta_theta= (dist_right-dist_left)/WHEEL_BASE
    x+=distance*math.cos(theta)
    y+=distance*math.sin(theta)
    theta+= delta_theta
    print(x, y, theta)
    print(f"pos=({x:.2f}, {y:.2f}) heading={theta:.2f} obstacle={closest:.2f}m")