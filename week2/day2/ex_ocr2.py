import cv2
import easyocr
import numpy as np
import matplotlib.pyplot as plt

img_org = cv2.imread('./img/car1.png')
height, width, channel = img_org.shape
print(height, width, channel)
#plt.imshow(img_org)
#plt.show()

gray = cv2.cvtColor(img_org, cv2.COLOR_BGR2GRAY)
#plt.imshow(gray)
#plt.show()
img_blurred = cv2.GaussianBlur(gray, ksize=(5,5), sigmaX=0)
#plt.imshow(img_blurred)
#plt.show()
img_thresh = cv2.adaptiveThreshold(img_blurred, maxValue=255.0, adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   thresholdType=cv2.THRESH_BINARY_INV,
                                   blockSize=19,
                                   C=9)
plt.imshow(img_thresh, cmap='gray')
plt.show()
reader = easyocr.Reader(['en','ko'])
result = reader.readtext(img_thresh)
for bbox, text, prob in result:
    print(result)