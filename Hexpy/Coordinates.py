from math import sqrt, cos, sin, pi, atan, fabs

import StandardAddress as sa
import CanonAddress as ca
import SpiralAddress as spa

from CanonAddress import CanonAddress as Canon
from StandardAddress import StandardAddress as Standard
from SpiralAddress import SpiralAddress as Spiral

class addressToUVW:

    def __init__(self,aggregate=5):
        self.aggregate = aggregate
        self.calculateMappingMatrices(self.aggregate-1)

    def __call__(self,address,scale=1,rotation=0):
        addressAggregate = address.aggregate()
        if addressAggregate > self.aggregate:
            self.calculateMappingMatrices(addressAggregate-1)
            self.aggregate = addressAggregate

        if type(address) is Spiral:
            standard = sa.standardFromSpiral(address)    
        elif type(address) is Canon:
            standard = sa.standardFromCanon(address)
        elif type(address) is Standard:
            standard = address

        coeffs = [0,0,0]

        digits = standard.digits()
        digits.reverse()

        for i in range(addressAggregate):
            B = self.matrices[i]
            for j in range(3):
                for num,bit in zip(B[j],digits[i]):
                    coeffs[j] += num*int(bit)

        if scale != 1:
            for i in range(3):
                coeffs[i] *= scale
        
        if rotation != 0:
            print 'Rotation isn\'t implemented yet!!'

        return coeffs

    def __str__(self):
        out = 'Aggregate: '
        out += str(self.aggregate)
        for i,matrix in enumerate(self.matrices):
            out += '\nM'+str(i+1) + ': '+str(matrix)
        return out

        
    def calculateMappingMatrices(self,N):

        self.matrices = []
        B0 = [[1,-0.5,-0.5],[-0.5,1,-0.5],[-0.5,-0.5,1]]
        self.matrices.append(B0)

        for j in range(1,N+1,1):

            A = [[0,0,0],[0,0,0],[0,0,0]]
            for mat in self.matrices[:j]:
                for i in range(3):
                    for j in range(3):
                        A[i][j] += mat[i][j]

            vec = [1,-0.5,-0.5]
            for i in range(3):
                vec[i] += A[i][0]*2 + A[i][2]
                
            B = [[0,0,0],[0,0,0],[0,0,0]]
            for i in range(3):
                p = vec[-i::]+vec[:-i:]
                B[0][i] = p[0]
                B[1][i] = p[1]
                B[2][i] = p[2]

            self.matrices.append(B)

def coordinatesToAddress(coords,address_type='standard',scale=1):

    assert len(coords) == 3, "Must be 3 coords given (u,v,w)"
    assert sum(coords) == 0, "u + v + w must equal zero"
    
    du = (2.0/3.0)*(2*coords[0]+coords[1])
    dv = (2.0/3.0)*(coords[0]+2*coords[1])

    u_step = Standard(bin='100')
    v_step = Standard(bin='010')

    if du < 0: u_step = ~u_step
    if dv < 0: v_step = ~v_step

    out = Standard(bin='000')

    for i in range(int(fabs(du))):
        out = out + u_step
    for i in range(int(fabs(dv))):
        out = out + v_step

    if address_type.lower() == 'standard':
        return out
    elif address_type.lower() == 'canon':
        return ca.canonFromStandard(out)
    elif address_type.lower() == 'spiral':
        return spa.spiralFromStandard(out)
    else:
        raise Exception, 'address_type '+address_type+' is not valid'
    
def UVWToXY(uvw):

    uvw_basis = [[0,1],[0.5*sqrt(3),-0.5],[-0.5*sqrt(3),-0.5]]
    out = [0,0]

    for vector,magnitude in zip(uvw_basis,uvw):
        out[0] += vector[0]*magnitude
        out[1] += vector[1]*magnitude

    #FIX ME! Probably buggered up the maths. Check the basis vectors in (x,y)
    out[0] /= 1.5
    out[1] /= 1.5

    return out

def XYToUVW(xy):

    x,y = xy

    r = sqrt(x**2 + y**2)
    if x == 0:
        phi = pi/2.0
    else:
        phi = atan(y/x)

    u = y
    w = r*cos(phi - pi/6)
    v = -(u+w)

    return [u,v,w]



