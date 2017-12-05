#! / usr / bin / python
 
Mininet.net import Mininet
de mininet.node Import Node
da mininet.link importar TCLink
de mininet.log import setLogLevel, informações
do temporizador de importação do threading
de mininet.util import quietRun
desde o tempo de importação de sono
da mininet.cli import CLI
 
def myNet (cname = 'controller', cargs = '- v ptcp:'):
    "Crie uma rede a partir do zero usando Open vSwitch".
    info ("*** Criando nós \ n")
    controller = Node ('c0', inNamespace = False)
    s0 = Nó ('s0', inNamespace = Falso)
    s1 = Node ('s1', inNamespace = False)
    h0 = Nó ('h0')
    h1 = Nó ('h1')
    h2 = Nó ('h2')
 
    info ("*** Criando links \ n")
    linkopts0 = dict (bw = 10, delay = '1ms', loss = 0)
    TCLink (h0, s0, ** linkopts0)
    TCLink (h1, s0, ** linkopts0)
    TCLink (s0, s1, ** linkopts0)
    TCLink (s1, h2, ** linkopts0)
 
 
    info ("*** Configurando hosts \ n")
    h0.setIP ('192.168.123.1/24')
    h1.setIP ('192.168.123.2/24')
    h2.setIP ('192.168.123.3/24')
               
    info ("*** Iniciando a rede usando Open vSwitch \ n")
    s0.cmd ('ovs-vsctl del-br dp0')
    s0.cmd ('ovs-vsctl add-br dp0')
    s1.cmd ('ovs-vsctl del-br dp1')
    s1.cmd ('ovs-vsctl add-br dp1')
 
    controller.cmd (cname + '' + cargs + '&')          
    para intf em s0.intfs.values ​​():
        impressão int.
        imprimir s0.cmd ('ovs-vsctl add-port dp0% s'% intf)
   
    para intf em s1.intfs.values ​​():
        impressão int.
        imprimir s1.cmd ('ovs-vsctl add-port dp1% s'% intf)
  
    # Nota: o controlador e o interruptor estão no namespace de raiz, e nós
    # pode se conectar via interface de loopback
    s0.cmd ('ovs-vsctl set-controller dp0 tcp: 127.0.0.1: 6633')
    s1.cmd ('ovs-vsctl set-controller dp0 tcp: 127.0.0.1: 6633')
   
    info ('*** Esperando a mudança para se conectar ao controlador')
    enquanto 'is_connected' não está em quietRun ('show ovs-vsctl'):
        dormir (1)
        info ('.')
    info ('\ n')
 
    #print s0.cmd ('ovs-ofctl show dp0')
 
    #info ("*** Executando o teste \ n")
    h0.cmdPrint ('ping -c 3' + h2.IP ())
    h1.cmdPrint ('ping -c 3' + h2.IP ())
    h2.cmd ('iperf -s &')
    imprimir "iperf: h0 - s0 - s1 - h2"
    h0.cmdPrint ('iperf -c 192.168.123.3 -t 10')
    imprimir "iperf: h1 - s0 - s1 - h2"
    h1.cmdPrint ('iperf -c 192.168.123.3 -t 10')
    imprimir "limitar a largura de banda para o fluxo h0-h2"
    s0.cmdPrint ('ethtool -K s0-eth2 gro off')
    s0.cmdPrint ('tc qdisc del dev s0-eth2 root')
    s0.cmdPrint ('tc qdisc add dev s0-eth2 root handle 1: cbq avpkt 1000 bandwidth 10Mbit')
    s0.cmdPrint ('tc class add dev s0-eth2 parent 1: classid 1: 1 taxa cbq 512kbit allot 1500 prio 5 limitado isolado')
    s0.cmdPrint ('tc filter add dev s0-eth2 parent 1: protocolo ip prio 16 u32 correspondência ip src 192.168.123.1 flowid 1: 1')
    s0.cmdPrint ('tc qdisc add dev s0-eth2 parent 1: 1 sfq perturb 10')
    h0.cmdPrint ('iperf -c 192.168.123.3 -t 10')
    imprimir "iperf: h1 - s0 - s1 - h2" 
    h1.cmdPrint ('iperf -c 192.168.123.3 -t 10')
 
    info ("*** Parando a rede \ n")
    controller.cmd ('kill%' + cname)
    s0.cmd ('ovs-vsctl del-br dp0')
    s0.deleteIntfs ()
    s1.cmd ('ovs-vsctl del-br dp1')
    s1.deleteIntfs ()
    info ('\ n')
 
se __name__ == '__main__':
    rede global
    setLogLevel ('info')
    info ('*** Demonstração da rede Scratch (kernel datapath) \ n')
    Mininet.init ()
    myNet ()
