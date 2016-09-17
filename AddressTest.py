#!/usr/bin/python

import sys, getopt
from optparse import OptionParser

from Hexpy import StandardAddress as sa
from Hexpy import CanonAddress as ca
from Hexpy import SpiralAddress as spa

from Hexpy.CanonAddress import CanonAddress as Canon
from Hexpy.StandardAddress import StandardAddress as Standard
from Hexpy.SpiralAddress import SpiralAddress as Spiral



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

    ca1 = Canon(opt.a)
    ca2 = Canon(opt.b)

    print "\nCanon test:"
    print ca1
    print ca2
    print ca1,'+',ca2,'=',ca1 + ca2
    print ca1,'-',ca2,'=',ca1 - ca2
    print '~',ca1,' = ',~ca1
    print '~',ca2,' = ',~ca2
    print ca1,'++ = ',
    ca1.increment()
    print ca1
    ca1.decrement()

    sa1 = sa.standardFromCanon(ca1)
    sa2 = sa.standardFromCanon(ca2)

    print "\nStandard test:"
    print sa1
    print sa2
    sa1psa2 = sa1 + sa2
    sa1msa2 = sa1 - sa2
    print sa1,'+',sa2,'=',sa1psa2.bin
    print sa1,'-',sa2,'=',sa1msa2.bin
    print '~',sa1,' = ',~sa1
    print '~',sa2,' = ',~sa2
    print sa1,'++ = ',
    sa1.increment()
    print sa1
    
    spa1 = spa.spiralFromCanon(opt.a)
    spa2 = spa.spiralFromCanon(opt.b)

    print "\nSpiral test:"
    print spa1
    print spa2
    print spa1,'+',spa2,'=',(spa1 + spa2)
    print spa1,'-',spa2,'=',(spa1 - spa2)
    print '~',spa1,' = ',~spa1
    print '~',spa2,' = ',~spa2
    print spa1,'++ = ',
    spa1.increment()
    print spa1

    print "\nItterating up to spiral = 49"

    spiral = spa.SpiralAddress(0)
    for i in range(49):
        
        print spiral,' ',
        print ca.canonFromSpiral(spiral),' ',
        print sa.standardFromSpiral(spiral),' ',
        print ~spiral,' ',
        print ~ca.canonFromSpiral(spiral),' ',
        print ~sa.standardFromSpiral(spiral),' '
        spiral.increment()





