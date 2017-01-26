#! /usr/bin/env python

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import rospy

class Collision():

    def __init__(self):
        rospy.init_node('collision')
        self.sub = rospy.Subscriber('/scan', LaserScan, self.callback, queue_size=10)
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    def callback(self, msg):
        print "Callback"
        twist_msg = Twist()
        if (msg.ranges[0] <= 1 and msg.ranges[0] > .01):
            twist_msg.linear.x = 0
            print "Hit!"
        else:
            print "Miss!"
            twist_msg.linear.x = 1
        self.pub.publish(twist_msg)

if (__name__=="__main__"):
    collide = Collision()
    r = rospy.Rate(10)
    while (not rospy.is_shutdown()):
        r.sleep()
