#!/usr/bin/python
 
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, UserSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link, TCLink, Intf
 
def topology():
    "Create a network."
    net = Mininet( controller=RemoteController, link=TCLink )
    print "*** Creating nodes"
    h1 = net.addHost( 'h1')
    h2 = net.addHost( 'h2')
    SwitchList = []
    # set n to different numbers, you can set that each path to contain n switches
    n = 3
    for x in range(1, n*2-2+1):
      PREFIX="s"
      SwitchList.append(net.addSwitch(PREFIX+str(x)))  
 
    c0 = net.addController( 'c0', controller=RemoteController, ip='127.0.0.1', port=6633 )
 
    print "*** Creating links"
    linkBW = {'bw':100}
    net.addLink(h1, SwitchList[0], cls=TCLink, **linkBW)
    net.addLink(h2, SwitchList[n-1], cls=TCLink, **linkBW)
    for i in range(n*2-2):
     if i==(n-1):
       net.addLink(SwitchList[0], SwitchList[i+1], cls=TCLink, **linkBW) 
     elif i!=(n-1) and i!=(n*2-2-1):
        net.addLink(SwitchList[i], SwitchList[i+1], cls=TCLink, **linkBW)
     else:
        net.addLink(SwitchList[i], SwitchList[n-1], cls=TCLink, **linkBW)
  
    print "*** Starting network"
    net.build()
    c0.start()
    for sw in SwitchList:
      sw.start([c0])
 
    #using the static arp, the hosts don't need to run arp protocol. Speed up the emulation.
    h1.cmd('arp -s '+ h2.IP()+' '+h2.MAC())
    h1.cmdPrint('arp -n')
    h2.cmd('arp -s '+h1.IP()+' '+h1.MAC())
    h2.cmdPrint('arp -n')
 
    #print "*** Running CLI"
    CLI( net )
 
    print "*** Stopping network"
    net.stop()
 
if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()
