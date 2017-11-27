# Usando  a regra de inundação padrão para o switch. Defina regras de prioridade mais altas para conduzir o encaminhamento de pacotes IP pré-dsefinido]

#!/usr/bin/python
 
from mininet.net import Mininet
from mininet.node import Node
from mininet.link import Link
from mininet.log import  setLogLevel, info
 
def myNet():
    "Create network from scratch using Open vSwitch."
 
    info( "*** Creating nodes\n" )
    switch0 = Node( 's0', inNamespace=False )
 
    h0 = Node( 'h0' )
    h1 = Node( 'h1' )
    h2 = Node( 'h2' )
 
    info( "*** Creating links\n" )
    Link( h0, switch0)
    Link( h1, switch0)
    Link( h2, switch0)
 
    info( "*** Configuring hosts\n" )
    h0.setIP( '192.168.123.1/24' )
    h1.setIP( '192.168.123.2/24' )
    h2.setIP( '192.168.123.3/24' )
       
    info( "*** Starting network using Open vSwitch\n" )
    switch0.cmd( 'ovs-vsctl del-br dp0' )
    switch0.cmd( 'ovs-vsctl add-br dp0' )
 
    for intf in switch0.intfs.values():
        print intf
        print switch0.cmd( 'ovs-vsctl add-port dp0 %s' % intf )
 
    # Note: controller and switch are in root namespace, and we
    # can connect via loopback interface
    #switch0.cmd( 'ovs-vsctl set-controller dp0 tcp:127.0.0.1:6633' )
  
    print switch0.cmd(r'ovs-vsctl show')
 
    print switch0.cmd(r'ovs-ofctl add-flow dp0 idle_timeout=0,priority=1,in_port=1,actions=flood' ) 
    print switch0.cmd(r'ovs-ofctl add-flow dp0 idle_timeout=0,priority=1,in_port=2,actions=flood' )
    print switch0.cmd(r'ovs-ofctl add-flow dp0 idle_timeout=0,priority=1,in_port=3,actions=flood' )
  
    print switch0.cmd(r'ovs-ofctl add-flow dp0 idle_timeout=0,priority=10,ip,nw_dst=192.168.123.1,actions=output:1' ) 
    print switch0.cmd(r'ovs-ofctl add-flow dp0 idle_timeout=0,priority=10,ip,nw_dst=192.168.123.2,actions=output:2' ) 
    print switch0.cmd(r'ovs-ofctl add-flow dp0 idle_timeout=0,priority=10,ip,nw_dst=192.168.123.3,actions=output:3')
 
    #switch0.cmd('tcpdump -i s0-eth0 -U -w aaa &')
    #h0.cmd('tcpdump -i h0-eth0 -U -w aaa &')
    info( "*** Running test\n" )
    h0.cmdPrint( 'ping -c 3 ' + h1.IP() )
    h0.cmdPrint( 'ping -c 3 ' + h2.IP() )
 
    #print switch0.cmd( 'ovs-ofctl show dp0' )    
    #print switch0.cmd( 'ovs-ofctl dump-tables  dp0' )
    #print switch0.cmd( 'ovs-ofctl dump-ports   dp0' )
    #print switch0.cmd( 'ovs-ofctl dump-flows  dp0' )
    #print switch0.cmd( 'ovs-ofctl dump-aggregate  dp0' )
    #print switch0.cmd( 'ovs-ofctl queue-stats dp0' )
 
    info( "*** Stopping network\n" )
    switch0.cmd( 'ovs-vsctl del-br dp0' )
    switch0.deleteIntfs()
    info( '\n' )
 
if __name__ == '__main__':
    setLogLevel( 'info' )
    info( '*** Scratch network demo (kernel datapath)\n' )
    Mininet.init()
    myNet()

