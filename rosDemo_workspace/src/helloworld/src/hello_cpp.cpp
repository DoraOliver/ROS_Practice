//1.include ros head file
#include "ros/ros.h"

//2. main function
int main(int argc, char *argv[]){

	//initiate ros node
	ros::init(argc, argv, "hello_node");
	
	//创建ros节点句柄（非必须）
	//ros::NodeHandle n;
	
	//print hello world
	ROS_INFO("Hello world!");
	return 0;

}
