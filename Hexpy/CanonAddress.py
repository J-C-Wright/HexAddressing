import StandardAddress as sa
import SpiralAddress as spa

class CanonAddress(object):

    def __init__(self,address):
        assert address.isdigit() or isinstance(address,int),'Must give an integer input'
        address=str(address)
        for i in address:
            assert int(i) < 7,'Number must be in base 7'

        self.address = address

    def __str__(self):
        return self.address

    def __int__(self):
        return int(self.address)

    def __add__(self,other):
        standard_self = sa.standardFromCanon(self)
        standard_other = sa.standardFromCanon(other)
        return canonFromStandard(standard_self + standard_other)

    def __sub__(self,other):
        standard_self = sa.standardFromCanon(self)
        standard_other = sa.standardFromCanon(other)
        return canonFromStandard(standard_self - standard_other)

    def __invert__(self):
        standard_self = sa.standardFromCanon(self)
        return canonFromStandard(~standard_self)

    def aggregate(self):
        return len(self.address)

    def digits(self):
        digits = []
        for digit in self.address:
            digits.append(digit)
        return digits

    def increment(self,step=1):
        spiral_self = spa.spiralFromCanon(self)
        spiral_self.increment(step=step)
        self.address = canonFromSpiral(spiral_self).address

    def decrement(self,step=1):
        spiral_self = spa.spiralFromCanon(self)
        spiral_self.decrement(step=step)
        self.address = canonFromSpiral(spiral_self).address

def canonFromStandard(address):

    canonStr = ''
    for digit in address.digits():
        if digit.bin == '100':
            canonStr += '1'
        elif digit.bin == '010':
            canonStr += '2'
        elif digit.bin == '110':
            canonStr += '3'
        elif digit.bin == '001':
            canonStr += '4'
        elif digit.bin == '101':
            canonStr += '5'
        elif digit.bin == '011':
            canonStr += '6'
        else: 
            canonStr += '0'  #111 = 000
    return CanonAddress(canonStr)
        
def canonFromSpiral(spiral):

    address = int(spiral)
    if address == 0: return CanonAddress('0')

    digits = []
    while address:
        digit_b7 = address % 7

        if digit_b7 == 0:
            digits.append('0')
        elif digit_b7 == 1:
            digits.append('1')
        elif digit_b7 == 2:
            digits.append('3')
        elif digit_b7 == 3:
            digits.append('2')
        elif digit_b7 == 4:
            digits.append('6')
        elif digit_b7 == 5:
            digits.append('4')
        elif digit_b7 == 6:
            digits.append('5')
        else:
            raise Exception, "Something has gone quite wrong. It's not base 7!"

        address /= 7
    digits.reverse()
    
    return CanonAddress(''.join(digits))

    
    
    
