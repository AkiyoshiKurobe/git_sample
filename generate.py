from function import *
from datetime import datetime
import numpy as np
import cv2

point_cloud = []

fx = 794.3418
fy = 798.8184
cx = 982.8135
cy = 549.8863

A = [[fx, 0, cx], [0, fy, cy], [0, 0, 1]]
A = np.array(A)
# point_cloud_tmp = read_csv('converted_pointcloud.csv')
# point_cloud = np.array(point_cloud_tmp)

point_cloud = np.load('../npy/point_2_and_3_half_integrate_converted_cut.npy')

translation_tmp = read_csv('../csv/translation_generate.csv')
t = np.array([[translation_tmp[0][0]], [translation_tmp[0][1]], [translation_tmp[0][2]]])

rotation_tmp = read_csv('../csv/rotation.csv')
r = r = np.array([[rotation_tmp[0][0]], [rotation_tmp[0][1]], [rotation_tmp[0][2]]])
R = cv2.Rodrigues(r)[0]

R_inv = R.T
t_inv = -R_inv.dot(t)
Rt = np.array(np.hstack((R_inv, t_inv)))
# Rt = np.array(np.hstack((R, t)))
P_mat = np.array(A.dot(Rt))

generate_image_tmp = np.ones((1088, 2044, 3))
generate_image = np.zeros_like(generate_image_tmp)

for i in point_cloud:
    if i[2] > 0:
        t_tmp = np.array([[i[0]], [i[1]], [i[2]], [1.0]])
        tmp = np.array(P_mat.dot(t_tmp))
        u = 1088 - int(tmp[1] / tmp[2])
        v = int(tmp[0] / tmp[2])

        if u >=0 and u <=1087 and v >= 0 and v <= 2043:
            generate_image[u][v][0] = i[5]
            generate_image[u][v][1] = i[4]
            generate_image[u][v][2] = i[3]

time_stump = datetime.now().strftime("%Y%m%d-%H%M%S")
cv2.imwrite('../generated_image/' + time_stump + '_generated.jpg', generate_image)
print "finish"

