#!/usr/bin/python

# Written by Lars Baumgaertner (c) 2017
#
# Simple example for setting a new position
# change recipient SID below and user and password for local servald
#
# deps:
#  sudo apt install python-geometry-msgs python-rospy python-yaml python-roslib python-rosgraph-msgs
#  https://github.com/umr-ds/pyserval

import rospy
from geometry_msgs.msg import *
import time
import cPickle
import bz2
from pyserval.client import ServalClient

npos = PoseStamped()
npos.header.frame_id = "world"
npos.pose.position.x = -1.2
npos.pose.position.y = 0.4
npos.pose.orientation.w = 1.0
topic = "/move_base/simple_goal"

np = bz2.compress(cPickle.dumps(npos)).encode("base64").replace("\n","")
print topic
print np

client = ServalClient(user="pum", passwd="pum123")
sender = client.keyring.get_or_create(1)
recipient = "FE638D04EEE9236BCCF004A8C811E12FFEC5B6A1CD5BF0499A7AF84052DEFA78"

msg = "ros " + topic + " " + np
#print "Sending (" + sender[0].sid + " -> " + recipient + ": " + msg
client.meshms.send_message(sender=sender[0].sid,
    recipient=recipient,
    message=msg)
