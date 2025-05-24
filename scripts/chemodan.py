#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def callback(msg):
    rospy.loginfo(f"Overflow detected: {msg.data}")

def listener():
    rospy.init_node('overflow_listener')
    rospy.Subscriber('overflow', Int32, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
