#!/usr/bin/env python3

import rospy
from plumbing_server_client.srv import *
import sys

"""
  客户端：组织并提交请求，处理服务端响应
    1.导包
    2.初始化ROS节点
    3.创建客户端对象
    4.组织请求数据，并发送请求
    5.处理响应

  优化实现：
    1.在执行节点是传入参数
    2.如果先启动客户端：
      方案一：
      client.wait_for_service()
      方案二：
      rospy.wait_for_service("话题名称")

"""



if __name__ == "__main__":
  
  #判断参数长度：
  if len(sys.argv) != 3: #argv[0] 存储的是函数名
    rospy.logerr("传入的参数个数不对。")
    sys.exit(1)

  rospy.init_node("NeedSum")

  client = rospy.ServiceProxy("addInts", AddInts)
  rospy.loginfo("客户端对象创建")
  #4.组织请求数据，并发送请求
  num1 = int(sys.argv[1])
  num2 = int(sys.argv[2])

  #等待服务器启动
  #方式一：
  #client.wait_for_service()
  #方式二：
  rospy.wait_for_service("addInts")

  response = client.call(num1, num2)

  rospy.loginfo("响应的数据： %d", response.sum)