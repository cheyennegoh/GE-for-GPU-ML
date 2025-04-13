# datasets.py

import math
import numpy as np

def mkspiral(a=96, b=16, c=6.5, d=104):
    '''
        Generates training data for a network with 2 inputs and 1 output.

        Adapted from mkspiral.c by Alexis P. Wieland of the MITRE Corporation.
    '''
    ds = []

    for i in range(a + 1):
        angle = i * math.pi / b
        radius = c * (d - i) / d

        x = radius * math.sin(angle)
        y = radius * math.cos(angle)

        ds.append([x, y, 1])
        ds.append([-x, -y, 0])
    
    return np.array(ds)
