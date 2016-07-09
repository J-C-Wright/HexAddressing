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

canons1 = ['001','002','003','004','005','006','016',
             '066','024','034','013','026','061','042',
             '026','021','033','015','046','063','030',
             '044','051','056','053','045','064']

canons2 = ['000',
             '011','012','013','014','015','016',
             '021','022','023','024','025','026',
             '031','032','033','034','035','036',
             '041','042','043','044','045','046',
             '051','052','053','054','055','056',
             '061','062','063','064','065','066']

canons3 = ha.makeCanonArray(0,0,1,3)
drawHexes(canons3)





