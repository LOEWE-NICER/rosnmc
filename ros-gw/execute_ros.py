#!/usr/bin/python

# Written by Lars Baumgaertner (c) 2017
#
# Set local IP and ROS_MASTER_URI to ROS server
# export ROS_IP=192.168.1.244
# export ROS_MASTER_URI=http://192.168.1.147:11311
#
# usage: $0 <topic> <base64_cpickle_msg>

import rospy
from geometry_msgs.msg import *
import time
import cPickle
import bz2
import sys


rospy.init_node("client")
#npos = PoseStamped()
#npos.header.frame_id = "world"
#npos.pose.position.x = -1.2
#npos.pose.position.y = 0.4
#npos.pose.orientation.w = 1.0
#pub = rospy.Publisher("/move_base/simple_goal", PoseStamped)
#time.sleep(2)
#print "sending command"
#pub.publish(npos)

if len(sys.argv) != 3:
    print "usage: " + sys.argv[0] + " <topic> <base_64_cpickle_msg>"
    print "example: ./execute_ros.py \"/move_base/simple_goal\" Y2NvcHlfcmVnCl9yZWNvbnN0cnVjdG9yCnAxCihjZ2VvbWV0cnlfbXNncy5tc2cuX1Bvc2VTdGFtcGVkClBvc2VTdGFtcGVkCnAyCmNfX2J1aWx0aW5fXwpvYmplY3QKcDMKTnRScDQKKGxwNQpnMQooY3N0ZF9tc2dzLm1zZy5fSGVhZGVyCkhlYWRlcgpwNgpnMwpOdFJwNwoobHA4CkkwCmFnMQooY2dlbnB5LnJvc3RpbWUKVGltZQpwOQpnMwpOdFJwMTAKKGxwMTEKSTAKYUkwCmFiYVMnd29ybGQnCnAxMgphYmFnMQooY2dlb21ldHJ5X21zZ3MubXNnLl9Qb3NlClBvc2UKcDEzCmczCk50UnAxNAoobHAxNQpnMQooY2dlb21ldHJ5X21zZ3MubXNnLl9Qb2ludApQb2ludApwMTYKZzMKTnRScDE3CihscDE4CkYtMS4yCmFGMC40MDAwMDAwMDAwMDAwMDAwMgphRjAKYWJhZzEKKGNnZW9tZXRyeV9tc2dzLm1zZy5fUXVhdGVybmlvbgpRdWF0ZXJuaW9uCnAxOQpnMwpOdFJwMjAKKGxwMjEKRjAKYUYwCmFGMAphRjEKYWJhYmFiLg=="
    sys.exit(1)

topic = sys.argv[1]
b64 = sys.argv[2]

#np = cPickle.dumps(npos).encode("base64").replace("\n","")
#print np
#print len(np)
npos2 = cPickle.loads(bz2.decompress(b64.decode("base64")))
print npos2
pub = rospy.Publisher(topic, type(npos2))
time.sleep(1)
pub.publish(npos2)
#rospy.spin()

