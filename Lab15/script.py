#!/usr/bin/bash
input=$1
tshark -d tcp.port==6633,openflow -r $input > mlog
sed -n '/Type:/p' "mlog" | awk '{print $9}' > mlog_1
 
HELLO=0
PORT_STATUS=0
SET_CONFIG=0
FEATURES_REQUEST=0
FEATURES_REPLY=0
PACKET_IN=0
PACKET_OUT=0
FLOW_MOD=0
STATS_REQUEST=0
STATS_REPLY=0
BARRIER_REQUEST=0
BARRIER_REPLY=0
total=0
 
while read -r line
do
  if [ "$line" = "OFPT_PORT_STATUS" ]
  then
    PORT_STATUS=$(($PORT_STATUS+1))
    total=$(($total+1))
  elif [ "$line" = "OFPT_FEATURES_REQUEST" ]
  then
    FEATURES_REQUEST=$(($FEATURES_REQUEST+1))
    total=$(($total+1))
  elif [ "$line" = "OFPT_FEATURES_REPLY" ]
  then
    FEATURES_REPLY=$(($FEATURES_REPLY+1))
    total=$(($total+1))
  elif [ "$line" = "OFPT_SET_CONFIG" ]
  then
    SET_CONFIG=$(($SET_CONFIG+1))
    total=$(($total+1))
  elif [ "$line" = "OFPT_PACKET_IN" ]
  then
    PACKET_IN=$((PACKET_IN+1))
    total=$(($total+1))
  elif [ "$line" = "OFPT_PACKET_OUT" ]
  then
    PACKET_OUT=$((PACKET_OUT+1))
    total=$(($total+1))
  elif [ "$line" = "OFPT_FLOW_MOD" ]
  then
    FLOW_MOD=$((FLOW_MOD+1))
    total=$(($total+1))
  elif [ "$line" = "OFPT_HELLO" ]
  then
    HELLO=$(($HELLO+1))
    total=$(($total+1))
  elif [ "$line" = "OFPT_STATS_REQUEST" ]
  then
    STATS_REQUEST=$(($STATS_REQUEST+1))
    total=$(($total+1))
  elif [ "$line" = "OFPT_STATS_REPLY" ]
  then
    STATS_REPLY=$(($STATS_REPLY+1))
    total=$(($total+1))
  elif [ "$line" = "OFPT_BARRIER_REQUEST" ]
  then
    BARRIER_REQUEST=$((BARRIER_REQUEST+1))
    total=$(($total+1))
  elif [ "$line" = "OFPT_BARRIER_REPLY" ]
  then
    BARRIER_REPLY=$(($BARRIER_REPLY+1))
    total=$(($total+1))
  else
    echo $line
  fi
done < "mlog_1"
 
echo "HELLO=" $HELLO
echo "PORT_STATUS=" $PORT_STATUS
echo "FEATURES_REQUEST=" $FEATURES_REQUEST
echo "FEATURES_REPLY=" $FEATURES_REPLY
echo "SET_CONFIG=" $SET_CONFIG
echo "PACKET_IN=" $PACKET_IN
echo "PACKET_OUT=" $PACKET_OUT
echo "FLOW_MOD=" $FLOW_MOD
echo "STATS_REQUEST=" $STATS_REQUEST
echo "STATS_REPLY=" $STATS_REPLY
echo "BARRIER_REQUEST=" $BARRIER_REQUEST
echo "BARRIER_REPLY=" $BARRIER_REPLY
echo "number of OpenFlow packets=" $total
