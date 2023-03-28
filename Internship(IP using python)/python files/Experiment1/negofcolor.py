# NEGATIVE IMAGE
from PIL import Image

img = Image.open("images\Dogs.jpg")

row, col = img.size
for i in range(row):
    for j in range(col):
        r, g, b = img.getpixel((i, j))
        r = 255-r
        g = 255-g
        b = 255-b
        img.putpixel((i, j), (r, g, b))
img.show()
