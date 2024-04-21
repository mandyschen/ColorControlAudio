import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import numpy as np
from PIL import Image

image = np.array(Image.open('hellokitty.jpg')).astype(np.uint8)

sobel_x = np.array([[ -1, 0, 1],
                    [ -2, 0, 2],
                    [ -1, 2, 1]])
sobel_y = np.array([[ -1, -2, -1],
                    [ 0, 0, 0],
                    [ 1, 2, 1]])

gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
edgeImage = gray

height, width, channel = image.shape

for x in range(1, height-1):
    for y in range(1, width-1):
        pixel_x = (sobel_x[0][0] * gray[x-1][y-1]) + \
                    (sobel_x[0][1] * gray[x-1][y]) + \
                    (sobel_x[0][2] * gray[x-1][y+1]) + (sobel_x[1][0] * gray[x][y-1]) + \
                    (sobel_x[1][1] * gray[x][y]) + (sobel_x[1][2] * gray[x][y+1]) + \
                    (sobel_x[2][0] * gray[x+1][y-1]) + (sobel_x[2][1] * gray[x+1][y]) + \
                    (sobel_x[2][2] * gray[x+1][y+1])
        pixel_y = (sobel_y[0][0] * gray[x-1][y-1]) + (sobel_y[0][1] * gray[x-1][y]) + \
                    (sobel_y[0][2] * gray[x-1][y+1]) + (sobel_y[1][0] * gray[x][y-1]) + \
                    (sobel_y[1][1] * gray[x][y]) + (sobel_y[1][2] * gray[x][y+1]) + \
                    (sobel_y[2][0] * gray[x+1][y-1]) + (sobel_y[2][1] * gray[x+1][y]) + \
                    (sobel_y[2][2] * gray[x+1][y+1])

        val = math.sqrt((pixel_x * pixel_x) + (pixel_y * pixel_y))
        if val > 255:
            val =255
        elif val <= 0:
            val = 0
        edgeImage[x-1,y-1] = val
        
plt.figure()
plt.title('OIP_sobel_gray.png')
plt.imsave('OIP-sobel_gray.png', edgeImage, cmap='gray', format='png')
plt.imshow(edgeImage, cmap='gray')
plt.show()

