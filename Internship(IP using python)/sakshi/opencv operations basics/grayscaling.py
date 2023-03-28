
import cv2


# Read First Image
img1 = cv2.imread('images\ladybug.jpg')
cv2.imshow('Original image', img1)
cv2.waitKey(0)

img2=cv2.imread('images\ladybug.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Grayscaled image', img2)
cv2.waitKey(0)

cv2.destroyAllWindows()


# note: for grayscaling a photo just add cv2.IMREAD_GRAYSCALE
