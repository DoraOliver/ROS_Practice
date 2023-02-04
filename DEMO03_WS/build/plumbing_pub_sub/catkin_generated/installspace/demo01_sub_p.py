#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

"""
  订阅实现流程：
    1.导报
    2.初始化ros节点
    3.创建订阅者对象
    4.回调函数处理数据
    5.spin() ros消息回调处理函数, 分为spin() 和 spinOnce()
"""
#回调函数
def doMsg(msg):
  rospy.loginfo("我订阅的数据：%s", msg.data)

if __name__ == "__main__":
  
  # 2.初始化ros节点
  rospy.init_node("huaHUa")
  # 3.创建订阅者对象
  sub = rospy.Subscriber("car", String, doMsg, queue_size=10)
  # 4.回调函数处理数据
  # 5.spin() ros消息回调处理函数,直到这个节点被停止
  rospy.spin() #回头执行回调函数
 
