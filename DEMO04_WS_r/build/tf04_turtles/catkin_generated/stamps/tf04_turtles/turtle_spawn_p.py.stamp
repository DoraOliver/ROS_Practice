#! /usr/bin/env python

import rospy
from turtlesim.srv import Spawn, SpawnRequest, SetPenRequest
"""
  向服务器请求生成一个乌龟
  话题: /spawn
  消息: turtlesim/Spwan
"""

if __name__ == "__main__":

  rospy.init_node("service_call_new_turtle")

  client = rospy.ServiceProxy("spawn", Spawn)

  request = SpawnRequest()

  request.x = 4.5
  request.y = 2.0
  request.theta = -3
  request.name = "turtle2"

  client.wait_for_service()
  try:
    response = client.call(request)
    rospy.loginfo("生成乌龟的名字： %s", response.name)
  except Exception as e:
    rospy.loginfo("请求处理异常")
