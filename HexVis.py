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

def hexLabel(axes,address,fontSize):
    ad = ha.intToAddress(address)
    coords = hc.addressToXY(ad)
    axes.annotate(address,(coords[0]-0.15,coords[1]-0.05),fontsize=fontSize)

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

    scale = 3.0
    ax.set_xlim(-4*scale,4*scale)
    ax.set_ylim(-4*scale,4*scale)

    for address in addresses:
        hexLabel(ax,address,10/scale)

    plt.axes().set_aspect('equal')
    plt.show()


canons = ha.makeCanonArray(start=0,shift=0,step=5,order=3)
drawHexes(canons)





