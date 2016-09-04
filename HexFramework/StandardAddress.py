from bitstring import Bits
from bitstring import BitArray
from math import pow
import CanonAddress as ca

class StandardAddress(Bits):

    #Adds an assert to make sure that the digits have length 3
    def __init__(self, *args, **kwargs):
        super(StandardAddress, self).__init__(*args, **kwargs)
        assert len(self.bin)%3 == 0, 'Length of address must be a multiple of three.'
    
    #Addition overload
    def __add__(self,other):
        
        while (len(self) != len(other)):
            if (len(self) < len(other)):
                self = Bits(bin='000'+self.bin)
            else:
                other = Bits(bin='000'+other.bin)

        digits1 = []
        digits2 = []

        for i in range(len(self)/3):
            digits1.append(self[0+i*3:3+i*3])
            digits2.append(other[0+i*3:3+i*3])
        
        digits1.reverse()
        digits2.reverse()

        addressOut = []
        carries = []
        for digit1,digit2 in zip(digits1,digits2):

            digits = [digit1,digit2] + carries

            carries = []
            rem = Bits(bin='000')
            for digit in digits:

                remtemp = remainderDigits(rem,digit)
                car = carryDigits([rem,digit,remtemp])
                rem = remtemp
                carries.append(car)

            addressOut.append(rem)
        
        addressOut.reverse()
        bits = BitArray('')

        #If there are still non-zero carries
        if not all(c.bin == '000' or c.bin == '111' for c in carries):
            rem = Bits(bin='000')
            for digit in carries:
                remtemp = remainderDigits(rem,digit)
                car = carryDigits([rem,digit,remtemp])
                rem = remtemp
            if rem.bin != '000' and rem.bin != '111': bits.append(rem)

        for digit in addressOut:
            bits.append(digit)

        return bits

    #Subtraction overload
    def __sub__(self,other):
        return self + ~other

    #String overload method
    def __str__(self):
        return self.bin

def standardFromCanon(canon):

    binString = ''
    for digit in canon.address:
        if digit == '0':
            binString += '000'
        elif digit == '1':
            binString += '100'
        elif digit == '2':
            binString += '010'
        elif digit == '3':
            binString += '110'
        elif digit == '4':
            binString += '001'
        elif digit == '5':
            binString += '101'
        elif digit == '6':
            binString += '011'

    return StandardAddress(bin=binString)

def standardFromSpiral(spiral):

    canon = ca.canonFromSpiral(spiral)
    return standardFromCanon(canon)

def addDigits(digit1,digit2):

    bits = BitArray('')
    wrapCarry = False

    for i in range(3):
        xorBit = digit1.bin[i] != digit2.bin[i]
        remainder = xorBit != wrapCarry

        if wrapCarry:
            wrapCarry = xorBit or (digit1.bin[i] == '1' and digit2.bin[i] == '1')
        else:
            wrapCarry = digit1.bin[i] == '1' and digit2.bin[i] == '1'

        bits.append(Bits(bool=remainder))

    return [wrapCarry,bits]

def remainderDigits(digit1,digit2):

    wrapCarry,bits = addDigits(digit1,digit2)

    while (wrapCarry):
        wrap = Bits(bin='100')
        wrapCarry,bits = addDigits(bits,wrap)

    return bits

def carryDigits(digits):

    bits = BitArray(bin='000')
    for digit in digits:
        bits = bits ^ digit
    bits.rol(1)
    return bits

