#!/usr/bin/env python

""" Exploring the basics of creating messages inside of a ROS node """

from geometry_msgs.msg import PointStamped, Point
from std_msgs.msg import Header
import rospy

rospy.init_node('my_first_node')
pub = rospy.Publisher('/cool_point', PointStamped, queue_size=10)

r = rospy.Rate(2)
while True:
        header_message = Header(stamp=rospy.Time.now(), frame_id="odom")
	point_message = Point(x=1.0, y=2.0)
        point_stamped_message = PointStamped(header=header_message,
                                             point=point_message)
        pub.publish(point_stamped_message)
	r.sleep()

print "Node is finished!"
