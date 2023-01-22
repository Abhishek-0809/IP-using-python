import cv2
import numpy as np
from PIL import Image

# Read First Image
img1 = cv2.imread('images\women.jpg')

# Read Second Image
img2 = cv2.imread('images\women.jpg')

cv2.imshow('Title: Dogs', img1)
cv2.imshow('Title: PugDog', img2)

# concatanate image Horizontally
img_concate_Hori = np.concatenate((img1, img2), axis=1)

# concatanate image Vertically
img_concate_Verti = np.concatenate((img1, img2), axis=0)

cv2.imshow('concatenated_Hori', img_concate_Hori)
cv2.imshow('concatenated_Verti', img_concate_Verti)
cv2.waitKey(0)
cv2.destroyAllWindows()
