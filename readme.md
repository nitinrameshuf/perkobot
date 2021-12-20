# Perkobot V1

This is the repository for the SmartSystems Lab's custom autonomous robot: Perkobot

## Getting Started
The IP address for the robot changes for some reason, even though I set it to static, maybe there is more setup that is required, so you will have to plug in a mouse, keyboard, and monitor into the Jetson Xavier to login and verify the IP so you can SSH into it.

The password to login is: **password1234**


**Before you can use this package you have to add the Odrive Driver package I created; which can be found [here](https://github.com/NicoPowers/odrive_interface).**

## Using this package to control the robot through teleop

1. Ensure the odrive_interface package works by running the odrive_controller node and seeing if you can connect to the ODrive successfully.
2. Download this repo by cloning it into your catkin_ws
3. Perform ```catkin_make``` in you catkin_ws and then source the devel/setup.bash
4. Launch the teleop node by doing ```roslaunch perkobot teleop.launch``` (if you have problems finding the launch file, you may have to do ```rosls``` or ```roscd perkobot``` first.


