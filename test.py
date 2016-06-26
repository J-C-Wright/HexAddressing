import HexAddresses as ha
import HexCoordinates as hc


print ""
print "Demonstration of neighbour finding and address->coordinates conversion"
ad1 = ha.intToAddress('000')
print "Neighbours of ", ha.addressToInt(ad1),":"

neighbours = ha.getL1Neighbours(ad1)
for tile in neighbours:

    coords = hc.addressToXY(tile)
    print ha.addressToInt(tile),
    print tile.bin,
    print "({:7.4f},{:7.4f})".format(coords[0],coords[1])





