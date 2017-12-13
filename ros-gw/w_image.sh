#!/bin/bash

# Written by Lars Baumgaertner (c) 2017
#
# check for new images and add to mobile cloud

WATCHDIR=dir
WATCHDIR=~/mnt/ros/ugv001_image_rgb

handlenew() {
    echo new $1
	ls -la $WATCHDIR/$1/image_color.jpg
	rhizome put $WATCHDIR/$1/image_color.jpg
}

echo "WATCHING $WATCHDIR"
LASTFILES=/tmp/w.1
ls -1 $WATCHDIR > $LASTFILES
while true
do
    CURFILES=/tmp/w.2
    ls -1 $WATCHDIR > $CURFILES
    for file in $(diff -r $LASTFILES $CURFILES | grep ">"  | cut -d " " -f 2); do
        handlenew $(echo $file)
    done
    sleep 10
    cp $CURFILES $LASTFILES
done
