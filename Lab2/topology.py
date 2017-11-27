#Topologia para ser utilizada em conjundo com forwarding.l2_learning(componente do POX)


#!/usr/bin/python
 
from mininet.net import Mininet
from mininet.node import Controller
from mininet.topo import SingleSwitchTopo
from mininet.log import setLogLevel
 
import os
 
class POXBridge( Controller ):
    "Custom Controller class to invoke POX forwarding.l2_learning"
    def start ( self ):
        "Start POX learning switch"
        self.pox = '%s/pox/pox.py' % os.environ[ 'HOME' ]
        self.cmd( self.pox, 'forwarding.l2_learning &' )
        #self.cmd( self.pox, 'forwarding.hub &' )
    def stop ( self ):
        "Stop POX"
      self.cmd( 'kill %' + self.pox )
 
controllers = { 'poxbridge': POXBridge }
 
if __name__ == '__main__':
    setLogLevel( 'info' )
    net = Mininet( topo=SingleSwitchTopo( 2), controller=POXBridge )
    net.start()
    net.pingAll()
    h1, h2 = net.get( 'h1', 'h2' )
    #net.iperf((h1, h2))
    result1=h1.cmd('ping -c 5 10.0.0.2')
    print result1
    result2=h2.cmd('ping -c 5 10.0.0.1')
    print result2
    net.stop()
