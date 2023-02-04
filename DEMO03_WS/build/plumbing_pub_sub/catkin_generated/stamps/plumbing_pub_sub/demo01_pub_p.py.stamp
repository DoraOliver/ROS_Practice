#！ /usr/bin/env python

#1.导入包
import os
import rospy
import sys

from std_msgs.msg import String #发布消息的类型

#设置临时环境变量
#sys.path.insert(0,"/home/doraoliver/DEMO03_WS/src/plumbing_pub_sub/scripts")
#但路径写死影响代码可移植性，可优化，可以动态获取路径
path = os.path.abspath(".")
sys.path.insert(0,path + "/src/plumbing_pub_sub/scripts")
import tools

"""
  使用python实现消息的发布方
  1.导入包
  2.初始化ros节点
  3.(python不需要创建句柄)创建发布对象
  4.编写发布逻辑并编写数据
"""

if __name__ == "__main__":

  #2.初始化ROS节点
  rospy.init_node("sanDai") #传入节点名称
  """
    latch 为 True: 保留最后一次发送的信息, 在有新订阅者连接的时候发送最后一次发送过的信息
  """

  #异常：ModuleNotFoundError: No module named 'tools
  # 原因：rosrun 执行时，参考路径是工作空间的路径，在工作空间下无法查找依赖的模块
  #解决： 可以声明python的环境变量，当依赖某个模块时，先去指定的环境变量中查找依赖
  rospy.loginfo("num = %d", tools.num)


  #3.创建发布者对象
  pub = rospy.Publisher("car", String, queue_size=10)
  
  # 4.编写发布逻辑并发布数据
  #创建数据
  msg = String()
  #指定发布频率
  rate = rospy.Rate(1)
  #设置计数器
  count = 0
  #使用循环发布数据
  while not rospy.is_shutdown():
    count += 1
    msg.data = "hello" + str(count)
    #发布数据
    pub.publish(msg)
    #添加ros日志
    rospy.loginfo("发布的数据是：%s", msg.data)
    rate.sleep()