import numpy as np

v1 = np.array([  1, 2, 3 ])
v2 = np.array([ -1, 0, 1 ])

# outer product
np.outer(v1,v2)

# manual
op = np.zeros((len(v1),len(v1)))
for i in range(0,len(v1)):
    for j in range(0,len(v2)):
        op[i,j] = v1[i] * v2[j]

print(op)
