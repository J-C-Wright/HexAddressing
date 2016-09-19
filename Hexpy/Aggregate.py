import os
import inspect

from math import sqrt

import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

import StandardAddress as sa
import CanonAddress as ca
import SpiralAddress as spa

from CanonAddress import CanonAddress as Canon
from StandardAddress import StandardAddress as Standard
from SpiralAddress import SpiralAddress as Spiral
from Hexagon import Hexagon

import Coordinates as coords

class HexagonAggregate(object):

    def __init__(self,hexagons=None,addresses=None,start=0,end=7,steps=[1],level=None,values=[]):

        frame = inspect.currentframe()
        _,_,_,values = inspect.getargvalues(frame)
        nones = values.values().count(None)
        inputs = 3
        if  inputs-nones > 1:
            raise Exception, "Must specify one of either hexagons/addresses/level"

        converter = coords.addressToUVW(4)
        self.hexagon_array = []

        if hexagons != None:
            self.hexagon_array = hexagons
        elif addresses != None:
            self.addresses = addresses
        elif level != None:
            for i in range(7**level):
                self.hexagon_array.append(Hexagon(spiral=Spiral(i),converter=converter))
        else:
            i = start
            while i < end:
                for n in steps:
                    self.hexagon_array.append(Hexagon(spiral=Spiral(i),converter=converter))
                    i += n


    def __getitem__(self,index):

        if type(index) is Standard:
            i = int(spa.spiralFromStandard(index))
            return self.hexagon_array[i]
        elif type(index) is Canon:
            i = int(spa.spiralFromCanon(index))
            return self.hexagon_array[i]
        elif type(index) is Spiral:
            i = int(index)
            return self.hexagon_array[i]
        elif type(index) is int:
            return self.hexagon_array[index]

    def __len__(self):
        return len(self.hexagon_array)

    def setValues(self,values):

        if len(self) != len(values):
            raise Exception, "Number of values and hexagons must match"

        for hexagon,value in zip(self.hexagon_array,values):
            hexagon.value = value
            
class AddressAggregate(object):

    def __init__(self):
        print "Dummy class..."
        

#test = HexagonAggregate(start=0,end=7,steps=[1,2,4])

test = HexagonAggregate(level=1)

#for hexagon in test:
#    print
#    print hexagon

test.setValues(range(len(test)))

#for hexagon in test:
#    print
#    print hexagon

print "Indexing tests"
print test[2]
print 
print test[Canon('2')]
print 
print test[Standard(bin='010')]
print 
print test[Spiral(2)]






