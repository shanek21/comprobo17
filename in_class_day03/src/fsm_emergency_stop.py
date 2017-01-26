#! /usr/bin/env python

from neato_node.msg import Bump
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import rospy

class Collision():

    def __init__(self):
        rospy.init_node('collision')
        rospy.Subscriber('/bump', Bump, self.bump_callback,
                                    queue_size=10)
        rospy.Subscriber('/scan', LaserScan, self.laser_callback,
                                    queue_size=10)
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.isBump = False
        self.frontScan = 0
        self.state = "forward"
        self.time_interval = rospy.get_time()

    def bump_callback(self, msg):
        if (msg.leftFront or msg.rightFront or msg.leftSide or msg.rightSide):
            self.isBump = True
        else:
            self.isBump = False

    def laser_callback(self, msg):
        self.frontScan = msg.ranges[0]

    def act(self):
        twist_msg = Twist()
        if (self.state == "forward"):
            if (self.isBump):
                self.state = "backward"
                twist_msg.linear.x = 0
            else:
                twist_msg.linear.x = 1
        elif (self.state == "backward"):
            if (self.frontScan >= 2):
                self.state = "rotate_left"
                twist_msg.linear.x = 0
                self.time_interval = rospy.get_time()
            else:
                twist_msg.linear.x = -1
        elif (self.state == "rotate_left"):
            if (rospy.get_time() - self.time_interval >= 1):
                self.state = "forward"
                twist_msg.angular.z = 0
            else:
                twist_msg.angular.z = 1
        self.pub.publish(twist_msg)

if (__name__=="__main__"):
    collide = Collision()
    r = rospy.Rate(10)
    while (not rospy.is_shutdown()):
        r.sleep()
        collide.act()
