#!/usr/bin/python

import sys, getopt
import HexAddresses as ha
import HexCoordinates as hc
from optparse import OptionParser

from Hexpy import StandardAddress as sa
from Hexpy import CanonAddress as ca
from Hexpy import SpiralAddress as spa

def get_options():

    parser = OptionParser()

    parser.add_option('-a','--first',
                      dest='a',default='',
                      help='''
                      Specify the first number to add
                      ''')
    parser.add_option('-b','--second',
                      dest='b',default='',
                      help='''
                      Specify the second number to add
                      ''')


    return parser.parse_args()

if __name__ == '__main__':

    (opt,args) = get_options()

    ca1 = ca.CanonAddress(opt.a)
    ca2 = ca.CanonAddress(opt.b)

    print "Canon test:"
    print ca1
    print ca2
    print ca1,'+',ca2,'=',ca1 + ca2
    print ca1,'-',ca2,'=',ca1 - ca2
    print '~a = ',~ca1
    print '~b = ',~ca2
    print

    sa1 = sa.standardFromCanon(ca1)
    sa2 = sa.standardFromCanon(ca2)

    print "Standard test:"
    print sa1
    print sa2
    print sa1,'+',sa2,'=',(sa1 + sa2).bin
    print sa1,'-',sa2,'=',(sa1 - sa2).bin
    print '~a = ',~sa1
    print '~b = ',~sa2
    print
    
    spa1 = spa.spiralFromCanon(opt.a)
    spa2 = spa.spiralFromCanon(opt.b)

    print "Spiral test:"
    print spa1
    print spa2
    print spa1,'+',spa2,'=',(spa1 + spa2)
    print spa1,'-',spa2,'=',(spa1 - spa2)
    print '~a = ',~spa1
    print '~b = ',~spa2
    print

    print "Itterating up to spiral = 49"

    spiral = spa.SpiralAddress(0)
    for i in range(49):
        
        print spiral,' ',
        print ca.canonFromSpiral(spiral),' ',
        print sa.standardFromSpiral(spiral),' ',
        print ~spiral,' ',
        print ~ca.canonFromSpiral(spiral),' ',
        print ~sa.standardFromSpiral(spiral),' '
        spiral.increment()





