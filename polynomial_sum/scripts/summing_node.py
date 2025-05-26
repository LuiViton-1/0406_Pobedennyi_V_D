#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32MultiArray, Int32

# Инициализация узла
rospy.init_node('summing_node', anonymous=True)

# Создание Publisher и Subscriber
pub = rospy.Publisher('/summing_output', Int32, queue_size=10)

def callback(data):
    # Суммируем 
    result = sum(data.data)

    # Создаем сообщение
    msg = Int32()
    msg.data = result

    # Публикуем результат
    pub.publish(msg)

# Подписываемся на топик
rospy.Subscriber('/polynomial_output', Int32MultiArray, callback)

try:
    rospy.spin()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')
