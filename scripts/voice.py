#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from gtts import gTTS
 
def cb (message):
    mytext = '''ご利用ありがとうございました'''
    tts = gTTS(text=mytext, lang='ja')
    tts.save('./voice.mp3')
 
if __name__ == '__main__':
    rospy.init_node('voice')
    sub = rospy.Subscriber('yoko', String, cb)
    rospy.spin()
