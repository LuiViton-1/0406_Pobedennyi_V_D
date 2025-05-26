#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32MultiArray, Int32

# Инициализация узла
rospy.init_node('request_node', anonymous=False)

# Создание Publisher
pub = rospy.Publisher('/polynomial_input', Int32MultiArray, queue_size=10)

def callback(data):
    # Выводим результат сразу в колбэке
    print("Результат:", data.data)
    rospy.signal_shutdown("Got the result")

def send_request():
    numbers = list(map(int, input("Введите три числа через пробел: ").split()))
    if len(numbers) != 3:
        rospy.logerr("Необходимо ввести ровно три числа.")
        return

    msg = Int32MultiArray()
    msg.data = numbers
    pub.publish(msg)

# Подписываемся на топик
rospy.Subscriber('/summing_output', Int32, callback)

try:
    # Отправляем запрос
    send_request()
    # Запускаем цикл обработки событий ROS
    rospy.spin()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')
