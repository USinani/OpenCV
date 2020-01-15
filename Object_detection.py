import cv2, numpy as np

img = cv2.imread('pentagon.jpg')
# convert colored image to grayScale value
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# convert colored imate to HSV scale
hsvScale = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# show the output
cv2.imshow('grayscale Image', grayImg)
cv2.imshow('HSV scale', hsvScale)
# def approxPolyDP(curve, epsilon, closed, approxCurve)
approximate = cv2.approxPolyDP()
x = approximate.ravel()[]

cv2.waitKey()
cv2.destroyAllWindows()
