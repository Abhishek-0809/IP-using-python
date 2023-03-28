# Contrast Stretching
# R1 > S1  and  R2 < S2

from PIL import Image

img = Image.open("images\Baboon.jpg")
im_gray = img.convert('L')

R1 = int(input("Enter R1 "))
R2 = int(input("Enter R2 "))

S1 = int(input("Enter S1 "))
S2 = int(input("Enter S2 "))

row, col = im_gray.size
for i in range(row):
    for j in range(col):
        IMAGE = im_gray.getpixel((i, j))
       
        if IMAGE < R1: 
            out = round((S1/R1)* IMAGE) #Section1
        elif IMAGE>R2:
            out = round((((255-S2)/(255-R2))* (IMAGE-R2)) + S2)  #Section3
        else:
            out = round((((S2-S1)/(R2-R1))* (IMAGE-R1)) + S1)  #Section2
        im_gray.putpixel((i, j), out)
im_gray.show()
