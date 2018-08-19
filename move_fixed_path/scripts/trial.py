#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

move_cmd = Twist()

def move_forward():
    start = rospy.get_rostime().to_nsec()
    speed = 0.2
    distance = 0
    while distance <= 2:
		move_cmd.linear.x = 0
		move_cmd.linear.y = 0
		move_cmd.linear.z = 0
		move_cmd.linear.x = speed
		move_cmd.linear.y = 0
		move_cmd.linear.z = 0
		cmd.publish(move_cmd)
		distance = speed * (rospy.get_rostime().secs - start)

def move_semi_circle():
	start = rospy.get_rostime().secs
	distance = 0
	angular_speed = 0.2
	linear_speed = 0.2
	while distance <= 3.1415:
		move_cmd.linear.x = linear_speed
		move_cmd.linear.y = 0
		move_cmd.linear.z = 0
		move_cmd.angular.z = angular_speed
		move_cmd.angular.y = 0
		move_cmd.angular.x = 0
		cmd.publish(move_cmd)
		distance = linear_speed * (rospy.get_rostime().secs - start)

def turn_left():
	start = rospy.get_rostime().secs
	distance = 0
	angular_speed = 0.2
	while distance <= 1.57:
		move_cmd.linear.x = 0
		move_cmd.linear.y = 0
		move_cmd.linear.z = 0
		move_cmd.angular.z = angular_speed
		move_cmd.angular.y = 0
		move_cmd.angular.x = 0
		cmd.publish(move_cmd)
		distance = angular_speed * (rospy.get_rostime().secs - start)


def stop():
	move_cmd.linear.x = 0
	move_cmd.linear.y = 0
	move_cmd.linear.z = 0
	move_cmd.angular.z = 0
	move_cmd.angular.y = 0
	move_cmd.angular.x = 0
	cmd.publish(move_cmd)
    
def on_shutdown():
	rospy.loginfo("Shutting down")
	cmd.publish(Twist()) # stop robot 
	rospy.sleep(1)

if __name__ == '__main__':
	global cmd
	rospy.init_node('fixed_path', anonymous=False)
	rospy.on_shutdown(on_shutdown)
	cmd = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=5)
	move_forward()
	stop()
	move_semi_circle()
	stop()
	move_forward()
	stop()
	turn_left()
	stop()
	move_forward()
	stop()
	turn_left()
	stop()
	rospy.spin()
