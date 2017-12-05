
from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpidToStr
from pox.lib.addresses import IPAddr, EthAddr
from pox.lib.packet.arp import arp
from pox.lib.packet.ethernet import ethernet, ETHER_BROADCAST
from pox.lib.packet.packet_base import packet_base
from pox.lib.packet.packet_utils import *
import pox.lib.packet as pkt
from pox.lib.recoco import Timer
import time

s1_dpid=0
s2_dpid=0
s3_dpid=0
s4_dpid=0
s5_dpid=0
s6_dpid=0

s1_p1=0
s1_p2=0
s1_p3=0

s2_p1=0
s2_p2=0
s2_p3=0
s2_p4=0

s3_p1=0
s3_p2=0
s3_p3=0

s4_p1=0
s4_p2=0
s4_p3=0

s5_p1=0
s5_p2=0
s5_p3=0
s5_p4=0

s6_p1=0
s6_p2=0
s6_p3=0

####################
pre_s1_p1=0
pre_s1_p2=0
pre_s1_p3=0

pre_s2_p1=0
pre_s2_p2=0
pre_s2_p3=0
pre_s2_p4=0

pre_s3_p1=0
pre_s3_p2=0
pre_s3_p3=0

pre_s4_p1=0
pre_s4_p2=0
pre_s4_p3=0

pre_s5_p1=0
pre_s5_p2=0
pre_s5_p3=0
pre_s5_p4=0

pre_s6_p1=0
pre_s6_p2=0
pre_s6_p3=0

s1_dpid=0
s2_dpid=0
s3_dpid=0
s4_dpid=0
s5_dpid=0

def _handle_portstats_received (event):
 global s1_dpid, s2_dpid, s3_dpid, s4_dpid, s5_dpid, s6_dpid
 global s1_p1, s1_p2, s1_p3, s2_p1, s2_p2, s2_p3, s2_p4, s3_p1, s3_p1, s3_p2, s4_p1, s4_p2, s4_p3, s5_p1, s5_p2, s5_p3, s5_p4, s6_p1, s6_p2, s6_p3
 global pre_s1_p1, pre_s1_p2, pre_s1_p3, pre_s2_p1, pre_s2_p2, pre_s2_p3, pre_s2_p4, pre_s3_p1, pre_s3_p2, pre_s3_p3, pre_s4_p1, pre_s4_p2, pre_s4_p3, pre_s5_p1, pre_s5_p2, pre_s5_p3, pre_s5_p4, pre_s6_p1, pre_s6_p2, pre_s6_p3
 
 if event.connection.dpid==s1_dpid:
   for f in event.stats:
    if int(f.port_no)<65534:
      if f.port_no==1:
        pre_s1_p1=s1_p1
        s1_p1=f.rx_packets
      if f.port_no==2:
        pre_s1_p2=s1_p2
        s1_p2=f.tx_packets
      if f.port_no==3:
        pre_s1_p3=s1_p3
        s1_p3=f.tx_packets

 if event.connection.dpid==s2_dpid:
   for f in event.stats:
    if int(f.port_no)<65534:
      if f.port_no==1:
        pre_s2_p1=s2_p1
        s2_p1=f.rx_packets
      if f.port_no==2:
        pre_s2_p2=s2_p2
        s2_p2=f.tx_packets
      if f.port_no==3:
        pre_s2_p3=p2_p3
        s2_p3=f.tx_packets
      if f.port_no==4:
        pre_s2_p4=p2_p4
        s2_p4=f.tx_packets

 if event.connection.dpid==s3_dpid:
   for f in event.stats:
    if int(f.port_no)<65534:
      if f.port_no==1:
        pre_s3_p1=s3_p1
        s3_p1=f.rx_packets
      if f.port_no==2:
        pre_s3_p2=s3_p2
        s3_p2=f.tx_packets
      if f.port_no==3:
        pre_s3_p3=s3_p3
        s3_p3=f.tx_packets

 if event.connection.dpid==s4_dpid:
   for f in event.stats:
    if int(f.port_no)<65534:
      if f.port_no==1:
        pre_s4_p1=s4_p1
        s4_p1=f.rx_packets
      if f.port_no==2:
        pre_s4_p2=s4_p2
        s4_p2=f.tx_packets
      if f.port_no==3:
        pre_s4_p3=s4_p3
        s4_p3=f.tx_packets

 if event.connection.dpid==s5_dpid:
   for f in event.stats:
    if int(f.port_no)<65534:
      if f.port_no==1:
        pre_s5_p1=s5_p1
        s5_p1=f.rx_packets
      if f.port_no==2:
        pre_s5_p2=s5_p2
        s5_p2=f.tx_packets
      if f.port_no==3:
        pre_s5_p3=p5_p3
        s5_p3=f.tx_packets
      if f.port_no==4:
        pre_s5_p4=p5_p4
        s5_p4=f.tx_packets

 if event.connection.dpid==s6_dpid:
   for f in event.stats:
    if int(f.port_no)<65534:
      if f.port_no==1:
        pre_s6_p1=s6_p1
        s6_p1=f.rx_packets
      if f.port_no==2:
        pre_s6_p2=s6_p2
        s6_p2=f.tx_packets
      if f.port_no==3:
        pre_s6_p3=s6_p3
        s6_p3=f.tx_packets

