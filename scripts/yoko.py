#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
  
rospy.init_node('yoko')
pub = rospy.Publisher('yoko', String, queue_size=1)

while not rospy.is_shutdown():
    str = input("文字を入力してください:")
    pub.publish(str)
