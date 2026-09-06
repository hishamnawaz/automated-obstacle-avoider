## Getting Started

### Prerequisites
- [Webots](https://cyberbotics.com/) R2025a or later (free, from Cyberbotics)
- Python (bundled with Webots — no separate install needed for running the
  controller, though Webots must be able to find a system Python install
  for some features)

### Opening the project
1. Launch Webots
2. File > Open World...
3. Navigate to `worlds/OBstacle_Avoider.wbt` in this repo and open it
4. Press the Play (▶) button in the simulation toolbar

### What you should see
A small differential-drive robot with visible wheels, a rear caster, and
a mounted LiDAR/camera, sitting in an empty arena alongside a static red
obstacle box. On play, it drives toward a fixed target point using PID
steering, printing live position/sensor data to the Console panel
(bottom of the Webots window).

# Automated Obstacle Avoider

A simulated differential-drive robot in Webots which can detect objects using OpenCV and YOLO and recalculate path based on obstacles in the path, built as a scaled-down version of an autonomous robot's software stack.

## Built so far
- Custom chassis with tuned suspension (spring/damper on both wheels)
- Free-rolling ball-joint caster
- Wheel encoders, IMU, LiDAR, camera — all wired and verified
- Self-computed odometry (x, y, theta from encoder deltas)

## In progress
- Stage 3: PID path following
- Stage 4: Management of video files using OpenCV
- Stage 5: Using YOLO to make object detection much more accurate

## Later
- Real LiDAR-based perception (full scan, not just closest point)
- Occupancy grid mapping
- EKF localization
- A* path planning
- Full autonomous obstacle avoidance
- Live visualization dashboard

### Known issues (see below for detail)
- Odometry (the robot's self-computed position) can silently diverge from
  its real simulated position — likely a left/right sign mismatch in the
  wheel encoder math. Not yet fixed; see "In progress" section.
- No obstacle avoidance yet — PID will drive straight through anything in
  its path. The visible obstacle box currently exists for LiDAR-testing
  purposes, not as something the robot reacts to.