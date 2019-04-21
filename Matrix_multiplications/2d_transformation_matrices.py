import numpy as np
import math
import matplotlib.pyplot as plt

v = np.array([ 3, -2 ])
A = np.array([ [1,-1], [2,1] ])
w = A@np.matrix.transpose(v)

plt.plot([0,v[0]],[0,v[1]],label='v')
plt.plot([0,w[0]],[0,w[1]],label='Av')

plt.grid()
plt.axis((-6, 6, -6, 6))
plt.legend()
plt.title('Rotation + stretching')
plt.show()

# Pure rotation

v = np.array([ 3, -2 ])
th = 5*np.pi/24
A = np.array([ [math.cos(th),-math.sin(th)], [math.sin(th),math.cos(th)] ])
w = A@np.matrix.transpose(v)

plt.plot([0,v[0]],[0,v[1]],label='v')
plt.plot([0,w[0]],[0,w[1]],label='Av')

plt.grid()
plt.axis((-4, 4, -4, 4))
plt.legend()
plt.title('Pure rotation')
plt.show()
