#!/usr/bin/env python

import cv2
import numpy

def salt(img, n):
    for k in range(n):
        i = int(numpy.random.random() * img.shape[0])
        j = int(numpy.random.random() * img.shape[1])
        if img.ndim == 2:
            img[i, j] = 255
        elif img.ndim == 3:
            for kk in range(3):
                img[i, j, kk] = 255

    return img

if __name__ == '__main__':
    img = cv2.imread("akhead.png")
    saltImage = salt(img, 500)
    cv2.imshow("Salt", saltImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()