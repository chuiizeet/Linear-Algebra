import numpy as np

M = np.round( 5*np.random.randn(4,4) )
d = np.diag(M)
D = np.diag(d) 
print(d)
print(D)

tr = np.trace(M)
tr2 = sum( np.diag(M) )
print(tr)
print(tr2)
