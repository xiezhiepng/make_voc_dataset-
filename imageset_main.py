#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 16:20:35 2019

@author: XZP

Function: Generate train.txt, test.txt, val.txt, trainval.txt according to annotations and jpegimage
"""

import os
import random
 
trainval_percent = 0.5
train_percent = 0.5
#enter xml file path
xmlfilepath = '/Volumes/文档/Tensorflow/VOC2007/Annotations/'
#enter four txt file path
txtsavepath = '/Volumes/文档/Tensorflow/VOC2007/ImageSets/Main'
total_xml = os.listdir(xmlfilepath)
 
num=len(total_xml)
list=range(num)
tv=int(num*trainval_percent)
tr=int(tv*train_percent)
trainval= random.sample(list,tv)
train=random.sample(trainval,tr)
 
ftrainval = open(txtsavepath+'/trainval.txt', 'w')
ftest = open(txtsavepath+'/test.txt', 'w')
ftrain = open(txtsavepath+'/train.txt', 'w')
fval = open(txtsavepath+'/val.txt', 'w')
 
for i  in list:
    name=total_xml[i][:-4]+'\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)
 
ftrainval.close()
ftrain.close()
fval.close()
ftest .close()

