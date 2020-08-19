#!/usr/bin/env python3

import numpy as np
import cv2

dd = np.loadtxt("spin_angles.dat")
print(dd.shape)
ntemp = 60                      # number of temperatures

lsize = 256
cc = np.zeros((lsize, lsize, 3))

# original
DIR = '256'
for i in range(ntemp):
    d = dd[i*lsize:(i+1)*lsize, :]
    d[:] = (d[:] % np.pi)
    px = np.floor(255 * d/np.pi)
    px = px.astype('uint8')
    cv2.imwrite(DIR + '/' + 'gray-' + str(i)+'.png', px)
    # prepare color images
    cc[:, :, 0] = 0.5 * (1 + np.cos(d))
    cc[:, :, 2] = 0.5 * (1 + np.sin(d))
    cc[:, :, 1] = 0.1
    cpx = np.floor(255 * cc).astype('uint8')
    cv2.imwrite(DIR + '/' + 'color-' + str(i)+'.png', cpx)
    print(i)
#

# reduced 64,64
DIR = '64'
for i in range(ntemp):
    d = dd[i*lsize:(i+1)*lsize, :]
    d[:] = (d[:] % np.pi)
    px = np.floor(255 * d/np.pi)
    px = px.astype('uint8')
    rpx = cv2.resize(px, (64, 64), interpolation=cv2.INTER_AREA)
    cv2.imwrite(DIR + '/' + 'gray-' + str(i)+'.png', rpx)
    # prepare color images
    cc[:, :, 0] = 0.5 * (1 + np.cos(d))
    cc[:, :, 2] = 0.5 * (1 + np.sin(d))
    cc[:, :, 1] = 0.1
    cpx = np.floor(255 * cc).astype('uint8')
    rcx = cv2.resize(cpx, (64, 64), interpolation=cv2.INTER_AREA)
    cv2.imwrite(DIR + '/' + 'color-' + str(i)+'.png', rpx)
    print(i)
#
