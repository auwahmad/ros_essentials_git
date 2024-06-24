#!/usr/bin/env python

# TEST CODE 
# First subcriber node development 
# Subscribes to the /turtle1/Pose topic and prints the position of turtle in a call back function
# 
# Atta ul Wasay 
# 6 Jun 2024

import rospy
from turtlesim.msg import Pose

def pos_callback(message):
    #get_caller_id(): Get fully resolved name of local node
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", message.data)
    x_pos = round(message.x, 2)
    X_pos = "X - Coordinate %s" %x_pos
    y_pos = round(message.y, 2)
    Y_pos = "Y - Coordinate %s" %y_pos
    print(X_pos)
    print(Y_pos)
    print("*********************")

def pos_sub():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('pos_sub', anonymous=True)

    rospy.Subscriber("/turtle1/pose", Pose, pos_callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    pos_sub()
