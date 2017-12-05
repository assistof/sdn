#!/usr/bin/python
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, UserSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link, TCLink
 
 
def topology():
  net = Mininet(controller=RemoteController, link=TCLink, switch=OVSKernelSwitch)
  c0 = net.addController( 'c0', controller=RemoteController, ip='127.0.0.1', port=6633 )
  s1 = net.addSwitch('s1')
  s2 = net.addSwitch('s2')
  s3 = net.addSwitch('s3')
  s4 = net.addSwitch('s4')
  s5 = net.addSwitch('s5')
  h1 = net.addHost('h1')
  net.addLink(s4, h1, bw=10)
  h2 = net.addHost('h2')
  net.addLink(s2, h2, bw=10)
  net.addLink(s1, s2, bw=3)
  net.addLink(s1, s3, bw=10)
  net.addLink(s1, s4, bw=6)
  net.addLink(s1, s5, bw=1)
  net.addLink(s2, s3, bw=3)
  net.addLink(s2, s5, bw=6)
  net.addLink(s3, s4, bw=10)
  net.addLink(s3, s5, bw=8)
  net.addLink(s4, s5, bw=9)
  net.build()
  c0.start()
  s1.start([c0])
  s2.start([c0])
  s3.start([c0])
  s4.start([c0])
  s5.start([c0])
  CLI( net )
  net.stop()
 
 
if __name__ == '__main__':
  setLogLevel( 'info' )
  topology()
