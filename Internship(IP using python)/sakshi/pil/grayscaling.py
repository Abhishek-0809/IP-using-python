
# Getting bands of the image 
from PIL import Image
image = Image.open('images\ladybug.jpg')
print(image.getbands())  #RGB

# Change in the mode of the image 

# RGB TO CMYK 
cmyk_img=image.convert('CMYK')
cmyk_img.show()
# CMYK--> The abbreviation CMYK refers to the four ink plates used: cyan, magenta, yellow, and key (black).

# RGB TO GRAY 
gray_img=image.convert('L')
gray_img.show()

