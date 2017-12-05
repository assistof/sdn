#!/usr/bin/python
 
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel, info
from mininet.node import Controller 
from mininet.cli import CLI
from functools import partial
from mininet.node import RemoteController
import os
from time import sleep
from iperf import IPerfAllTest

class MyTopo(Topo):
    "Single switch connected to n hosts."
    def __init__(self):
        Topo.__init__(self)
        s1=self.addSwitch('s1')
        s2=self.addSwitch('s2')
        s3=self.addSwitch('s3')
        s4=self.addSwitch('s4')
        s5=self.addSwitch('s5')
        s6=self.addSwitch('s6') 
 
        h1=self.addHost('h1')
        h2=self.addHost('h2')
        h3=self.addHost('h3')
        h4=self.addHost('h4')
        h5=self.addHost('h5')
        h6=self.addHost('h6')
         
        self.addLink(h1, s1, bw=100, delay='10ms', loss=0, max_queue_size=1000, use_htb=True)
        self.addLink(h2, s2, bw=100, delay='10ms', loss=0, max_queue_size=1000, use_htb=True) 
        self.addLink(h3, s3, bw=100, delay='10ms', loss=0, max_queue_size=1000, use_htb=True)
        self.addLink(h4, s4, bw=100, delay='10ms', loss=0, max_queue_size=1000, use_htb=True) 
        self.addLink(h5, s5, bw=100, delay='10ms', loss=0, max_queue_size=1000, use_htb=True) 
        self.addLink(h6, s6, bw=100, delay='10ms', loss=0, max_queue_size=1000, use_htb=True) 
        self.addLink(s1, s2, bw=100, delay='10ms', loss=0, max_queue_size=1000, use_htb=True) 
        self.addLink(s1, s6, bw=100, delay='10ms', loss=0, max_queue_size=1000, use_htb=True)  
        self.addLink(s2, s3, bw=100, delay='10ms', loss=0, max_queue_size=1000, use_htb=True) 
        self.addLink(s2, s5, bw=100, delay='10ms', loss=0, max_queue_size=1000, use_htb=True)
        self.addLink(s3, s4, bw=100, delay='10ms', loss=0, max_queue_size=1000, use_htb=True) 
        self.addLink(s4, s5, bw=100, delay='10ms', loss=0, max_queue_size=1000, use_htb=True) 
        self.addLink(s5, s6, bw=100, delay='10ms', loss=0, max_queue_size=1000, use_htb=True) 

def configureNetwork():
    "Create network and run simple performance test"
    topo = MyTopo()
    #net = Mininet(topo=topo, host=CPULimitedHost, link=TCLink, controller=POXcontroller1)
    net = Mininet(topo=topo, host=CPULimitedHost, link=TCLink, controller=partial(RemoteController, ip='127.0.0.1', port=6633))
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    h1=net.get('h1')
    h2=net.get('h2')
    h3=net.get('h3')
    h4=net.get('h4')
    h5=net.get('h5')
    h6=net.get('h6')
    h1.setMAC("0:0:0:0:0:1")
    h2.setMAC("0:0:0:0:0:2")
    h3.setMAC("0:0:0:0:0:3")
    h4.setMAC("0:0:0:0:0:4")
    h5.setMAC("0:0:0:0:0:5")
    h6.setMAC("0:0:0:0:0:6")
    info( '\n' )
    info( "*** Starting iperf Measurement ***\n" )
    info( '\n' )
    info( "*** Stop old iperf server ***" )
    os.system('pkill -f \'iperf -s\'')
    sleep(1)
    info( '\n' )
    info( "*** Running test with iperf ***\n" )


    it = IPerfAllTest(net.hosts)
    it.start()

   # it = IPerfOneToAllPairTest(net.hosts)
   # it.start()

    
#   h1.cmdPrint( 'ping -c 3 ' + h2.IP() )
#   h2.cmdPrint( 'ping -c 3 ' + h3.IP() )
#   h1.cmd('iperf -s &')
#   print "iperf: h1--s0--s1--h2"
#   h2.cmdPrint('iperf -c 10.0.0.1 -t 10')
#   print "limit the bandwidth for flow h1-h2"
#
    CLI(net)
    net.stop()

    
if __name__ == '__main__':
    setLogLevel('info')
    configureNetwork()
