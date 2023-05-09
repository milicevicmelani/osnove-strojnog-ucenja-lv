import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from mlxtend.plotting import plot_decision_regions
from sklearn . metrics import accuracy_score, classification_report, precision_score
from sklearn . metrics import confusion_matrix , ConfusionMatrixDisplay

X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
                            random_state=213, n_clusters_per_class=1, class_sep=1)

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

#A. Prikažite podatke za ucenje u x1−x2 ravnini matplotlib biblioteke pri cemu podatke obojite 
# s obzirom na klasu. Prikažite i podatke iz skupa za testiranje, ali za njih koristite drugi
# marker (npr. ’x’). Koristite funkciju scatter koja osim podataka prima i parametre c i
# cmap kojima je moguce definirati boju svake klase.


plt.figure()
plt.scatter(X_train[:,0],X_train[:,1],marker='o',c=y_train,cmap='viridis',s=10)
plt.scatter(X_test[:,0],X_test[:,0],marker='x',c=y_test,cmap='plasma',s=25)

#B. Izgradite model logisticke regresije pomocu scikit-learn biblioteke na temelju skupa podataka
# za ucenje.

LogRegression_model = LogisticRegression ()
LogRegression_model.fit ( X_train , y_train )

#c.
theta0=LogRegression_model.intercept_
coefs = LogRegression_model.coef_.T
a = -coefs[0]/coefs[1]
b = -theta0/coefs[1]

xy_min, xy_max = -4, 4

x1 = np.array([xy_min, xy_max])
y1 = a*x1 + b

plt.figure()
plt.plot(x1, y1, linestyle='--',label='Granica odluke')
plt.scatter(X_train[:, 0], X_train[:, 1], marker="o", c=y_train, s=10, cmap='plasma')

#D. Provedite klasifikaciju skupa podataka za testiranje pomocu izgradenog modela logisticke regresije. 
# Izracunajte i prikažite matricu zabune na testnim podacima. Izracunate tocnost,
# preciznost i odziv na skupu podataka za testiranje.

y_test_p = LogRegression_model.predict(X_test)

#matrica zabune
cm = confusion_matrix( y_test , y_test_p )
print("Matrica zabune:" , cm)
disp = ConfusionMatrixDisplay ( confusion_matrix (y_test , y_test_p ))
disp.plot ()

#tocnost
print (" Tocnost :\n ",accuracy_score(y_test , y_test_p ))
#preciznost
print("Preciznost logističke regresije: \n", precision_score(y_test,y_test_p))
#odziv
print ("Odziv:\n", classification_report(y_test , y_test_p ))

#E. Prikažite skup za testiranje u ravnini x1−x2. Zelenom bojom oznacite dobro klasificirane
# primjere dok pogrešno klasificirane primjere oznacite crnom bojom.

y_color = (y_test == y_test_p)
plt.figure()
plt.scatter(X_test[:, 0], X_test[:, 1], marker="o", c=y_color, s=15, cmap=mcolors.ListedColormap(["black", "green"]))
print(y_color)
plt.show()