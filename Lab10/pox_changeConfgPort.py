
from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpidToStr
 
log = core.getLogger()
 
def _handle_features_reply (event):
  print "got the features_reply"
  print event.connection.features.datapath_id, event.connection.features.n_buffers, event.connection.features.n_tables, event.connection.features.capabilities, event.connection.features.actions
  print “OFPPF_10GB_FD=”, of.OFPPF_10GB_FD
  print “OFPPF_COPPER=”, of.OFPPF_COPPER
 
  for m in event.connection.features.ports:
    print m.name,m.port_no,m.hw_addr,m.curr,m.advertised,m.supported,m.peer,m.config,m.state
 
def _handle_ConnectionUp (event):
  for m in event.connection.features.ports:
    if m.name == "s1-eth1":
      core.openflow.getConnection(event.connection.dpid).send(of.ofp_features_request())
  msg = of.ofp_flow_mod()
  msg.priority =1
  msg.idle_timeout = 0
  msg.hard_timeout = 0
  msg.match.in_port =1
  msg.actions.append(of.ofp_action_output(port = 2))
  event.connection.send(msg)
 
  msg = of.ofp_flow_mod()
  msg.priority =1
  msg.idle_timeout = 0
  msg.hard_timeout = 0
  msg.match.in_port =2
  msg.actions.append(of.ofp_action_output(port = 1))
  event.connection.send(msg)
 
def launch ():
  core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
  core.openflow.addListenerByName("FeaturesReceived", _handle_features_reply)
