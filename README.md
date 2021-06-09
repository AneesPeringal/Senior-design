# Senior-design
this code is used for the senior design project 2021 ( autonomous assembly of aircrafts mid flight. the objective is to get pose data from optitrack, and use that for the localization of the aircrafts that are used in this project. The code also inludes a position controller to decide how the two drones should move with respect to each other. 
The code will be run on the campanion computrer. in our case, it is the raspberry pi 3 which is running ubuntu 20, ros noetic. 

dependencies: 
1) ros: http://wiki.ros.org/ROS/Installation
2) mavros: sudo apt install ros-noetic-mavros ros-noetic-mavros-extras  http://wiki.ros.org/mavros
3) python 3: sudo apt install python3 ( this should be installed with ros noetic)
4) vrpn_client: sudo apt-get install ros-noetic-vrpn-client-ros

Note: there is some discrepancy between the code that is available here and the code that is in the report. I will update the code here at some point.
