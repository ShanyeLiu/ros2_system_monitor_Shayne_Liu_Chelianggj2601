import sys
import rclpy
from rclpy.node import Node
from status_interfaces.msg import SystemStatus
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QThread, pyqtSignal

class RosThread(QThread):
    signal = pyqtSignal(SystemStatus)
    def __init__(self):
        super().__init__()
        self.node = None
    def run(self):
        rclpy.init()
        self.node = Node("sys_status_sub")
        self.node.create_subscription(
            SystemStatus,
            "sys_status",
            self.callback,
            10
        )
        rclpy.spin(self.node)
    def callback(self,msg):
        self.signal.emit(msg)

class GuiWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("系统状态监控")
        self.resize(400,300)
        self.vl = QVBoxLayout()
        self.label = QLabel("等待数据...")
        self.vl.addWidget(self.label)
        self.setLayout(self.vl)

        self.ros_thread = RosThread()
        self.ros_thread.signal.connect(self.update_ui)
        self.ros_thread.start()

    def update_ui(self,msg:SystemStatus):
        text = (
            f"主机名: {msg.hostname}\n"
            f"CPU使用率: {msg.cpu_percent:.2f} %\n"
            f"内存使用率: {msg.memory_percent:.2f} %\n"
            f"总内存: {msg.memory_total:.2f} GB\n"
            f"可用内存: {msg.memory_available:.2f} GB\n"
            f"网络发送: {msg.net_sent:.2f} MB\n"
            f"网络接收: {msg.net_recv:.2f} MB"
        )
        self.label.setText(text)

def main():
    app = QApplication(sys.argv)
    w = GuiWindow()
    w.show()
    app.exec_()

if __name__ == '__main__':
    main()
