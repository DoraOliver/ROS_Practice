#! /usr/bin/env python

import rospy

"""
  1:时间相关操作(获取当前时刻 + 设置指定时刻)

  2: 程序执行中停顿5s

  3: 获取程序开始执行的时刻，且已知持续运行的时间，计算程序结束的时间

  4: 创建定时器, 实现类似于 ros::Rate 的功能(隔某个时间间隔执行某种操作)

"""

def doMsg(event):
  rospy.loginfo("++++++++")
  rospy.loginfo("调用回调函数的时刻：%.2f",event.current_real.to_sec())

if __name__ == "__main__":

  #1. 时间相关操作(获取当前时刻 + 设置指定时刻)
  rospy.init_node("hello_time")

  #获取时刻
  right_now = rospy.Time.now()
  rospy.loginfo("Recent time:%.2f", right_now.to_sec()) #与过去1970年01月01日 00：00：00 对比
  rospy.loginfo("Recent time:%d", right_now.secs)
  #设置指定
  time1 = rospy.Time(100) #将时间起点从1970年01月01日 00:00:00 指定为100秒
  time2 = rospy.Time(100, 312345678) #多加上100。312345678s

  #从某个时间值获取时间对象
  time3 = rospy.Time.from_sec(200.12)
  rospy.loginfo("指定时刻3:%.2f", time3.to_sec())

  # 2.程序停顿5s
  rospy.loginfo("休眠前--------")
    #1. 创建一个持续时间对象
  dua = rospy.Duration(5)
    #2. 再将持续时间休眠
  # rospy.sleep(dua)
  rospy.loginfo("休眠后--------")

  # 3.持续时间与时刻运算
  # 1.获取一个时刻
  t1 = rospy.Time.now()
  # 2.设置一个持续时间 du1
  du1 = rospy.Duration(5)
  # 3.结束时刻 t2 = t1 + du1
  t2 = t1 + du1
  rospy.loginfo("开始时刻： %.2f", t1.to_sec())
  rospy.loginfo("结束时刻： %.2f", t2.to_sec())

  # 4. 创建定时器
  # timer = rospy.Timer(rospy.Duration(2), doMsg, oneshot=True)
  timer = rospy.Timer(rospy.Duration(2), doMsg)
  rospy.spin()