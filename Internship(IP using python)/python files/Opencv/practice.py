# Step 1 – Import libraries.
import cv2
import matplotlib.pyplot as plt

# Step 2 – Let’s read the image.
imgpath = 'images\Dogs.jpg'
img = cv2.imread(imgpath)
cv2.imshow('BGR IMAGE', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# plt.subplot(1, 2, 1)
# plt.title('DEFAULT')
# plt.imshow(img)

# plt.show()
