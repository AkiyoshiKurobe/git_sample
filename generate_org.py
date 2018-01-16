import cv2
import numpy as np
import math
import sys
import csv
from function import *

rotation_tmp = []
translation_tmp = []
point_cloud = []

fx = 794.3418
fy = 798.8184
cx = 982.8135
cy = 549.8863

A = [[fx, 0, cx], [0, fy, cy], [0, 0, 1]]
A = np.array(A)

point_tmp = []
rotation_tmp = []

with open('Ogura_Rikkyo_2_downsampling.csv') as point:
    reader_point = csv.reader(point)
    for row in reader_point:
        point_tmp.append(np.float32(row))

point_cloud = np.reshape(point_tmp, (len(point_tmp), 6))


with open('rotation.csv') as r:
    reader_rotation = csv.reader(r)
    for row_rotation in reader_rotation:
        rotation_tmp.append(np.float32(row_rotation))

r = np.array([[rotation_tmp[0][0]], [rotation_tmp[0][1]], [rotation_tmp[0][2]]])
R = cv2.Rodrigues(r)[0]

with open('translation.csv') as t:
    reader_translation = csv.reader(t)
    for row_translation in reader_translation:
        translation_tmp.append(np.float32(row_translation))

t = np.array([[translation_tmp[0][0]], [translation_tmp[0][1]], [translation_tmp[0][2]]])
R_inv = R.T
t_inv = -R_inv.dot(t)

Rt = np.array(np.hstack((R_inv, t_inv)))
Rt = np.array(np.hstack((R, t)))
P_mat = np.array(A.dot(Rt))

generate_image_tmp = np.ones((1088,2048,3))
generate_image = np.zeros_like(generate_image_tmp)

for i in point_cloud:
    t_tmp = np.array([[i[0]], [i[1]], [i[2]], [1.0]])
    tmp = np.array(P_mat.dot(t_tmp))
    u = int(tmp[0] / tmp[2])
    v = int(tmp[1] / tmp[2])

    if u >=0 and u <=1087 and v >= 0 and v <= 2043:
        generate_image[u][v][0] = i[3]
        generate_image[u][v][1] = i[4]
        generate_image[u][v][2] = i[5]

# cv2.imshow("sample", generate_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cv2.imwrite('generate_image.png', generate_image)
print "finish"
