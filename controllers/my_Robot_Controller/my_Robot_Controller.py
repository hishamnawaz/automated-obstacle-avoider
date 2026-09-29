wheelradius=0.045
wheelbase=0.30
import math
from controller import Robot
import numpy as np
from Objectdetection import yolodetection

robot = Robot()
camera=robot.getDevice('camera')
imu= robot.getDevice('imu')
lidar=robot.getDevice('lidar')
leftmotor = robot.getDevice('LEFT_WHEEL_MOTOR')
rightmotor = robot.getDevice('RIGHT_WHEEL_MOTOR')
leftmotor.setPosition(float('inf'))
rightmotor.setPosition(float('inf'))
timestep = int(robot.getBasicTimeStep())
x=0.0
y=0.0
theta=0.0
lastleft=0.0
lastright=0.0
leftencoder = robot.getDevice('LEFT_WHEEL sensor')
rightencoder = robot.getDevice('RIGHT_WHEEL sensor')
camera.enable(timestep)
imu.enable(timestep)
lidar.enable(timestep)
leftencoder.enable(timestep)
rightencoder.enable(timestep)
#target_x = -2.0
#target_y = 2.0

waypoints = [(-2.0, 2.0), (2.0, -2.0), (0.0, 0.0)]
initialwaypoint = 0
targetx, targety = waypoints[initialwaypoint]

Kp = 2.0
Ki = 0.0
Kd = 0.5

integral = 0.0
lasterror = 0.0
basespeed = 5.0
avoiddist = 0.4
while robot.step(timestep) != -1:
    print("x,y:", x, y)
    print(leftencoder.getValue(), rightencoder.getValue())
    roll, pitch, yaw= imu.getRollPitchYaw()
    print(yaw)
    scan= lidar.getRangeImage()
    closest= min(scan)
    #print(closest)
    image=camera.getImage()
    width=camera.getWidth()
    height=camera.getHeight()
    print(width, height)
    img_array = np.frombuffer(image, dtype=np.uint8).reshape((height, width, 4))
    frame = img_array[:, :, :3]
    result=yolodetection(frame)
    if len(result.boxes) > 0:
        print("Detections found:", result.boxes.xyxy)
    else:
        print("No objects detected in this frame.")
    print("Detections:", result.boxes.xyxy) 
    centerx = width // 2
    centery = height // 2
    r = camera.imageGetRed(image, width, centerx, centery)
    g = camera.imageGetGreen(image, width, centerx, centery)
    b = camera.imageGetBlue(image, width, centerx, centery)
    leftnow= leftencoder.getValue()
    rightnow= rightencoder.getValue()
    deltaleft= leftnow - lastleft
    deltaright= rightnow - lastright
    lastleft=leftnow
    lastright=rightnow
    distleft = deltaleft * wheelradius
    distright = deltaright * wheelradius
    distance= (distleft + distright)/2
    deltatheta= (distleft-distright)/wheelbase
    x+=distance*math.cos(theta)
    y+=distance*math.sin(theta)
    theta+= deltatheta
    print(x, y, theta)
    #print(f"pos=({x:.2f}, {y:.2f}) heading={theta:.2f} obstacle={closest:.2f}m")
    desiredtheta = math.atan2(targety - y, targetx - x)
    error = desiredtheta - theta
    error = math.atan2(math.sin(error), math.cos(error))
    dt = timestep / 1000.0
    integral += error * dt
    derivative = error - lasterror
    derivative = math.atan2(math.sin(derivative), math.cos(derivative))
    derivative = derivative / dt
    correction = Kp * error + Ki * integral + Kd * derivative
    lasterror = error
    distancetotarget = math.sqrt((targetx - x)**2 + (targety - y)**2)
    print(f"pos=({x:.2f},{y:.2f}) heading={theta:.2f} closest={closest:.2f} waypoint={initialwaypoint}")
    #print("dist:", distance_to_target)
    if closest<avoiddist:
        leftmotor.setVelocity(-4.0)
        rightmotor.setVelocity(4.0)
    elif distancetotarget < 0.2:
        initialwaypoint += 1
        if initialwaypoint >= len(waypoints):
            leftmotor.setVelocity(0)
            rightmotor.setVelocity(0)
        else:
            targetx, targety = waypoints[initialwaypoint]
    else:
        effectivespeed = basespeed * math.cos(error)
        leftmotor.setVelocity(effectivespeed - correction)
        rightmotor.setVelocity(effectivespeed + correction)
    #left_motor.setVelocity(-3)
    #right_motor.setVelocity(3)