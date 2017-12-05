#!/usr/bin/python
 
"""
Script created by VND - Visual Network Description (SDN version)
"""
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, IVSSwitch, UserSwitch
from mininet.link import Link, TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel
 
def topology():
 
    "Create a network."
    net = Mininet( controller=RemoteController, link=TCLink, switch=OVSKernelSwitch )
 
    print "*** Creating nodes"
    h1 = net.addHost( 'h1', mac='00:00:00:00:00:01', ip='10.0.0.1/24' )
    h2 = net.addHost( 'h2', mac='00:00:00:00:00:02', ip='192.168.1.10/24' )
    s3 = net.addSwitch( 's3', protocols='OpenFlow10', listenPort=6673)
    c4 = net.addController( 'c4', ip='127.0.0.1', port=6633 )
 
    print "*** Creating links"
    net.addLink(h1, s3)
    net.addLink(s3, h2)
 
    print "*** Starting network"
    net.build()
    c4.start()
    s3.start( [c4] )
 
    print "*** Running CLI"
    h2.cmd("ip route add default via 192.168.1.1 dev h2-eth0")
    h1.cmd("ip route add default via 10.0.0.2 dev h1-eth0")
    CLI( net )
 
    print "*** Stopping network"
    net.stop()
 
if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()
