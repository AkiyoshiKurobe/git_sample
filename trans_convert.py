import cv2
import numpy as np
import math
import sys
import csv
from function import *

t_converted = []
convert_point_cloud = []

# point_cloud_rgb = np.reshape(point_tmp, (len(point_tmp), 6))
# point_cloud_rgb = np.load('./Ogura_Rikkyo_2_downsampling.npy')
point_cloud_rgb = np.load('../npy/point_2_and_3_half_integrate.npy')
# point_cloud_rgb = np.load("../np/denso.npy")

# point_cloud_rgb[:, 2:3] = -point_cloud_rgb[:, 2:3]
point_cloud_T = point_cloud_rgb[:, 0:3].T

translation_tmp = read_csv('../csv/translation.csv')
t = np.array([[translation_tmp[0][0]], [translation_tmp[0][1]], [translation_tmp[0][2]]])

# rotation_tmp = read_csv('rotation.csv')
# r = r = np.array([[rotation_tmp[0][0]], [rotation_tmp[0][1]], [rotation_tmp[0][2]]])
# R = cv2.Rodrigues(r)[0]

# R = computeMatrixFromAngles_roll_pith_yaw(96,47,-5.1)
# R = computeMatrixFromAngles_roll_pith_yaw(-60, 0, 90) good_result
# t = (2.32,24,-2.5) good_result
# t = (-4.59,18.47,2.0) good result
R = computeMatrixFromAngles_roll_pith_yaw(-60, 0, 90)

R_inv = R.T
t_inv = -R_inv.dot(t)
Rt = np.array(np.hstack((R_inv, t_inv)))

# converted_pointcloud = np.concatenate(((R.dot(point_cloud_T) + t).T, point_cloud_rgb[:, 3:6]), axis=1)
converted_pointcloud = np.concatenate((R_inv.dot(point_cloud_T - t).T, point_cloud_rgb[:, 3:6]), axis=1)
converted_pointcloud[:, 2:3] = -converted_pointcloud[:, 2:3]
# Rt = np.array(np.hstack((R, t)))

write_csv('../csv/point_2_and_3_half_integrate_converted.csv', converted_pointcloud)
np.save('../npy/point_2_and_3_half_integrate_converted.npy', converted_pointcloud)
print "finish"
