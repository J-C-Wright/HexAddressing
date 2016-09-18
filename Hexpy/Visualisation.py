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

order = 5
limit = 7**(order+1)
step = 1

norm = mpl.colors.Normalize(vmin=0, vmax=limit)
cmap = cm.plasma
m = cm.ScalarMappable(norm=norm, cmap=cmap)

hexes = []
for i in range(0,limit,step):
    test_hex = Hexagon(spiral=Spiral(i),colour=m.to_rgba(i),line_width=0.0,side_size=1/sqrt(3))
    hexes.append(test_hex)

fig = plt.figure()
fig.set_canvas(plt.gcf().canvas)
ax = fig.add_subplot(111)
for test_hex in hexes:
    ax.add_patch(test_hex.getPatch())
plt.axes().set_aspect('equal')
ax.set_xlim(-3.0**order,3.0**order)
ax.set_ylim(-3.0**order,3.0**order)

fig.savefig('test.pdf',format='pdf')
plt.show()





