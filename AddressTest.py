#!/usr/bin/python

import sys, getopt
import HexAddresses as ha
import HexCoordinates as hc
from optparse import OptionParser

from Hexpy import StandardAddress as sa
from Hexpy import CanonAddress as ca

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

    print ca1
    print ca2
    print

    sa1 = sa.standardFromCanon(ca1)
    sa2 = sa.standardFromCanon(ca2)

    print sa1
    print sa2
    print

    print ca1 + ca2
    print ca1 - ca2
    print

    print (sa1 + sa2).bin
    print (sa1 - sa2).bin
    

