#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 15:15:55 2019

@author: XZP

Function: Generate voc format xml file according to groundtruth.txt
"""

import os, sys
import glob
from PIL import Image
 
# image path
src_img_dir = "/Volumes/文档/Tensorflow/VOC2007/JPEGImages/"
# ground truth path
src_txt_dir = "/Volumes/文档/Tensorflow/VOC2007/txt/"
src_ann_dir = "Volumes/文档/Tensorflow/VOC2007/Annotations"

xml_dir = "/Volumes/文档/Tensorflow/VOC2007/Annotations/"

img_Lists = glob.glob(src_img_dir + '/*.jpg')
 
img_basenames = [] # e.g. 100.jpg
for item in img_Lists:
    img_basenames.append(os.path.basename(item))
 
img_names = [] # e.g. 100
for item in img_basenames:
    temp1, temp2 = os.path.splitext(item)
    img_names.append(temp1)
i=0
for img in img_names:
    im = Image.open((src_img_dir + '/' + img + '.jpg'))
    width, height = im.size
    # open the crospronding txt file
    
    gt = open(src_txt_dir +'GroundTruth.txt').read().splitlines()

    # write in xml file
    #os.mknod(src_txt_dir + '/' + img + '.xml')
    xml_file = open((xml_dir + img + '.xml'), 'w')
                                                                       #    xml_file = open(('00000.xml'), 'w')
    xml_file.write('<annotation>\n')
    xml_file.write('\t<folder>simple</folder>\n')
    xml_file.write('\t<filename>' + str(img) + '.jpg' + '</filename>\n')
    xml_file.write('\t<source>\n')
    xml_file.write('\t\t<database>' +'The simple Database' + '</database>\n')
    xml_file.write('\t\t<annotation>' +'simple' + '</annotation>\n')
    xml_file.write('\t\t<image>flickr</image>\n')
    xml_file.write('\t\t<flickrid>325991873</flickrid>\n')
    xml_file.write('\t</source>\n')
    xml_file.write('\t<owner>\n')
    xml_file.write('\t\t<flickrid>archin</flickrid>\n')
    xml_file.write('\t\t<name>?</name>\n')
    xml_file.write('\t</owner>\n')
    xml_file.write('\t<size>\n')
    xml_file.write('\t\t<width>' + str(width) + '</width>\n')
    xml_file.write('\t\t<height>' + str(height) + '</height>\n')
    xml_file.write('\t\t<depth>3</depth>\n')
    xml_file.write('\t</size>\n')
    xml_file.write('\t<segmented>0</segmented>\n')
    # write the region of text on xml file
    
    '''
    test------gt
    '''
#    print(gt[0])
#    
#    for img_each_label in gt:
#    spt = img_each_label.split(';')
    i=0
    #Find the label corresponding to the same img
    while(i<len(gt)): 
        spt = gt[i].split(';')
        i=i+1 
#        print(int(img))
#        print(int(spt[0].split('.')[0]))
#        print(i)
        if int(img)==int(spt[0].split('.')[0]):
           
            print("img"+img)
        #    print(spt)
            xml_file.write('\t<object>\n')
            xml_file.write('\t\t<name>' + str(spt[5]) + '</name>\n')
            xml_file.write('\t\t<pose>Unspecified</pose>\n')
            xml_file.write('\t\t<truncated>0</truncated>\n')
            xml_file.write('\t\t<difficult>0</difficult>\n')
            xml_file.write('\t\t<bndbox>\n')
            xml_file.write('\t\t\t<xmin>' + str(spt[1]) + '</xmin>\n')
            xml_file.write('\t\t\t<ymin>' + str(spt[2]) + '</ymin>\n')
            xml_file.write('\t\t\t<xmax>' + str(spt[3]) + '</xmax>\n')
            xml_file.write('\t\t\t<ymax>' + str(spt[4]) + '</ymax>\n')
            xml_file.write('\t\t</bndbox>\n')
            xml_file.write('\t</object>\n')
        # 
    xml_file.write('</annotation>')