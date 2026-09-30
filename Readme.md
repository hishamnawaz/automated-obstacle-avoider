# Automated Obstacle Avoider
## Getting Started

### Prerequisites
- [Webots](https://cyberbotics.com/) R2025a or later
- Python (bundled with Webots)

### Opening the project
1. Launch Webots
2. File > Open World...
3. Navigate to `worlds/OBstacle_Avoider.wbt` in this repo and open it
4. Press the Play button in the simulation toolbar

### What you should see
A small differential-drive robot with visible wheels, a rear caster, and
a mounted LiDAR/camera, sitting in an empty arena alongside a static blue
obstacle box. On play, it drives toward a fixed target point using PID
steering, printing live position/sensor data to the Console panel
(bottom of the Webots window).

# Introduction

A simulated differential-drive robot in Webots which can detect objects using OpenCV and YOLO and recalculate path based on obstacles in the path, built as a scaled-down version of an autonomous robot's software stack.

## Built so far
- Custom chassis with tuned suspension (spring/damper on both wheels)
- Free-rolling ball-joint caster
- Wheel encoders, IMU, LiDAR, camera — all wired and verified
- Self-computed odometry (x, y, theta from encoder deltas)
- Simple object detection and stopping
- PID path following
- Waypoints method
- Management of video files using OpenCV
- Using YOLO to make object detection much more accurate


## Later
- Real LiDAR-based perception (full scan, not just closest point)
- Occupancy grid mapping
- EKF localization
- A* path planning
- Full autonomous obstacle avoidance
- Live visualization dashboard
- Extended Kalman Filter

