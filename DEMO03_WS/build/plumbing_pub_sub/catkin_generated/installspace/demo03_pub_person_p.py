#!/usr/bin/env python3

import rospy
from plumbing_pub_sub.msg import Person


if __name__ == "__main__":

  rospy.init_node("daMa")

  pub = rospy.Publisher("chat", Person, queue_size=10)

  p = Person()

  p.name = "Jack"
  p.age = 18
  p.height = 1.85

  rate = rospy.Rate(1)

  while not rospy.is_shutdown():
    pub.publish(p)
    rospy.loginfo("发布的消息：%s, %d, %.2f", p.name, p.age, p.height)
    rate.sleep()



 