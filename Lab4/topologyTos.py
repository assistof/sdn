#Semelhante ao exmeplo anterior porém utilizando caractéristicas ToS

#!/usr/bin/python
 
from mininet.net import Mininet
from mininet.node import Node
from mininet.link import TCLink
from mininet.log import  setLogLevel, info
 
def myNet():
    "Create network from scratch using Open vSwitch."
 
    info( "*** Creating nodes\n" )
    switch0 = Node( 's0', inNamespace=False )
    switch1 = Node( 's1', inNamespace=False )
    switch2 = Node( 's2', inNamespace=False )
    switch3 = Node( 's3', inNamespace=False )
    switch4 = Node( 's4', inNamespace=False )
    h0 = Node( 'h0' )
    h1 = Node( 'h1' )
 
    info( "*** Creating links\n" )
    linkopts0=dict(bw=100, delay='1ms', loss=0)
    linkopts1=dict(bw=1, delay='100ms', loss=0)
    linkopts2=dict(bw=10, delay='50ms', loss=0)
    linkopts3=dict(bw=100, delay='1ms', loss=0)
    TCLink( h0, switch0, **linkopts0)
    TCLink( switch0, switch1, **linkopts0)
    TCLink( switch0, switch2, **linkopts0)
    TCLink( switch0, switch3, **linkopts0)
    TCLink( switch1, switch4,**linkopts1)
    TCLink( switch2, switch4,**linkopts2)
    TCLink( switch3, switch4,**linkopts3)
    TCLink( h1, switch4, **linkopts0)
 
    info( "*** Configuring hosts\n" )
    h0.setIP( '192.168.123.1/24' )
    h1.setIP( '192.168.123.2/24' )
    info( str( h0 ) + '\n' )
    info( str( h1 ) + '\n' )
       
    info( "*** Starting network using Open vSwitch\n" )
    switch0.cmd( 'ovs-vsctl del-br dp0' )
    switch0.cmd( 'ovs-vsctl add-br dp0' )
    switch1.cmd( 'ovs-vsctl del-br dp1' )
    switch1.cmd( 'ovs-vsctl add-br dp1' )
    switch2.cmd( 'ovs-vsctl del-br dp2' )
    switch2.cmd( 'ovs-vsctl add-br dp2' )
    switch3.cmd( 'ovs-vsctl del-br dp3' )
    switch3.cmd( 'ovs-vsctl add-br dp3' )
    switch4.cmd( 'ovs-vsctl del-br dp4' )
    switch4.cmd( 'ovs-vsctl add-br dp4' )
 
    for intf in switch0.intfs.values():
        print intf
        print switch0.cmd( 'ovs-vsctl add-port dp0 %s' % intf )
 
    for intf in switch1.intfs.values():
        print intf
        print switch1.cmd( 'ovs-vsctl add-port dp1 %s' % intf )
 
    for intf in switch2.intfs.values():
        print intf
        print switch2.cmd( 'ovs-vsctl add-port dp2 %s' % intf )
 
    for intf in switch3.intfs.values():
        print intf
        print switch3.cmd( 'ovs-vsctl add-port dp3 %s' % intf )
 
    for intf in switch4.intfs.values():
        print intf
        print switch4.cmd( 'ovs-vsctl add-port dp4 %s' % intf )
   
    print switch1.cmd(r'ovs-ofctl add-flow dp1 idle_timeout=0,priority=1,in_port=1,actions=flood' )
    print switch1.cmd(r'ovs-ofctl add-flow dp1 idle_timeout=0,priority=1,in_port=1,actions=output:2' ) 
    print switch1.cmd(r'ovs-ofctl add-flow dp1 idle_timeout=0,priority=1,in_port=2,actions=output:1' )
    print switch2.cmd(r'ovs-ofctl add-flow dp2 idle_timeout=0,priority=1,in_port=1,actions=output:2' )
    print switch2.cmd(r'ovs-ofctl add-flow dp2 idle_timeout=0,priority=1,in_port=2,actions=output:1' )
    print switch3.cmd(r'ovs-ofctl add-flow dp3 idle_timeout=0,priority=1,in_port=1,actions=output:2' )    
    print switch3.cmd(r'ovs-ofctl add-flow dp3 idle_timeout=0,priority=1,in_port=2,actions=output:1' )
    print switch4.cmd(r'ovs-ofctl add-flow dp4 idle_timeout=0,priority=1,in_port=1,actions=output:4' )
    print switch4.cmd(r'ovs-ofctl add-flow dp4 idle_timeout=0,priority=1,in_port=2,actions=output:4' )
    print switch4.cmd(r'ovs-ofctl add-flow dp4 idle_timeout=0,priority=1,in_port=3,actions=output:4' )
    print switch4.cmd(r'ovs-ofctl add-flow dp4 idle_timeout=0,priority=1,in_port=4,actions=output:3' )
   
    #print switch0.cmd(r'ovs-ofctl add-flow dp0 idle_timeout=0,priority=10,ip,nw_dst=192.168.123.2,actions=output:4')
    print switch0.cmd(r'ovs-ofctl add-flow dp0 idle_timeout=0,priority=10,ip,nw_dst=192.168.123.2,nw_tos=0x10,actions=output:2') 
    print switch0.cmd(r'ovs-ofctl add-flow dp0 idle_timeout=0,priority=10,ip,nw_dst=192.168.123.2,nw_tos=0x20,actions=output:3')
    print switch0.cmd(r'ovs-ofctl add-flow dp0 idle_timeout=0,priority=10,ip,nw_dst=192.168.123.2,nw_tos=0x30,actions=output:4') 
    #print switch0.cmd(r'ovs-ofctl add-flow dp0 idle_timeout=0,priority=10,ip,nw_dst=192.168.123.1,actions=output:1')
 
    #switch0.cmd('tcpdump -i s0-eth0 -U -w aaa &')
    #h0.cmd('tcpdump -i h0-eth0 -U -w aaa &')
    info( "*** Running test\n" )
    h0.cmdPrint( 'ping -Q 0x10 -c 3 ' + h1.IP() )
    h0.cmdPrint( 'ping -Q 0x20 -c 3 ' + h1.IP() )
    h0.cmdPrint( 'ping -Q 0x30 -c 3 ' + h1.IP() )
    #h1.cmdPrint('iperf -s -p 12345 -u &')
    #h0.cmdPrint('iperf -c ' + h1.IP() +' -u -b 10m -p 12345 -t 10 -i 1')
 
    #print switch0.cmd( 'ovs-ofctl show dp0' )    
    #print switch1.cmd( 'ovs-ofctl show dp1' )
    #print switch2.cmd( 'ovs-ofctl show dp2' )
    #print switch3.cmd( 'ovs-ofctl show dp3' )
    #print switch4.cmd( 'ovs-ofctl show dp4' )  
    #print switch0.cmd( 'ovs-ofctl dump-tables  dp0' )
    #print switch0.cmd( 'ovs-ofctl dump-ports   dp0' )
    #print switch0.cmd( 'ovs-ofctl dump-flows  dp0' )
    #print switch0.cmd( 'ovs-ofctl dump-aggregate  dp0' )
    #print switch0.cmd( 'ovs-ofctl queue-stats dp0' )
 
    #print "Testing video transmission between h1 and h2"
    #h1.cmd('./myrtg_svc -u > myrd &')
    #h0.cmd('./mystg_svc -trace st 192.168.123.2')
 
    info( "*** Stopping network\n" )
    switch0.cmd( 'ovs-vsctl del-br dp0' )
    switch0.deleteIntfs()
    switch1.cmd( 'ovs-vsctl del-br dp1' )
    switch1.deleteIntfs()
    switch2.cmd( 'ovs-vsctl del-br dp2' )
    switch2.deleteIntfs()
    switch3.cmd( 'ovs-vsctl del-br dp3' )
    switch3.deleteIntfs()
    switch4.cmd( 'ovs-vsctl del-br dp4' )
    switch4.deleteIntfs()
    info( '\n' )
 
if __name__ == '__main__':
    setLogLevel( 'info' )
    info( '*** Scratch network demo (kernel datapath)\n' )
    Mininet.init()
    myNet()
