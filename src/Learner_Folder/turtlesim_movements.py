#!/usr/bin/env python

# TEST CODE FOR MOVEMENTS 
# 1. Subscribe to the Pose of the Turtle and call back to get the position info for the main function
# 2. Define move function that will calculate the required velocities to achieve the goal
# 3. The velocities will be published to /cmd_vel node 

# Atta ul Wasay 
# 10 Jun 2024

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math
import time

def pos_callback(pose_message):
    # setting the global variables for the Robot Position
    global x, y, yaw

    x = pose_message.x
    y = pose_message.y
    yaw = pose_message.theta

def rotate(velocity_publisher, angular_speed_degree, relative_angle_degree, clockwise):
    
    velocity_message = Twist()

    angular_speed = math.radians(abs(angular_speed_degree))

    if(clockwise):
        velocity_message.angular.z = -abs(angular_speed)
    else:
        velocity_message.angular.z = -abs(angular_speed)

    loop_rate = rospy.Rate(10)
    t0 = rospy.Time.now().to_sec()

    while True:
        rospy.loginfo("Turtlsim rotates")
        velocity_publisher.publish(velocity_message)

        t1 = rospy.Time.now().to_sec()
        current_angle_degree = (t1-t0)*angular_speed_degree
        loop_rate.sleep()

        if (current_angle_degree > relative_angle_degree):
            rospy.loginfo("reached")
            break
    velocity_message.angular.z = 0
    velocity_publisher.publish(velocity_message)

def move(velocity_publisher, speed, distance, is_forward):

    # declare a Twist message to send velocity commands
    # declaring Twist object
    velocity_message = Twist()

    # get the current location of the turtle
    global x, y
    x0 = x
    y0 = y

    if (is_forward):
        velocity_message.linear.x = abs(speed)
    else:
        velocity_message.linear.x = -abs(speed)

    distance_moved = 0.0

    loop_rate = rospy.Rate(1)

    while True:
        rospy.loginfo("TURTLE MOVES")
        # moving turtle in "X" with the given speed
        velocity_publisher.publish(velocity_message)
        loop_rate.sleep()

        # calculating distance whether desired distance has been reached or not
        distance_moved = abs(math.sqrt(((x - x0)**2) + ((y - y0)**2)))
        print(distance_moved)
        print(x)
        if (distance_moved > distance):
            rospy.loginfo("TURTLE REACHED")
            break

    velocity_message.linear.x = 0
    velocity_publisher.publish(velocity_message)

def goal_to_goal(velocity_publisher, x_goal, y_goal):
    global x
    global y, yaw
    
    loop_rate = rospy.Rate(10)
    velocity_message = Twist()

    while (True):
        K_linear = 20
        distance = abs(math.sqrt(((x_goal -x)**2) + ((y_goal-y)**2)))

        linear_speed = distance * K_linear

        K_angular = 4.0
        desired_angle_goal = math.atan2(y_goal-y, x_goal-x)
        angular_speed = (desired_angle_goal - yaw) * K_angular

        velocity_message.linear.x = linear_speed
        velocity_message.angular.z = angular_speed

        velocity_publisher.publish(velocity_message)
        print('x = ', x, ', y = ', y, ', distance_to_goal: ', distance)

        if (distance<0.01):
            break


if __name__ == '__main__':
    try:
        # initialize the node
        rospy.init_node('turtle_movements', anonymous=True)

        velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        pose_subscriber = rospy.Subscriber("/turtle1/pose", Pose, pos_callback)
        time.sleep(2)

        # spin() simply keeps python from exiting until this node is stopped
        #rospy.spin()

        #move(velocity_publisher, 6.0, 4.0, True) 
        #rotate(velocity_publisher, 30, 90, True)
        goal_to_goal(velocity_publisher, 2.0, 2.0)
    
    
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated")

