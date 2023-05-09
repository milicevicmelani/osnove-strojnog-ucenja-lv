from sklearn . model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
from sklearn.preprocessing import StandardScaler
import sklearn.metrics 
import math

# ucitaj ugradeni podatkovni skup
data = pd.read_csv("lv3\\data_C02_emission.csv" )

data.drop(["Make", "Model"], axis = 1)

input_variables = ['Fuel Consumption City (L/100km)','Fuel Consumption Hwy (L/100km)','Fuel Consumption Comb (L/100km)','Fuel Consumption Comb (mpg)', 'Engine Size (L)', 'Cylinders']

output_variable = ['CO2 Emissions (g/km)']

X = data[input_variables].to_numpy()
y = data[output_variable].to_numpy()

X_train , X_test , y_train , y_test = train_test_split(X , y , test_size = 0.2, random_state = 1)

#B.Pomocu matplotlib biblioteke i dijagrama raspršenja prikažite ovisnost emisije C02 plinova
# o jednoj numerickoj velicini. Pri tome podatke koji pripadaju skupu za ucenje oznacite plavom bojom, 
# a podatke koji pripadaju skupu za testiranje oznacite crvenom bojom.

plt.scatter(X_train[:,0],y_train,c='blue',label='train')
plt.xlabel('Fuel Consumption City (L/100km)')
plt.scatter(X_test[:,0],y_test,c='red',label='test')
plt.xlabel('Fuel Consumption City (L/100km)')
plt.legend()

#C. Izvršite standardizaciju ulaznih velicina skupa za ucenje. Prikažite histogram vrijednosti
#jedne ulazne velicine prije i nakon skaliranja. Na temelju dobivenih parametara skaliranja
#transformirajte ulazne velicine skupa podataka za testiranje.

sc = StandardScaler ()
X_train_n = sc.fit_transform(X_train)
X_test_n = sc. transform ( X_test )

plt.figure("Prije sklairanja")
plt.hist(X_train[:,0],label='Prije skaliranja',color='orange')
plt.xlabel('Fuel Consumption City (L/100km)')
plt.figure("Nakon skaliranja")
plt.hist(X_train_n[:,0],label='Nakon skaliranja',color='green')
plt.xlabel('Fuel Consumption City (L/100km)')

#D.Izgradite linearni regresijski modeli. Ispišite u terminal dobivene parametre modela i
# povežite ih s izrazom 4.6
linearModel = lm.LinearRegression ()
linearModel.fit( X_train_n , y_train )
print(y_train)

#E Izvršite procjenu izlazne velicine na temelju ulaznih velicina skupa za testiranje. 
# Prikažite pomocu dijagrama raspršenja odnos izmedu stvarnih vrijednosti izlazne velicine i procjene
# dobivene modelom.

y_test_p = linearModel.predict(X_test_n)
plt.figure('Real vs predicted')
plt.scatter(y_test,y_test_p,label='Real vs predicted')


#F Izvršite vrednovanje modela na nacin da izracunate vrijednosti regresijskih metrika na skupu 
# podataka za testiranje.

MAE =sklearn.metrics.mean_absolute_error( y_test , y_test_p )
print("Vrednjovanje modela MAE:",MAE)
MSE=sklearn.metrics.mean_squared_error(y_test,y_test_p)
print("Vrednjovanje modela MSE:",MSE)
RMSE=math.sqrt(MSE)
print("Vrednjovanje modela RMSE:",RMSE)
MAPE=sklearn.metrics.mean_absolute_percentage_error(y_test,y_test_p)
print("Vrednjovanje modela MAPE:",MAPE)
R2=sklearn.metrics.r2_score(y_test,y_test_p)
print("Vrednjovanje modela R2:",R2)

#G. Što se dogada s vrijednostima evaluacijskih metrika na testnom skupu kada mijenjate broj ulaznih velicina?

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size = 0.4,random_state=1)

ss = StandardScaler()
X_train_n=ss.fit_transform(X_train)
X_test_n=ss.transform(X_test)

linModel = lm.LinearRegression()
linModel.fit(X_train_n,y_train)
print(linModel.coef_)

y_test_p=linModel.predict(X_test_n)

MAE=sklearn.metrics.mean_absolute_error(y_test,y_test_p)
MSE=sklearn.metrics.mean_squared_error(y_test,y_test_p)
RMSE=math.sqrt(MSE)
MAPE=sklearn.metrics.mean_absolute_percentage_error(y_test,y_test_p)
R2=sklearn.metrics.r2_score(y_test,y_test_p)

print("Vrednovanje metrika nakon promjene broja ulaznih velicina")
print('MAE:',MAE)
print('MSE:',MSE)
print('RMSE:',RMSE)
print('MAPE:',MAPE)
print('R2:',R2)

plt.show()

