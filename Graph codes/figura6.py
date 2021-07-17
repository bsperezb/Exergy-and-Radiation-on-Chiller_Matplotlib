import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

figura6 = pd.read_excel('Figura6.xlsx',
		header = 0, 
		dtype={'Month':str, 'x':float, 'y':float},
		usecols=[0,1,2],)
print(figura6)

matriz6 = figura6.T
matriz6 = matriz6.values
print(matriz6)

index1 = matriz6[0]
index = np.arange(0,12)
x1 = matriz6[1]
x2 = matriz6[2]

fig = plt.figure(6)
graf1= fig.add_subplot(111)
graf2 = graf1.twinx()
#plt.title('Mass Flow')

#creo barras
color = [0.98,0.98,0.98]
color1 = [0.9,0.9,0.9]
leyenda = ['Mass Flow Ratio', 'Mass Flow in Evaporator']

bw = 0.3
bar1 = graf1.bar(index, x1,bw, color=color,hatch ='\\\\\\\\', label = leyenda[1])
bar2 = graf2.bar(index+bw, x2,bw, color= color1,hatch ='xxxxx',label=leyenda[0] )

plt.xlabel('')
#graf1.yaxes(0,0.08)
plt.minorticks_on()
plt.xticks(index+0.5*bw, index1)
graf1.grid(True, which = 'major',ls='-.', lw=0.25)
graf2.grid(True, which = 'major',ls='-.', lw=0.25)
graf1.legend(loc=2)
graf2.legend()
graf1.set_ylim(0,0.06)
graf2.set_ylim(0,0.1)
plt.show()
