#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from create_node.msg import TurtlebotSensorState

LINEAR_SPEED = 0.2
ANGULAR_SPEED = 0.2
		
class RobotController():
	def __init__(self):
		self.move_cmd = Twist()
		rospy.on_shutdown(self.on_shutdown)
		self.navi_pub = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10) # navigation topic
		rospy.Subscriber('/odom', Odometry, self.odometry_callback) # get odometry
		rospy.Subscriber('mobile_base/sensors/core', TurtlebotSensorState, self.on_sensor_event) # subsriber to all sensors in 'iRobot create'

		self.last_t = 0
		self.x = 0
		self.y = 0
		self.file = open('data.txt', 'w+')

	def on_sensor_event(self, data): # safety calback
		if(data.cliff_left or data.cliff_right or data.cliff_front_right or data.cliff_front_left or data.bumps_wheeldrops > 0):
		    print('* CLiff or Bump *') # print warning
		    self.stop()

	def move_forward(self):
		start = rospy.get_rostime().secs
		distance = 0
		while distance <= 2: # until current distance is 2
			self.move_cmd.angular.x = 0
			self.move_cmd.angular.y = 0
			self.move_cmd.angular.z = 0
			self.move_cmd.linear.x = LINEAR_SPEED
			self.move_cmd.linear.y = 0
			self.move_cmd.linear.z = 0
			self.navi_pub.publish(self.move_cmd) move robot straight
			distance = LINEAR_SPEED * (rospy.get_rostime().secs - start) # calculate current distance

	def move_semi_circle(self):
		start = rospy.get_rostime().secs
		distance = 0
		while distance <= 3.1415: # PI meters as r = 1
			self.move_cmd.linear.x = LINEAR_SPEED
			self.move_cmd.linear.y = 0
			self.move_cmd.linear.z = 0
			self.move_cmd.angular.z = ANGULAR_SPEED
			self.move_cmd.angular.y = 0
			self.move_cmd.angular.x = 0
			self.navi_pub.publish(self.move_cmd)
			distance = LINEAR_SPEED * (rospy.get_rostime().secs - start) # calulate circumference

	def turn_left(self):
		start = rospy.get_rostime().secs
		distance = 0
		while distance <= 1.6: # calculate angle for pi/2
			self.move_cmd.linear.x = 0
			self.move_cmd.linear.y = 0
			self.move_cmd.linear.z = 0
			self.move_cmd.angular.z = ANGULAR_SPEED
			self.move_cmd.angular.y = 0
			self.move_cmd.angular.x = 0
			self.navi_pub.publish(self.move_cmd)
			distance = ANGULAR_SPEED * (rospy.get_rostime().secs - start)

	def stop(self):
		self.move_cmd = Twist()
		self.navi_pub.publish(self.move_cmd)

	def send_data(self):
		odometry.header.stamp = rospy.get_rostime() # create header
		odometry.header.frame_id = "odom"
		odometry.child_frame_id = "base_link"
		odometry.pose.pose.position.x = self.x
		odometry.pose.pose.position.y = self.y
		odometry.pose.pose.position.z = 0.0
		odom_pub.publish(odometry) # send to new topic

	def odometry_callback(self, data):
		odometry = Odometry()
		if(self.last_t == 0):
			self.last_t = get_time(data) # get time from the header for t0
			pass
		current_t = get_time(data)
		dt  = current_t - self.last_t # delta t
		dtheta = angular_vel * dt
		angular_vel = data.twist.twist.angular.z
		self.theta = self.theta + dtheta # calculate theta
		v = data.twist.twist.linear.x
		dx = v * dt
		self.x = self.x + dx * math.cos(self.theta + dtheta/2) # trapezoidal rule to integrate 
		self.y = self.y + dx * math.sin(self.theta + dtheta/2)
		print(self.x, self.y, self.theta)
		self.last_t = current_t
		self.send_data() # send estimated pos
		self.save_data_to_file() # save values to file
    
	def save_data_to_file(self):
		self.file.write()

	def on_shutdown(self):
		rospy.loginfo("Shutting down")
		self.navi_pub.publish(Twist()) # stop robot
		rospy.sleep(1)

def get_time(data):
	return float(str(data.header.stamp.secs) + '.' + str(data.header.stamp.nsecs))

if __name__ == '__main__':
	rospy.init_node('fixed_path', anonymous=False)
	odom_pub = rospy.Publisher('~estimated_odom', Odometry, queue_size=10) # new topic
	robot_ctrl = RobotController()
	try:
		robot_ctrl.move_forward()
		robot_ctrl.move_semi_circle()
		robot_ctrl.move_forward()
		robot_ctrl.turn_left()
		robot_ctrl.move_forward()
		robot_ctrl.turn_left()
		robot_ctrl.stop()
	except rospy.ROSInterruptException: pass
