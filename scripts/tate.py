#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
 
def cb(message):
    str = message.data
 
    for i in range(len(str)):
        print(str[i])
 
 
if __name__ == '__main__':
    rospy.init_node('tate')
    sub = rospy.Subscriber('yoko', String, cb)
    rospy.spin()
