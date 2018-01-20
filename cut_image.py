from function import *
import cv2
img_org = cv2.imread("./generate_image_1.png")

dst_img = img_org[0:200,900:1200]
cv2.imwrite("cut_image.png", dst_img)
print "testtest"
