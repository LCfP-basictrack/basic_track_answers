import numpy as np

m = int(input("Please give me a value for m "))
while m < 0:
    print("That is an invalid value for m, please provide a positive value")
    m = int(input("Please give me a value for m "))

matrix = np.array(np.zeros(m))
print("zeros\n", matrix)

matrix = np.append([matrix], [np.ones(m)], axis=0)
print("ones\n", matrix)

matrix = np.append(matrix, [np.ones(m) * 7], axis=0)
print("sevens\n", matrix)

matrix = np.append(matrix, [[10 ** n for n in range(m)]], axis=0)
print("orders of magnitude\n", matrix)

matrix = np.append(matrix, [[2 ** (n + 1) for n in range(m)]], axis=0)
print("powers of two\n", matrix)
