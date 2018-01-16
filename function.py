import cv2
import numpy as np
import math
import sys
import csv
import os
from datetime import datetime

def read_csv(csvfile_name):
    tmp = []
    with open(csvfile_name) as f:
        reader = csv.reader(f)
        for row in reader:
            tmp.append(np.float32(row))
    return tmp

def write_csv(csvfile_name, content):
    with open(csvfile_name, 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(content)

def computeMatrixFromAngles_Euler(degx, degy, degz):
    R = np.zeros((3, 3), np.float32)
    x = np.radians(degx)
    y = np.radians(degy)
    z = np.radians(degz)

    R[0, 0] = np.cos(y)*np.cos(z) - np.sin(x)*np.sin(y)*np.sin(z)
    R[0, 1] = -np.cos(x)*np.sin(z)
    R[0, 2] = np.sin(y)*np.cos(z) + np.sin(x)*np.cos(y)*np.sin(z)
    R[1, 0] = np.cos(y)*np.sin(z) + np.sin(x)*np.sin(y)*np.cos(z)
    R[1, 1] = np.cos(x)*np.cos(z)
    R[1, 2] = np.sin(y)*np.sin(z) - np.sin(x)*np.cos(y)*np.cos(z)
    R[2, 0] = -np.cos(x)*np.sin(y)
    R[2, 1] = np.sin(x)
    R[2, 2] = np.cos(x)*np.cos(y)

    return R

def computeMatrixFromAngles_roll_pith_yaw(degx, degy, degz):
    R = np.zeros((3, 3), np.float32)
    x = np.radians(degx)
    y = np.radians(degy)
    z = np.radians(degz)

    R[0, 0] = np.cos(x)*np.cos(y)
    R[0, 1] = np.cos(x)*np.sin(y)*np.sin(z) - np.sin(x)*np.cos(z)
    R[0, 2] = np.cos(x)*np.sin(y)*np.cos(z) + np.sin(x)*np.sin(z)

    R[1, 0] = np.sin(x)*np.cos(y)
    R[1, 1] = np.sin(x)*np.sin(y)*np.sin(z) + np.cos(x)*np.cos(z)
    R[1, 2] = np.sin(x)*np.sin(y)*np.cos(z) - np.cos(x)*np.sin(z)

    R[2, 0] = -np.sin(y)
    R[2, 1] = np.cos(y)*np.sin(z)
    R[2, 2] = np.cos(y)*np.cos(z)

    return R
