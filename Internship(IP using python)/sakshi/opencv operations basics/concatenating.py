
import cv2
# import numpy as np


# Read First Image
img1 = cv2.imread('images\countryside.jpg')

# Read Second Image
img2 = cv2.imread('images\countryside.jpg')


#Concatenating both the images
# v_img=cv2.vconcat([img1,img2])
h_img = cv2.hconcat([img1, img2])


cv2.imshow('Horizontal', h_img)
# cv2.imshow('Vertical',v_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# DOUBT- DONO  alag IMAGES CONCATENATE NAHI HO RAHE HAI