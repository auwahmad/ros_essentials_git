#!/usr/bin/env python
# license removed for brevity

# TEST CODE 
# First publisher node development 
# Publishes x linear velocity to /turtle1/cmd_vel and moves turtlesim using a loop
# 
# Atta ul Wasay 
# 6 Jun 2024

import rospy
from geometry_msgs.msg import Twist

def speed_pub():
    #create a new publisher. we specify the topic name, then type of message then the queue size
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    #we need to initialize the node
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'speed_pub' node 
    rospy.init_node('speed_pub', anonymous=True)
    #set the loop rate
    rate = rospy.Rate(.25) # 1hz

    velocity_msg = Twist()
    velocity_msg.linear.x = 1.0

    #keep publishing until a Ctrl-C is pressed
    
    i = 0
    while not rospy.is_shutdown():
        
        rospy.loginfo("TURTLE MOVES %s" %i)
        pub.publish(velocity_msg)
        rate.sleep()
        i = i + 1
        if i > 5:
            rospy.loginfo("TURTLE completed %s" %i, " loops")
            break

if __name__ == '__main__':
    try:
        speed_pub()
    except rospy.ROSInterruptException:
        pass
