#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32MultiArray

# Инициализация узла
rospy.init_node('polynomial_node', anonymous=True)

# Создание Publisher и Subscriber
pub = rospy.Publisher('/polynomial_output', Int32MultiArray, queue_size=10)

def callback(data):
    if len(data.data) != 3:
        rospy.logerr("Ожидалось 3 числа, получено: %d", len(data.data))
        return  # ← Исправлено: одинаковый отступ с if

    result = [
        data.data[0] ** 3,  
        data.data[1] ** 2,  
        data.data[2] ** 1   
    ]

    # Создаем сообщение
    msg = Int32MultiArray()
    msg.data = result

    # Публикуем результат
    pub.publish(msg)

# Подписываемся на топик
rospy.Subscriber('/polynomial_input', Int32MultiArray, callback)

try:
    rospy.spin()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')
