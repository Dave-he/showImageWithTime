#!/usr/bin/python3
# -*- coding: utf-8 -*-

from collections import namedtuple
import cv2
import numpy as np
from getFlieList import GetFileList

path = "/home/hyx/Pictures"
files = GetFileList(path,"jpg")
#for f in files:


ref = namedtuple('Reference', ['width', 'height','deepheight','sPosition'])(
    640, 480, 0, 1000
)

def map_pixel(t, leftimg, rightimg):
    def map_pixel(x, y):
        w ,h =x, y
        selected = leftimg if h < (t- ref.sPosition*2)*(w+ref.deepheight)/ref.sPosition+320 else rightimg
        return selected[w][h]
    return map_pixel



i = 0
while files :
    src1 = cv2.imread(files[i])
    src2 = cv2.imread(files[i+1])
    i+=1
    if i == len(files)-1:
        i = 0
    src1 = cv2.resize(src1,(640,480),cv2.INTER_LINEAR)
    src2 = cv2.resize(src2,(640,480),cv2.INTER_LINEAR)

    t=0
    while t< ref.sPosition*5:  
        src = np.zeros((480,640,3), np.uint8)  
        mapper = map_pixel(t, src1, src2) 
        for x in range(ref.height):
            for y in range(ref.width):          
                src[x,y] = mapper(x, y)
                    
        cv2.imshow("tu",src) 
        t+= 100
        if cv2.waitKey(1) == ord('q') :
            break

    if cv2.waitKey(0) == ord('q') :
        break
 
    
