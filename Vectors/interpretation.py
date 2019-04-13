# Vector: An ordered list of numbers
# Dimensionality: The number of numbers

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

v2 = [ 3, -2 ]

v3 = [ 4, -3, 2 ]

v3t = np.transpose(v3)

plt.plot([0,v2[0]],[0,v2[1]])
plt.axis('equal')
plt.plot([-4, 4],[0, 0],'k--')
plt.plot([0, 0],[-4, 4],'k--')
plt.grid()
plt.axis((-4, 4, -4, 4))
plt.show()

# plot the 3D vector
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot([0, v3[0]],[0, v3[1]],[0, v3[2]])

# make the plot look nicer
plt.axis('equal')
ax.plot([0, 0],[0, 0],[-4, 4],'k--')
ax.plot([0, 0],[-4, 4],[0, 0],'k--')
ax.plot([-4, 4],[0, 0],[0, 0],'k--')
plt.show()
