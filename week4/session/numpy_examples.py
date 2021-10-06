import numpy as np


a_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
a_numpy_array = np.asarray(a_list)

# print(a_list)
# print(a_numpy_array)

a_vector = np.array([-3, -2, -1, 0, 1, 2, 3])
# print(a_vector[-2])

a_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(a_matrix[-2, -2])

a_random_matrix = np.random.rand(33, 31)
# print(a_random_matrix)

bool_matrix = np.random.choice([False, True], size=(5, 7))
# print(bool_matrix)

a_real_random_vector = np.random.uniform(low=0, high=5, size=10)
print(a_real_random_vector)

a_guassian_surface = np.random.normal(loc=(0, 0, 0), scale=2, size=(3, 3, 3))
print(a_guassian_surface)
