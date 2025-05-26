#!/usr/bin/env python3
import rospy
# Инициализация узла
rospy.init_node('primer')
# Приватный параметр (~)
rospy.set_param('~ros_priv_param', 'Hi, I am private =)')
# Локальный параметр (без /)
rospy.set_param('ros_loc_param', 'Hi, I am local =)')
# Глобальный параметр (/)
rospy.set_param('/ros_glob_param', 'Hi, I am global =)')
# Получение параметров
global_param = rospy.get_param('/rosdistro')
rospy.loginfo("Global parameter '/rosdistro': %s", global_param)
local_param = rospy.get_param('ros_loc_param')
rospy.loginfo("Local parameter 'ros_loc_param': %s", local_param)
private_param = rospy.get_param('~ros_priv_param')
rospy.loginfo("Private parameter '~ros_priv_param': %s", private_param)
custom_global_param = rospy.get_param('/ros_glob_param')
rospy.loginfo("Custom global parameter '/ros_glob_param': %s", custom_global_param)

