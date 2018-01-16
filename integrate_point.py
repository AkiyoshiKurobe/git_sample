from function import *

# point_cloud_2_tmp = read_csv("Ogura_Rikkyo_2_half.csv")
# point_cloud_2_tmp = np.array(point_cloud_2_tmp)
# point_cloud_3_tmp = read_csv("Ogura_Rikkyo_3_half.csv")
# point_cloud_3_tmp = np.array(point_cloud_3_tmp)
#
# point_cloud_2 = np.array(np.reshape(point_cloud_2_tmp, (len(point_cloud_2_tmp), 6)))
# point_cloud_3 = np.array(np.reshape(point_cloud_3_tmp, (len(point_cloud_3_tmp), 6)))
#
# np.save('Ogura_Rikkyo_2_half.npy', point_cloud_2)
# np.save('Ogura_Rikkyo3_half.npy', point_cloud_3)

# point2 = np.load("./Ogura_Rikkyo_2_half.npy")
# point3 = np.load("./Ogura_Rikkyo_3_half.npy")
#
# point_2_and_3_half_integrate = np.concatenate((point2, point3), axis=0)
# np.save("point_2_and_3_half_integrate.npy", point_2_and_3_half_integrate)

# point_2_3 = np.load("../npy/point_2_and_3_half_integrate_converted.npy")
# point_light = np.unique(point_2_3, axis=0)

# point2 = np.load("../npy/Ogura_Rikkyo_2.npy")
# point2_light = np.unique(point2, axis=0)

# data = np.array([[1, 1], [1, 1], [1, 2], [1, 2], [1, 3]])
# data_light = np.unique(data, axis=0)


# point_densoit_tmp = read_csv("../csv/d_las.csv")
# point_densoit_tmp = np.array(point_densoit_tmp)
# point_densoit = np.array(np.reshape(point_densoit_tmp, (len(point_densoit_tmp), 11)))
# np.save("d_las.npy", point_densoit)

# a = np.random.rand(3, 5)
# b = a[:, 0:1:3]
# print a
# print b

# point_densoit = []
# point_densoit_org = np.load("../npy/d_las.npy")
# point_densoit_xyz = point_densoit_org[:, 0:3]
# point_densoit_rgb = point_densoit_org[:, 7:10]
# point_densoit_xyz_rgb_org = np.concatenate((point_densoit_xyz, point_densoit_rgb), axis=1)
#
# for i in point_densoit_xyz_rgb_org:
#     if not(i[3] == 0 and i[4] == 0 and i[5] == 0):
#         point_densoit.append(i)
#
# print "finish"


# vector_final = []
# vector = np.array(range(25)).reshape(5,5)
#
# for i in vector:
#     if i[2] == 2 and i[3] == 3:
#         vector_final.append(i)

# point_tmp = np.load("../npy/denso.npy")
# point = np.unique(point_tmp, axis=0)

# point_denso = np.load("../npy/denso.npy")
# np.savetxt('../csv/denso.csv', point_denso, delimiter=',')

point_cloud_org = np.load('../npy/point_2_and_3_half_integrate_converted.npy')
rows, cols = np.where(point_cloud_org < 0)
point_cloud = np.delete(point_cloud_org, rows[np.where(cols == 1)], 0)

# np.savetxt('../csv//point_2_and_3_half_integrate_converted_cut.csv', point_cloud, delimiter=',')
np.save('../npy//point_2_and_3_half_integrate_converted_cut.npy', point_cloud)
