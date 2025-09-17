import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/dok4ever/ros2_tutorial_workspace/install/python_package_with_a_library'
