#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    c0=net.addController(name='c0',
                      controller=Controller,
                      protocol='tcp',
                      port=6633)

    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)

    h1 = net.addHost('h1', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.3', defaultRoute=None)

    net.addLink(h1, s1)
    net.addLink(s1, h2)

    net.build()

   



if __name__ == '__main__':
    setLogLevel( 'info' )


    net = Mininet(host=CPULimitedHost, link = TCLink)
    c0 = net.addController(name='c0')
    s0 = net.addSwitch("s0",cls=OVSKernelSwitch)
    h0 = net.addHost("h0",cls=Host)
    h1 = net.addHost("h1", cls=Host,cpu=0.5)
    h2 = net.addHost("h2", cls=Host,cpu=0.5)
    net.addLink(s0, h0, bw = 10,delay = '5ms',max_queue_size=1000,loss=10)
    net.addLink(s0,h1)
    net.addLink(s0,h2)


    for controller in net.controllers:
        controller.start()

    net.build()
    net.get('s0').start([c0])
    CLI(net)
    net.pingAll()
    net.stop()
