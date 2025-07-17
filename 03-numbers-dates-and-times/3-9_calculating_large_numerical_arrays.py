# Numpy arrays
import numpy as np
ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])
print(ax * 2)

print(ax + 10)

print(ax + ay)

print(ax * ay)

def test_function(x):
    return 3*x**2 - 2*x + 7

print(test_function(ax))

# Universal Function with np

print(np.sqrt(ax))
print(np.cos(ax))

grid = np.zeros(shape=(10000,10000), dtype=float)

grid += 10
print(grid)