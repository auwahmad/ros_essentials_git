# Assignment 2
# Creating:
# 1. Subscriber for the topic that will show the location of the robot
# 2. Publisher to the topic that will make the robot move
# Questions:
# 1. What is the topic of the position? Ans: /turtle1/pose
# 2. What is the topic that make the robot move? Ans: /turtle1/cmd_ve

#!/usr/bin/env python
# license removed for brevity
import rospy
#from std_msgs.msg import String
from geometry_msgs.msg import Twist

def move():
    #create a new publisher. we specify the topic name, then type of message then the queue size
    speed_publisher = rospy.Publisher('/turtle1/cmd_ve', String, queue_size=10)
    #we need to initialize the node
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'talker' node 
    rospy.init_node('move', anonymous=True)
    #set the loop rate
    rate = rospy.Rate(1) # 1hz
    #keep publishing until a Ctrl-C is pressed
    i = 0
    while not rospy.is_shutdown():
        move_x = Twist()
        move_x.linear.x = 1.0
        

if __name__ == '__main__':
    try:
        move_x()
    except rospy.ROSInterruptException:
        pass
