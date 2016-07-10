from bitstring import Bits
from bitstring import BitArray
from math import pow

def carry(digits):

    for digit in digits:
        assert len(digit) == 3, "Bitstrings must have length = 3"

    bits = BitArray(bin='000')
    for digit in digits:
        bits = bits ^ digit
    bits.rol(1)
    return bits

def remainder(a,b):

    assert len(a) == 3 and len(b) == 3, "Bitstrings must have length = 3"

    rem = add(a,b)
    while (rem[0]):
        wrap = Bits(bin='100')
        rem = add(rem[1],wrap)
    return rem[1]

def add(a,b):

    bits = BitArray('')
    carTemp = False

    for i in range(3):

        xorBit = a.bin[i] != b.bin[i]
        remainder = xorBit != carTemp

        if carTemp:
            carTemp = xorBit or (a.bin[i] == '1' and b.bin[i] == '1')
        if not carTemp:
            carTemp = a.bin[i] == '1' and b.bin[i] == '1'
            
        bits.append(Bits(bool=remainder))

    return [carTemp,bits]

def bitsToCanon(trip):
    assert len(trip) == 3, "Must be three bits long"

    if trip == '100':
        return '1'
    elif trip == '010':
        return '2'
    elif trip == '110':
        return '3'
    elif trip == '001':
        return '4'
    elif trip == '101':
        return '5'
    elif trip == '011':
        return '6'
    else: 
        return '0'  #111 = 000

def canonToBits(digit):
    assert digit <= 6 and digit >= 0, "Must be between 0 and 6"

    if digit == 0:
        return '000'
    elif digit == 1:
        return '100'
    elif digit == 2:
        return '010'
    elif digit == 3:
        return '110'
    elif digit == 4:
        return '001'
    elif digit == 5:
        return '101'
    elif digit == 6:
        return '011'

def addressToCanon(address):

    assert len(address)%3 == 0, "Bitstring length must be multiple of three"

    numDigits = len(address)/3
    digits = ""
    trips = address.bin
    
    for i in range(numDigits):
        trip = trips[0+i*3:3+i*3]
        digits += bitsToCanon(trip)
        
    return digits

def canonToAddress(canonAddress):
    bitString = ""
    for digit in canonAddress:
        bitString += canonToBits(int(digit))
    return Bits(bin=bitString)

def addressAdd(address1,address2):

    assert len(address1)%3 == 0 and len(address2)%3 == 0, "Bitstring length must be multiple of three"
    
    while (len(address1) != len(address2)):
        if (len(address1) < len(address2)):
            address1 = Bits(bin='000'+address1.bin)
        else:
            address2 = Bits(bin='000'+address2.bin)

    assert len(address1) == len(address2), "Bitstrings must be equal length"
    
    numDigits = len(address1)/3

    trips1 = []
    trips2 = []

    for i in range(numDigits):
        trips1.append(address1[0+i*3:3+i*3])
        trips2.append(address2[0+i*3:3+i*3])
    
    trips1.reverse()
    trips2.reverse()

    addressOut = []
    car = Bits(bin='000')
    for i in range(numDigits):

        rem = remainder(trips1[i],trips2[i])
        rem = remainder(rem,car)
        car = carry([car,trips1[i],trips2[i],rem])

        addressOut.append(rem)

    addressOut.reverse()
    bits = BitArray('')

    if (car.bin != '000' and car.bin != '111'):
        bits.append(car)
    for i in range(numDigits):
        bits.append(addressOut[i])

    return bits

def getL1Neighbours(address):

    directions = ['001','003','002','006','004','005']
    addresses = []
    for direction in directions:
        dirAddress = canonToAddress(direction)
        neighbour = addressAdd(address,dirAddress)
        addresses.append(neighbour)
    return addresses

def getL2Neighbours(address):

    directions = ['001','003','002','006','004','005',
                  '012','034','036','025','024','061',
                  '065','043','041','052','053','016']
    addresses = []
    for direction in directions:
        dirAddress = canonToAddress(direction)
        neighbour = addressAdd(address,dirAddress)
        addresses.append(neighbour)
    return addresses

def addressToIndex(address):

    digits = addressToCanon(address)
    digits = digits[::-1]
       
    index = 0
    for i in range(len(digits)):
        index += int(digits[i]) * 7**i

    return index

def indexToCanon(index):

    length = len(str(index))
    digit = index
    canon = ''

    for i in range(length,-1,-1):
        rem = digit % 7**i
        if (rem != digit):
            canon += str((digit - rem)/(7**i))
            digit = rem
        else:
            canon += '0'
    if canon[0] == '0':
        return canon[1:]  #Fix this
    else:
        return canon

def makeCanonArray(start,shift,step,order):

    canons = []
    for i in range(start,7**order-shift,step):
        canons.append(indexToCanon(i+shift))

    return canons




