import numpy as np

m = 4

# matrices
N = np.round( 10*np.random.randn(m,m) )
S = np.round( np.matrix.transpose(N)*N/m**2 )

# vector
w = np.array([-1, 0, 1, 2])


print(S@w)
np.matrix.transpose(S@w)
print(w@S)
np.matrix.transpose(w)@np.matrix.transpose(S)
np.matrix.transpose(w)@S


# with nonsymmetric matrix
print(N@w)
np.matrix.transpose(N@w)
print(w@N)
np.matrix.transpose(w)@np.matrix.transpose(N)
np.matrix.transpose(w)@N
