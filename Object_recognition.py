import cv2
import numpy as np

''' image --> grayscale--> threshold[retval, thresh] -->
 findContours[contours, hierarchy] -->drawContours-->
    imshow
'''
def nothing(x):
    pass

img = cv2.imread('shapes.png', 1)
# CreatedImg = np.zeros((512,600,3), np.uint8)
# createTrackbar(trackbarName, windowName, value, count, onChange)
cv2.namedWindow('Trackbars')
font = cv2.FONT_HERSHEY_COMPLEX

#while True:
# get current positions of four trackbars
cv2.createTrackbar('R', 'image', 0, 127, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 10, nothing)
# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)
# getTrackbarPos(trackbarname, winname)
r = cv2.getTrackbarPos('R','image')
g = cv2.getTrackbarPos('G','image')
b = cv2.getTrackbarPos('B','image')
s = cv2.getTrackbarPos(switch,'image')

grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#retval, thresh = cv2.threshold(grayImg, 127,255,0 )
retval, thresh = cv2.threshold(grayImg, r, g, cv2.THRESH_BINARY)
cv2.imshow('thresh', thresh )
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE )
drawContours = cv2.drawContours(img, contours, -1, (0, 0, 255), 5)

for cnt in contours:

    area = cv2.contourArea(cnt)
    # def approxPolyDP(curve, epsilon, closed, approxCurve)
    approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
    x = approx.ravel()[0]
    y = approx.ravel()[1]

    if area > 400:
        cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)

        if len(approx) == 3:
            cv2.putText(img, "Triangle", (x, y), font, 1, (0, 0, 0))
        elif len(approx) == 4:
            cv2.putText(img, "Rectangle", (x, y), font, 1, (0, 0, 0))
        elif 10 < len(approx) < 20:
            cv2.putText(img, "Circle", (x, y), font, 1, (0, 0, 0))

    cv2.imshow('contours', drawContours)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''
    if s==0:
        img[:] = 0
    else:
        img[:] = [b,g,r]
'''
#img.release()
cv2.destroyAllWindows()
