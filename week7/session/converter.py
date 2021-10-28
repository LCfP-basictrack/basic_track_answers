from PIL import Image
import numpy as np


def convert_color_to_grey(image):
    pixels = np.array(image, dtype='uint8')
    new_pix = [[(sum(pixels[row, col]) / 3) for col in range(pixels.shape[1])] for row in range(pixels.shape[0])]
    new_image = Image.fromarray(np.array(new_pix, dtype='uint8'))
    return new_image


def fade_and_shift_bw(image):
    pixels = np.array(image, dtype='uint8')
    pixels //= 4
    pixels += 80
    new_image = Image.fromarray(np.array(pixels, dtype='uint8'))

    return new_image


if __name__ == "__main__":
    im = Image.open("fruit.jpg")
    im = convert_color_to_grey(im)
    # im = fade_and_shift_bw(im)
    im.save("fruit.png", "PNG")
    im = Image.open("Tuscany_Landscape_Volterra_Italy_Landscape_Photography_(158574951).jpeg")
    im = convert_color_to_grey(im)
    # im = fade_and_shift_bw(im)
    im.save("tuscany_landscape.png", "PNG")
