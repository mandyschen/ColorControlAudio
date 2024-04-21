import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import numpy as np
from PIL import Image

vid = cv2.VideoCapture(0) 
  
while True: 
    width  = int(vid.get(3)) 
    height = int(vid.get(4)) 
  
    _, frame = vid.read() 
    image = frame
  
    #cv2.imshow("frame", frame)

    sobel_x = np.array([[ -1, 0, 1],
                        [ -2, 0, 2],
                        [ -1, 2, 1]])
    sobel_y = np.array([[ -1, -2, -1],
                        [ 0, 0, 0],
                        [ 1, 2, 1]])

    filtered_image = cv2.filter2D(image, -1, sobel_y)

    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    edgeImage = gray

    height, width, channel = image.shape

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3) 
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    abs_sobel_x = cv2.convertScaleAbs(sobel_x)    
    abs_sobel_y = cv2.convertScaleAbs(sobel_y)
    
    sobel_combined = cv2.addWeighted(abs_sobel_x, 0.5, abs_sobel_y, 0.5, 0)

    cv2.imshow('Sobel Edge Detection', sobel_combined)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
vid.release()
cv2.destroyAllWindows()
        

