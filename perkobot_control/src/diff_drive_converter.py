#!/usr/bin/env python3
from __future__ import print_function

import rospy
from geometry_msgs.msg import Twist
from odrive_interface.msg import VelocityControl
from odrive_interface.srv import *

pub = rospy.Publisher("odrive_cmd_vel", VelocityControl, queue_size=10)

def callback(data):
    global pub
    
    velocity_right = (data.angular.z*0.5)/2 + data.linear.x
    velocity_left = data.linear.x*2-velocity_right

    data_to_publish = VelocityControl()
    data_to_publish.axis0_velocity = velocity_left
    data_to_publish.axis1_velocity = velocity_right

    pub.publish(data_to_publish)

def listener():
    rospy.init_node("teleop")
    rospy.Subscriber("cmd_vel", Twist, callback)
    rospy.spin()


if __name__ == '__main__':    
    try:
        listener()
    except rospy.ROSInterruptException:
        sys.exit()    
    

