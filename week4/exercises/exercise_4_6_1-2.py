import numpy as np

my_vector = np.array([5, 8, 9, 6, 3, 2, 1, 4, 7])
my_bi_dimensional_array = np.array([[1, 2], [3, 4], [8, 7], [6, 5]])

print(my_vector[-3])
print(my_bi_dimensional_array[-1, -2])
# a negative index starts at the back instead of the front

print("lengths:", len(my_vector), len(my_bi_dimensional_array))
print("sizes:", my_vector.size, my_bi_dimensional_array.size)
print("shapes:", my_vector.shape, my_bi_dimensional_array.shape)
print("dimensions:", my_vector.ndim, my_bi_dimensional_array.ndim)
