import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
import scipy.ndimage as ndimage
from sklearn import linear_model
import pandas as pd


#read the csv with all informations
info = pd.read_csv('meta.csv', sep = ';')
#get unique ids
uisd = info["se_id"].unique()
us = info["side"].unique()

#define the image path
image_path = "./../no_sync/SmtImageData/"
       
#define the path to the matched marks
markers_path = ".\\matched_markers\\"

for ii in uisd:
    for jj in us:
        for kk in ["pre", "post"]:
            #find pre post pairs
            pair = info[(info["se_id"] == ii) & (info["side"] == jj)]
            #define the image names
            image_name = pair.loc[pair["state"] == kk, "image_name"].values[0]
            
            #read the image
            input_img=cv.imread(image_path + image_name)
            
            pre_img= input_img[0:450, 0:600]
            
            gray = cv.cvtColor(pre_img,cv.COLOR_BGR2GRAY)
            ret, thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
            
            # noise removal
            kernel = np.ones((4,4),np.uint8)
            opening = cv.morphologyEx(thresh,cv.MORPH_OPEN,kernel, iterations = 3)
            # sure background area
            sure_bg = cv.dilate(opening,kernel,iterations=5)
            # Finding sure foreground area
            dist_transform = cv.distanceTransform(opening,cv.DIST_L2,5)
            ret, sure_fg = cv.threshold(dist_transform,0.7*dist_transform.max(),255,0)
            # Finding unknown region
            sure_fg = np.uint8(sure_fg)
            unknown = cv.subtract(sure_bg,sure_fg)
    
            # Marker labelling
            ret, markers = cv.connectedComponents(sure_fg)
            # Add one to all labels so that sure background is not 0, but 1
            markers = markers+1
            # Now, mark the region of unknown with zero
            markers[unknown==255] = 0
    #
            markers = cv.watershed(pre_img,markers)
            pre_img[markers == -1] = [255,0,0]
    
            k = np.array([[-1,2,-1],[-1,2,-1],[-1,2,-1],[-1,2,-1]])
            img_vert = ndimage.convolve(img_border, k, mode='nearest', cval=0.0)
            img_vert=np.abs(img_vert)
            
            thres=np.max(img_vert)*0.2
            seg_img_vert=np.copy(img_vert)
            seg_img_vert[img_vert>thres]=1
            seg_img_vert[img_vert<=thres]=0
   
            img_diff = img_border - img_vert
    
            thres=np.max(img_diff)*0.2
            seg_img_hor=np.copy(img_diff)
            seg_img_hor[img_diff>thres]=1
            seg_img_hor[img_diff<=thres]=0
    
            ##horizontal line fit
            listX=[]
            listY=[]
            eps=5
    #
            for yi in range(eps,np.size(seg_img_hor,0)-eps):
                for xi in range(eps,np.size(seg_img_hor,1)-eps):
                    if seg_img_hor[yi,xi]>0:
                        listX.append(xi)
                        listY.append(yi)
                        
            #First half horizontal
            meanY=np.sum(listY)/np.size(listY,0);
            #print(meanY)
            listYHalf=[x for x in listY if x < meanY]
            listXHalf=listX[0:len(listYHalf)]
            z1=np.polyfit(listXHalf, listYHalf, 2)
            p1 = np.poly1d(z1)
    #
            lin_x = np.linspace(0,599,600)
            lin_y1 = p1(lin_x)
   
            listY_second_Half=[x for x in listY if x >= meanY]
            listX_second_Half=listX[-len(listY_second_Half):]
   
            z2=np.polyfit(listX_second_Half, listY_second_Half, 2)
            p2 = np.poly1d(z2)
            
            lin_y2 = p2(lin_x)
    #
            ##vertical line fit
            listX_vert=[]
            listY_vert=[]
            eps=5
    #
            for yi in range(eps,np.size(seg_img_vert,0)-eps):
                for xi in range(eps,np.size(seg_img_vert,1)-eps):
                    if seg_img_vert[yi,xi]>0:
                        #swap x,y for vertical lines
                        listX_vert.append(yi)
                        listY_vert.append(xi)
                        
            z3=np.polyfit(listX_vert, listY_vert, 1)
            
            p3 = np.poly1d(z3)
            
            lin_y3 = p3(lin_x)
            x_intersect=np.argmin(np.abs(lin_y3-lin_x))
            upperX=x_intersect
            upperY=p1(x_intersect)
            
            x_intersect=np.argmin(np.abs(lin_y3-lin_x))
            
            lowerX=x_intersect
            lowerY=p2(x_intersect)
            
            if kk == "pre":
                x_low_pre = lowerX
                y_low_pre = lowerY
                x_up_pre = upperX
                y_up_pre = upperY
            elif kk == "post":
                x_low_post = lowerX
                y_low_post = lowerY
                x_up_post = upperX
                y_up_post = upperY
                
            #save the z3 parameter to judge fit quality
            info.loc[(info["se_id"] == ii) & (info["side"] == jj) & (info["state"] == kk), "z3"] = z3[0]
            
        markers_name = str(ii) + "_" + jj + ".csv"  
        markers = pd.read_csv(markers_path + markers_name, sep = ";")
        
        dx_low_pre = markers["x_pre"].values  - x_low_pre
        dy_low_pre = markers["y_pre"].values  - y_low_pre
        dr_low_pre = np.sqrt(dx_low_pre**2 + dy_low_pre**2)
        dx_up_pre = markers["x_pre"].values  - x_up_pre
        dy_up_pre = markers["y_pre"].values  - y_up_pre
        dr_up_pre = np.sqrt(dx_up_pre**2 + dy_up_pre**2)
       
        dx_low_post = markers["x_post"].values  - x_low_post
        dy_low_post = markers["y_post"].values  - y_low_post
        dr_low_post = np.sqrt(dx_low_post**2 + dy_low_post**2)
        dx_up_post = markers["x_post"].values  - x_up_post
        dy_up_post = markers["y_post"].values  - y_up_post
        dr_up_post = np.sqrt(dx_up_post**2 + dy_up_post**2)
        
        quality = np.mean([np.mean(np.abs(dr_low_pre - dr_low_post)), np.mean(np.abs(dr_up_pre - dr_up_post))])
        print(quality)
        
        #attach to dataframe
        info.loc[(info["se_id"] == ii) & (info["side"] == jj) & (info["state"] == "post"), "quality"] = quality
        
#save meta data
info.to_csv("meta.csv", sep = ";", index = False)