def _handle_ConnectionUp (event):
 global s1_dpid, s2_dpid, s3_dpid, s4_dpid, s5_dpid, s6_dpid
 print "ConnectionUp: ",dpidToStr(event.connection.dpid)

 for m in event.connection.features.ports:
  if m.name == "s1-eth1":
    s1_dpid = event.connection.dpid
    print "s1_dpid=", s1_dpid
  elif m.name == "s2-eth1":
    s2_dpid = event.connection.dpid
    print "s2_dpid=", s2_dpid
  elif m.name == "s3-eth1":
    s3_dpid = event.connection.dpid
    print "s3_dpid=", s3_dpid
  elif m.name == "s4-eth1":
    s4_dpid = event.connection.dpid
    print "s4_dpid=", s4_dpid
  elif m.name == "s5-eth1":
    s5_dpid = event.connection.dpid
    print "s5_dpid=", s5_dpid
  elif m.name == "s6-eth1":
    s6_dpid = event.connection.dpid
    print "s6_dpid=", s6_dpid



def _handle_PacketIn(event):
 global s1_dpid, s2_dpid, s3_dpid, s4_dpid, s5_dpid, s6_dpid
 packet=event.parsed
 print "_handle_PacketIn is called, packet.type:", packet.type, " event.connection.dpid:", event.connection.dpid

###################################
 if event.connection.dpid==s1_dpid:
    a=packet.find('arp')
    if a and a.protodst=="10.0.0.1":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=1))
       event.connection.send(msg)
    if a and a.protodst=="10.0.0.2":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=2))
       event.connection.send(msg)
    if a and a.protodst=="10.0.0.6":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=3))
       event.connection.send(msg)
    if a and a.protodst=="10.0.0.3":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=2))
       event.connection.send(msg)
    if a and a.protodst=="10.0.0.4":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=2))
       event.connection.send(msg)
    if a and a.protodst=="10.0.0.5":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=3))
       event.connection.send(msg)

#AddFlows s1
    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.1"
    msg.match.nw_dst = "10.0.0.2"
    msg.actions.append(of.ofp_action_output(port = 2))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.1"
    msg.match.nw_dst = "10.0.0.3"
    msg.actions.append(of.ofp_action_output(port = 2))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.1"
    msg.match.nw_dst = "10.0.0.4"
    msg.actions.append(of.ofp_action_output(port = 2))
    event.connection.send(msg)
    
    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.1"
    msg.match.nw_dst = "10.0.0.5"
    msg.actions.append(of.ofp_action_output(port = 3))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.1"
    msg.match.nw_dst = "10.0.0.6"
    msg.actions.append(of.ofp_action_output(port = 3))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.2"
    msg.match.nw_dst = "10.0.0.1"
    msg.actions.append(of.ofp_action_output(port = 1))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.2"
    msg.match.nw_dst = "10.0.0.6"
    msg.actions.append(of.ofp_action_output(port = 3))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.3"
    msg.match.nw_dst = "10.0.0.1"
    msg.actions.append(of.ofp_action_output(port = 1))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.3"
    msg.match.nw_dst = "10.0.0.6"
    msg.actions.append(of.ofp_action_output(port = 3))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.4"
    msg.match.nw_dst = "10.0.0.1"
    msg.actions.append(of.ofp_action_output(port = 1))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.5"
    msg.match.nw_dst = "10.0.0.1"
    msg.actions.append(of.ofp_action_output(port = 1))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.6"
    msg.match.nw_dst = "10.0.0.1"
    msg.actions.append(of.ofp_action_output(port = 1))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.6"
    msg.match.nw_dst = "10.0.0.2"
    msg.actions.append(of.ofp_action_output(port = 2))
    event.connection.send(msg)
    
