import cv2 
import numpy as np 
import audioChange

audio_control = audioChange.VolumeChange()
  
vid = cv2.VideoCapture(0) 
  
while True: 

    width  = int(cv2.CAP_PROP_FRAME_WIDTH) 
    height = int(cv2.CAP_PROP_FRAME_WIDTH) 
  
    _, frame = vid.read() 
  
    cv2.imshow("frame", frame)  

    total_blue = 0
    total_green = 0
    total_red = 0

    for row in range(0, width):
        for col in range(0, height):
            b,g,r = (frame[row, col])
            total_blue += b
            total_green += g
            total_red += r
  
    if (total_blue > total_green and total_blue > total_red): 
        print("Blue") 
        audio_control.muteVolume()
    elif (total_green > total_red and total_green > total_blue): 
        print("Green") 
        audio_control.raiseVolume()
    else: 
        print("Red")
        audio_control.lowerVolume()