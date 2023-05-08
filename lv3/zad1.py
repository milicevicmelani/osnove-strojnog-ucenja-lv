import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("lv3\\data_C02_emission.csv" )


#A. broj mjerenja
print ("Ukupno je",len(data),"mjerenja")

#  tip svake veličine
print (data.dtypes)

#  izostale,duplicirane vrijednosti
print ("Izostale vrijednosti:",data.isnull().sum())
print("Duplicirane vrijednosti:",data.duplicated().sum())
data.dropna(axis=0)
data.drop_duplicates()
#promjena kategorickih velicina
data[['Make', 'Model','Vehicle Class','Transmission','Fuel Type']] = data[['Make', 'Model','Vehicle Class','Transmission','Fuel Type']].astype('category')
print(data.dtypes)

#B. 3 automobila najvece/najmanje gradske potrošnje
fuel_data=data.sort_values(by=['Fuel Consumption City (L/100km)'],ascending=False)
print("Najveca gradska potrošnja:\n",fuel_data.head(3)[['Make','Model','Fuel Consumption City (L/100km)']])
print("Najmanja gradska potrošnja:\n",fuel_data.tail(3)[['Make','Model','Fuel Consumption City (L/100km)']])

#C. Koliko vozila ima velicinu motora izmedu 2.5 i 3.5 L?
#  Kolika je prosjecna C02 emisija plinova za ova vozila?
engine_data=data[(data['Engine Size (L)']>2.5) & (data['Engine Size (L)'] < 3.5)]
print("Broj vozila velicine motora izmedu 2.5 i 3.5 L:",len(engine_data))
print("Prosjecna CO2 emsija plinova za ta vozila:", engine_data['CO2 Emissions (g/km)'].mean())

#D.Koliko mjerenja se odnosi na vozila proizvodaca Audi?
#  Kolika je prosjecna emisija C02 plinova automobila proizvodaca Audi koji imaju 4 cilindara?
Audi_data=data[data['Make']=='Audi']
print("Broj mjerenja vozila proizvodaca Audi:",len(Audi_data))
print("Prosjecna emisija CO2 plinova Audi automobila sa 4 cilindra", Audi_data['CO2 Emissions (g/km)'][Audi_data['Cylinders']==4].mean().round(2))

#E. Koliko je vozila s 4,6,8. . . cilindara? 
# Kolika je prosjecna emisija C02 plinova s obzirom na broj cilindara?
evenCylinders_data=data[data['Cylinders']%2==0]
print("Broj vozila s parnim brojem cilindara:",len(evenCylinders_data))
print("Prosjecna emisija CO2 plinova ovinso o broju cilindara \n",evenCylinders_data.groupby('Cylinders')['CO2 Emissions (g/km)'].mean().round(2))

#F. Kolika je prosjecna gradska potrošnja u slucaju vozila koja koriste dizel, 
# a kolika za vozila koja koriste regularni benzin? 
# Koliko iznose medijalne vrijednosti?

print("Prosjecna potrosnja dizel automobila:", data['Fuel Consumption City (L/100km)'][data['Fuel Type']=='D'].mean().round(2))
print("Prosjecna potrosnja regulanog benzin automobila:", data['Fuel Consumption City (L/100km)'][data['Fuel Type']=='X'].mean().round(2))

#G. Koje vozilo s 4 cilindra koje koristi dizelski motor ima najve´cu gradsku potrošnju goriva?
diesel_4Cylinders_data=data[(data['Cylinders']==4) & (data['Fuel Type']=='X')]
diesel_4Cylinders_data.sort_values(by='Fuel Consumption City (L/100km)',ascending=True)
print("Dizel automobil s najvecom  gradskom potrosnjom goriva:\n",diesel_4Cylinders_data.head(1))

#H. Koliko ima vozila ima rucni tip mjenjaca (bez obzira na broj brzina)?
manual_data=data[data['Transmission']=='M']
print("Broj vozila s rucnim mjenjačom: ", len(manual_data))

#I. Izracunajte korelaciju izmedu numerickih velicina. Komentirajte dobiveni rezultat.
print ( data.corr(numeric_only = True))