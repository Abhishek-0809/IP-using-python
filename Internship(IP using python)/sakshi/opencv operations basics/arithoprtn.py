
# Basic arithmetic operations

import cv2
img = cv2.imread('images\Dogs.jpg', 1)
print(img.shape)  # (rows,columns,channels)
print(img.size)  # size of the image  (total no of pixels)
print(img.dtype)  # output is datatype of the image

# b,g,r=cv2.split(img)
# # cv2.imshow('splitted',r)
# img=cv2.merge((b,g,r))
img = cv2.resize(img, (500, 400))
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
