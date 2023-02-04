#! /usr/bin/env python
##compile

#1.package
import rospy

#2.main
if __name__ == "__main__":
	#3.initiate ros node
	rospy.init_node("hello_p")
	#4.get hello world
	rospy.loginfo("Hello world! by python")
