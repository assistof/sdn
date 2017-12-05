#!/usr/bin/python
 
from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.link import Intf
from mininet.log import setLogLevel, info
 
def myNetwork():
 
    net = Mininet( topo=None, build=False, controller=RemoteController)
 
    info( '*** Adding controller\n' )
    net.addController(name='c0', ip='127.0.0.1', port=6633 )
 
    info( '*** Add switches\n')
    s1 = net.addSwitch('s1')
    Intf( 'eth1', node=s1 )
 
    info( '*** Add hosts\n')
    h1 = net.addHost('h1', ip='10.0.0.1/24')
 
    info( '*** Add links\n')
    net.addLink(h1, s1)
 
    info( '*** Starting network\n')
    net.start()
    CLI(net)
    net.stop()
 
if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()
