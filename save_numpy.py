from function import *

point_tmp = read_csv('./Ogura_Rikkyo_2.csv')
point = np.array(np.reshape(point_tmp, (len(point_tmp), 6)))
np.save('Ogura_Rikkyo_2.npy', point)
