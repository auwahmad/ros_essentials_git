#!/usr/bin/env python

from ros_essentials_cpp.srv import MultiplyTwoInts
from ros_essentials_cpp.srv import MultiplyTwoIntsRequest
from ros_essentials_cpp.srv import MultiplyTwoIntsResponse

import rospy

def handle_multiply_two_ints(req):
    print ("Returning [%s x %s = %s]"%(req.a, req.b, (req.a * req.b)))
    return MultiplyTwoIntsResponse(req.a * req.b)

def multiply_two_ints_server():
    rospy.init_node('multiply_two_ints_server')
    s = rospy.Service('multiply_two_ints', MultiplyTwoInts, handle_multiply_two_ints)
    print ("Ready to multiply two ints.")
    rospy.spin()
    
if __name__ == "__main__":
    multiply_two_ints_server()
