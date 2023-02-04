#!/usr/bin/env python3

import rospy

"""
  参数删除：
    delete_param()
"""

if __name__ == "__main__":
  
  rospy.init_node("del_param_p")

  try:
    #删除参数
    rospy.delete_param("radius_p")
  except Exception as e:
    rospy.loginfo("被删除的参数不存在")
