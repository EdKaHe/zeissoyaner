# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 14:30:02 2019

@author: David & Jasper 
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

left_pre=mpimg.imread('342165_20161020-205235_L.tif').astype(float)
left_pre= np.divide(left_pre, np.max(left_pre))

left_post=mpimg.imread('342165_20161020-205603_L.tif').astype(float)
left_post= np.divide(left_post, np.max(left_post))

plt.figure(1)
imgplot = plt.imshow(left_pre-left_post, cmap="gray")

y_s = 650 #start coordinate pixel
x_s = 300  #start coordinate pixel
area = 100 #area of subwindow 
move = 50 #itterations to move the grid an substract
# carfull dont move area to the sides of the picture
dist = np.empty([move,move])

# =============================================================================
# for i in range(0,move):
#     np.roll(left_post,i, axis = 0)
#     for j in range(0,move):
#         np.roll(left_post,j, axis = 1)
#         sub_pre = left_pre[x_s:x_s+area,y_s:y_s+area]
#         sub_post = left_post[x_s:x_s+area,y_s:y_s+area]
#         diff_sub = np.absolute(np.subtract(sub_pre, sub_post))
#         dist[i,j] = np.sum(diff_sub)
# =============================================================================
sub_pre = np.copy(left_pre[y_s:y_s+area,x_s:x_s+area])



for yi in range(0,move):
    for xi in range(0,move):
        dist[yi,xi]=np.sum(np.abs(sub_pre-left_post[y_s+yi:y_s+area+yi, x_s+xi:x_s+area+xi]))

plt.figure(2)
imgplot = plt.imshow(dist, cmap = "gray")

