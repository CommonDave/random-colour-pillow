from PIL import Image, ImageDraw
import random

width = random.randint(1, 500)
height = random.randint(1,500)
red = random.randint(1, 255)
blue = random.randint(1, 255)
green = random.randint(1, 255)
name = random.randint(1, 999999999999)

size = str(width) + ", " + str(height)
colour = str(red) + ", " + str(green) + ", " + str(blue)

img = Image.new('RGB', (width, height))
