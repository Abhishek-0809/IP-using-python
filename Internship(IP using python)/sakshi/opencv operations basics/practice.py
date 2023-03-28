import cv2
# image = cv2.imread('images\countryside.jpg')
# cv2.namedWindow('Normal Window', cv2.WINDOW_NORMAL)
# cv2.imshow('Normal Window', image)
# cv2.waitKey(0)

image= cv2.imread('images\countryside.jpg')
scale_percent =100 # percent of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resize", resized)
cv2.waitKey(0)