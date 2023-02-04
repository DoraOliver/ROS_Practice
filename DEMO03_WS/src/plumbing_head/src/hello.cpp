#include "ros/ros.h"
#include "plumbing_head/hello.h"

namespace hello_ns{ 
// namespace hello_ns 

void MyHello::run(){
  ROS_INFO("run 函数执行。。。");
}
}

int main(int argc, char *argv[])
{
  setlocale(LC_ALL,"");
  ros::init(argc,argv,"hello_hedad");
  hello_ns::MyHello myHello;

  return 0;
}