# Automated Obstacle Avoider

A simulated differential-drive robot in Webots, built as a scaled-down
version of an autonomous robot's software stack.

## Built so far
- Custom chassis with tuned suspension (spring/damper on both wheels)
- Free-rolling ball-joint caster
- Wheel encoders, IMU, LiDAR, camera — all wired and verified
- Self-computed odometry (x, y, theta from encoder deltas)

## In progress
- Stage 3: PID path following

## Later
- Real LiDAR-based perception (full scan, not just closest point)
- Occupancy grid mapping
- EKF localization
- A* path planning
- Full autonomous obstacle avoidance
- Live visualization dashboard