from __future__ import print_function
from my2darray import Array2D

ab = Array2D(8,8)

for r in range(8):
    for c in range(8):
        ab[r,c] = 0
ab[1,2] = 1
ab[1,5] = 2
ab[2,1] = 1
ab[2,2] = 1
ab[2,3] = 1
ab[2,4] = 2
ab[2,5] = 1
ab[3,2] = 1
ab[3,3] = 2
ab[3,4] = 1
ab[3,5] = 1
ab[3,6] = 1
ab[3,7] = 1
ab[4,2] = 2
ab[4,3] = 1
ab[4,4] = 1
ab[5,1] = 2
ab[5,2] = 2
ab[5,3] = 2
ab[5,4] = 2
ab[5,5] = 1
ab[6,0] = 2
ab[6,1] = 2
ab[6,3] = 1
ab[6,4] = 1
ab[6,5] = 1
ab[6,6] = 1
ab[7,0] = 2
ab[7,3] = 1
ab[7,4] = 1
for r in range(8):
    for c in range(8):
        print (ab[r,c], sep = '   ', end = '   ')
    print ('\n')

