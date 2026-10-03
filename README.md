# ros2_system_monitor_Shayne_Liu_Chelianggj2601
ROS2 system status monitor project for interview
# ROS2 System Status Monitor
ROS2 Humble project, two packages to monitor system status and show by Qt GUI.

Environment:
Ubuntu 22.04 + ROS2 Humble + Python3 + PyQt5 + psutil

## Packages
1. status_interfaces: Custom message package, define SystemStatus.msg
2. status_publisher: Data publisher and Qt GUI subscriber

## Build
```bash
cd ~/ros2_ws
source /opt/ros/humble/setup.bash
colcon build --packages-select status_interfaces status_publisher
source install/setup.bash
