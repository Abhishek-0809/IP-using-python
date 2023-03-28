from PIL import Image, ImageOps

# In the ImageOps module of the Python image processing library Pillow (PIL), invert() for negative-positive inverting (inverting pixel values) of an image is provided.

img=Image.open('images\ladybug.jpg')
img.show()
x,y=img.size
print(x,y)

neg=ImageOps.invert(img)
neg.show()

gray=img.convert('L')
gray.show()

neg_gray=ImageOps.invert(gray)
neg_gray.show()




