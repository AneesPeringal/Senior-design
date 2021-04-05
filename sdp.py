#!/usr/bin/env python

import rospy
from mavros_msgs.msg import *
from mavros_msgs.srv import *
import math
from time import sleep

def setArm():
	rospy.wait_for_service('/mavros/cmd/arming')
	try:
		armService = rospy.ServiceProxy('mavros/cmd/arming', mavros_msgs.srv.CommandBool)
		armService(True)
	except rospy.ServiceException, e:
		print "Service arming call failed: %s"%e

def setDisarm():
	rospy.wait_for_service('mavros/cmd/arming')
	try:
		armService = rospyService('mavros/cmd/arming',mavros_msgs.srv.CommandBool)
		armService(False)
	except rospy.Exception, e:
		print "Service disarming call failed: %s"%e

def setOffboardMode():
	rospy.wait_for_service('mavros/set_mode')
	try:
		flightModeService = rospy.ServiceProxy('mavros/set_mode', mavros_msgs.srv.SetMode)
		flightModeService(custom_mode = 'OFFBOARD')
	except rospy.ServiceException, e:
		print "Service set_mode call failed %s. Offboard mode could not be set."%e


class Controller:
	def __init__(self):
		self.state = State()
		self.sp = PoseStamped()
		yaw_degrees = 0
		yaw = math.radians(yaw_degrees)
		quaternion = quaternion_from_euler(0,0,yaw)
		self.sp.pose.orientation = Quaternion(*quaternion)
		self.local_pos = point(0,0,0)
		self.position_target_pub = rospy.Publisher('gi/set_pose/position', PoseStamped, queue_size=10)

	def posCb(self, msg):
		self.local_pos.x = msg.pose.position.x
		self.local_pos.y = msg.pose.position.y
		self.local_pos.z = msg.pose.position.z

	def stateCb(self, msg):
		self.state = msg

	##write code to update setpoint later
	def set_pose(self, x=0, y=0, z=2, BODY_FLU = True):
		pose = PoseStamped()
		pose.header.stamp = rospy.Time.now()

		# ROS uses ENU internally, so we will stick to this convention
		if BODY_FLU:
		    pose.header.frame_id = 'base_link'

		else:
		    pose.header.frame_id = 'map'

		pose.pose.position.x = x
		pose.pose.position.y = y
		pose.pose.position.z = z

		return pose



def main():
	rospy.init_node(sdp_node, anonymous = True)
	drone = Controller()
	target = Controller()
	rate = rospy.Rate(20)
	##subscribe to the pose data
	rospy.Subscriber('/mavros/state', State, drone.State)
	rospy.Subscriber('/mavros/vision_pose/pose', PoseStamped, drone.posCb)
	rospy.Subscriber('/mavros/vision_pose/pose2', PoseStamped, target.posCb)
	error_x = 

	
	sp_pub = rospy.Publisher(##publish the setpoints later)



	while not drone.state.armed:
		setArm()
		rate.sleep()
	setOffboardMode()
	
	


	rospy.spin() ##keeps the node running till it is stopped

	
	
