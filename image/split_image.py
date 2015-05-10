#!/usr/bin/env python

import cv2
import numpy

img = cv2.imread("akhead.png")
b, g, r = cv2.split(img)
cv2.imshow("Blue", r)
cv2.imshow("Red", g)
cv2.imshow("Green", b)
cv2.waitKey(0)
cv2.destroyAllWindows()
