
# This is for how to read, write and show images in opencv


import cv2

# #to display image in color
img = cv2.imread('images\countryside.jpg', 1)
img = cv2.imread('images\countryside.jpg', cv2.IMREAD_COLOR)

# # to display image in grayscale
# img = cv2.imread('images\countryside.jpg', 0)
# img = cv2.imread('images\countryside.jpg', cv2.IMREAD_GRAYSCALE)

# to display image as it is or show the alpha channel
# img = cv2.imread('images\countryside.jpg', -1)
# img = cv2.imread('images\countryside.jpg', cv2.IMREAD_UNCHANGED)


print(img)  # prints the output in the form of matrix
cv2.imshow('Image', img)
# after this execution the image is shown for a millisecond
k = cv2.waitKey(0)


# a copy of the image is created using the write method
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('images\countryside_copy.jpg', img)
