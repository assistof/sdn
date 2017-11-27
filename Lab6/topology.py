#!/usr/bin/python
 
from mininet.net import Mininet
from mininet.node import Node
from mininet.link import TCLink
from mininet.log import  setLogLevel, info
from threading import Timer
from mininet.util import quietRun
from time import sleep
 
def myNet(cname='controller', cargs='-v ptcp:'):
    "Create network from scratch using Open vSwitch."
    info( "*** Creating nodes\n" )
    controller = Node( 'c0', inNamespace=False )
    switch = Node( 's0', inNamespace=False )
    h0 = Node( 'h0' )
    h1 = Node( 'h1' )
    h2 = Node( 'h2' )
 
    info( "*** Creating links\n" )
    linkopts0=dict(bw=100, delay='1ms', loss=0)
    TCLink( h0, switch, **linkopts0)
    TCLink( h1, switch, **linkopts0)
    TCLink( h2, switch, **linkopts0)
 
    info( "*** Configuring hosts\n" )
    h0.setIP( '192.168.123.1/24' )
    h1.setIP( '192.168.123.2/24' )
    h2.setIP( '192.168.123.3/24' )
       
    info( "*** Starting network using Open vSwitch\n" )
    switch.cmd( 'ovs-vsctl del-br dp0' )
    switch.cmd( 'ovs-vsctl add-br dp0' )
 
    controller.cmd( cname + ' ' + cargs + '&' )    
    for intf in switch.intfs.values():
        print intf
        print switch.cmd( 'ovs-vsctl add-port dp0 %s' % intf )
  
    # Note: controller and switch are in root namespace, and we
    # can connect via loopback interface
    switch.cmd( 'ovs-vsctl set-controller dp0 tcp:127.0.0.1:6633' )
   
    info( '*** Waiting for switch to connect to controller' )
    while 'is_connected' not in quietRun( 'ovs-vsctl show' ):
        sleep( 1 )
        info( '.' )
    info( '\n' )
 
    #info( "*** Running test\n" )
    h0.cmdPrint( 'ping -c 3 ' + h1.IP() )
    h0.cmdPrint( 'ping -c 3 ' + h2.IP() )
    h2.cmdPrint( 'ping -c 3 ' + h1.IP() )
 
    info( "*** Stopping network\n" )
    controller.cmd( 'kill %' + cname )
    switch.cmd( 'ovs-vsctl del-br dp0' )
    switch.deleteIntfs()
    info( '\n' )
 
if __name__ == '__main__':
    setLogLevel( 'info' )
    info( '*** Scratch network demo (kernel datapath)\n' )
    Mininet.init()
    myNet()
