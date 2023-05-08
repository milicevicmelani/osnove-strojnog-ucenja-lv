import numpy as np
import matplotlib.pyplot as plt

#učitavanje data.csv ali bez prvog retka
array=np.loadtxt("lv2\data.csv",skiprows=1,delimiter=',')

#A. Izračun broja osoba na kojima je provedeno mjerenje
lenght=len(array)
print(lenght)

#B. Odnos visine i mase
plt.figure(1)
for i in range(lenght):
    plt.scatter(array[i,1],array[i,2])


#C. Odnos visine i mase za svaku 50tu osobu
plt.figure(2)
for i in range(0,lenght,50):
    plt.scatter(array[i,1],array[i,2])
#plt.show()

#D. minimalna,maksimalna i prosječna visina 
print("Minimalna visina:", np.min(array[:,1]))
print("Maksialna visina:", np.max(array[:,1]))
print("Prosječna visina", np.average(array[:,1]))

#E. 
male_data = array[array[:, 0] == 1]
female_data = array[array[:, 0] == 0] 

print("Minimalna muska visina:", np.min(male_data[:,1]),"Minimalna zenska visina:",np.min(female_data[:,1]))
print("Maksimalna muska visina:", np.max(male_data[:,1]),"Maksimalna zenska visina:",np.max(female_data[:,1]))
print("Prosječna muska visina:", np.average( male_data[:,1]),"Prosječna zenska visina:",np.average(female_data[:,1]))


