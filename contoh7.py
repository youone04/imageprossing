import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('black-and-white-19.jpg')


grid_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.figure(figsize=(20,8))
# plt.imshow(grid_RGB) # Printing the original picture after converting to RGB


grid_HSV = cv2.cvtColor(grid_RGB, cv2.COLOR_RGB2HSV) # Converting to HSV

lower_white = np.array([0,0,0])
upper_white = np.array([0,0,255])

lower_black = np.array([0,0,0])
upper_black = np.array([50,50,100])

lower_green = np.array([25,52,72])
upper_green = np.array([102,255,255])


mask_white = cv2.inRange(grid_HSV, lower_white, upper_white)
mask_black= cv2.inRange(grid_HSV, lower_black, upper_black)
mask_green = cv2.inRange(grid_HSV, lower_green, upper_green)
green_perc = (mask_green>0).mean()
white_perc = (mask_white>0).mean()
black_perc = (mask_black>0).mean()
# res = cv2.bitwise_and(img, img, mask=mask_green) # Generating image with the green part

# print("Green Part of Image")
print('green_perc =',round(green_perc, 2) * 100,'%')
print('mask_black', round(black_perc, 2) * 100,'%')
print('white_perc =',round(white_perc, 2) * 100,'%')
# print(grid_HSV)
# plt.figure(figsize=(20,8))
# plt.imshow(res)