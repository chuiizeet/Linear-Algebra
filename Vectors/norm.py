# Vector length aka magnitude/norm
import numpy as np

v1 = np.array([ 1, 2, 3, 4, 5, 6, ])
vl = np.sqrt( sum( np.multiply(v1,v1)) )
vl = np.linalg.norm(v1)

print(vl)
