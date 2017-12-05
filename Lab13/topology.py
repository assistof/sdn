#! / usr / bin / env python
 
Mininet.net import Mininet
de mininet.node import RemoteController
da mininet.link importar TCLink
da mininet.cli import CLI
de mininet.util import quietRun
 
net = Mininet (link = TCLink);
 
# Adicionar hosts e switches
Host1 = net.addHost ('h1')
Host2 = net.addHost ('h2')
 
Switch1 = net.addSwitch ('s1')
Switch2 = net.addSwitch ('s2')
Switch3 = net.addSwitch ('s3')
Switch4 = net.addSwitch ('s4')
Switch5 = net.addSwitch ('s5')
 
# Adicionar links
# ajusta velocidades de link para 10Mbit / s
linkopts = dict (bw = 10)
net.addLink (Host1, Switch1, ** linkopts)
net.addLink (Switch1, Switch2, ** linkopts)
net.addLink (Switch1, Switch3, ** linkopts)
net.addLink (Switch3, Switch4, ** linkopts)
net.addLink (Switch2, Switch5, ** linkopts)
net.addLink (Switch4, Switch5, ** linkopts)
net.addLink (Switch4, Host2, ** linkopts)
 
# Iniciar
net.addController ('c', controller = RemoteController, ip = '127.0.0.1', port = 6633)
net.build ()
net.start ()
 
# CLI
CLI (rede)
 
# Limpar
net.stop ()
