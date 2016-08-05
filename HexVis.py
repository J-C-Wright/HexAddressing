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
    return patches.PathPatch(path, facecolor='orange', lw=0.05)
         
def drawHexes(canons,show=True,save=False,directory='',fileName='',scale=1.0):

    patchList = []
    for canon in canons:
        path = getPath(canon)
        patchList.append(getPatch(path))

    fig = plt.figure()
    fig.set_canvas(plt.gcf().canvas)
    ax = fig.add_subplot(111)

    for patch in patchList:
        ax.add_patch(patch)

    ax.set_xlim(-2.0-scale,2.0+scale)
    ax.set_ylim(-2.0-scale,2.0+scale)

    for canon in canons:
        hexLabel(ax,canon,int(30/scale))

    plt.axes().set_aspect('equal')
    if (save):
        print "Saving "+directory+fileName+".pdf"
        if not os.path.exists(directory):
                os.makedirs(directory)
        fig.savefig(directory+fileName+".pdf",format='pdf')
    if (show):
        plt.show()

def arrayDiff(array1,array2):
    s = set(array2)
    return [x for x in array1 if x not in s]


canons1 = ha.makeCanonArray(0,0,2,4)
canons2 = ha.makeCanonArray(0,0,4,4)
canons3 = arrayDiff(canons1,canons2)

canons4 = [ '000','001','002','004',
            '010','020','040',
            '100','200','400',
            '1000','2000','4000',
            '10000','20000','40000',
            ]
canons6 = ['000','001','002','003','004','005','006',
           '010','020','030','040','050','060',
           '100','200','300','400','500','600',
           '1000','2000','3000','4000','5000','6000',
           '10000','20000','30000','40000','50000','60000',
           '100000','200000','300000','400000','500000','600000',
           ]
srt = 0
shf = 0
stp = 1
odr = 6
canons5 = ha.makeCanonArray(srt,shf,stp,odr)


#drawHexes(canons5,show=False,save=True,directory="Plots/",fileName="Aggregate"+str(odr),scale=3**(odr-1))
#drawHexes(canons3,show=False,save=True,directory="Plots/",fileName="Diff")

#name = 'Start'+str(srt)+'_Shift'+str(shf)+'_Step'+str(stp)+'_Order'+str(odr)
#drawHexes(canons5,show=False,save=True,directory="Plots/",fileName=name)





'''
for i in range(1,6,1):
    agLvl = i
    canons7 = ha.makeCanonArray(0,0,1,agLvl)
    drawHexes(canons7,show=False,save=True,directory="Plots/",fileName="Aggregate"+str(agLvl),scale=3**(i-1))


for i in range(1,21,1):
    canons = ha.makeCanonArray(start=srt,shift=shf,step=i,order=odr)
    name = 'Start'+str(srt)+'_Shift'+str(shf)+'_Step'+str(i)+'_Order'+str(odr)
    drawHexes(canons,show=False,save=True,directory="Plots/",fileName=name)
'''
