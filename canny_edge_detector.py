import cv2, numpy as np

def nothing(x):
    pass

# create image window
cv2.namedWindow('image')

# create trackbars for threshold()
cv2.createTrackbar('thresh', 'image', 1, 255, nothing)
cv2.createTrackbar('maxval', 'image', 1, 255, nothing)
# create trackbars for Canny()
cv2.createTrackbar('threshOne', 'image', 1, 255, nothing)
cv2.createTrackbar('threshTwo', 'image', 1, 255, nothing)

# main camera input
input_scr = cv2.VideoCapture(0)

while True:

    # read captured frames
    src_flag, src_frames = input_scr.read()
    # convert captured frames to gray scale
 
    # Canny() trackbar input values
    thresh1 = cv2.getTrackbarPos('threshOne', 'image')
    thresh2 = cv2.getTrackbarPos('threshTwo', 'image')
    
    # canny edge detection
    canny = cv2.Canny(src_frames, thresh1, thresh2, 1)
    cv2.imshow('Canny edge detection', canny)


    if cv2.waitKey(1) & 0xFF == ord('c'):
        break

input_scr.release()
cv2.destroyAllWindows()
