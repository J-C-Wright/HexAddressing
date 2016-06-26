import HexAddresses as ha
import HexCoordinates as hc



ad1 = ha.intToAddress('001')
print "Neighbours of ", ha.addressToInt(ad1),":"

neighbours = ha.getL1Neighbours(ad1)
for tile in neighbours:

    coeffs = hc.coefficients(tile)

    print tile.bin, " -- ",

    print ha.addressToInt(tile), " -- ",
                 
    for coeff in coeffs:
        print coeff,
    print " -- ",
    coords = hc.coordinates(coeffs)
    print "({:7.4f},{:7.4f})".format(coords[0],coords[1])





