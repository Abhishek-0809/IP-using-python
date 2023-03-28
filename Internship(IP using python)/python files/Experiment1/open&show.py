# Import required library
import cv2

# Open Image
im = cv2.imread("images\Dogs.jpg")

# Show Image
cv2.imshow('Title: Dog', im)
cv2.waitKey(0)

# GrayScale
im_gray = cv2.imread("images\Dogs.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow('Title: Dog', im_gray)
cv2.waitKey(0)
