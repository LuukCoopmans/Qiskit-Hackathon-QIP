#!/usr/bin/env python3

import numpy as np
import cv2

for i in range(99):
    fname = 'snapshot' + str(i).zfill(3)
    d=np.loadtxt(fname)
    px=d[:,2].reshape(64,64)*255
    px = px.astype('uint8')
    cv2.imwrite(str(i)+'.png', px)
    print(fname)
#
