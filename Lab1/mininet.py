''' 

Prepare uma classe SingleSwitchTopo que adicione uma única opção e n hosts em uma rede. 
Cada link conectado do host ao switch pode definir a largura de banda, o tempo de atraso e a taxa de perda. 
Em seguida, crie uma rede que contenha um switch e 4 hosts. 
Finalmente, use iperf para testar a largura de banda entre o host 1 e o host 4.
'''


#!/usr/bin/python
 
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
 
class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def __init__(self, n=2, **opts):
        Topo.__init__(self, **opts)
        switch = self.addSwitch('s1')
        for h in range(n):
            #Each host gets 50%/n of system CPU
            host = self.addHost('h%s' % (h + 1), cpu=.5/n)
            #10 Mbps, 5ms delay, 0% Loss, 1000 packet queue
            self.addLink(host, switch, bw=10, delay='5ms', loss=0, max_queue_size=1000, use_htb=True)
 
def perfTest():
    "Create network and run simple performance test"
    topo = SingleSwitchTopo(n=4)
    net = Mininet(topo=topo,host=CPULimitedHost, link=TCLink)
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Testing network connectivity"
    net.pingAll()
    print "Testing bandwidth between h1 and h4"
    h1, h4 = net.get('h1', 'h4')
    net.iperf((h1, h4))
    net.stop()
 
if __name__=='__main__':
    setLogLevel('info')
    perfTest()
