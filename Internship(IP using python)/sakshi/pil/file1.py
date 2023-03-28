from PIL import Image

img=Image.open('images\countryside.jpg')
img.show()
# The .show() method saves the image as a temporary file and displays it using your operating system’s native software for dealing with images.

print(img.size)   #The size shows the width and height of the image in pixels.
print(img.format) #The format of an image shows what type of image you’re dealing with.
print(img.mode)   #The mode of this image is 'RGB'