####################################
 if event.connection.dpid==s2_dpid:
    a=packet.find('arp')
    if a and a.protodst=="10.0.0.2":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=1))
       event.connection.send(msg)
    if a and a.protodst=="10.0.0.1":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=2))
       event.connection.send(msg)
    if a and a.protodst=="10.0.0.3":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=3))
       event.connection.send(msg)
    if a and a.protodst=="10.0.0.5":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=4))
       event.connection.send(msg)
    if a and a.protodst=="10.0.0.4":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=3))
       event.connection.send(msg)
    if a and a.protodst=="10.0.0.6":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=2))
       event.connection.send(msg)
       
#Add flows s2
    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.1"
    msg.match.nw_dst = "10.0.0.2"
    msg.actions.append(of.ofp_action_output(port = 1))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.1"
    msg.match.nw_dst = "10.0.0.3"
    msg.actions.append(of.ofp_action_output(port = 3))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.1"
    msg.match.nw_dst = "10.0.0.4"
    msg.actions.append(of.ofp_action_output(port = 3))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.2"
    msg.match.nw_dst = "10.0.0.1"
    msg.actions.append(of.ofp_action_output(port = 2))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.2"
    msg.match.nw_dst = "10.0.0.3"
    msg.actions.append(of.ofp_action_output(port = 3))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.2"
    msg.match.nw_dst = "10.0.0.4"
    msg.actions.append(of.ofp_action_output(port = 3))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.2"
    msg.match.nw_dst = "10.0.0.5"
    msg.actions.append(of.ofp_action_output(port = 4))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.2"
    msg.match.nw_dst = "10.0.0.6"
    msg.actions.append(of.ofp_action_output(port = 2))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.3"
    msg.match.nw_dst = "10.0.0.1"
    msg.actions.append(of.ofp_action_output(port = 2))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.3"
    msg.match.nw_dst = "10.0.0.2"
    msg.actions.append(of.ofp_action_output(port = 1))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.3"
    msg.match.nw_dst = "10.0.0.6"
    msg.actions.append(of.ofp_action_output(port = 2))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.4"
    msg.match.nw_dst = "10.0.0.2"
    msg.actions.append(of.ofp_action_output(port = 1))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.5"
    msg.match.nw_dst = "10.0.0.2"
    msg.actions.append(of.ofp_action_output(port = 1))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.6"
    msg.match.nw_dst = "10.0.0.2"
    msg.actions.append(of.ofp_action_output(port = 1))
    event.connection.send(msg)
    
####################################
 if event.connection.dpid==s3_dpid:
    a=packet.find('arp')
    if a and a.protodst=="10.0.0.3":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=1))
       event.connection.send(msg)
    if a and a.protodst=="10.0.0.2":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=2))
       event.connection.send(msg)
    if a and a.protodst=="10.0.0.6":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=2))
       event.connection.send(msg)
    if a and a.protodst=="10.0.0.4":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=3))
       event.connection.send(msg)
    if a and a.protodst=="10.0.0.5":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=3))
       event.connection.send(msg)
    if a and a.protodst=="10.0.0.1":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=2))
       event.connection.send(msg)

