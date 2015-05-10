#!/usr/bin/env python

import cv2
import numpy

img = cv2.imread("akhead.jpg")
print ("img.shape: ", img.shape)
emptyImage = numpy.zeros(img.shape, numpy.uint8)

emptyImage2 = img.copy()

emptyImage3 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# emptyImage3[...] = 0

cv2.imshow("emptyImage", emptyImage)
cv2.imshow("Image", img)
cv2.imshow("emptyImage2", emptyImage2)
cv2.imshow("emptyImage3", emptyImage3)
cv2.imwrite("./akhead2.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 5])
cv2.imwrite("./akhead3.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
cv2.imwrite("./akhead1.png", img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
cv2.imwrite("./akhead2.png", img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])

cv2.waitKey(0)
cv2.destroyAllWindows()
