from PIL import Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2

def get_marker(img):
    #apply hough transformation to get major circles
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT,0.1, 10,
                            param1=50,param2=50,minRadius=15,maxRadius=35)
    
    #initialize a dict with the coordinates to big markers
    major = dict(x = [], y = [], r = [])
    
    #get the major coordinates
    for ic in circles[0,:]:
        major['x'].append(ic[0])
        major['y'].append(ic[1])
        major['r'].append(ic[2]) 
    
    #show the image below the big markers
    y_up = int(max(major['y'])) + int(max(major['r']))
    y_low = int(min(major['y'])) - int(max(major['r']))
    sub_img = img[y_low:y_up]
    
    #get the y-offset that is introduced by cropping the image
    y_offset = y_low
    
    #apply hough transformation to get minor circles
    circles = cv2.HoughCircles(sub_img, cv2.HOUGH_GRADIENT,0.1, 5,
                                param1=50,param2=20,minRadius=1,maxRadius=8)

    #initialize a dict with the coordinates to small markers
    minor = dict(x = [], y = [], r = [])
    
    #get the minor coordinates
    for ic in circles[0,:]:
        minor['x'].append(ic[0])
        minor['y'].append(ic[1] + y_offset)
        minor['r'].append(ic[2]) 
        
    return minor, major

def export_marker(img_pre, img_post, se_id, side):
    #get the markers in pre and post
    minor_pre, major_pre = get_marker(img_pre)
    minor_post, major_post = get_marker(img_post)
    
    #summarize data in dataframe
    pre_marker = pd.DataFrame(dict(x_pre = minor_pre['x'] + major_pre['x'],
                               y_pre = minor_pre['y'] + major_pre['y'],
                               r_pre = minor_pre['r'] + major_pre['r'],
                               sz_pre = len(minor_pre['x'])*[0] + len(major_pre['x'])*[1]))
    post_marker = pd.DataFrame(dict(x_post = minor_post['x'] + major_post['x'],
                               y_post = minor_post['y'] + major_post['y'],
                               r_post = minor_post['r'] + major_post['r'],
                               sz_post = len(minor_post['x'])*[0] + len(major_post['x'])*[1]))
    marker = pd.DataFrame(data = dict(x_pre = [], y_pre = [], r_pre = [], sz_pre = [],
                                      x_post = [], y_post = [], r_post = [], sz_post = []))

    for idx in post_marker.index:
        #get the row in the post marker dataframe
        post_row = post_marker.iloc[[idx]]
        
        #calculate the geometrical distance
        dx = pre_marker['x_pre'].values - post_row['x_post'].values[0]
        dy = pre_marker['y_pre'].values - post_row['y_post'].values[0]
        dr = np.sqrt(dx**2 + dy**2)
        
        #find the closest row
        pre_row = pre_marker.iloc[[np.argmin(dr)]]
        
        #reset the indices of both rows
        pre_row.reset_index(drop = True, inplace = True)
        post_row.reset_index(drop = True, inplace = True)
        
        if pre_row["sz_pre"].values[0] == post_row["sz_post"].values[0] :#and (pre_row["x_pre"].values[0] - post_row["x_post"].values[0])**2 + (pre_row["y_pre"].values[0] - post_row["y_post"].values[0])**2 < 900:
            #concatenate both rows horizontally and append to the marker dataframe
            marker_row = pd.concat([pre_row, post_row], axis = 1)
            marker = pd.concat([marker, marker_row], axis = 0)
    
    #reorder the columns and reset the index
    marker = marker[["x_pre", "x_post", "y_pre", "y_post", "r_pre", "r_post", "sz_pre", "sz_post"]]
    marker.reset_index(drop = True)
    
    #define the save path
    save_path = ".\\matched_markers\\"
    
    #export the file as csv
    marker.to_csv(save_path + str(se_id) + "_" + side + ".csv", sep = ";", index = False)

if __name__=='__main__':
    #read the csv with all informations
    info = pd.read_csv('meta.csv', sep = ';')
    #get unique ids
    uisd = info["se_id"].unique()
    us = info["side"].unique()
    
    for ii in uisd:
        for jj in us:
            #find pre post pairs
            pair = info[(info["se_id"] == ii) & (info["side"] == jj)]
            #define the image names
            img_name_pre = pair.loc[pair["state"] == "pre", "image_name"].values[0]
            img_name_post = pair.loc[pair["state"] == "post", "image_name"].values[0]
            
            #define the image path
            image_path = "./../no_sync/SmtImageData/"
    
    
#    side = info.loc[info['image_name'] == image_name, 'side'].values[0]
#    se_id = info.loc[info['image_name'] == image_name, 'se_id'].values[0]
#    
#    pair = info[(info['side'] == side) & (info['se_id'] == se_id)]
#    
#    img_name_pre = pair.loc[pair['state'] == 'pre', 'image_name'].values[0]
#    img_name_post = pair.loc[pair['state'] == 'post', 'image_name'].values[0]
    
            #load the image
            img_pre = Image.open(image_path + img_name_pre)
            img_pre = np.asarray(img_pre)
            img_post = Image.open(image_path + img_name_post)
            img_post = np.asarray(img_post)
            
            #convert from 16 to 8bit
            img_pre = (img_pre/256).astype('uint8')
            img_post = (img_post/256).astype('uint8')
            
            #export the marker
            export_marker(img_pre, img_post, ii, jj)