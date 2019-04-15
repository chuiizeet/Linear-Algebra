import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

v1 = np.array([ 3, -1 ])
l  = -4
v1m = v1*l

plt.plot([0, v1[0]],[0, v1[1]],'b',label='v_1')
plt.plot([0, v1m[0]],[0, v1m[1]],'r:',label='\lambda v_1')

plt.axis('square')
plt.axis((-3,3,-3,3))
plt.grid()
plt.show()
