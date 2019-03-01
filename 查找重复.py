#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 15:59:54 2019

@author: XZP
"""

a = [1, 2, 3, 2, 1, 5, 6, 5, 5, 5]
source = a
from collections import defaultdict
def list_duplicates(seq):
    tally = defaultdict(list)
    for i,item in enumerate(seq):
        tally[item].append(i)
    return ((key,locs) for key,locs in tally.items() 
                            if len(locs)>1)
 
for dup in sorted(list_duplicates(source)):
    print(dup)
    print("test:"+str(dup[1][0])+"len:"+str(len(dup[1])))

