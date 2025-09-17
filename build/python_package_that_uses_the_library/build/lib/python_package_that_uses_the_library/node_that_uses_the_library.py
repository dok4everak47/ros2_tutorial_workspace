import random
import string

import rclpy
from rclpy.node import Node
from python_package_with_a_library.sample_python_library import SampleClass, sample_function_for_square_of_sum

class NodeThatUsesTheLibrary(Node):

    def __init__(self):
        super().__init__('node_that_uses_the_library')
        timer_period: float = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):

        a: float = random.uniform(0, 1)
        b: float = random.uniform(1, 2)
        c: float = sample_function_for_square_of_sum(a, b)
        self.get_logger().info(f'sample_function_for_square_of_sum({a},{b}) returned {c}.')
        
        random_name_ascii: str = ''.join(random.choice(string.ascii_letters) for _ in range(10))
        sample_class_with_random_name = SampleClass(name=random_name_ascii)
        self.get_logger().info(f'sample_class_with_random_name.get_name() 'f'returned {sample_class_with_random_name.get_name()}.')

def main(args=None):
    try:
        # comment: 
        rclpy.init(args=args)
    
        node_that_uses_the_library=NodeThatUsesTheLibrary()
        
        rclpy.spin(node_that_uses_the_library)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
# end try


if __name__ == '__main__':
    main()
