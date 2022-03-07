# Perkobot V1

This is the repository for the SmartSystems Lab's custom autonomous robot: Perkobot

## Documentation

### SSH'ing to the Robot
The robot automatically connects to the TP-Link_SSL WiFi on boot up, so if that WiFi is no longer available, none of this will work.

The IP address for the robot should be static, 192.168.1.107, so you should be able to ssh into it by doing ```ssh bobdabot@192.168.1.107``` where the password is ```password1234```

If you cannot ssh because it is not responding, you will have to plug in an external monitor, keyboard, and mouse, and figure out what happened to the WiFi or IP address.

**Before you can use this package you have to add the Odrive Driver package I created; which can be found [here](https://github.com/NicoPowers/odrive_interface).**

## Using this package to control the robot through teleop

1. Ensure the odrive_interface package works by running the odrive_controller node and seeing if you can connect to the ODrive successfully.
2. Download this repo by cloning it into your catkin_ws
3. Perform ```catkin_make``` in you catkin_ws and then source the devel/setup.bash
4. Launch the teleop node by doing ```roslaunch perkobot teleop.launch``` (if you have problems finding the launch file, you may have to do ```rosls``` or ```roscd perkobot``` first.

## Next steps for making the robot autonomous

### Add more ODrive functionality

1. Right now the velocity being sent to the ODrive isn't the real velocity of the robot; because it is not taking into account the gear reduction ratio and the circumference of the wheel, so the next step is to make a node that does the neccessary math to scale the input velocity and send a modified velocity value to the ODrive that reflects the desired velocity. You may also be able to use the diff_drive_controller package, there seems to be options for configuring this kind of thing.
2. Add some functionality to retrieve the current velocity of each wheel to use for odometry (you may assume the velocity you set is the real velocity, and this may work, but it should use the real velocity to calculate the odometry for best results)
3. Ensure watchdog still works after modifying the controller; it should timeout after 2 seconds of not receiving data. You can modify this by changing the ```watchdog_timeout``` in the ```odrive_controller.py``` file in the odrive_interface package.

### Ensure the RPLidar works with ROS
1. For some reason the RPLidar can connect fine through USB, but it's not sending any data. I am not sure why this is happening, more debugging needs to be done.
2. Once the RPLidar is working verify proper scans in RviZ

### Integrate robot URDF with ROS and attemp to start Gmapping SLAM
1. With the velocity being returned to the perkobot, now we can use joint_state_publisher and robot_state_publisher to generate transforms for our robot using the URDF for the robot.
2. Once the transforms are being published, create a launch file that starts the joint_state_publisher, robot_state_publisher, odriver_interface, and gmapping nodes.
3. There may be additional configurations required, but see if a map is now being generated in Rviz

### Attempt to save map and use map to navigate the robot
1. Once map generation is possible, try to save the map to rosbag (i think)
2. Then in RviZ try to set an initial pose and waypoint (you may need to also start the amcl node along with this, although I think RviZ has its own costmap and planner for navigation)
3. 
