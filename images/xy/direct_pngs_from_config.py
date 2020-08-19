#!/usr/bin/env python3

import numpy as np
import cv2

dd = np.loadtxt("spin_angles.dat")
print(dd.shape)
ntemp = 60                      # number of temperatures

lsize = 256
cc = np.zeros((lsize, lsize, 3))
for i in range(ntemp):
    d = dd[i*lsize:(i+1)*lsize, :]
    d[:] = (d[:] % np.pi)
    px = np.floor(255 * d/np.pi)
    px = px.astype('uint8')
    cv2.imwrite('gray-' + str(i)+'.png', px)
    # prepare color images
    cc[:, :, 0] = 0.5 * (1 + np.cos(d))
    cc[:, :, 2] = 0.5 * (1 + np.sin(d))
    cc[:, :, 1] = 0.1
    cpx = np.floor(255 * cc).astype('uint8')
    cv2.imwrite('color-' + str(i)+'.png', cpx)
    print(i)
#
