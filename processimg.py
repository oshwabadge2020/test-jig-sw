
# -*- coding: utf-8 -*-
import qrtools
import cv2
import numpy as np
import sys

imgPath = sys.argv[1]

img = cv2.imread(imgPath, 0)
kernel = np.ones((5, 5), np.uint8)
processed=cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
ret,thresh1 = cv2.threshold(processed,60,255,cv2.THRESH_BINARY)
cv2.imwrite('processed.png', thresh1)
