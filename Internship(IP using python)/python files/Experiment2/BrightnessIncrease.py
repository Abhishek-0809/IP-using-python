# Brightness Manipulation - Increase
from PIL import Image

img = Image.open("images\Baboon.jpg")
im_gray = img.convert('L')


row, col = im_gray.size
for i in range(row):
    for j in range(col):
        IMAGE = im_gray.getpixel((i, j))
       
        temp = IMAGE+20
        if temp>255:
            out = 255
        else:
            out=temp
        im_gray.putpixel((i, j), out)
im_gray.show()
