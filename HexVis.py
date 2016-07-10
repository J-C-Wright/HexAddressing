import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import os
import HexAddresses as ha
import HexCoordinates as hc

from math import sqrt

def getPath(address):
    
    scale = 1/sqrt(3)
    ad = ha.canonToAddress(address)
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

def hexLabel(axes,canon,fontSize):
    ad = ha.canonToAddress(canon)
    coords = hc.addressToXY(ad)
    axes.annotate(canon,(coords[0]-0.15,coords[1]-0.05),fontsize=fontSize)

def getPatch(path):
    return patches.PathPatch(path, facecolor='orange', lw=1)
         
def drawHexes(canons,show=True,save=False,directory='',fileName=''):

    patchList = []
    for canon in canons:
        path = getPath(canon)
        patchList.append(getPatch(path))

    fig = plt.figure()
    fig.set_canvas(plt.gcf().canvas)
    ax = fig.add_subplot(111)

    for patch in patchList:
        ax.add_patch(patch)

    scale = 9.0
    ax.set_xlim(-4*scale,4*scale)
    ax.set_ylim(-4*scale,4*scale)

    for canon in canons:
        hexLabel(ax,canon,10/scale)

    plt.axes().set_aspect('equal')
    if (save):
        print "Saving "+directory+fileName+".pdf"
        if not os.path.exists(directory):
                os.makedirs(directory)
        fig.savefig(directory+fileName+".pdf",format='pdf')
    if (show):
        plt.show()

'''
canons1 = ha.makeCanonArray(0,0,1,3)
canons2 = []#ha.makeCanonArray(0,0,1,3)
s = set(canons2)
canons3 = [x for x in canons1 if x not in s]

canons4 = ['000','001','002','004','010','020','040','100','200','400']
'''

canons5 = ha.makeCanonArray(0,0,1,4)


drawHexes(canons5,show=False,save=True,directory="Plots/",fileName="FourthAggregate")

'''
srt = 0
shf = 0
stp = 1
odr = 3
for i in range(1,21,1):
    canons = ha.makeCanonArray(start=srt,shift=shf,step=i,order=odr)
    name = 'Start'+str(srt)+'_Shift'+str(shf)+'_Step'+str(i)+'_Order'+str(odr)
    drawHexes(canons,show=False,save=True,directory="Plots/",fileName=name)
'''
