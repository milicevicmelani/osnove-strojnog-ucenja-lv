import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as Image
from sklearn.cluster import KMeans
import random

# ucitaj sliku
img = Image.imread("lv7\\imgs\\test_1.jpg")

# prikazi originalnu sliku
plt.figure()
plt.title("Originalna slika")
plt.imshow(img)
plt.tight_layout()

# pretvori vrijednosti elemenata slike u raspon 0 do 1
img = img.astype(np.float64) / 255

# transfromiraj sliku u 2D numpy polje (jedan red su RGB komponente elementa slike)
w,h,d = img.shape
img_array = np.reshape(img, (w*h, d))

# rezultatna slika
img_array_aprox = img_array.copy()
unique_colors=len(np.unique(img_array_aprox,axis=0))

print("Broj prisutnih boja u slici:",unique_colors)
clusters=3

# inicijalizacija algoritma K srednjih vrijednosti
km = KMeans ( n_clusters =clusters)
# pokretanje grupiranja primjera
km. fit (img_array_aprox)
# dodijeljivanje grupe svakom primjeru
labels = km. predict (img_array_aprox)

rgb_cols = km.cluster_centers_.astype(np.float64)
print(rgb_cols)
img_quant = np.reshape(rgb_cols[labels],(w,h,d))

plt.figure()
plt.imshow(img_quant)


#6

distortions = []
K = range(1,10)
for k in K:
    kmeanModel = KMeans(n_clusters=k)
    kmeanModel.fit(img_array)
    distortions.append(kmeanModel.inertia_)

plt.figure(figsize=(16,8))
plt.plot(K, distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal k')


#7

for i in range(clusters): 
    bit_values = labels==[i]
    binary_img = np.reshape(bit_values, (img.shape[0:2]))
    binary_img = binary_img*1
    x=int(i/2)
    y=i%2

plt.figure("Binary image")
plt.imshow(binary_img)
plt.show()