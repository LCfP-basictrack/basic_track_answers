import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, -5, 6])

a_dot_b = np.dot(a, b)
print(a_dot_b)

a = np.array([a, [7, 8, 9], [10, 11, 12]])
a_prod_b = np.inner(a, b)
print(a_prod_b)

