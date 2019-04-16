import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

S1 = np.array([1, 1, 0])
S2 = np.array([1, 7, 0])

v = np.array([1, 2, 0])
w = np.array([3, 2, 1])

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot([0, S1[0]],[0, S1[1]],[0, S1[2]],'r')
ax.plot([0, S2[0]],[0, S2[1]],[0, S2[2]],'r')

ax.plot([0, v[0]],[0, v[1]],[0, v[2]],'k')
ax.plot([0, w[0]],[0, w[1]],[0, w[2]],'b')

xx, yy = np.meshgrid(range(30), range(30))
cp = np.cross(S1,S2)
z1 = (-cp[0]*xx - cp[1]*yy)*1./cp[2]
ax.plot_surface(xx,yy,z1, cmap='winter_r')

plt.show()
