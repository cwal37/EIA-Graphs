# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 14:09:10 2016

@author: Connor
"""

from matplotlib import pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection

x = np.linspace(0,10,10000)
y = 2 - 0.5*np.abs(x-4)
lwidths = (1+x)**2 # scatter 'o' marker size is specified by area not radius 
plt.scatter(x,y, s=lwidths, color='blue')
plt.xlim(0,9)
plt.ylim(0,2.1)
plt.savefig('one.png', dpi=600)
plt.close()

x=np.linspace(0,4*np.pi,10000)
y=np.cos(x)
lwidths=1+x[:-1]
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
lc = LineCollection(segments, linewidths=lwidths,color='blue')
fig,a = plt.subplots()
a.add_collection(lc)
a.set_xlim(0,4*np.pi)
a.set_ylim(-1.1,1.1)
plt.savefig('two.png', dpi=600)
plt.close()