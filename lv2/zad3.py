import numpy as np
import matplotlib . pyplot as plt

img = plt.imread ("lv2\\road.jpg")

#A. posvijetli
plt.figure(1)
plt.imshow (img,cmap ="gray",alpha=0.5)

#B. crop
h,w,_=img.shape
w=w//4
crop_img=img[1:h,1:w]
plt.figure(2)
plt.imshow(crop_img)


#C. zaokreni
rotate_img=np.rot90(img,3)
plt.figure(3)
plt.imshow(rotate_img)

#D. zrcali
mirror_img=np.fliplr(img)
plt.figure(4)
plt.imshow(mirror_img)


plt.show()