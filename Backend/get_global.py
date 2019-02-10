# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from scipy.spatial.distance import pdist
import os
import glob


#define the path to the matched marks
markers_path = ".\\matched_markers\\"
markers_ext = "*.csv"


    
#load the info csv
info = pd.read_csv('.\meta.csv', sep = ";")
info["g_scale_x"] = 0
info["g_scale_y"] = 0
info["g_shift_x"] = 0
info["g_shift_y"] = 0
info["g_alpha"] = 0

for path in glob.glob(markers_path + markers_ext):
    #import a csv with pre nd post coordinates of the markers
    df = pd.read_csv(path, sep = ";")
    
    #get gradient in y-direction between the states
    df["dx"]= (df["x_pre"] - df["x_post"])
    df["dy"] = (df["y_pre"] - df["y_post"])
    
    #get the major marks
    major = df[df["sz_pre"] == 1]
    minor = df[df["sz_pre"] == 0]
    
    if minor.shape[0] != 0:
        #get the minor coordinates
        x_minor_pre = minor["x_pre"].values
        x_minor_pre = np.array([[0]*len(x_minor_pre), x_minor_pre]).T
        y_minor_pre = minor["y_pre"].values
        y_minor_pre = np.array([[0]*len(y_minor_pre), y_minor_pre]).T
        x_minor_post = minor["x_pre"].values
        x_minor_post = np.array([[0]*len(x_minor_post), x_minor_post]).T
        y_minor_post = minor["y_pre"].values
        y_minor_post = np.array([[0]*len(y_minor_post), y_minor_post]).T
    
        #get the distance between the most distant minor marks
        dx_minor_pre = pdist(x_minor_pre, "euclidean")
        dy_minor_pre = pdist(y_minor_pre, "euclidean")
        dx_minor_post = pdist(x_minor_post, "euclidean")
        dy_minor_post = pdist(y_minor_post, "euclidean")
        
        
        #get the index of the biggest distance of minor marks
        minor_idx = np.argmax(dx_minor_pre**2 + dy_minor_pre**2)
        dx_minor_pre = dx_minor_pre[minor_idx]
        dy_minor_pre = dy_minor_pre[minor_idx]
        dx_minor_post = dx_minor_post[minor_idx]
        dy_minor_post = dy_minor_post[minor_idx]
                    
        #caclulate the scaling of post and pre in x and y direction
        if dx_minor_pre != 0:
            scale_x = np.mean([dx_minor_post/dx_minor_pre])
        elif dx_minor_post == 0:
            scale_x = 1
        else:
            scale_x = np.nan
            
        if dy_minor_pre != 0:
            scale_y = np.mean([dy_minor_post/dy_minor_pre])
        elif dy_minor_post == 0:
            scale_y = 1
        else:
            scale_y = np.nan
        
        #calculate the angle from the distance changes
        if (dy_minor_pre * scale_y - dy_minor_post )< 1e-3:
             alpha_minor = 0
        else:
            alpha_minor = np.arctan(dx_minor_pre * scale_x / (dy_minor_pre * scale_y - dy_minor_post))
            
        alpha = np.mean([alpha_minor])
        
        #calculate the shift in x and y direction
        shift_x = df['dx'].abs().min()
        shift_y = df['dy'].abs().min()
        
    if major.shape[0] != 0:
        #get the major coordinates
        x_major_pre = major["x_pre"].values
        x_major_pre = np.array([[0]*len(x_major_pre), x_major_pre]).T
        y_major_pre = major["y_pre"].values
        y_major_pre = np.array([[0]*len(y_major_pre), y_major_pre]).T
        x_major_post = major["x_pre"].values
        x_major_post = np.array([[0]*len(x_major_post), x_major_post]).T
        y_major_post = major["y_pre"].values
        y_major_post = np.array([[0]*len(y_major_post), y_major_post]).T
        
        #get the distance between the most distant major marks
        dx_major_pre = pdist(x_major_pre, "euclidean")
        dy_major_pre = pdist(y_major_pre, "euclidean")
        dx_major_post = pdist(x_major_post, "euclidean")
        dy_major_post = pdist(y_major_post, "euclidean")
        
        #get the index of the biggest distance of major marks
        major_idx = np.argmax(dx_major_pre**2 + dy_major_pre**2)
        dx_major_pre = dx_major_pre[major_idx]
        dy_major_pre = dy_major_pre[major_idx]
        dx_major_post = dx_major_post[major_idx]
        dy_major_post = dy_major_post[major_idx]
        
        #caclulate the scaling of post and pre in x and y direction
        if dx_major_pre != 0:
            scale_x = np.mean([dx_major_post/dx_major_pre])
        elif dx_major_post == 0:
            scale_x = 1
        else:
            scale_x = np.nan
            
        if dy_major_pre != 0:
            scale_y = np.mean([dy_major_post/dy_major_pre])
        elif dy_major_post == 0:
            scale_y = 1
        else:
            scale_y = np.nan
        
        #calculate the angle from the distance changes
        if (dy_major_pre * scale_y - dy_major_post )< 1e-3:
             alpha_major = 0
        else:
            alpha_major = np.arctan(dx_major_pre * scale_x / (dy_major_pre * scale_y - dy_major_post))
           
        alpha = np.mean([alpha_major])
        
        #calculate the shift in x and y direction
        shift_x = df['dx'].abs().min()
        shift_y = df['dy'].abs().min()
        
    if minor.shape[0] != 0 and major.shape[0] != 0:
        #caclulate the scaling of post and pre in x and y direction
        if dx_minor_pre != 0:
            minor_scale_x = np.mean([dx_minor_post/dx_minor_pre])
        elif dx_minor_post == 0:
            minor_scale_x = 1
        else:
            minor_scale_x = np.nan
            
        if dy_minor_pre != 0:
            minor_scale_y = np.mean([dy_minor_post/dy_minor_pre])
        elif dy_minor_post == 0:
            minor_scale_y = 1
        else:
            minor_scale_y = np.nan
        
        if dx_major_pre != 0:
            major_scale_x = np.mean([dx_major_post/dx_major_pre])
        elif dx_major_post == 0:
            major_scale_x = 1
        else:
            major_scale_x = np.nan
            
        if dy_major_pre != 0:
            major_scale_y = np.mean([dy_major_post/dy_major_pre])
        elif dy_major_post == 0:
            major_scale_y = 1
        else:
            major_scale_y = np.nan
        
        
        scale_x = np.mean([major_scale_x, minor_scale_x])
        scale_y = np.mean([major_scale_y, minor_scale_y])
        
        #calculate the angle from the distance changes
        if (dy_major_pre * scale_y - dy_major_post )< 1e-3:
             alpha_major = 0
        else:
            alpha_major = np.arctan(dx_major_pre * scale_x / (dy_major_pre * scale_y - dy_major_post))
            
        if (dy_minor_pre * scale_y - dy_minor_post )< 1e-3:
             alpha_minor = 0
        else:
            alpha_minor = np.arctan(dx_minor_pre * scale_x / (dy_minor_pre * scale_y - dy_minor_post))
            
        alpha = np.mean([alpha_minor, alpha_major])
        
        #calculate the shift in x and y direction
        shift_x = df['dx'].abs().min()
        shift_y = df['dy'].abs().min()
    
    #get the image name from the path
    markers_file = os.path.basename(path)
    
    #split the markers filename to retrieve informations
    markers_file, _ = os.path.splitext(markers_file)
    markers_file_split = markers_file.split("_")
    #get the id and side of the current csv
    se_id = int(markers_file_split[0])
    side = markers_file_split[1]
    
    #set up the filter
    info_filter = (info["se_id"] == se_id) & (info["side"] == side) & (info["state"] == "post")
    
    #find the correct row in the meta file
    info.loc[info_filter, "g_shift_x"] = shift_x
    info.loc[info_filter, "g_shift_y"] = shift_y
    info.loc[info_filter, "g_scale_x"] = scale_x
    info.loc[info_filter, "g_scale_y"] = scale_y
    info.loc[info_filter, "g_alpha"] = alpha
    
info = info.fillna(0)
info.to_csv("meta.csv", sep = ";", index = False)