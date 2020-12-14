import cv2
import numpy as np
import pytesseract
import matplotlib.pyplot as plt
from PIL import Image

img = cv2.imread("ktp.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
th, threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
result = pytesseract.image_to_string((threshed), lang="ind")
print(result)

cv2.imshow("gray", gray)
cv2.imshow("threshed", threshed)
cv2.waitKey(delay=0)