"""Traffic generator utility

Usage:
  mnrecv [--topology=FILE] <packets> <filter> [--iface=IFACE] [--timeout=TIMEOUT]
  mnrecv (-h | --help)

Options:
  -h --help         Show this screen.
  --topology=FILE   Topolofy file name [default: mn-topo.yml].
  --iface=IFACE     Interface name
  --timeout=TIMEOUT Timeout in seconds. Default 30
  --version         Show version.

"""

import os
import sys
import yaml
from mntopo.docopt import docopt
import mntopo.topo
from mininet.log import setLogLevel, info, error
from scapy.all import *


class Shell(object):

    def __init__(self):
        arguments = docopt(__doc__, version='Mininet Topology Utility 1.0')

        setLogLevel('info')
        file = 'mn-topo.yml'
        if arguments['--topology']:
            file = arguments['--topology']

        props = None
        if (os.path.isfile(file)):
            with open(file, 'r') as f:
                props = yaml.load(f)

        if props is None:
            print "ERROR: yml topology file not found"
            sys.exit()

        topo = mntopo.topo.Topo(props)

        count=int(arguments['<packets>'])
        iface = None
        if arguments['--iface']:
            iface = arguments['--iface']
        timeout=60
        if arguments['--timeout']:
            timeout = int(arguments['--timeout'])

        if len(sniff(count=count, iface=iface, filter=arguments['<filter>'],timeout=timeout)) != count:
            sys.exit(1)


def main():
    Shell()

if __name__ == "__main__":
    Shell()
