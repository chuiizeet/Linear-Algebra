# many ways to compute the dot product
import numpy as np

v1 = np.array([ 1, 0, 2, 5, -2 ])
v2 = np.array([ 2, 8, -6, 1, 0 ])

# method 1
dp = sum( np.multiply(v1,v2) )

# method 2
dp = np.dot( v1,v2 )

# method 3
dp = np.matmul( v1,v2 )

# method 4
dp = 0  # initialize

for i in range(0,len(v1)):

    dp = dp + v1[i]*v2[i]

print(dp)
