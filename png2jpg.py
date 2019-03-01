#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 12:48:03 2019

@author: XZP

Function: Convert png image to jpg in the specified directory
"""

import os
import string
#Enter picture path
dirName = "/Volumes/文档/Tensorflow/VOC2007/JPEGImages/"         #最后要加双斜杠，不然会报错

li=os.listdir(dirName)
for filename in li:
    newname = filename
    newname = newname.split(".")
    if newname[-1]=="png":
        newname[-1]="jpg"
        newname = str.join(".",newname)  #这里要用str.join
        filename = dirName+filename
        newname = dirName+newname
        os.rename(filename,newname)
        print(newname,"updated successfully")