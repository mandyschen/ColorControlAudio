# %%
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import numpy as np
from PIL import Image

image = mpimg.imread('./img.jpeg') 

# image = np.array(Image.open('./img.jpeg')).astype(np.uint8)

gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
plt.imshow(gray, cmap='gray')

# %%

sobel_x = np.array([[ -1, 0, 1],
                    [ -2, 0, 2],
                    [ -1, 2, 1]])
sobel_y = np.array([[ -1, -2, -1],
                    [ 0, 0, 0],
                    [ 1, 2, 1]])

filtered_image = cv2.filter2D(image, -1, sobel_y)

# edgeImage = gray

# height, width, channel = image.shape

# for x in range(1, height-1):
#     for y in range(1, width-1):
#         pixel_x = (sobel_x[0][0] * gray[x-1][y-1]) + (sobel_x[0][1] * gray[x-1][y]) + \
#                     (sobel_x[0][2] * gray[x-1][y+1]) + (sobel_x[1][0] * gray[x][y-1]) + \
#                     (sobel_x[1][1] * gray[x][y]) + (sobel_x[1][2] * gray[x][y+1]) + \
#                     (sobel_x[2][0] * gray[x+1][y-1]) + (sobel_x[2][1] * gray[x+1][y]) + \
#                     (sobel_x[2][2] * gray[x+1][y+1])
#         pixel_y = (sobel_y[0][0] * gray[x-1][y-1]) + (sobel_y[0][1] * gray[x-1][y]) + \
#                     (sobel_y[0][2] * gray[x-1][y+1]) + (sobel_y[1][0] * gray[x][y-1]) + \
#                     (sobel_y[1][1] * gray[x][y]) + (sobel_y[1][2] * gray[x][y+1]) + \
#                     (sobel_y[2][0] * gray[x+1][y-1]) + (sobel_y[2][1] * gray[x+1][y]) + \
#                     (sobel_y[2][2] * gray[x+1][y+1])
 
#         val = math.sqrt((pixel_x * pixel_x) + (pixel_y * pixel_y))
#         edgeImage[x-1,y-1] = val

plt.imshow(filtered_image, cmap='gray')

# # %%
# sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1)
# plt.imshow(sobely, cmap = 'gray')

# # %%
# thresh_min = 20
# thresh_max = 100
# sxbinary = np.zeros_like(sobel_y)
# sxbinary[(sobel_x >= thresh_min) & (sobel_y <= thresh_max)] = 1
# plt.imshow(sxbinary, cmap='gray')

# # %%

# %%
