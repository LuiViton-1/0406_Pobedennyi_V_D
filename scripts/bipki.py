#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def publisher():
    rospy.init_node('even_numbers_publisher', anonymous=True)
    pub_even = rospy.Publisher('even_numbers', Int32, queue_size=10)
    pub_overflow = rospy.Publisher('overflow', Int32, queue_size=10)
    rate = rospy.Rate(10)
    count = 0

    while not rospy.is_shutdown():
        if count <= 100:
            pub_even.publish(count)
            rospy.loginfo(f"Even: {count}")
            count += 2
        else:
            pub_overflow.publish(count)
            rospy.loginfo("Overflow! Resetting to 0.")
            count = 0
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
