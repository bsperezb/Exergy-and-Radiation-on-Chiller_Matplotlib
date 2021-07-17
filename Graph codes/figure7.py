import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

figura7 = pd.read_excel('Figura 7.xlsx',
		header = 0, 
		dtype={'Month':str, 'x':float, 'y':float},
		usecols=[0,1,2,3,4,5])
print(figura7)

matriz7 = figura7.T
matriz7 = matriz7.values
print(matriz7)
#main graph -------------------------
fig,ax_main = plt.subplots()
ax_main.plot(matriz7[0],matriz7[1], 'k-.^',matriz7[2],matriz7[3], 'k-*',matriz7[4], matriz7[5], 'k--o', linewidth = 1)
ax_main.set_xlabel('Generator Temperature [°C]', fontsize = 10)
ax_main.set_ylabel('COP', fontsize = 10)
#ax_main.set_title('titulo', fontsize = 14 )
ax_main.minorticks_on()
ax_main.grid(True, ls = '--', lw = 0.5)
ax_main.grid(True, which='minor', ls = '-.', lw=0.2)
#subplot -----------------------------------
ax_sub = fig.add_axes([0.52,0.38,0.35,0.25])
ax_sub.set_xlim([85,90])
ax_sub.set_ylim([0.70,0.78])
ax_sub.plot(matriz7[0],matriz7[1], 'k-.^',matriz7[2],matriz7[3], 'k-*',matriz7[4], matriz7[5], 'k--o', linewidth = 1)
ax_sub.minorticks_on()
ax_sub.grid(True, ls = '--', lw = 0.5)
ax_sub.grid(True, which='minor', ls = '-.', lw= 0.2)

leyenda = ['2°', '4°', '7°']
ax_main.legend(leyenda, title='Evaporator Temperature',
		loc='lower center',
		frameon = True, 
		borderaxespad=0.9, 
		fontsize= 9)
plt.show()