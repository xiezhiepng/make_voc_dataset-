#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 13:35:33 2019

@author: XZP

Function: Generate xml file with the same name according to jpg file name
"""

import os
import glob

#Enter xml path
path="/Volumes/文档/Tensorflow/VOC2007/Annotations/"
#Enter img path      
src_img_dir = "/Volumes/文档/Tensorflow/VOC2007/JPEGImages/"
#coding:utf8
import os;

img_Lists = glob.glob(src_img_dir + '/*.jpg')
img_basenames = [] # e.g. 100.jpg
for item in img_Lists:
    img_basenames.append(os.path.basename(item))
 
img_names = [] # e.g. 100
for item in img_basenames:
    temp1, temp2 = os.path.splitext(item)
    img_names.append(temp1)
  
def rename():
        i=0
        filelist=os.listdir(path)#该文件夹下所有的文件（包括文件夹）
        for files in filelist:#遍历所有文件
            i=i+1
            Olddir=os.path.join(path,files);#原来的文件路径                
            if os.path.isdir(Olddir):#如果是文件夹则跳过
                    continue;
            filename=os.path.splitext(files)[0];#文件名
            filetype=os.path.splitext(files)[1];#文件扩展名
            print(str(i))
            if i<1000:
                Newdir=os.path.join(path,img_names[i-1]+filetype);#新的文件路径
                os.rename(Olddir,Newdir)#重命名
print("img_names"+img_names[0])
rename()