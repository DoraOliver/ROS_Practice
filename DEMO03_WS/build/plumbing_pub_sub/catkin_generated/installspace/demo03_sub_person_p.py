#!/usr/bin/env python3

import rospy
from plumbing_pub_sub.msg import Person

def doMsg(p):
  rospy.loginfo("受到的消息：%s,%d,%.2f", p.name, p.age, p.height)

if __name__ == "__main__":

  rospy.init_node("Telephone")

  sub = rospy.Subscriber("chat", Person, doMsg)

  rospy.spin()
