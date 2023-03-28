# Brightness Manipulation - Decrease
from PIL import Image

img = Image.open("images\Baboon.jpg")
im_gray = img.convert('L')


row, col = im_gray.size
for i in range(row):
    for j in range(col):
        IMAGE = im_gray.getpixel((i, j))
       
        temp = IMAGE-100
        if temp<0:
            out = 0
        else:
            out=temp
        im_gray.putpixel((i, j), out)
im_gray.show()
