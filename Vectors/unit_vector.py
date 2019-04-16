import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

v1 = np.array([ -3, 6 ])
mu = 1/np.linalg.norm(v1)
v1n = v1*mu

plt.plot([0, v1[0]],[0, v1[1]],'g',label='v1')
h=plt.plot([0, v1n[0]],[0, v1n[1]],'r',label='v1-norm')
plt.setp(h,linewidth=5)

plt.axis('square')
plt.axis(( -6, 6, -6, 6 ))
plt.grid()
plt.legend()
plt.show()
