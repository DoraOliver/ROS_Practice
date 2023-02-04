#! /usr/bin/env python

from urllib import response
from grpc import server
import rospy
from plumbing_server_client.srv import AddInts, AddIntsRequest, AddIntsResponse
#from plumbing_server_client.srv import *
"""
  服务端：解析客户端请求，产生响应。

    1.导报
    2.初始化ROS节点
    3.创建服务对象
    4.处理请求并产生响应 -- 处理逻辑（回调函数）
    5.spin()


"""

def doNum(request):
  #1.解析提交的两个整数
  num1 = request.num1
  num2 = request.num2

  sum = num1 + num2

  response = AddIntsResponse()
  response.sum = sum

  rospy.loginfo("服务器解析的数据num1 = %d, num2 = %d, 响应的结果： sum = %d", num1, num2, sum)

  return response

if __name__ == "__main__":
  #2.初始化节点
  rospy.init_node("Sum")
  #3.创建服务端对象
  server = rospy.Service("addInts", AddInts, doNum)
  rospy.loginfo("服务器已经启动了")
  #4.回调函数
  #5.spin()
  rospy.spin()