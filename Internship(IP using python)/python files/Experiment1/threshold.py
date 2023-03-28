#Threshold

from PIL import Image

img = Image.open("images\Dogs.jpg")
im_gray = img.convert('L')

row, col = im_gray.size
for i in range(row):
    for j in range(col):
        IMAGE = im_gray.getpixel((i, j))
        if IMAGE<150:
            Th = 0
        else:
            Th = 255    
        im_gray.putpixel((i, j), Th)
im_gray.show()