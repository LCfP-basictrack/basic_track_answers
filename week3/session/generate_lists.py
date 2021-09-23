squares = []
length_of_list = 101

for side in range(length_of_list):
    squares.append(side ** 2)

cubes = [side ** 3 for side in range(length_of_list)]

for index, (square, cube) in enumerate(zip(squares, cubes)):
    print("{:3} {:5} {:^7}".format(index, square, cube))
