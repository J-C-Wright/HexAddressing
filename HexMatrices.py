#!/usr/bin/python

import sys, getopt
import HexAddresses as ha
import HexCoordinates as hc

Bs = hc.getMappingMatrices(15)

for B in Bs:
    for row in B: 
        print row
    print 
