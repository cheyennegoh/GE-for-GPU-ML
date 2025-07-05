# datasets.py

import math
import numpy as np

def mkspiral():
    '''
        Generates training data for a network with 2 inputs and 1 output.

        Adapted from mkspiral.c by Alexis P. Wieland of the MITRE Corporation.
    '''
    ds = []

    for i in range(96 + 1):
        angle = i * math.pi / 16
        radius = 6.5 * (104 - i) / 104

        x = radius * math.sin(angle)
        y = radius * math.cos(angle)

        ds.append([x, y, 1])
        ds.append([-x, -y, 0])
    
    return np.array(ds)