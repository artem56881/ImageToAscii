from io import StringIO

import PIL.Image
import random

def avg_color(colors):
    red, green, blue = 0, 0, 0
    for i in colors:
        red += i[0]
        green += i[1]
        blue += i[2]
    red //= len(colors)
    green //= len(colors)
    blue //= len(colors)
    return red, green, blue


def color_to_grayscale(color):
    gray_color = color[0] + color[1] + color[2]
    gray_color //= 3
    return gray_color, gray_color, gray_color


def get_random(color):
    rand_range = 50
    return color[0]+random.randint(0, rand_range), color[1]+random.randint(0, rand_range), color[2]+random.randint(0, rand_range)


def apply_effect(img: PIL.Image, effect):
    nX, nY = img.size[0], img.size[1]

    NewImage = PIL.Image.new('RGB', (nX, nY), color='white')

    for x in range(nX):
        for y in range(nY):
            newAvg_color = effect(img.getpixel((x, y)))
            NewImage.putpixel((x, y), newAvg_color)
    return NewImage


def shrink_values(value: int, range1: int, range2: int):
    return round((range2/range1)*value)

def color_to_alphabet(color, alphabet, max_color=255):
    index = shrink_values(color[0], max_color, len(alphabet)-1)
    return alphabet[index]

def ascii_art(png_image: PIL.Image,  scale=2, alphabet="▁▂▃▄▅▆▇█"):
    imgX = png_image.size[0]
    imgY = png_image.size[1]
    for y in range(0, imgY - 3, 3 * scale):
        for x in range(0, imgX - 2, 2 * scale - 2):
            colors = [png_image.getpixel((x, y)), png_image.getpixel((x + 1, y)), png_image.getpixel((x, y + 1)),
                      png_image.getpixel((x + 1, y + 1)), png_image.getpixel((x, y + 2)), png_image.getpixel((x + 1, y + 2))]
            new_avg_color = avg_color(colors)
            print(color_to_alphabet(new_avg_color, alphabet), end='')
        print()

# braille_alphabet = "▁▂▃▄▅▆▇█"
braille_alphabet = "⠈⠐⠠⠉⠑⠡⠃⠅⠉⠊⠒⠢⠌⠔⠤⠇⠕⠥⠆⠎⠖⠦⠧⠏⠍⠇⠗⠨⠙⠪⠬⠭⠛⠝⠮⠟⠛⠜⠝⠯⠳⠴⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿"
# braille_alphabet = " .,aA"

img = PIL.Image.open("./image.png")


ascii_art(img, alphabet=braille_alphabet, scale=4)