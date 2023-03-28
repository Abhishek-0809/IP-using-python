# Import required library
from PIL import Image

# Open Image
im = Image.open("images\Dogs.jpg")
im2 = Image.open("images\pug dog.png")
im3 = Image.open("images\\flower.png")
im4 = Image.open("images\women.png")

# Show Image
im.show()
im2.show()
im3.show()
im4.show()

# Rotate Image
im.rotate(180).show()
