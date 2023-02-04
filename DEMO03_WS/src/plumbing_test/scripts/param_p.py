#! /usr/bin/env python

import rospy

"""
  修改背景色
    1.初始化节点
    2.设置参数
"""

if __name__ == "__main__":

  rospy.init_node("change_bgColor")
  rospy.set_param("/turtlesim/background_r", 100)
  rospy.set_param("/turtlesim/background_b", 200)
  rospy.set_param("/turtlesim/background_g", 50)
  pass