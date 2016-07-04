import HexAddresses as ha
from math import sqrt, cos, sin, pi, atan

def coefficients(address):

    assert len(address)%3 == 0, "Bitstring length must be multiple of three"

    numDigits = len(address)/3
    coeffs = [0,0,0]
    trips = []

    B0 = [[1,-0.5,-0.5],[-0.5,1,-0.5],[-0.5,-0.5,1]]
    B1 = [[2.5,-0.5,-2],[-2,2.5,-0.5],[-0.5,-2,2.5]]
    B2 = [[5.5,1,-6.5],[-6.5,5.5,1],[1,-6.5,5.5]]
    
    for i in range(numDigits):
        trips.append(address.bin[0+i*3:3+i*3])
    
    for i in range(3):
        if i==0:
            for j in range(3):
                for num,bit in zip(B2[j],trips[i]):
                    coeffs[j] += num*int(bit)
        elif i==1:
            for j in range(3):
                for num,bit in zip(B1[j],trips[i]):
                    coeffs[j] += num*int(bit)
        elif i==2:
            for j in range(3):
                for num,bit in zip(B0[j],trips[i]):
                    coeffs[j] += num * int(bit)
    
    return coeffs


def coordinates(coeffs):

    assert len(coeffs) == 3, "Must be three coefficients"

    vs = [[0,1],[0.5*sqrt(3),-0.5],[-0.5*sqrt(3),-0.5]]
    out = [0,0]

    for v,coeff in zip(vs,coeffs):
        out[0] += v[0]*coeff
        out[1] += v[1]*coeff
    
    return out

def addressToXY(address):

    coeffs = coefficients(address)
    coords = coordinates(coeffs)

    #Apply transformation into desired setup
    theta = 0
    scale = 1/1.5 #Where did the factor of 1.5 come from?

    x = cos(theta)*coords[0] - sin(theta)*coords[1]
    y = sin(theta)*coords[0] + cos(theta)*coords[1]

    x *= scale
    y *= scale

    return [x,y]


    










