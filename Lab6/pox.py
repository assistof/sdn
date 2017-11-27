# Uma configuração simples do pox, onde a gente define estaticamente as flows no controlador 

# Copyright 2012 James McCauley
#
# This file is part of POX.
#
# POX is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# POX is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with POX.  If not, see <http://www.gnu.org/licenses/>.
 
"""
Turns your complex OpenFlow switches into stupid hubs.
"""
 
from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpidToStr
 
log = core.getLogger()
 
def _handle_ConnectionUp (event):
 
  msg = of.ofp_flow_mod()
  msg.priority =1
  msg.idle_timeout = 0
  msg.match.in_port =1
  msg.actions.append(of.ofp_action_output(port = of.OFPP_ALL))
  event.connection.send(msg)
 
  msg = of.ofp_flow_mod()
  msg.priority =1
  msg.idle_timeout = 0
  msg.match.in_port =2
  msg.actions.append(of.ofp_action_output(port = of.OFPP_ALL))
  event.connection.send(msg)
 
  msg = of.ofp_flow_mod()
  msg.priority =1
  msg.idle_timeout = 0
  msg.match.in_port =3
  msg.actions.append(of.ofp_action_output(port = of.OFPP_ALL))
  event.connection.send(msg)
 
  msg = of.ofp_flow_mod()
  msg.priority =10
  msg.idle_timeout = 0
  msg.hard_timeout = 0
  msg.match.dl_type = 0x0800
  msg.match.nw_dst = "192.168.123.3"
  msg.actions.append(of.ofp_action_output(port = 3))
  event.connection.send(msg)
 
  msg = of.ofp_flow_mod()
  msg.priority =10
  msg.idle_timeout = 0
  msg.hard_timeout = 0
  msg.match.dl_type = 0x0800
  msg.match.nw_dst = "192.168.123.2"
  msg.actions.append(of.ofp_action_output(port = 2))
  event.connection.send(msg)
 
  msg = of.ofp_flow_mod()
  msg.priority =10
  msg.idle_timeout = 0
  msg.hard_timeout = 0
  msg.match.dl_type = 0x0800
  msg.match.nw_dst = "192.168.123.1"
  msg.actions.append(of.ofp_action_output(port = 1))
  event.connection.send(msg)
 
def launch ():
  core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
 
  log.info("mypox1")
