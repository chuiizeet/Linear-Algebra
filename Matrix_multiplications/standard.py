import math
import numpy as np

m = 4
n = 3
k = 6

A = np.random.randn(m,n)
B = np.random.randn(n,k)
C = np.random.randn(m,k)

np.matmul(A,B)
# np.matmul(A,A)
np.matmul(np.matrix.transpose(A),C)
np.matmul(B,np.matrix.transpose(B))
np.matmul(np.matrix.transpose(B),B)
# np.matmul(B,C)
# np.matmul(C,B)
# np.matmul(np.matrix.transpose(C),B)
np.matmul(C,np.matrix.transpose(B))
