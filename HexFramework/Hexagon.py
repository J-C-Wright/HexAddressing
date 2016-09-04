import inspect
from bitstring import Bits
from bitstring import BitArray
from math import pow
import StandardAddress as sta
import CanonAddress as ca
import SpiralAddress as spa

class Hexagon:

    def __init__(self,canon_address=None,standard_address=None,
                 spiral_address=None,hexagon=None,coordinates=None):


        frame = inspect.currentframe()
        _,_,_,values = inspect.getargvalues(frame)

        numberOfNones = values.values().count(None)
        assert 5-numberOfNones <= 1,"Too many inputs. Must specify one or zero input values"

        if canon_address is not None:
            self.canon_address = canon_address
        if standard_address is not None:
            self.standard_address = standard_address
        if spiral_address is not None:
            self.spiral_address = spiral_address
        if hexagon is not None:
            self.hexagon = hexagon
        if coordinates is not None:
            self.coordinates = coordinates

