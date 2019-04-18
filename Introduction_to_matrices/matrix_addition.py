import numpy as np

A = np.random.randn(5,4)
B = np.random.randn(5,4)
C = np.random.randn(5,4)

A+B
A+C

l = .3 # lambda
N = 5  # size of square matrix
D = np.random.randn(N,N)

Ds = D + l*np.eye(N)
print(Ds)
