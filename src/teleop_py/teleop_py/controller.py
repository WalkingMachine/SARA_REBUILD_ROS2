from curses.ascii import ctrl
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from utils.remote_controller.controller_reader import XBoxControllerReader


class ControllerPublisher(Node):
    
    def __init__(self):
        super().__init__('controller_publisher')

        self._publisher = self.create_publisher(Twist, "sara/cmd_move", 10)
        self.controller = XBoxControllerReader(self.callback_function)
        self._last_x = 0.0
        self._last_y = 0.0
        self._last_r = 0.0


    def callback_function(self, ctrl_vals):
        ctrl_vals = self.controller.read()
        msg = Twist()
        if ctrl_vals["L_BUMPER"]==1 and ctrl_vals["R_BUMPER"] == 1:
            r_joy_y = ctrl_vals["JOY_RY"]*-1
            r_joy_x = ctrl_vals["JOY_RX"]
            l_joy_x = ctrl_vals["JOY_LX"]

            msg.linear.x = float(r_joy_x)
            msg.linear.y = float(r_joy_y)
            msg.angular.z = float(l_joy_x)
            self._last_x = float(r_joy_x)
            self._last_y = float(r_joy_y)
            self._last_r = float(l_joy_x)
            self.get_logger().debug("Controller message sent")
            self._publisher.publish(msg)
        else:
            msg.linear.x = 0.0
            msg.linear.y = 0.0
            msg.angluar.z = 0.0
            if not(msg.linear.x== self._last_x and \
                msg.linear.y == self._last_y and \
                msg.angular.z == self._last_r):
                self._publisher.publish(msg)
        self._last_x = msg.translation.translation_x
        self._last_y = msg.translation.translation_y
        self._last_r = msg.rotation.rotation


def main(args=None):
    rclpy.init(args=args)

    node = ControllerPublisher()

    node.controller.start()
    print("Hello")
    rclpy.spin(node)
    node.controller.stop()

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
