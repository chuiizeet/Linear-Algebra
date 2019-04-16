import numpy as np

S = np.random.randn(5,5)
R = np.random.randn(5,2)
print(R)

# identity
I = np.eye(3)
print(I)

# zeros
Z = np.zeros((4,4))
print(Z)

# diagonal
D = np.diag([ 1, 2, 3, 5, 2 ])
print(D)

# create triangular matrix from full matrices
S = np.random.randn(5,5)
U = np.triu(S)
L = np.tril(S)
print(L)

# concatenate matrices (sizes must match!)
A = np.random.randn(3,2)
B = np.random.randn(3,2)
C = np.concatenate((A,B),axis=1)
print(C)
