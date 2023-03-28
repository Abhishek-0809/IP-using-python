from PIL import Image

img=Image.open('images\ladybug.jpg')
# img.show()


# Splitting of the modes of the image 
red, green, blue = img.split()
print(img.mode)
print(red.mode)
print(green.mode)
print(blue.mode)

new_img1=Image.merge('RGB',(blue,green,red))
new_img1.show()

new_img2=Image.merge('RGB',(blue,red,green))
new_img2.show()

new_img3=Image.merge('RGB',(green,blue,red))
new_img3.show()

new_img4=Image.merge('RGB',(red,green,blue))

# Different variations in the modes of the image 
new_img4.show()
# print(new_img)