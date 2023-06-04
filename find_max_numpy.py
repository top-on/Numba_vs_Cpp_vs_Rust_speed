import time

import numpy as np
from numba import njit


@njit
def find_max(a, b):
    print(len(a), len(b))
    return np.outer(a, b).max()


a = np.array([])
b = np.array([])
for i in range(20000):
    a = np.append(a, 0.5)
    b = np.append(b, 0.4)

arr = np.array([])
for i in range(10):
    t0 = time.time()
    find_max(a, b)
    t1 = time.time()
    t2 = (t1 - t0) * 1000
    print(f'Time taken: {t2} milliseconds')
    arr = np.append(arr, t2)
print(f'Array List: {arr}')
print(f'Average of the array: {np.average(arr)}')
print(f'Array List: {arr}')
print(f'Average of the array: {np.average(arr)}')
