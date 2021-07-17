import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#------------------		FUNCIONES	---------------------------
def etiquetas(vect_sum):
	tamaño = int(vect_sum.size)
	y = list(range(0,tamaño))
	for i in range(0,tamaño):
		x = float(vect_sum[i]) + 0.07
		aux = i + 0.17
		y = plt.text(x,aux,vect_sum[i], fontsize=9,alpha=0.8 )
	return y
#-------------------	FIN FUNCIONES	-----------------------
#import CSV
figura3 = pd.read_csv('figura3.csv',sep=';', 
		encoding = 'utf-8', 
		dtype= {'Month':str, 'IDH':float, 'Idh':float, 'ITH':float}, 
		usecols = [0,1,2,3],
		header=0)
#figurax = figura3.T 		con esto se resume lo siguiente.
#seriesx = figurax.values
#print(seriesx)

vect_sum = figura3.iloc[:,3]
vect_sum = vect_sum.T
vect_totales = vect_sum.values

index_1 = figura3.iloc[:,0]
serie_1 = figura3.iloc[:,1]
serie_2 = figura3.iloc[:,2]

index_1 = index_1.T
index_1 = index_1.values
serie_1 = serie_1.T
serie_1 = serie_1.values
serie_2 = serie_2.T
serie_2 = serie_2.values

color = [0.98,0.98,0.98]
color1 = [0.9,0.9,0.9]
#plt.title('$Total\ Solar\ Radiation$', fontsize=16, )
plt.grid(True, ls='-.', lw=0.25,)
plt.axis([0,9,11.5,-0.5])

#plt.tick_params(which='both',width=2)
#plt.tick_params(which='major', length=7)
#plt.tick_params(which='minor', length=4, color='r')

ax = plt.barh(index_1, serie_1, color = color1, hatch ='\\\\\\\\')
plt.barh(index_1, serie_2, color = color1, hatch = 'ooo', left= serie_1)
#plt.axis.set_minor_locator(tck.AutoMinorLocator())
plt.ylabel('$Month$', fontsize=12)
plt.xlabel(r'$Solar\ Radiation\ [\frac{kWh}{m^2}]$', fontsize=12)
plt.legend(['Solar Direct Radiation [IDH]', 'Solar Fuzzy Radiation [IdH]'],
		 bbox_to_anchor=(0., 1.02, 1., .102),
		 loc='lower left',
         ncol=2, mode="expand", 
         borderaxespad=0.)
plt.minorticks_on()
etiquetas(vect_totales)
#etiquetas_box(serie_1)

plt.show()
#print(figura3)
#print(figura3['Month'])
#print(figura3.sort_values(by='IDH'))