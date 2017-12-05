 
Mininet está escrito quase completamente em Python, então, eventualmente, você pode querer acessar mais de suas capacidades. Isso significa que você pode executar o Mininet a partir do shell Python interativo ou mesmo um shell Python aprimorado, como o IPython . A única ressalva importante é que você deve sudoentrar no shell python, ou seja, use o comando Linux sudo pythonpara iniciar a sessão python.

Como exemplo, você pode inserir o código no Exemplo de Código 1, uma linha de cada vez em um shell Python interativo para criar uma topologia Mininet personalizada e executar testes ping e iperf .

Exemplo de código 1. Script simples do Python ExMNsimple.py para gerar uma topologia personalizada e executar alguns testes.

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
