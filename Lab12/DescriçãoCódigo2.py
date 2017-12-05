No exemplo de código 2. criamos uma rede um pouco mais complicada com dois switches e três hosts. Além disso, aproveitamos uma classe especial de links Mininet chamada "TCLink". Esta classe usa as capacidades de controle de tráfego do Linux para nos permitir especificar um limite de banda e atraso para cada link. Isso nos permitirá obter ainda mais informações sobre caminhos em nossas redes emuladas usando ping e iperf.

Se você usou o Mininet um pouco, uma coisa que você não gostaria sobre o Exemplo de Código 1 é que você não obtém a CLI do Mininet agradável que facilita picar e testar sua rede. No Exemplo de Código 2 na linha 18, trazemos a linda CLI Mininet. Enquanto você pode inserir o Exemplo de Código 2 linha a linha em um shell python, você pode, mais facilmente, executá-lo na VM Mininet com o comando sudo python Codigo2.py em uma janela de terminal.

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
