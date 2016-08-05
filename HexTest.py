#!/usr/bin/python

import sys, getopt
import HexAddresses as ha
import HexCoordinates as hc

ad1String = ''
ad2String = ''
myopts, args = getopt.getopt(sys.argv[1:],"a:b:")
for o, a in myopts:
    if o == '-a':
        ad1String = a
    if o == '-b':
        ad2String = a
#assert len(ad1String)==3, "Address is not 3 digits"

print

print "Demonstration of neighbour finding and address->coordinates conversion"
print "Input cell address is:", ad1String
ad1 = ha.canonToAddress(ad1String)
ad2 = ha.canonToAddress(ad2String)
out = ha.addressAdd(ad1,ad2)

print ha.addressToCanon(ad1), " -- ",
print ad1.bin," -- ",
coeffs = hc.coefficients(ad1)
print "({:3.1f},{:3.1f},{:3.1f})".format(coeffs[0],coeffs[1],coeffs[2])," -- ",
coords = hc.addressToXY(ad1)
print "({:6.3f},{:6.3f})".format(coords[0],coords[1])," -- ",
reco = hc.coordinatesToAddress(coeffs)
print ha.addressToCanon(reco)," -- ",
print ha.addressToIndex(ad1)

print ha.addressToCanon(ad2), " -- ",
print ad2.bin," -- ",
coeffs = hc.coefficients(ad2)
print "({:3.1f},{:3.1f},{:3.1f})".format(coeffs[0],coeffs[1],coeffs[2])," -- ",
coords = hc.addressToXY(ad2)
print "({:6.3f},{:6.3f})".format(coords[0],coords[1])," -- ",
reco = hc.coordinatesToAddress(coeffs)
print ha.addressToCanon(reco)," -- ",
print ha.addressToIndex(ad2)

print ha.addressToCanon(out), " -- ",
print out.bin," -- ",
coeffs = hc.coefficients(out)
print "({:3.1f},{:3.1f},{:3.1f})".format(coeffs[0],coeffs[1],coeffs[2])," -- ",
coords = hc.addressToXY(out)
print "({:6.3f},{:6.3f})".format(coords[0],coords[1])," -- ",
reco = hc.coordinatesToAddress(coeffs)
print ha.addressToCanon(reco)," -- ",
print ha.addressToIndex(out)

print
neg = ha.negateAddress(ad1)
print neg.bin,"=",ha.addressToCanon(neg)
diff = ha.addressSubtract(out,ad2)
print diff.bin,"=",ha.addressToCanon(diff)
print

print "L1 Neighbours of ", ha.addressToCanon(ad1),":"
neighbours = ha.getL1Neighbours(ad1)
for tile in neighbours:

    print ha.addressToCanon(tile), " -- ",
    print tile.bin," -- ",
    coeffs = hc.coefficients(tile)
    print "({:3.1f},{:3.1f},{:3.1f})".format(coeffs[0],coeffs[1],coeffs[2])," -- ",
    coords = hc.addressToXY(tile)
    print "({:6.3f},{:6.3f})".format(coords[0],coords[1])," -- ",
    reco = hc.coordinatesToAddress(coeffs)
    print ha.addressToCanon(reco)," -- ",
    print ha.addressToIndex(tile)


