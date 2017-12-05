 
from mininet.net import Mininet
from mininet.topo import Topo
topo = Topo()  # Create an empty topology
topo.addSwitch("s1")  # Add switches and hosts to the topology
topo.addHost("h1")
topo.addHost("h2")
topo.addLink("h1", "s1") # Wire the switches and hosts together with links
topo.addLink("h2", "s1")
net = Mininet(topo)  # Create the Mininet, start it and try some stuff
net.start()
net.pingAll()
net.iperf()
net.stop()
