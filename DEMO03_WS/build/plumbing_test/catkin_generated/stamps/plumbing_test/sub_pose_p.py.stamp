#! /usr/bin/env python

import rospy
from turtlesim.msg import Pose
"""
  订阅并输出乌龟的位姿信息

  1.导包
  2.初始化ROS节点
  3.创建订阅对象
  4.回调函数处理订阅消息
  5.spin()
"""

def doPose(msg:Pose):
  rospy.loginfo("乌龟位姿信息：坐标（%.2f, %.2f); 朝向：%.2f, 线速度：%.2f, 角速度：%.2f", 
                msg.x, msg.y, msg.theta, msg.linear_velocity, msg.angular_velocity)

if __name__ == "__main__":
  
  rospy.init_node("sub_pos_p")

  sub = rospy.Subscriber("/turtle1/pose", Pose, doPose, queue_size=10)

  rospy.spin()
  