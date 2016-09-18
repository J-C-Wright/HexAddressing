import os
import inspect

from math import sqrt

import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

import StandardAddress as sa
import CanonAddress as ca
import SpiralAddress as spa

from CanonAddress import CanonAddress as Canon
from StandardAddress import StandardAddress as Standard
from SpiralAddress import SpiralAddress as Spiral

import Coordinates as coords




fig = plt.figure()
fig.set_canvas(plt.gcf().canvas)
ax = fig.add_subplot(111)
ax.add_patch(patch)
ax.set_xlim(-2.0,2.0)
ax.set_ylim(-2.0,2.0)
plt.axes().set_aspect('equal')

plt.show()





