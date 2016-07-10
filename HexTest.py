#!/usr/bin/python

import sys, getopt
import HexAddresses as ha
import HexCoordinates as hc

adString = ''
oneString = ''
myopts, args = getopt.getopt(sys.argv[1:],"a:b:")
for o, a in myopts:
    if o == '-a':
        adString = a
    if o == '-b':
        oneString = a
#assert len(adString)==3, "Address is not 3 digits"

print "Demonstration of neighbour finding and address->coordinates conversion"
print "Input cell address is:", adString
ad1 = ha.canonToAddress(adString)
one = ha.canonToAddress(oneString)


print ha.addressToCanon(ad1), " -- ",
print ad1.bin," -- ",
coeffs = hc.coefficients(ad1)
print "({:3.1f},{:3.1f},{:3.1f})".format(coeffs[0],coeffs[1],coeffs[2])," -- ",
coords = hc.addressToXY(ad1)
print "({:6.3f},{:6.3f})".format(coords[0],coords[1])," -- ",
print ha.addressToIndex(ad1)

print ha.addressToCanon(one), " -- ",
print one.bin," -- ",
coeffs = hc.coefficients(one)
print "({:3.1f},{:3.1f},{:3.1f})".format(coeffs[0],coeffs[1],coeffs[2])," -- ",
coords = hc.addressToXY(one)
print "({:6.3f},{:6.3f})".format(coords[0],coords[1])," -- ",
print ha.addressToIndex(one)


up1 = ha.addressAdd(ad1,one);
print "--->",up1.bin, " -- ",
print ha.addressToCanon(up1), " -- ",
coeffs = hc.coefficients(up1)
print "({:3.1f},{:3.1f},{:3.1f})".format(coeffs[0],coeffs[1],coeffs[2])," -- ",
coords = hc.addressToXY(up1)
print "({:6.3f},{:6.3f})".format(coords[0],coords[1])," -- ",
print ha.addressToIndex(up1)

print
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
    print ha.addressToIndex(tile)


