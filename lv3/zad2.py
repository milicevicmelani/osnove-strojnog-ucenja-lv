import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("lv3\\data_C02_emission.csv" )

#A.Pomocu histograma prikažite emisiju C02 plinova. Komentirajte dobiveni prikaz.
plt.figure ('CO2 Emissions')
data['CO2 Emissions (g/km)'].plot(kind ='hist', bins = 20)

#B.Pomocu dijagrama raspršenja prikažite odnos izmedu gradske potrošnje goriva i emisije 
# C02 plinova. Komentirajte dobiveni prikaz. Kako biste bolje razumjeli odnose izmedu 
# velicina, obojite tockice na dijagramu raspršenja s obzirom na tip goriva.

fuel=data['Fuel Type']
fuel_colors={'X':'red', 'Z':'blue' ,'D':'green' ,'E':'yellow', 'N':'orange'} #different color for each fuel type
fuel_type={'X':'Regular gasoline', 'Z':'Premium gasoline' ,'D':'Diesel' ,'E':'Ethanol (E85)', 'N':'Natural gas'}

data.plot.scatter(x='Fuel Consumption City (L/100km)',y='CO2 Emissions (g/km)',c=[fuel_colors[g] for g in fuel],s=5)
legenda = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=fuel_colors[f], markersize=10, label=fuel_type[f]) for f in fuel_colors]
plt.legend(handles=legenda)
plt.title('Fuel Consumption and Emission by Fuel Type')
plt.xlabel('Fuel Consumption City (L/100km)')
plt.ylabel('CO2 Emissions (g/km)')


#C. Pomocu kutijastog dijagrama prikažite razdiobu izvangradske potrošnje s obzirom na tip goriva. 
# Primjecujete li grubu mjernu pogrešku u podacima?

data.boxplot( column =['Fuel Consumption Hwy (L/100km)'], by='Fuel Type')

#D.Pomocu stupcastog dijagrama prikažite broj vozila po tipu goriva. Koristite metodu groupby.
fig, (ax1, ax2) = plt.subplots(2, 1)
vehicles_byFuel=data.groupby('Fuel Type')['Make'].count()
vehicles_byFuel.plot.bar(ax=ax1,color='red')
ax1.set_title('Number of cars by fuel type')
ax1.set_ylabel('Number of cars')

#E. Pomocu stupcastog grafa prikažite na istoj slici prosjecnu C02 emisiju vozila s obzirom na broj cilindara.
average_emission=data.groupby('Cylinders')['CO2 Emissions (g/km)'].mean()
average_emission.plot.bar(ax2)
ax2.set_title('Average CO2 emission depending on number of cylinders')
ax2.set_ylabel('Average CO2 emission')
plt.tight_layout()
plt.show()