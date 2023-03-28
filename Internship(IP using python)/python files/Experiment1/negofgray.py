# NEGATIVE IMAGE OF GRAYSCALE IMAGE
from PIL import Image

img = Image.open("images\Dogs.jpg")
im_gray = img.convert('L')

row, col = im_gray.size
for i in range(row):
    for j in range(col):
        neg = im_gray.getpixel((i, j))
        Negimg = 255 - neg
        im_gray.putpixel((i, j), Negimg)
im_gray.show()
