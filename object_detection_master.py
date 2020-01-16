import cv2
import numpy as np


def nothing(x):
    pass

# create trackbar window
cv2.namedWindow('image', cv2.WINDOW_GUI_NORMAL)

# create trackbar
cv2.createTrackbar('maxVal', 'image', 0, 255, nothing)

# create trackbar for upper boundary color selection
cv2.createTrackbar('upperB', 'image', 0, 255, nothing)
cv2.createTrackbar('upperG', 'image', 0, 255, nothing)
cv2.createTrackbar('upperR', 'image', 0, 255, nothing)
# create trackbar for lower boundary color selection
cv2.createTrackbar('lowerB', 'image', 0, 255, nothing)
cv2.createTrackbar('lowerG', 'image', 0, 255, nothing)
cv2.createTrackbar('lowerR', 'image', 0, 255, nothing)

# main camera input
input_scr = cv2.VideoCapture(0)

while True:

    # read captured frames
    src_flag, src_frames = input_scr.read()
    # convert captured frames to gray scale
    gray_scale = cv2.cvtColor(src_frames, cv2.COLOR_BGR2GRAY)
    # convert to HSV color space
    hsv = cv2.cvtColor(src_frames, cv2.COLOR_BGR2HSV)

    # get trackbar position for upper boundary color
    upper_B = cv2.getTrackbarPos('upperB', 'image')
    upper_G = cv2.getTrackbarPos('upperG', 'image')
    upper_R = cv2.getTrackbarPos('upperR', 'image')
    upper_boundary = np.array([upper_B,upper_G,upper_R])

    # get trackbar position for lower boundary color
    lower_B = cv2.getTrackbarPos('lowerB', 'image')
    lower_G = cv2.getTrackbarPos('lowerB', 'image')
    lower_R = cv2.getTrackbarPos('lowerB', 'image')
    lower_boundary = np.array([lower_B,lower_G,lower_R])

    # apply inRange ()
    in_range = cv2.inRange(src=hsv, lowerb=lower_boundary, upperb=upper_boundary)
    
    # apply findContours()
    find_contours, hierarchy = cv2.findContours(image = gray_scale, 
    mode = cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
    
    # get trackbar value for max_val
    max_val = cv2.getTrackbarPos('maxVal', 'image')
    
    # apply adaptive threshold
    cv2.adaptiveThreshold(src=in_range, maxValue=max_val, 
    adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C, thresholdType=cv2.THRESH_BINARY, blockSize=3, C=5)
    # draw contours
    draw_contours = cv2.drawContours(image=src_frames, 
    contours=find_contours, contourIdx = -1, color = (255,0,0), thickness= 1 )
    
    
    print('find contours', find_contours)
    cv2.imshow('captured frames', src_frames)
    # Converter frames
    cv2.imshow('Converted frames', draw_contours)


    if cv2.waitKey(1) & 0xFF == ord('c'):
        break

input_scr.release()
cv2.destroyAllWindows()
