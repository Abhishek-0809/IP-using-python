# import required library
from PIL import Image

# Open Image
im = Image.open("images\women.png")

# Print Iimage Details
print(im)

print(im.size)

print(im.format)

# We can change the format of image from one form to another, like below. Now if we see the folder, we have same image in two different formats.

im.save("images\women.jpg")

# Resize-thumbnails() - We can change the size of image using thumbnail() method of pillow
im.thumbnail((900, 150))
im.show()
