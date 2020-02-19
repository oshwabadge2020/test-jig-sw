# -*- coding: utf-8 -*-
import qrtools
import cv2
import numpy as np
import sys
import imutils

imgPath = sys.argv[1]

# Open up our input image
img_ur = cv2.imread(imgPath,  cv2.IMREAD_UNCHANGED)

# Camera is sligly rotated, correct.
img = imutils.rotate(img_ur,2.5)

# Crop out screen
cropped = img[294:626, 851:1164]

# Greyscale it
grayscaled = cv2.cvtColor(cropped,cv2.COLOR_BGR2GRAY)

#Threshold out the QR so zimage doesn't choke
th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imwrite('processed.png', th)
