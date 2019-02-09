# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 14:30:02 2019

@author: Jasper
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

#left_pre=mpimg.imread()

#left_post=mpimg.imread('342165_20161020-205603_L.png')

filtersize=100;
filterkernel= np.ones([filtersize, 1], dtype = float)
filter_img=left_pre;

y=635
for x in range (0, np.size(left_pre,1)):
    sum =0
    for w in range(0, filtersize)
        sum = sum + filterkernel
        filter_img[y,x]=


plt.figure(2)
plt.imshow(filter_img, cmap="gray")