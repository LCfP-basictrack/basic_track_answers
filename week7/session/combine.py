from PIL import Image
import numpy as np

# open the image to be accessed using 'im'
im = Image.open("fruit.png")
fruit = np.array(im)

im2 = Image.open("tuscany_landscape.png")
landscape = np.array(im2)

# create a new list for the new image
for row in range(fruit.shape[0]):
    for column in range(fruit.shape[1]):
        # if fruit[row, column] > 230:
        #     fruit[row, column] = landscape[row, column]
        fruit[row, column] = landscape[row, column] - fruit[row, column]

# convert the new image to an array of 8 bit integers
# uint8 => unsigned (no negative numbers) integers of 8 bits
new_pix = np.array(fruit).astype('uint8')
# convert the array into an image
im2 = Image.fromarray(new_pix)
# show the new image
im2.show()
# im2.save("fruit_fade_2.png")
