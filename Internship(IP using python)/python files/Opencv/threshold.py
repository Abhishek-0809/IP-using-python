# Step 1 – Import libraries.
import cv2
import matplotlib.pyplot as plt

# Step 2 – Let’s read the image.
imgpath = 'images\Dogs.jpg'
img = cv2.imread(imgpath)
# cv2.imshow('BGR IMAGE', img)
plt.subplot(3, 2, 1)
plt.title('DEFAULT')
plt.imshow(img)

# Step 3 – Convert the image to RGB
# Here we are just converting the image from BGR to RGB because cv2 reads the image in BGR format by default.That’s why we need to convert it back to RGB format.
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cv2.imshow('RGB IMAGE', img)
plt.subplot(3, 2, 2)
plt.title('BGR TO RGB')
plt.imshow(img)


# Step 4 – Let’s read the image in grayscale also.
gray = cv2.imread(imgpath, 0)
# cv2.imshow('GRAY IMAGE', gray)
plt.subplot(3, 2, 3)
plt.title('GRAY')
plt.imshow(gray)
# We are also reading the image in grayscale mode to generate its negative.

# Step 5 – Lets generate the negative image.
# Algorithm of finding the negative:
# Get the red green blue values of each pixel.
# Subtract each color value from 255 and save them as new color values.
# Create a new pixel value from the modified colors.
# set the new value to the pixel.

img2 = cv2.imread(imgpath)
colored_negative = abs(255-img2)
# cv2.imshow('COLORED NEGATIVE IMAGE', colored_negative)
plt.subplot(3, 2, 4)
plt.title('NEGATIVE')
plt.imshow(colored_negative)

gray_negative = abs(255-gray)
# cv2.imshow('GRAY NEGATIVE IMAGE', gray_negative)
plt.subplot(3, 2, 5)
plt.title('GRAY NEGATIVE')
plt.imshow(gray_negative)

plt.show()

# cv2.waitKey(0)
# cv2.destroyAllWindows()
