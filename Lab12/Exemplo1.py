Agora vamos tentar alguns experimentos simples na linha de comando Mininet. Na linha 2 do Exemplo a seguir, executamos um teste de ping do host "h1" para o host "h2". A partir da nossa descrição de topologia, os anfitriões h1 e h2 estão conectados ao switch s1 e têm 10ms de atraso em cada um dos links, portanto, sem outros atrasos de processamento, esperamos um tempo de ida e volta em torno de 40ms. Na linha 6, realizamos o mesmo teste entre o host h1 e h3 se somarmos os atrasos nos links entre h1 e h3, recebemos 10ms + 40ms + 7ms = 57ms de uma maneira. Portanto, esperamos um pouco acima do atraso de ônibus de 114ms. O que vemos na linha 9, mas não na linha 8 (o primeiro ping).

Na linha 10 usamos iperf para determinar a largura de banda disponível entre h1 e h2. O link de h1 a s1 tem uma largura de banda de 20Mbps e de h2 a s1 tem uma largura de banda de 25Mbps. Daí o primeiro link é o gargalo e esperamos cerca de 20Mbps de throughput que é confirmado na linha 12. Na linha 13, testamos a taxa de transferência entre hosts h1 e h3 neste caso, o link entre s1 e s2 com uma largura de banda de 11Mbps é o gargalo conforme confirmado nas linhas 14 e 15.

Exemplo:

mininet@mininet-vm:~/dev/FlowPractice/mnExt$ sudo python Codigo2.py
mininet> h1 ping -c 2 h2
PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=45.6 ms
64 bytes from 10.0.0.2: icmp_seq=2 ttl=64 time=43.2 ms
mininet> h1 ping -c 2 h3
PING 10.0.0.3 (10.0.0.3) 56(84) bytes of data.
64 bytes from 10.0.0.3: icmp_seq=1 ttl=64 time=245 ms
64 bytes from 10.0.0.3: icmp_seq=2 ttl=64 time=116 ms
mininet> iperf h1 h2
*** Iperf: testing TCP bandwidth between h1 and h2
*** Results: ['18.9 Mbits/sec', '22.2 Mbits/sec']
mininet> iperf h1 h3
*** Iperf: testing TCP bandwidth between h1 and h3
*** Results: ['10.1 Mbits/sec', '13.6 Mbits/sec']