#Add flows s3
    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.1"
    msg.match.nw_dst = "10.0.0.3"
    msg.actions.append(of.ofp_action_output(port = 1))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.1"
    msg.match.nw_dst = "10.0.0.4"
    msg.actions.append(of.ofp_action_output(port = 3))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.2"
    msg.match.nw_dst = "10.0.0.3"
    msg.actions.append(of.ofp_action_output(port = 1))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.2"
    msg.match.nw_dst = "10.0.0.4"
    msg.actions.append(of.ofp_action_output(port = 3))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.3"
    msg.match.nw_dst = "10.0.0.1"
    msg.actions.append(of.ofp_action_output(port = 2))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.3"
    msg.match.nw_dst = "10.0.0.2"
    msg.actions.append(of.ofp_action_output(port = 2))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.3"
    msg.match.nw_dst = "10.0.0.4"
    msg.actions.append(of.ofp_action_output(port = 3))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.3"
    msg.match.nw_dst = "10.0.0.5"
    msg.actions.append(of.ofp_action_output(port = 3))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.3"
    msg.match.nw_dst = "10.0.0.6"
    msg.actions.append(of.ofp_action_output(port = 2))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.4"
    msg.match.nw_dst = "10.0.0.2"
    msg.actions.append(of.ofp_action_output(port = 2))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.4"
    msg.match.nw_dst = "10.0.0.3"
    msg.actions.append(of.ofp_action_output(port = 1))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.5"
    msg.match.nw_dst = "10.0.0.3"
    msg.actions.append(of.ofp_action_output(port = 1))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.6"
    msg.match.nw_dst = "10.0.0.3"
    msg.actions.append(of.ofp_action_output(port = 1))
    event.connection.send(msg)
 
####################################
 if event.connection.dpid==s4_dpid:
    a=packet.find('arp')
    if a and a.protodst=="10.0.0.4":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=1))
       event.connection.send(msg)
    if a and a.protodst=="10.0.0.3":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=2))
       event.connection.send(msg)
    if a and a.protodst=="10.0.0.1":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=2))
       event.connection.send(msg)
    if a and a.protodst=="10.0.0.2":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=2))
       event.connection.send(msg)
    if a and a.protodst=="10.0.0.5":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=3))
       event.connection.send(msg)
    if a and a.protodst=="10.0.0.6":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=3))
       event.connection.send(msg)
      
 #Add flows s4
    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.1"
    msg.match.nw_dst = "10.0.0.4"
    msg.actions.append(of.ofp_action_output(port = 1))
    event.connection.send(msg)
    
    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.2"
    msg.match.nw_dst = "10.0.0.4"
    msg.actions.append(of.ofp_action_output(port = 1))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.3"
    msg.match.nw_dst = "10.0.0.4"
    msg.actions.append(of.ofp_action_output(port = 1))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.3"
    msg.match.nw_dst = "10.0.0.5"
    msg.actions.append(of.ofp_action_output(port = 3))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.4"
    msg.match.nw_dst = "10.0.0.1"
    msg.actions.append(of.ofp_action_output(port = 3))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.4"
    msg.match.nw_dst = "10.0.0.2"
    msg.actions.append(of.ofp_action_output(port = 2))
    event.connection.send(msg)


    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.4"
    msg.match.nw_dst = "10.0.0.3"
    msg.actions.append(of.ofp_action_output(port = 2))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.4"
    msg.match.nw_dst = "10.0.0.5"
    msg.actions.append(of.ofp_action_output(port = 3))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.4"
    msg.match.nw_dst = "10.0.0.6"
    msg.actions.append(of.ofp_action_output(port = 3))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.5"
    msg.match.nw_dst = "10.0.0.3"
    msg.actions.append(of.ofp_action_output(port = 2))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.5"
    msg.match.nw_dst = "10.0.0.4"
    msg.actions.append(of.ofp_action_output(port = 1))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.6"
    msg.match.nw_dst = "10.0.0.3"
    msg.actions.append(of.ofp_action_output(port = 2))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.6"
    msg.match.nw_dst = "10.0.0.4"
    msg.actions.append(of.ofp_action_output(port = 1))
    event.connection.send(msg)
 
####################################
 if event.connection.dpid==s5_dpid:
    a=packet.find('arp')
    if a and a.protodst=="10.0.0.5":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=1))
       event.connection.send(msg)
    if a and a.protodst=="10.0.0.2":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=2))
       event.connection.send(msg)
    if a and a.protodst=="10.0.0.3":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=3))
       event.connection.send(msg)
    if a and a.protodst=="10.0.0.1":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=4))
       event.connection.send(msg)
    if a and a.protodst=="10.0.0.4":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=3))
       event.connection.send(msg)
    if a and a.protodst=="10.0.0.6":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=4))
       event.connection.send(msg)

