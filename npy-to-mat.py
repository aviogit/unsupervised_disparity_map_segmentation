#!/usr/bin/python3

import numpy as np
import scipy.io

depth = np.load('depth.npy')
mydata = dict()
mydata['depth'] = depth
scipy.io.savemat('depth.mat', {'mydata': mydata})

