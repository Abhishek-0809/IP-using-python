import cv2
import matplotlib.pyplot as plt

imgpath = 'images\Dogs.jpg'
img = cv2.imread(imgpath)

# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

gray = cv2.imread(imgpath, 0)

colored_negative = abs(255-img)
gray_negative = abs(255-gray)

# imgs = [img, gray, colored_negative, gray_negative]
# title = ['coloured', 'gray', 'coloured-negative', 'gray-negative']

plt.subplot(2, 2, 1)
plt.title('color')
plt.imshow(img)

plt.subplot(2, 2, 2)
plt.title('gray')
plt.imshow(gray)

plt.subplot(2, 2, 3)
plt.title('negative')
plt.imshow(colored_negative)

plt.subplot(2, 2, 4)
plt.title('gray_neg')
plt.imshow(gray_negative)

plt.show()
