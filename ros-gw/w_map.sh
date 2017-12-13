#!/bin/bash

# Written by Lars Baumgaertner (c) 2017
#
# update map.png from robot

#WATCHDIR=dir
WATCHFILE=~/mnt/ros/ugv001_map/map.png
MYSID=$(servald id self | tail -1)

handlenew() {
    echo new $1
	# get bundle id
	BID=$(journal ls | grep map.png | grep $MYSID | cut -d \" -f 4)
	if [ "$BID" == "" ]; then
		echo "add"
		rhizome put $WATCHFILE
	else
		echo "update"
		rhizome update $WATCHFILE $BID
	fi
}

echo "WATCHING $WATCHFILE"
LASTMD5=$(md5sum $WATCHFILE | cut -d " " -f 1)
#echo $LASTMD5
while true
do
    CURMD5=$(md5sum $WATCHFILE | cut -d " " -f 1)
    #echo $CURMD5
    if [ "$LASTMD5" != "$CURMD5" ]; then
        handlenew $CURMD5
    fi
    sleep 10
    LASTMD5=$CURMD5
done
