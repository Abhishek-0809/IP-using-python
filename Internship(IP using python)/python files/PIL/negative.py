# NEGATIVE IMAGE
from PIL import Image

img = Image.open("images\Dogs.jpg")

w, h = img.size
for i in range(w):
    for j in range(h):
        r, g, b = img.getpixel((i, j))
        r = 255-r
        g = 255-g
        b = 255-b
        img.putpixel((i, j), (r, g, b))
img.show()
