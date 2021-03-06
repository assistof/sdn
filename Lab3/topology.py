# SCript do mininet criando topologia simples  com faixa de ip especificada e adição de flows atráves do ovs-vctl

# um switch e dois hosts. Quando houver tráfego na porta 1, encaminhe-o para a porta 2 e vice-versa]

 #!/usr/bin/python
 
"""
Build a simple network from scratch, using mininet primitives.
This is more complicated than using the higher-level classes,
but it exposes the configuration details and allows customization.
 
For most tasks, the higher-level API will be preferable.
"""
 
from mininet.net import Mininet
from mininet.node import Node
from mininet.link import Link
from mininet.log import setLogLevel, info
from mininet.util import quietRun
 
from time import sleep
 
def scratchNet( cname='controller', cargs='-v ptcp:' ):
    "Create network from scratch using Open vSwitch."
 
    info( "*** Creating nodes\n" )
    controller = Node( 'c0', inNamespace=False )
    switch0 = Node( 's0', inNamespace=False )
    h0 = Node( 'h0' )
    h1 = Node( 'h1' )
 
    info( "*** Creating links\n" )
    Link( h0, switch0 )
    Link( h1, switch0 )
 
    info( "*** Configuring hosts\n" )
    h0.setIP( '192.168.123.1/24' )
    h1.setIP( '192.168.123.2/24' )
    info( str( h0 ) + '\n' )
    info( str( h1 ) + '\n' )
       
    info( "*** Starting network using Open vSwitch\n" )
    controller.cmd( cname + ' ' + cargs + '&' )
    switch0.cmd( 'ovs-vsctl del-br dp0' )
    switch0.cmd( 'ovs-vsctl add-br dp0' )
 
    for intf in switch0.intfs.values():
        print intf
        print switch0.cmd( 'ovs-vsctl add-port dp0 %s' % intf )
 
    # Note: controller and switch are in root namespace, and we
    # can connect via loopback interface
    switch0.cmd( 'ovs-vsctl set-controller dp0 tcp:127.0.0.1:6633' )
    switch0.cmd( 'ovs-ofctl add-flow dp0 \"in_port=1 actions=output:2\"' )
    switch0.cmd( 'ovs-ofctl add-flow dp0 \"in_port=2 actions=output:1\"' )
 
    info( '*** Waiting for switch to connect to controller' )
    while 'is_connected' not in quietRun( 'ovs-vsctl show' ):
        sleep( 1 )
        info( '.' )
    info( '\n' )
 
    info( "*** Running test\n" )
    h0.cmdPrint( 'ping -c3 ' + h1.IP() )
    h1.cmdPrint( 'ping -c3 ' + h0.IP() )  
 
    info( "*** Stopping network\n" )
    controller.cmd( 'kill %' + cname )
    switch0.cmd( 'ovs-vsctl del-br dp0' )
    switch0.deleteIntfs()
    info( '\n' )
 
if __name__ == '__main__':
    setLogLevel( 'info' )
    info( '*** Scratch network demo (kernel datapath)\n' )
    Mininet.init()
    scratchNet()
