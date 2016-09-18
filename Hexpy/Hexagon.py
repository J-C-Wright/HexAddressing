import os
import inspect

import StandardAddress as sa
import CanonAddress as ca
import SpiralAddress as spa

from CanonAddress import CanonAddress as Canon
from StandardAddress import StandardAddress as Standard
from SpiralAddress import SpiralAddress as Spiral

class Hexagon:

    def __init__(self,canon=None,standard=None,spiral=None,size=1):

        frame = inspect.currentframe()
        _,_,_,values = inspect.getargvalues(frame)

        numberOfNones = values.values().count(None)
        if  3-numberOfNones != 1:
            raise Exception, "Number of address inputs = {}. Must specify just one input to build hex".format(3-numberOfNones)



        

canon = Canon('5')
standard = Standard(bin='101')
spiral = Spiral(5)

Hexagon(canon = canon,standard=standard)
