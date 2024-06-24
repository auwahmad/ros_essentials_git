#!/usr/bin/env python

import sys
import rospy
from ros_essentials_cpp.srv import MultiplyTwoInts
from ros_essentials_cpp.srv import MultiplyTwoIntsRequest
from ros_essentials_cpp.srv import MultiplyTwoIntsResponse

def multiply_two_ints_client(x, y):
    rospy.wait_for_service('multiply_two_ints')
    try:
        multiply_two_ints = rospy.ServiceProxy('multiply_two_ints', MultiplyTwoInts)
        resp1 = multiply_two_ints(x, y)
        return resp1.prod
    except rospy.ServiceException(e):
        print ("Service call failed: %s"%e)

def usage():
    return 

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print ("%s [x y]"%sys.argv[0])
        sys.exit(1)
    print ("Requesting %sx%s"%(x, y))
    s = multiply_two_ints_client(x, y)
    print ("%s x %s = %s"%(x, y, s))
