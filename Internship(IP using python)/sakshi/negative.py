import cv2


img1=cv2.imread('images\ladybug.jpg')
cv2.imshow('Original image',img1)
cv2.waitKey(0)

img_size=img1.size
print(img_size)
r,c,ch=img1.shape
print(r,c,ch)


for x in range(0,r):
    for y in range(0,c):
        negative=abs(255-img1)
cv2.imshow('Final image',negative)
cv2.waitKey(0)
cv2.destroyAllWindows()
            
# import cv2
# import matplotlib.pyplot as plt
# img = cv2.imread('images\ladybug.jpg')
# cv2.imshow('Org image',img)
# cv2.waitKey(0)
# # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# # cv2.imshow('Org image',img)
# # cv2.waitKey(0)
# img2=cv2.imread('images\ladybug.jpg', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('Grayscaled image', img2)
# cv2.waitKey(0)
# colored_negative = abs(255-img)
# gray_negative = abs(255-img2)
# imgs = [img, img2, colored_negative, gray_negative]
# title = ['coloured', 'gray', 'coloured-negative', 'gray-negative']
# plt.subplot(2, 2, 1)
# plt.title(title[0])
# plt.imshow(imgs[0])
# plt.xticks([])
# plt.yticks([])
# plt.subplot(2, 2, 2)
# plt.title(title[1])
# plt.imshow(imgs[1], cmap='gray')
# plt.xticks([])
# plt.yticks([])
# plt.subplot(2, 2, 3)
# plt.title(title[2])
# plt.imshow(imgs[2])
# plt.xticks([])
# plt.yticks([])
# plt.subplot(2, 2, 4)
# plt.title(title[3])
# plt.imshow(imgs[3], cmap='gray')
# plt.xticks([])
# plt.yticks([])
# plt.show()