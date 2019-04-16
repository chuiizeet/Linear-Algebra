import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

v1  = [ -3,  2, 5 ]
v2  = [  4, -3, 0 ]

v3a = np.cross( v1,v2 )
print(v3a)

# Manual
v3b = [ [v1[1]*v2[1] - v1[2]*v2[1]],
        [v1[2]*v2[0] - v1[0]*v2[2]],
        [v1[0]*v2[1] - v1[1]*v2[0]] ]

fig = plt.figure()
ax = fig.gca(projection='3d')

xx, yy = np.meshgrid(np.linspace(-10,10,10),np.linspace(-10,10,10))
z1 = (-v3a[0]*xx - v3a[1]*yy)/v3a[2]
ax.plot_surface(xx,yy,z1)

ax.plot([0, v1[0]],[0, v1[1]],[0, v1[2]],'k')
ax.plot([0, v2[0]],[0, v2[1]],[0, v2[2]],'k')
ax.plot([0, v3a[0]],[0, v3a[1]],[0, v3a[2]],'r')


ax.view_init(azim=150,elev=45)
plt.show()
