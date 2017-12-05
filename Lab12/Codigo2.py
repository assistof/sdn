from mininet.net import Mininet
from mininet.topo import Topo
from mininet.link import TCLink  # So we can rate limit links
from mininet.cli import CLI  # So we can bring up the Mininet CLI
topo = Topo()  # Create an empty topology
topo.addSwitch("s1")  # Add switches and hosts to the topology
topo.addSwitch("s2")
topo.addHost("h1")
topo.addHost("h2")
topo.addHost("h3")
# Wire the switches and hosts together, links now have bandwidth and delay limits
topo.addLink("h1", "s1", bw=20.0, delay='10ms', use_htb=True)
topo.addLink("h2", "s1", bw=25.0, delay='10ms', use_htb=True)
topo.addLink("s1", "s2", bw=11.0, delay='40ms', use_htb=True)
topo.addLink("h3", "s2", bw=15.0, delay='7ms', use_htb=True)
net = Mininet(topo=topo, link=TCLink)
net.start()
CLI(net)  # Bring up the mininet CLI
net.stop()
