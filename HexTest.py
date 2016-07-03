#!/usr/bin/python

import sys, getopt
import HexAddresses as ha
import HexCoordinates as hc

adString = ''

myopts, args = getopt.getopt(sys.argv[1:],"a:")
for o, a in myopts:
    if o == '-a':
        adString = a
assert len(adString)==3, "Address is not 3 digits"

print "Demonstration of neighbour finding and address->coordinates conversion"
print "Input cell address is:", adString
ad1 = ha.intToAddress(adString)

print ha.addressToInt(ad1), " -- ",
print ad1.bin," -- ",
coeffs = hc.coefficients(ad1)
print "({:2.0f},{:2.0f},{:2.0f})".format(coeffs[0],coeffs[1],coeffs[2])," -- ",
coords = hc.addressToXY(ad1)
print "({:6.3f},{:6.3f})".format(coords[0],coords[1])," -- ",
print ha.addressToIndex(ad1)

print "L1 Neighbours of ", ha.addressToInt(ad1),":"
neighbours = ha.getL1Neighbours(ad1)
for tile in neighbours:

    print ha.addressToInt(tile), " -- ",
    print tile.bin," -- ",
    coeffs = hc.coefficients(tile)
    print "({:2.0f},{:2.0f},{:2.0f})".format(coeffs[0],coeffs[1],coeffs[2])," -- ",
    coords = hc.addressToXY(tile)
    print "({:6.3f},{:6.3f})".format(coords[0],coords[1])," -- ",
    print ha.addressToIndex(tile)

print "L2 Neighbours of ", ha.addressToInt(ad1),":"
neighbours = ha.getL2Neighbours(ad1)
for tile in neighbours:

    print ha.addressToInt(tile), " -- ",
    print tile.bin," -- ",
    coeffs = hc.coefficients(tile)
    print "({:2.0f},{:2.0f},{:2.0f})".format(coeffs[0],coeffs[1],coeffs[2])," -- ",
    coords = hc.addressToXY(tile)
    print "({:6.3f},{:6.3f})".format(coords[0],coords[1])," -- ",
    print ha.addressToIndex(tile)






