import numpy as np

z = np.complex(3,4)

print( np.linalg.norm(z) )
print( np.transpose(z)*z )
print( np.transpose(z.conjugate())*z )

v = np.array( [ 3, 4j, 5+2j, np.complex(2,-5) ] )

print( v.T )
print( np.transpose(v) )
print( np.transpose(v.conjugate()) )
