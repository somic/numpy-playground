#!/usr/bin/env python

import numpy as np

def is_solved(r):
  assert r.shape == (9,9), 'must by 9x9 2D sudoku'
  assert r.min() == 1, 'min must be 1'
  assert r.max() == 9, 'max must be 9'
  expected_sum = np.arange(1, len(r)+1).sum()

  for axis in range(r.ndim):
    s = r.sum(axis=axis)
    if s.ptp() != 0 or s.max() != expected_sum: return False

  for i in range(3):
    for j in range(3):
      _is = np.repeat(np.arange(3*i, 3+3*i), 3).reshape((3, 3))
      _js = np.ones((3, 3), np.int) * np.arange(3*j, 3*j+3)
      _r = r[_is, _js]
      if _r.sum() != expected_sum: return False

  return True

ex1 = np.array([
  [2, 9, 5, 7, 4, 3, 8, 6, 1],
  [4, 3, 1, 8, 6, 5, 9, 2, 7],
  [8, 7, 6, 1, 9, 2, 5, 4, 3],
  [3, 8, 7, 4, 5, 9, 2, 1, 6],
  [6, 1, 2, 3, 8, 7, 4, 9, 5],
  [5, 4, 9, 2, 1, 6, 7, 3, 8],
  [7, 6, 3, 5, 2, 4, 1, 8, 9],
  [9, 2, 8, 6, 7, 1, 3, 5, 4],
  [1, 5, 4, 9, 3, 8, 6, 7, 2]], np.int)
print ex1
assert is_solved(ex1)
print 'OK (solved)'

ex2 = ex1.copy()
ex2.itemset((3,4), 2)
print ex2
assert not is_solved(ex2)
print 'OK (not solved)'
