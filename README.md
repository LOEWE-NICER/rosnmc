# rosnmc

Example tools for connecting a ROS-Robot with a NICER-Gateway PC via Serval to the NICER Mobile Cloud. Tested on raspberry pi (raspbian 9.1 stretch) and ubuntu 16.04.

## Dependencies & Setup

### All involved machines (except robot)
* Installed version of servald http://github.com/servalproject/serval-dna
* ROS python libraries `sudo apt install python-geometry-msgs python-rospy python-yaml python-roslib python-rosgraph-msgs`


Set serval working directory:
```
export SERVALINSTANCE_PATH=/tmp/s
```

### Robot
* Install gatling `sudo apt-get install gatling`

Share output directory where images and sensor data is written.

### ROS Gateway (ros-gw)
* Serval shell scripts http://github.com/gh0st42/servalshellscripts
* install ftp fs `sudo apt-get install curlftpfs`


Set ROS_IP to local IP and ROS_MASTER_URI to robot IP.
```
export ROS_IP=192.168.1.244
export ROS_MASTER_URI=http://192.168.1.147:11311
```

Use `curlftpfs` to mount image directory from robot (`curlftpfs 192.168.1.147:2121 ~/mnt/ros`).

### Client

* pyserval library in PYTHONPATH or installed via pip https://github.com/umr-ds/pyserval

## Provided tools

### ros-gw/

* `execute_ros.py` - helper script to execute a ros publish to a topic with serialized ros message object
* `chatbot-ng` - handle incoming ros commands via meshms
* `w_image.sh` - monitor a directory for robot images and add each one to mobile cloud
* `w_map.sh` - monitor a directory for robot `map.png` and update entry in mobile cloud

### client/

* `servalros_example.py` - set position of robot via ros-over-serval