#Gray level Slicing with background

from PIL import Image

img = Image.open("images\Dogs.jpg")
im_gray = img.convert('L')

r1 = int(input("Enter R1 "))
r2 = int(input("Enter R2 "))

row, col = im_gray.size
for i in range(row):
    for j in range(col):
        IMAGE = im_gray.getpixel((i, j))
        if IMAGE<r1:
            out = IMAGE
        elif IMAGE>r2:
            out = IMAGE 
        else:   
            out = 255    
        im_gray.putpixel((i, j), out)
im_gray.show()