from bitstring import Bits
from bitstring import BitArray
from math import pow

def addDigits(digit1,digit2):

    bits = BitArray('')
    wrapCarry = False

    for i in range(3):
        xoxrBit = digit1.bin[i] != digit2.bin[i]
        remainder = xorBit != wrapCarry

        if wrapCarry:
            wrapCarry = xorBit or (digit1.bin[i] == '1' and digit2.bin[i] == '1')
        else:
            wrapCarry = digit1.bin[i] == '1' and digit2.bin[i] == '1'

        bits.append(Bits(bool=remainder))

    return [wrapCarry,bits]


def remainderDigits(digit1,digit2):

    assert len(digit1) == 3 and len(digit2) ==3, 'Digit bitstring must always be length three'

    wrapCarry,bits = addDigits(digit1,digit2)

    while (wrapCarry):
        wrap = Bits(bin='100')
        wrapCarry,bits = addDigits(bits,wrap)

    return bits

def carryDigits(digits):

    for digit in digits:
        assert len(digit) == 3, 'Digit bitstring must always be length three'

    bits = BitArray(bin='000')
    for digit in digits:
        bits = bits ^ digit
    bits.rol(1)
    return bits

def addAddresses(address1,address2):

    assert len(address1)%3 == 0 and len(address2)%3 == 0, "Bitstring must be made up of digits with three bits"

    while (len(address1) != len(address2)):
        if (len(address1) < len(address2)):
            address1 = Bits(bin='000'+address1.bin)
        else:
            address2 = Bits(bin='000'+address2.bin)

    numDigits = len(address1)/3

    digits1 = []
    digits2 = []

    for i in range(numDigits):
        digits1.append(address1[0+i*3:3+i*3])
        digits2.append(address2[0+i*3:3+i*3])

    digits1.reverse()
    digits2.reverse()

    addressOut = []
    car = Bits(bin='000')
    for i in range(numDigits):

        rem = remainderDigits(digits1[i],digits2[i])
        rem = remainderDigits(rem,car)
        testcar = remainderDigits(car,rem)
        car = carryDigits([testcar,digits1[i],digits2[i]])

        addressOut.append(rem)

    addressOut.reverse()
    bits = BitArray('')

    if (car.bin != '000' and car.bin != '111'):
        bits.append(car)
    for i in range(numDigits):
        bits.append(addressOut[i])

    return bits





