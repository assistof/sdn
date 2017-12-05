#!/usr/bin/python
"""
#Code created by VND - Visual Network Description (SDN version)
"""
from pox.core import core
from pox.lib.addresses import IPAddr
from pox.lib.addresses import EthAddr
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpid_to_str, str_to_bool
from pox.lib.packet.arp import arp
from pox.lib.packet.ethernet import ethernet, ETHER_BROADCAST
 
log = core.getLogger()
 
#flow3:
switch2 = 0000000000000003
flow2msg = of.ofp_flow_mod()
flow2msg.cookie = 0
flow2msg.match.in_port = 2
flow2msg.match.dl_type = 0x0800
flow2msg.match.nw_src = IPAddr("192.168.1.10")
# ACTIONS---------------------------------
flow2out = of.ofp_action_output (port = 1)
flow2srcIP = of.ofp_action_nw_addr.set_src(IPAddr("10.0.0.2"))
flow2srcMAC = of.ofp_action_dl_addr.set_src(EthAddr("00:00:00:00:00:04"))
flow2dstMAC = of.ofp_action_dl_addr.set_dst(EthAddr("00:00:00:00:00:01"))
flow2msg.actions = [flow2srcIP, flow2srcMAC, flow2dstMAC, flow2out]
 
#flow4:
switch3 = 0000000000000003
flow3msg = of.ofp_flow_mod()
flow3msg.cookie = 0
flow3msg.match.in_port = 1
flow3msg.match.dl_type = 0x0800
flow3msg.match.nw_dst = IPAddr("10.0.0.2")
# ACTIONS---------------------------------
flow3out = of.ofp_action_output (port = 2)
flow3dstIP = of.ofp_action_nw_addr.set_dst(IPAddr("192.168.1.10"))
flow3srcMAC = of.ofp_action_dl_addr.set_src(EthAddr("00:00:00:00:00:03"))
flow3dstMAC = of.ofp_action_dl_addr.set_dst(EthAddr("00:00:00:00:00:02"))
flow3msg.actions = [flow3dstIP, flow3srcMAC, flow3dstMAC, flow3out]
 
def install_flows():
   log.info("    *** Installing static flows... ***")
   # Push flows to switches
   core.openflow.sendToDPID(switch2, flow2msg)
   core.openflow.sendToDPID(switch3, flow3msg)
   log.info("    *** Static flows installed. ***")
 
def _handle_ConnectionUp (event):
   log.info("*** install flows ***")
   install_flows()
 
def _handle_PacketIn (event):
   #log.info("*** _handle_PacketIn... ***")
   dpid = event.connection.dpid
   inport = event.port
   packet = event.parsed
   if not packet.parsed:
      log.warning("%i %i ignoring unparsed packet", dpid, inport)
      return
 
   a = packet.find('arp')
   if not a: return
 
   log.info("%s ARP %s %s => %s", dpid_to_str(dpid),
      {arp.REQUEST:"request",arp.REPLY:"reply"}.get(a.opcode,
      'op:%i' % (a.opcode,)), str(a.protosrc), str(a.protodst))
    
   if a.prototype == arp.PROTO_TYPE_IP:
     if a.hwtype == arp.HW_TYPE_ETHERNET:
       if a.opcode == arp.REQUEST:
         if str(a.protodst)=="192.168.1.1":
           r = arp()
           r.hwtype = a.hwtype
           r.prototype = a.prototype
           r.hwlen = a.hwlen
           r.protolen = a.protolen
           r.opcode = arp.REPLY
           r.hwdst = a.hwsrc
           r.protodst = a.protosrc
           r.protosrc = a.protodst
           r.hwsrc = EthAddr("00:00:00:00:00:03")
           e = ethernet(type=packet.type, src=r.hwsrc,
                            dst=a.hwsrc)
           e.payload = r
           log.info("%s answering ARP for %s" % (dpid_to_str(dpid),
                str(r.protosrc)))
           msg = of.ofp_packet_out()
           msg.data = e.pack()
           msg.actions.append(of.ofp_action_output(port =
                                                    of.OFPP_IN_PORT))                            
           msg.in_port = inport
           event.connection.send(msg)  
         if str(a.protodst)=="10.0.0.2":
           r = arp()
           r.hwtype = a.hwtype
           r.prototype = a.prototype
           r.hwlen = a.hwlen
           r.protolen = a.protolen
           r.opcode = arp.REPLY
           r.hwdst = a.hwsrc
           r.protodst = a.protosrc
           r.protosrc = a.protodst
           r.hwsrc = EthAddr("00:00:00:00:00:04")
           e = ethernet(type=packet.type, src=r.hwsrc,
                            dst=a.hwsrc)
           e.payload = r
           log.info("%s answering ARP for %s" % (dpid_to_str(dpid),
                str(r.protosrc)))
           msg = of.ofp_packet_out()
           msg.data = e.pack()
           msg.actions.append(of.ofp_action_output(port =
                                                    of.OFPP_IN_PORT))                            
           msg.in_port = inport
           event.connection.send(msg)
 
def launch ():
   log.info("*** Starting... ***")
   log.info("*** Waiting for switches to connect.. ***")
   core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
   core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
