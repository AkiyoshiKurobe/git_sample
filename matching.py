from function import *
from datetime import datetime

# img1 = cv2.imread("../generated_image_folder/generated_image_1.png")
# img2 = cv2.imread("../image/first01159.png")

img2 = cv2.imread("../ei2018/g5.jpg")
img1 = cv2.imread("../ei2018/result75.jpg")

# for i in range(0, 10):
#     img1 = cv2.bilateralFilter(img1, 15, 60, 30)

akaze = cv2.AKAZE_create()
orb = cv2.ORB_create()
brisk = cv2.BRISK_create()

kp1, des1 = akaze.detectAndCompute(img1, None)
kp2, des2 = akaze.detectAndCompute(img2, None)

# kp1, des1 = brisk.detectAndCompute(img1, None)
# kp2, des2 = brisk.detectAndCompute(img2, None)

# kp1, des1 = orb.detectAndCompute(img1, None)
# kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)
ratio = 0.75
good = []

for m, n in matches:
    if m.distance < ratio * n.distance:
        good.append([m])

img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good[:10], None, flags=2)

cv2.imshow('a', img3)
time_stump = datetime.now().strftime("%Y%m%d-%H%M%S")
cv2.imwrite('../matching_result_image/' + time_stump + '_generated.jpg', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
print "finish"
