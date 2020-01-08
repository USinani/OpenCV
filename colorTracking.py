import cv2
import numpy as np


class Capture():
    def __init__(self):
        self.src = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        print ('Preparing to read the frames...')
        
    def src_frames(self):
        src_flag, frames = self.src.read()
        return frames

    def src_release(self):
        self.src.release()

while True:
    src_img = Capture().src_frames()
    resize_frames = cv2.resize(src_img, (0, 0), fx = 0.75, fy = 0.75)

    cv2.imshow('frames', resize_frames)

    if cv2.waitKey(1) & 0xFF == ord('q'):
            break



# release frames
Capture().src_release()

# close windows
cv2.destroyAllWindows()

if __name__ == '__main__':
    main()


# Example
'''
import cv2
class Camera():
    def __init__(self):
        self.cap = cv2.VideoCapture(0)  # Prepare the camera...
        print("Camera warming up ...")

    def get_frame(self):
        s, img = self.cap.read()
        if s:  # frame captures without errors...
            pass
        return img

    def release_camera(self):
        self.cap.release()

def main():
   while True:
        cam1 = Camera().get_frame()
        frame = cv2.resize(cam1, (0, 0), fx = 0.75, fy = 0.75)
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    Camera().release_camera()
    return ()

if __name__ == '__main__':
    main()
    cv2.destroyAllWindows()

'''
