#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

LINEAR_SPEED = 0.2
ANGULAR_SPEED = 0.2
		
class RobotController():
	def __init__(self):
		self.move_cmd = Twist()
		rospy.on_shutdown(self.on_shutdown)
		self.navi_pub = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
		rospy.Subscriber('/odom', Odometry, self.odometry_callback)
		self.last_t = 0
		self.x = 0
		self.y = 0
		self.file = open('data.txt', 'w+')

	def move_forward(self):
		start = rospy.get_rostime().secs
		distance = 0
		while distance <= 2:
			self.move_cmd.angular.x = 0
			self.move_cmd.angular.y = 0
			self.move_cmd.angular.z = 0
			self.move_cmd.linear.x = LINEAR_SPEED
			self.move_cmd.linear.y = 0
			self.move_cmd.linear.z = 0
			self.navi_pub.publish(self.move_cmd)
			distance = LINEAR_SPEED * (rospy.get_rostime().secs - start)

	def move_semi_circle(self):
		start = rospy.get_rostime().secs
		distance = 0
		while distance <= 3.1415:
			self.move_cmd.linear.x = LINEAR_SPEED
			self.move_cmd.linear.y = 0
			self.move_cmd.linear.z = 0
			self.move_cmd.angular.z = ANGULAR_SPEED
			self.move_cmd.angular.y = 0
			self.move_cmd.angular.x = 0
			self.navi_pub.publish(self.move_cmd)
			distance = LINEAR_SPEED * (rospy.get_rostime().secs - start)

	def turn_left(self):
		start = rospy.get_rostime().secs
		distance = 0
		while distance <= 1.6:
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
		odometry.header.stamp = rospy.get_rostime()
		odometry.header.frame_id = "odom"
		odometry.child_frame_id = "base_link"
		odometry.pose.pose.position.x = self.x
		odometry.pose.pose.position.y = self.y
		odometry.pose.pose.position.z = 0.0
		odom_pub.publish(odometry)

	def odometry_callback(self, data):
		odometry = Odometry()
		if(self.last_t == 0):
			self.last_t = get_time(data)
			pass
		current_t = get_time(data)
		dt  = current_t - self.last_t
		angular_vel = data.twist.twist.angular.z
		self.theta = self.theta + (angular_vel * dt)
		vx = data.twist.twist.linear.x
		vy = data.twist.twist.linear.y

		self.x = self.x + (vx * math.cos(self.theta) - vy * math.sin(self.theta)) * dt
		self.y = self.y + (vx * math.cos(self.theta) + vy * math.sin(self.theta)) * dt
		print(self.x, self.y, self.theta)
		self.last_t = current_t
		self.send_data()
		self.save_data_to_file()
    
	def save_data_to_file(self):
		self.file.write()

	def on_shutdown(self):
		rospy.loginfo("Shutting down")
		self.navi_pub.publish(Twist()) # stop robotController
		rospy.sleep(1)

def get_time(data):
	return float(str(data.header.stamp.secs) + '.' + str(data.header.stamp.nsecs))

if __name__ == '__main__':
	rospy.init_node('fixed_path', anonymous=False)
	odom_pub = rospy.Publisher('~estimated_odom', Odometry, queue_size=10)
	try:
		robot_ctrl = RobotController()
		robot_ctrl.move_forward()
		robot_ctrl.move_semi_circle()
		robot_ctrl.move_forward()
		robot_ctrl.turn_left()
		robot_ctrl.move_forward()
		robot_ctrl.turn_left()
		robot_ctrl.stop()
	except rospy.ROSInterruptException: pass
