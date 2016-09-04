import StandardAddress as sa

class CanonAddress:

    def __init__(self,address):
        assert address.isdigit(),'Must give an integer input'

        self.address = address

    def __str__(self):
        return self.address

    def __add__(self,other):

        standard_self = sa.standardFromCanon(self)
        standard_other = sa.standardFromCanon(other)
        return canonFromStandard(standard_self + standard_other)

    def __sub__(self,other):

        standard_self = sa.standardFromCanon(self)
        standard_other = sa.standardFromCanon(other)
        return canonFromStandard(standard_self - standard_other)

    






def canonFromStandard(address):

    standard = address.bin
    canonStr = ''

    for i in range(len(address)/3):
        digit = standard[0+i*3:3+i*3]
        if digit == '100':
            canonStr += '1'
        elif digit == '010':
            canonStr += '2'
        elif digit == '110':
            canonStr += '3'
        elif digit == '001':
            canonStr += '4'
        elif digit == '101':
            canonStr += '5'
        elif digit == '011':
            canonStr += '6'
        else: 
            canonStr += '0'  #111 = 000
           
    return CanonAddress(canonStr)
        
def canonFromSpiral(address):

    length = len(str(address))
    canonStr = ''

    for i in range(length,-1,-1):
        rem = address % 7**i
        if (rem != address):
            canonStr += str((address - rem)/(7**i))
            address = rem
        else:
            canonStr += '0'
    if canonStr[0] == '0':
        return CanonAddress(canonStr[1:])  #Fix this
    else:
        return CanonAddress(canonStr)

   
    
    
    