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

## Run
ros2 run status_publisher sys_status_pub
ros2 run status_publisher sys_status_gui

## 使用说明
本项目包含两个ROS2功能包：
- status_interfaces：自定义消息包，定义系统状态消息SystemStatus.msg
- status_publisher：发布者节点采集系统CPU、内存、网络信息；订阅者节点基于PyQt5绘制图形界面展示数据。

