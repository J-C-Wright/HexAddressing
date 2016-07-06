import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

import HexAddresses as ha
import HexCoordinates as hc

from math import sqrt


def getPatch(address):
    
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
    axes.annotate(address,(coords[0]-0.15,coords[1]-0.05))





adString = '000'
ad1 = ha.intToAddress(adString)

verts = []
neighbours = ha.getL1Neighbours(ad1)
for tile in neighbours:
    coords = hc.addressToXY(tile)
    verts.append((coords[0],coords[1]))
temp = hc.addressToXY(neighbours[0])
verts.append((temp[0],temp[1]))

codes = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.CLOSEPOLY,
         ]
         
path1 = getPatch('001')
path2 = getPatch('002')
path3 = getPatch('003')
path4 = getPatch('004')
path5 = getPatch('005')
path6 = getPatch('006')
path7 = getPatch('016')
path8 = getPatch('000')
path9 = getPatch('024')



fig = plt.figure()
ax = fig.add_subplot(111)

patch1 = patches.PathPatch(path1, facecolor='orange', lw=1)
patch2 = patches.PathPatch(path2, facecolor='orange', lw=1)
patch3 = patches.PathPatch(path3, facecolor='orange', lw=1)
patch4 = patches.PathPatch(path4, facecolor='orange', lw=1)
patch5 = patches.PathPatch(path5, facecolor='orange', lw=1)
patch6 = patches.PathPatch(path6, facecolor='orange', lw=1)
patch7 = patches.PathPatch(path7, facecolor='orange', lw=1)
patch8 = patches.PathPatch(path8, facecolor='orange', lw=1)
patch9 = patches.PathPatch(path9, facecolor='orange', lw=1)


ax.add_patch(patch1)
ax.add_patch(patch2)
ax.add_patch(patch3)
ax.add_patch(patch4)
ax.add_patch(patch5)
ax.add_patch(patch6)
ax.add_patch(patch7)
ax.add_patch(patch8)
ax.add_patch(patch9)

ax.set_xlim(-3,3)
ax.set_ylim(-3,3)

hexLabel(ax,'000')
hexLabel(ax,'001')
hexLabel(ax,'002')
hexLabel(ax,'003')
hexLabel(ax,'004')
hexLabel(ax,'005')
hexLabel(ax,'006')
hexLabel(ax,'016')
hexLabel(ax,'034')
hexLabel(ax,'012')
hexLabel(ax,'013')
hexLabel(ax,'024')

plt.axes().set_aspect('equal')
plt.show()




