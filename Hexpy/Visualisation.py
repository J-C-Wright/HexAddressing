import os
import inspect

from math import sqrt

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

import matplotlib.cm as cm

import StandardAddress as sa
import CanonAddress as ca
import SpiralAddress as spa

from CanonAddress import CanonAddress as Canon
from StandardAddress import StandardAddress as Standard
from SpiralAddress import SpiralAddress as Spiral

import Coordinates as coords
from Hexagon import Hexagon


from Coordinates import addressToUVW as Converter

converter = Converter(5)
for order in range(5):
    print "Starting order {}".format(order+1)
    limit = 7**(order+1)
    step = 1

    norm = mpl.colors.Normalize(vmin=0, vmax=limit)
    cmap = cm.plasma
    m = cm.ScalarMappable(norm=norm, cmap=cmap)

    hexes = []
    for i in range(0,limit,step):
        test_hex = Hexagon(spiral=Spiral(i),colour=m.to_rgba(i),line_width=0.0,side_size=1/sqrt(3),converter=converter)
        hexes.append(test_hex)

    fig = plt.figure()
    fig.set_canvas(plt.gcf().canvas)
    ax = fig.add_subplot(111)

    xmin = 999
    ymin = 999
    xmax = -999
    ymax = -999

    for test_hex in hexes:
        ax.add_patch(test_hex.getPatch())
        x,y = test_hex.centre_xy
        if x > xmax: xmax = x
        if x < xmin: xmin = x
        if y > ymax: ymax = y
        if y < ymin: ymin = y

    plt.axes().set_aspect('equal')
    ax.set_xlim(xmin-1,xmax+1)
    ax.set_ylim(ymin-1,ymax+1)
    plt.axis('off')
    print "Hexagons calculated. Saving to .png"
    fig.savefig('Plots/Aggregate_'+str(order+1)+'_step'+str(step)+'.png',format='png',dpi=1000)





