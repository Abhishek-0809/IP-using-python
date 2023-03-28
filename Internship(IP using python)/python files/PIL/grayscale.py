# GrayScale

#  Import required libraries
from PIL import Image

# Open Image
im = Image.open("images\Dogs.jpg")
im2 = Image.open("images\pug dog.png")
im3 = Image.open("images\\flower.png")
im4 = Image.open("images\women.png")

# GrayScale and Show
im_gray = im.convert('L').show()
im2_gray = im2.convert('L').show()
im3_gray = im3.convert('L').show()
im4_gray = im4.convert('L').show()
# Where "L" stands for 'luminous'.
