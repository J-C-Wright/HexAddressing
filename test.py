import HexAddresses as ha




ad1 = ha.intToAddress('406')
print "Neighbours of ", ha.addressToInt(ad1),":"
neighbours = ha.getL1Neighbours(ad1)
for tile in neighbours:
    print "   ", ha.addressToInt(tile)




