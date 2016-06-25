from bitstring import Bits
from bitstring import BitArray




def carry(a,b):

    assert len(a) == 3 and len(b) == 3, "Bitstrings must have length = 3"

    r = remainder(a,b)
    bits = BitArray( ((a ^ b) ^ r))
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

def bitsToInt(trip):
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

def intToBits(digit):
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

def addressToInt(address):

    assert len(address)%3 == 0, "Bitstring length must be multiple of three"

    numDigits = len(address)/3
    digits = ""
    trips = address.bin
    
    for i in range(numDigits):
        trip = trips[0+i*3:3+i*3]
        digits += bitsToInt(trip)
        
    return digits

def intToAddress(intAddress):
    bitString = ""
    for digit in intAddress:
        bitString += intToBits(int(digit))
    return Bits(bin=bitString)

def hexAdd(address1,address2):

    assert len(address1)%3 == 0 and len(address2)%3 == 0, "Bitstring length must be multiple of three"
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

        #Problem is here, carry is possibly wrong
        rem = remainder(trips1[i],trips2[i])
        rem = remainder(rem,car)
        car = carry(trips1[i],trips2[i])

        addressOut.append(rem)

    addressOut.reverse()
    bits = BitArray('')

    for i in range(numDigits):
        bits.append(addressOut[i])

    return bits

def getL1Neighbours(address):

    directions = ['001','002','003','004','005','006']
    addresses = []
    for direction in directions:
        dirAddress = intToAddress(direction)
        neighbour = hexAdd(address,dirAddress)
        addresses.append(neighbour)
    return addresses

def getL2Neighbours(address):

    directions = ['001','002','003','004','005','006',
                  '012','034','036','025','024','061',
                  '065','043','041','052','053','016']
    addresses = []
    for direction in directions:
        dirAddress = intToAddress(direction)
        neighbour = hexAdd(address,dirAddress)
        addresses.append(neighbour)
    return addresses


        



