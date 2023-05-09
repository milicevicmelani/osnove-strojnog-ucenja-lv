from sklearn . model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
from sklearn.preprocessing import OneHotEncoder
import sklearn . linear_model as lm
import sklearn.metrics 
import math

# Na temelju rješenja prethodnog zadatka izradite model koji koristi i kategoricku
#  varijable „Fuel Type“ kao ulaznu velicinu. Pri tome koristite 1-od-K kodiranje kategorickih
# velicina. Radi jednostavnosti nemojte skalirati ulazne velicine. Komentirajte dobivene rezultate.
# Kolika je maksimalna pogreška u procjeni emisije C02 plinova u g/km? O kojem se modelu
# vozila radi?

data = pd.read_csv("lv3\\data_C02_emission.csv" )

data.drop(["Make", "Model"], axis = 1)

input_variables = ['Fuel Consumption City (L/100km)','Fuel Consumption Hwy (L/100km)','Fuel Consumption Comb (L/100km)','Fuel Consumption Comb (mpg)', 'Engine Size (L)', 'Cylinders','Fuel Type']

output_variable = ['CO2 Emissions (g/km)']

ohe = OneHotEncoder ()
X_encoded = ohe.fit_transform (data[['Fuel Type']]). toarray ()
data['Fuel Type']=X_encoded

X = data[input_variables]
y = data[output_variable]

X_train , X_test , y_train , y_test = train_test_split(X , y , test_size = 0.2, random_state = 1)

linearModel = lm.LinearRegression()
linearModel.fit(X_train,y_train)
print(linearModel.coef_)


y_test_p = linearModel.predict(X_test)

MAE =sklearn.metrics.mean_absolute_error( y_test , y_test_p )
print("Vrednjovanje modela MAE:",MAE.round(2))
MSE=sklearn.metrics.mean_squared_error(y_test,y_test_p)
print("Vrednjovanje modela MSE:",MSE.round(2))
RMSE=math.sqrt(MSE)
print("Vrednjovanje modela RMSE:",RMSE)
MAPE=sklearn.metrics.mean_absolute_percentage_error(y_test,y_test_p)
print("Vrednjovanje modela MAPE:",MAPE.round(2))
R2=sklearn.metrics.r2_score(y_test,y_test_p)
print("Vrednjovanje modela R2:",R2.round(2))

error = abs(y_test_p-y_test)
model= data['Model'].to_numpy()

print('Najveća greška iznosi:',np.max(error).round(2))
print('Model auta s maksimalnom greškom procjene emisije CO2 plinova je',model[np.argmax(error)])