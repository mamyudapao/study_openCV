import numpy as np
import cv2 as cv

img = cv.imread('messi5.jpg')

res = cv.resize(img, None, fx=2, fy=2)

cv.imshow('converted', res)
k = cv.waitKey(0)
