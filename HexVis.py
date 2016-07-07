import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

import HexAddresses as ha
import HexCoordinates as hc

from math import sqrt

def getPath(address):
    
    scale = 1/sqrt(3)
    ad = ha.intToAddress(address)
    coords = hc.addressToXY(ad)

    hexVerts = [(-1.000*scale+coords[0], 0.000*scale+coords[1]),
                (-0.500*scale+coords[0], 0.866*scale+coords[1]),
                ( 0.500*scale+coords[0], 0.866*scale+coords[1]),
                ( 1.000*scale+coords[0],-0.000*scale+coords[1]),
                ( 0.500*scale+coords[0],-0.866*scale+coords[1]),
                (-0.500*scale+coords[0],-0.866*scale+coords[1]),
                (-1.000*scale+coords[0], 0.000*scale+coords[1]),
                ]

    codes = [Path.MOVETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.CLOSEPOLY,
             ]

    path = Path(hexVerts,codes)
    return path

def hexLabel(axes,address):
    ad = ha.intToAddress(address)
    coords = hc.addressToXY(ad)
    axes.annotate(address,(coords[0]-0.15,coords[1]-0.05),fontsize=10)

def getPatch(path):
    return patches.PathPatch(path, facecolor='orange', lw=1)
         
def drawHexes(addresses):

    patchList = []
    for address in addresses:
        path = getPath(address)
        patchList.append(getPatch(path))

    fig = plt.figure()
    ax = fig.add_subplot(111)

    for patch in patchList:
        ax.add_patch(patch)

    ax.set_xlim(-4,4)
    ax.set_ylim(-4,4)

    for address in addresses:
        hexLabel(ax,address)

    plt.axes().set_aspect('equal')
    plt.show()


addresses = ['001','002','003','004','005','006','016',
             '066','024','034','013','026','061','042',
             '044','051','056','053']
drawHexes(addresses)

