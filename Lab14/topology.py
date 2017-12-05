#! / usr / bin / python
 
Mininet.net import Mininet
de mininet.node import Controller, RemoteController, UserSwitch
da mininet.cli import CLI
de mininet.log import setLogLevel
de Mininet.link Import Link, TCLink, Intf
 
topologia def ():
    "Criar uma rede".
    net = Mininet (controlador = RemoteController, link = TCLink)
    imprimir "*** Criando nós"
    h1 = net.addHost ('h1')
    h2 = net.addHost ('h2')
    SwitchList = []
    # set n para números diferentes, você pode configurar que cada caminho contenha n switches
    n = 3
    para x no intervalo (1, n * 2-2 + 1):
      PREFIX = "s"
      SwitchList.append (net.addSwitch (PREFIX + str (x)))  
 
    c0 = net.addController ('c0', controller = RemoteController, ip = '127.0.0.1', port = 6633)
 
    imprimir "*** Criar links"
    linkBW = {'bw': 100}
    net.addLink (h1, SwitchList [0], cls = TCLink, ** linkBW)
    net.addLink (h2, SwitchList [n-1], cls = TCLink, ** linkBW)
    para i no alcance (n * 2-2):
     se i == (n-1):
       net.addLink (SwitchList [0], SwitchList [i + 1], cls = TCLink, ** linkBW) 
     elif i! = (n-1) e i! = (n * 2-2-1):
        net.addLink (SwitchList [i], SwitchList [i + 1], cls = TCLink, ** linkBW)
     outro:
        net.addLink (SwitchList [i], SwitchList [n-1], cls = TCLink, ** linkBW)
  
    imprimir "*** Rede inicial"
    net.build ()
    c0.start ()
    para sw in SwitchList:
      sw.start ([c0])
 
    # usando o arp estático, os hosts não precisam executar o protocolo arp. Acelere a emulação.
    h1.cmd ('arp -s' + h2.IP () + '' + h2.MAC ())
    h1.cmdPrint ('arp -n')
    h2.cmd ('arp -s' + h1.IP () + '' + h1.MAC ())
    h2.cmdPrint ('arp -n')
 
    #print "*** Running CLI"
    CLI (rede)
 
    imprimir "*** parar a rede"
    net.stop ()
 
se __name__ == '__main__':
    setLogLevel ('info')
    topologia ()
