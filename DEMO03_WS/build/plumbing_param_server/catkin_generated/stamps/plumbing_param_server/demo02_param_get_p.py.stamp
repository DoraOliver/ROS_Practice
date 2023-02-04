#! /usr/bin/env python

import rospy


"""
  参数的查询
    get_param(键,默认值) 使用RPC协议访问master获取数据
      当键存在时，返回对应的值，如果不存在返回默认值
    get_param_cached
      和get_param 使用一致，知识效率高
    get_param_names
      获取所有的参数的键
    has_param
      判断是否包含某个键
    search_param
      查找某个键，并返回完整的键名
"""
if __name__ == "__main__":
  
  rospy.init_node("get_param_p")
  #1. get_param
  radius = rospy.get_param("radius_p", 0.5)
  radius2 = rospy.get_param("radius_p_xxx", 0.5)
  rospy.loginfo("radius = %.2f", radius)
  rospy.loginfo("radius2 = %.2f", radius2)

  #2.get_param_cached
  #相比上一个方法效率更高
  radius = rospy.get_param_cached("radius_p", 0.5)
  radius2 = rospy.get_param_cached("radius_p_xxx", 0.5)
  rospy.loginfo("radius3 = %.2f", radius)
  rospy.loginfo("radius4 = %.2f", radius2)

  #3.get_param_names 获取键
  names = rospy.get_param_names()
  for name in names:
    rospy.loginfo("name = %s",name)

  #4. has_param
  flagl = rospy.has_param("radius_p_xxx")
  if flagl:
    rospy.loginfo("radius_p_xxx exict")
  else:
    rospy.loginfo("radius_p_xxx do not exict 不存在")

  # 5.search_param
  key = rospy.search_param("radius_p")
  rospy.loginfo("key = %s", key)
  pass
