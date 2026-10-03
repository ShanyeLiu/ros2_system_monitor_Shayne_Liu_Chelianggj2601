import rclpy
from rclpy.node import Node
from status_interfaces.msg import SystemStatus
import psutil
import platform

class SysStatusPub(Node):
    def __init__(self):
        super().__init__('sys_status_pub')
        self.publisher_ = self.create_publisher(SystemStatus, 'sys_status', 10)
        self.timer_period = 1.0
        self.timer = self.create_timer(self.timer_period, self.timer_callback)

    def timer_callback(self):
        msg = SystemStatus()
        msg.stamp = self.get_clock().now().to_msg()
        msg.hostname = platform.node()
        msg.cpu_percent = psutil.cpu_percent()
        msg.memory_percent = psutil.virtual_memory().percent
        msg.memory_total = psutil.virtual_memory().total / 1024 /1024 /1024
        msg.memory_available = psutil.virtual_memory().available /1024 /1024 /1024
        net_io = psutil.net_io_counters()
        msg.net_sent = net_io.bytes_sent /1024 /1024
        msg.net_recv = net_io.bytes_recv /1024 /1024
        self.publisher_.publish(msg)
        self.get_logger().info(f'发布:{msg}')

def main():
    rclpy.init()
    node = SysStatusPub()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
