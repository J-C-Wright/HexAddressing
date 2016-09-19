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

class Hexagon:

    def __init__(self,canon=None,standard=None,spiral=None,
                 side_size=1/sqrt(3),orientation='side',colour='Orange',
                 opacity = 1.0,line_width=0.0,converter=None,value=0):

        frame = inspect.currentframe()
        _,_,_,values = inspect.getargvalues(frame)
        numberOfNones = values.values().count(None)
        if  3-numberOfNones != 1:
            raise Exception, "Number of address inputs = {}. Must specify just one input to build hex".format(3-numberOfNones)

        self.side_size = side_size
        self.orientation = orientation
        self.colour = colour
        self.opacity = opacity
        self.line_width = line_width
        self.vertices = []

        self.value = value

        if standard != None:
            self.standard = standard
        elif canon != None:
            self.standard = sa.standardFromCanon(canon)
        elif spiral != None:
            self.standard = sa.standardFromSpiral(spiral)
        else:
            raise Exception, "No address in input"

        #Centre
        self.centre_uvw = converter(self.standard)
        self.centre_xy = coords.UVWToXY(self.centre_uvw)

    def __str__(self):
        string = ''
        string += 'Cell address: S-'+str(self.standard)+' C-'+str(ca.canonFromStandard(self.standard))
        string += ' Sp-'+str(spa.spiralFromStandard(self.standard))
        string += '\nValue: '+str(self.value)
        string += '\nSize: '+str(self.side_size)
        string += '\nOrientation: '+str(self.orientation)
        string += '\nColour: '+str(self.colour)
        string += '\nOpacity: '+str(self.opacity)
        string += '\nLine width: '+str(self.line_width)
        string += '\nCentre (UVW): '+str(self.centre_uvw)
        string += '\nCentre (XY): '+str(self.centre_uvw)
        return string

    def aggregate(self):
        return self.standard.aggregate()

    def makeVertices(self):
        if self.orientation == 'side':
            self.vertices = [(-1.0*self.side_size+self.centre_xy[0],self.centre_xy[1]),
                         (-0.5*self.side_size+self.centre_xy[0],self.side_size*sqrt(3)/2.0+self.centre_xy[1]),
                         (0.5*self.side_size+self.centre_xy[0],self.side_size*sqrt(3)/2.0+self.centre_xy[1]),
                         (1.0*self.side_size+self.centre_xy[0],self.centre_xy[1]),
                         (0.5*self.side_size+self.centre_xy[0],self.side_size*-sqrt(3)/2.0+self.centre_xy[1]),
                         (-0.5*self.side_size+self.centre_xy[0],self.side_size*-sqrt(3)/2.0+self.centre_xy[1])]
        elif self.orientation == 'corner':
            self.vertices = [(self.centre_xy[0],1.0*self.side_size+self.centre_xy[1]),
                         (self.side_size*sqrt(3)/2.0+self.centre_xy[0],self.side_size*0.5+self.centre_xy[1]),
                         (self.side_size*sqrt(3)/2.0+self.centre_xy[0],-self.side_size*0.5+self.centre_xy[1]),
                         (self.centre_xy[0],-1.0*self.side_size+self.centre_xy[1]),            
                         (-self.side_size*sqrt(3)/2.0+self.centre_xy[0],-self.side_size*0.5+self.centre_xy[1]),
                         (-self.side_size*sqrt(3)/2.0+self.centre_xy[0],self.side_size*0.5+self.centre_xy[1])]
    
    def getPatch(self):
        
        if len(self.vertices) == 0:
            self.makeVertices()

        codes = [Path.MOVETO,
                 Path.LINETO,
                 Path.LINETO,
                 Path.LINETO,
                 Path.LINETO,
                 Path.LINETO,
                 Path.CLOSEPOLY,
                 ]

        path = Path(self.vertices+[self.vertices[0]],codes) #+...[0] is for closure of shape
        
        return patches.PathPatch(path,facecolor=self.colour,lw=self.line_width)


