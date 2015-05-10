#!/usr/bin/env python

import cv2

img = cv2.imread("akhead.jpg")
cv2.namedWindow("akhead")
cv2.imshow("akhead", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
