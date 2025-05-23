#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("I heard %s", msg.data)

rospy.init_node('listener')
# Не требуется сохранять объект подписки, возврат функции игнорируется
rospy.Subscriber('my_chat_topic', String, callback, queue_size=10)
# В данном случае достаточно спина, по факту замена `while rospy.is_shutdown()`
rospy.spin()
