import rclpy
from rclpy.node import Node

class PrintForever(Node):
    def __init__(self):
        super().__init__('PrinterForever')
        timer_period:float=0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.print_count: int = 0

    def timer_callback(self):
        self.get_logger().info(f'Printed {self.print_count} times.')
        self.print_count = self.print_count + 1

def main(args=None):
    try:
        rclpy.init(args=args)
        print_forever_node = PrintForever()
        rclpy.spin(print_forever_node)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)

if __name__=='__main__':
    main()