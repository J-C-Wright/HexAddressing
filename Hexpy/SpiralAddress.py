from bitstring import Bits
from bitstring import BitArray
from math import pow
import StandardAddress as sa
import CanonAddress as ca

class SpiralAddress(object):

    def __init__(self,address):
        self.address = int(address)
        assert self.address >= 0,'Address must be positive integer'

    def order(self):
        order = 0
        while self.address > 7**order:
            order += 1
        return order

    def __str__(self):
        return str(self.address)

    def __int__(self):
        return self.address

    def __add__(self,other):
        standard_self = sa.standardFromSpiral(self)
        standard_other = sa.standardFromSpiral(other)
        return spiralFromStandard(standard_self+standard_other)

    def __sub__(self,other):
        standard_self = sa.standardFromSpiral(self)
        standard_other = sa.standardFromSpiral(other)
        return spiralFromStandard(standard_self-standard_other)

    def __invert__(self):
       standard_self = sa.standardFromSpiral(self)
       return spiralFromStandard(~standard_self)

    def increment(self,step=1):
        self.address += step

    def decrement(self,step=1):
        if self.address > 0:
            self.address -= step



        
def spiralFromStandard(address):

    standard = address.bin

    digits = []
    for i in range(len(standard)/3):
        digit = standard[0+i*3:3+i*3]
        if digit != '111':
            digits.append(digit)
        else:
            digits.append('000')



    digits.reverse()
    out = 0
    for i,digit in enumerate(digits):

        digitTemp = 0
        for j,bit in enumerate(digit):

            digitTemp += int(bit)*2**j
        out += digitTemp*7**i

    return SpiralAddress(out)

def spiralFromCanon(address):

    digits = [int(i) for i in str(address)]
    digits.reverse()

    out = 0
    for i,digit in enumerate(digits):
        out += digit*7**i
    return SpiralAddress(out)





        

