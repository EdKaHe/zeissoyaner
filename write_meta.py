# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 10:41:11 2019

@author: edizh
"""

import pandas as pd
from datetime import datetime
import glob
import os

#define the path to the images
image_path = ".\\no_sync\\SmtImageData\\"
#define the image extension
image_ext = "*.tif"

#init the lists with all informations
image_name_list = []
id_list = []
datetime_list = []
timestamp_list = []
side_list = []

#loop through all images
for path in glob.glob(image_path + image_ext):
    #get the image name from the path
    image_name = os.path.basename(path)
    #remove the file extension
    image_name_no_ext = os.path.splitext(image_name)[0]
    
    #split the image names to extract informations
    image_name_split = image_name_no_ext.split("_")
    
    #acquire the informations from the image name
    image_name_list.append(image_name)
    id_list.append(int(image_name_split[0]))
    datetime_list.append( pd.to_datetime(image_name_split[1], format = '%Y%m%d-%H%M%S') )
    side_list.append(image_name_split[2])

#add the informations to a dataframe
df = pd.DataFrame(data = dict(image_name = image_name_list, se_id = id_list, datetime = datetime_list, side = side_list, state = len(id_list)*[""]))

#get the unique surface element ids and sides
unique_id = pd.unique(df['se_id'])
unique_side = pd.unique(df['side'])

#get pairs of equal surface element id and side to get whether its post or pre welding
for uid in unique_id:
    for us in unique_side:
        pairs = df.loc[(df['se_id'] == uid) & (df['side'] == us)]
        
        if len(pairs) != 2:
            raise ValueError("Number of pairs must equal 2!")
        
        if pairs.loc[pairs.index[0], 'datetime'] > pairs.loc[pairs.index[1], 'datetime']:
            df.loc[[pairs.index[0]], 'state'] = 'post'
            df.loc[[pairs.index[1]], 'state'] = 'pre'
        else:
            df.loc[[pairs.index[1]], 'state'] = 'post'
            df.loc[[pairs.index[0]], 'state'] = 'pre'

#export meta to csv
df.to_csv('.\meta.csv', sep = ';')