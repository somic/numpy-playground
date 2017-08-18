#!/usr/bin/env python
#
# Generate 2d array (gen1_*) with specified values (see URL below)
# and another array (gen2) containing its 2nd and 4th rows
# http://www.scipy-lectures.org/intro/numpy/exercises.html

import numpy as np

row1 = np.cumsum(np.array([1, 5, 5])) # [ 1 6 11 ]

# solution 1
row1_1 = row1.copy()
gen1_1 = row1.copy()
for i in range(1, 5):
  gen1_1 = np.append(gen1_1, row1_1 + i * np.ones(3, np.int))
gen1_1 = gen1_1.reshape((5, 3))
print gen1_1; print

# solution 2
row1_2 = row1.copy()
gen1_2 = np.repeat(np.arange(5), 3).reshape((5, 3)) + row1_2
print gen1_2; print
assert np.array_equal(gen1_1, gen1_2)

gen2_1 = gen1_1[np.array([1,3])]
print gen2_1; print

"""
Output:

[[ 1  6 11]
 [ 2  7 12]
 [ 3  8 13]
 [ 4  9 14]
 [ 5 10 15]]

[[ 1  6 11]
 [ 2  7 12]
 [ 3  8 13]
 [ 4  9 14]
 [ 5 10 15]]

[[ 2  7 12]
 [ 4  9 14]]

"""
