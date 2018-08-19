#!/usr/bin/env python
import rospy
from create_node.msg import TurtlebotSensorState
from geometry_msgs.msg import Twist
import sys, select, termios, tty

DIRECTION_MAPPING = {
    'j': 1, # left
    'l': -1, # right
}

SPEED_MAPPING = {
    'i': 1, # increase speed
    'm': -1, # decrease speed
}

class Robot():
    def __init__(self):
        rospy.init_node('keyboard_teleop', anonymous=False)
        rospy.on_shutdown(self.on_shutdown)
        self.cmd_pub = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=5) # navigation message publisher
        self.should_stop = False # a flag to represent if robot should stop
        self.move_cmd = Twist() # new empty message
    
    def on_shutdown(self):
        rospy.loginfo("Shutting down")
        self.cmd_pub.publish(Twist()) # stop robot 
        rospy.sleep(1)

    def on_sensor_event(self, data): 
        if(data.cliff_left or data.cliff_right or data.cliff_front_right or data.cliff_front_left or data.bumps_wheeldrops > 0):
            print('********* CLiff or Bump *******************') # print warning
            self.should_stop = True # should stop if bumped or about to be cliff-ed
        else:
            self.should_stop = False

    def turn(self, direction, speed): 
        self.move_cmd.angular.z = direction * speed # just change direction and speed  of angular x 
        self.move_cmd.angular.y = 0
        self.move_cmd.angular.x = 0
        return self

    def move_forward(self, speed):
        self.move_cmd.linear.x = speed # set current speed 
        self.move_cmd.linear.y = 0
        self.move_cmd.linear.z = 0
        return self
        
    def stop(self):
        self.move_cmd = Twist() # all values to zero
        self.cmd_pub.publish(self.move_cmd)
    
    def do_it(self, time):
        rate = rospy.Rate(time)
        while(not self.should_stop):
            self.cmd_pub.publish(self.move_cmd)
            rate.sleep()

if __name__ == '__main__':
    robot = Robot() # create an instance of above Class
    rate = rospy.Rate(1)
    stop = False # flag to denote robot state
    while not rospy.is_shutdown():
        # if(robot.should_stop or stop): #stp if already stopped
        #     stop = True

        # if(stop):        
        #     robot.stop()
        # else:
        robot.move_forward(0.2)
        robot.do_it(10)
        robot.stop()

        robot.move_forward(0.1).turn(-1, 0.1)
        robot.do_it(5)
        robot.stop()

        robot.move_forward(0.2)
        robot.do_it(10)

        robot.turn(-1, 0.2)
        robot.do_it(5)
        robot.stop()

        robot.move_forward(0.2)
        robot.do_it(10)
        robot.stop()

        robot.turn(-1, 0.2)
        robot.do_it(5)
        robot.stop()

        rate.sleep()


        
