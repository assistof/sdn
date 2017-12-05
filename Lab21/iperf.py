"""
  A collection of tests
"""
from time import sleep
import os
import html
def log(s):
  print s

class IPerfAllTest:
  """ All Pairs iperf tests """

  def __init__(self, hosts):
    t=600
    self.hosts = hosts
    self.t = t
    self.hostnames = [h.name for h in hosts]

    log('IPerf tests on pairs %s for %d seconds' % (self.hostnames, t))
    for h in hosts:
      h.cmd('iperf -s &')
      print(h.IP())

  def start(self):
    log('Starting iperf tests on pairs %s' % self.hostnames)
    os.system('rm -rf iperf_output')
    os.system('mkdir -p iperf_output')
    for h1 in self.hosts: 
      print(h1.IP())
      for h2 in self.hosts:
        if h1 != h2:
          h1.cmd('iperf -t %d -c %s > iperf_output/%s-%s &' % (self.t, h2.IP(), h1.name, h2.name))
          print(h1.name, h2.name)
         # h1.cmdPrint('iperf -t %d -c %s > iperf_output/%s-%s &' % (self.t, h2.IP(), h1.name, h2.name))


  def end(self):
    sleep(self.t+5)
    log('Ending iperf tests on hosts %s' % self.hostnames)
    for h in self.hosts:
      h.cmd('killall -9 iperf')
    
    return self.output()