#Add flows s5
    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.1"
    msg.match.nw_dst = "10.0.0.5"
    msg.actions.append(of.ofp_action_output(port = 1))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.2"
    msg.match.nw_dst = "10.0.0.5"
    msg.actions.append(of.ofp_action_output(port = 1))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.3"
    msg.match.nw_dst = "10.0.0.5"
    msg.actions.append(of.ofp_action_output(port = 1))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.4"
    msg.match.nw_dst = "10.0.0.1"
    msg.actions.append(of.ofp_action_output(port = 4))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.4"
    msg.match.nw_dst = "10.0.0.5"
    msg.actions.append(of.ofp_action_output(port = 1))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.4"
    msg.match.nw_dst = "10.0.0.6"
    msg.actions.append(of.ofp_action_output(port = 4))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.5"
    msg.match.nw_dst = "10.0.0.1"
    msg.actions.append(of.ofp_action_output(port = 4))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.5"
    msg.match.nw_dst = "10.0.0.2"
    msg.actions.append(of.ofp_action_output(port = 2))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.5"
    msg.match.nw_dst = "10.0.0.3"
    msg.actions.append(of.ofp_action_output(port = 3))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.5"
    msg.match.nw_dst = "10.0.0.4"
    msg.actions.append(of.ofp_action_output(port = 3))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.5"
    msg.match.nw_dst = "10.0.0.6"
    msg.actions.append(of.ofp_action_output(port = 4))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.6"
    msg.match.nw_dst = "10.0.0.3"
    msg.actions.append(of.ofp_action_output(port = 3))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.6"
    msg.match.nw_dst = "10.0.0.4"
    msg.actions.append(of.ofp_action_output(port = 3))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.6"
    msg.match.nw_dst = "10.0.0.5"
    msg.actions.append(of.ofp_action_output(port = 1))
    event.connection.send(msg)

####################################
 if event.connection.dpid==s6_dpid:
    a=packet.find('arp')
    if a and a.protodst=="10.0.0.6":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=1))
       event.connection.send(msg)
    if a and a.protodst=="10.0.0.1":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=2))
       event.connection.send(msg)
    if a and a.protodst=="10.0.0.2":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=2))
       event.connection.send(msg)
    if a and a.protodst=="10.0.0.3":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=3))
       event.connection.send(msg)
    if a and a.protodst=="10.0.0.5":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=3))
       event.connection.send(msg)
    if a and a.protodst=="10.0.0.4":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=3))
       event.connection.send(msg)


#Add flows s6
    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.1"
    msg.match.nw_dst = "10.0.0.5"
    msg.actions.append(of.ofp_action_output(port = 3))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.1"
    msg.match.nw_dst = "10.0.0.6"
    msg.actions.append(of.ofp_action_output(port = 1))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.2"
    msg.match.nw_dst = "10.0.0.6"
    msg.actions.append(of.ofp_action_output(port = 1))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.3"
    msg.match.nw_dst = "10.0.0.6"
    msg.actions.append(of.ofp_action_output(port = 1))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.4"
    msg.match.nw_dst = "10.0.0.1"
    msg.actions.append(of.ofp_action_output(port = 2))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.4"
    msg.match.nw_dst = "10.0.0.6"
    msg.actions.append(of.ofp_action_output(port = 1))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.5"
    msg.match.nw_dst = "10.0.0.1"
    msg.actions.append(of.ofp_action_output(port = 2))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.5"
    msg.match.nw_dst = "10.0.0.6"
    msg.actions.append(of.ofp_action_output(port = 1))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.6"
    msg.match.nw_dst = "10.0.0.1"
    msg.actions.append(of.ofp_action_output(port = 2))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.6"
    msg.match.nw_dst = "10.0.0.2"
    msg.actions.append(of.ofp_action_output(port = 2))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.6"
    msg.match.nw_dst = "10.0.0.3"
    msg.actions.append(of.ofp_action_output(port = 3))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.6"
    msg.match.nw_dst = "10.0.0.4"
    msg.actions.append(of.ofp_action_output(port = 3))
    event.connection.send(msg)

    msg = of.ofp_flow_mod()
    msg.priority =100
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.6"
    msg.match.nw_dst = "10.0.0.5"
    msg.actions.append(of.ofp_action_output(port = 3))
    event.connection.send(msg)

################################################################################
def launch ():
 core.openflow.addListenerByName("PortStatsReceived",_handle_portstats_received)
 core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
 core.openflow.addListenerByName("PacketIn",_handle_PacketIn)
