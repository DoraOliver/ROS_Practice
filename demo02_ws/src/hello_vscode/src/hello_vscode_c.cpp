#include "ros/ros.h"

int main(int argc, char *argv[])
{
  ros::init(argc,argv,"hello_c");
  ROS_INFO("Hello");

  return 0;
}