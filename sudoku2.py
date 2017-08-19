#!/usr/bin/env python

import numpy as np

all_digits = np.arange(1,10)

def possible_candidates(a):
  z = np.ones_like(all_digits)
  z.put(a-1, np.zeros_like(a))
  r = all_digits * z
  return r.take(r.nonzero()).flatten()

assert np.array_equal(possible_candidates(np.array([4])),
  np.array([1, 2, 3, 5, 6, 7, 8, 9]))
assert np.array_equal(possible_candidates(np.array([2, 5, 9])),
  np.array([1, 3, 4, 6, 7, 8]))


def solve(a):
  print possible_candidates(np.array([3]))
  return 'FIXME'

if __name__ == '__main__':
  inp = np.array([
    0, 0, 6, 0, 0, 4, 0, 5, 0,
    0, 0, 0, 9, 5, 0, 0, 7, 0,
    5, 7, 0, 0, 0, 0, 4, 0, 9,
    0, 0, 5, 0, 4, 0, 0, 0, 3,
    0, 6, 0, 0, 0, 2, 1, 8, 0,
    4, 9, 0, 8, 0, 6, 0, 0, 0,
    7, 0, 0, 0, 8, 0, 0, 6, 2,
    2, 0, 9, 7, 0, 0, 0, 0, 0,
    0, 0, 3, 0, 0, 5, 9, 0, 7], np.int).reshape((9,9))
  sol = solve(np)
  print 'Solved:', sol
