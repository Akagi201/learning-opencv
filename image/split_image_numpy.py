#!/usr/bin/env python

import cv2
import numpy

img = cv2.imread("akhead.jpg")

b = numpy.zeros((img.shape[0], img.shape[1]), dtype=img.dtype)
g = numpy.zeros((img.shape[0], img.shape[1]), dtype=img.dtype)
r = numpy.zeros((img.shape[0], img.shape[1]), dtype=img.dtype)

b[:, :] = img[:, :, 0]
g[:, :] = img[:, :, 1]
r[:, :] = img[:, :, 2]

cv2.imshow("Blue", b)
cv2.imshow("Green", g)
cv2.imshow("Red", r)

cv2.waitKey(0)
cv2.destroyAllWindows()