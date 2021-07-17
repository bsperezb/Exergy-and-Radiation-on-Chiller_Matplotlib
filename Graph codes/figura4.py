import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

figura4 = pd.read_excel('Figura4.xlsx',header = 0, dtype={'x1':float, 'y1':float, 'x2':float, 'y2':float, 'x3':float, 'y3':float} )
print(figura4)

matriz4 = figura4.T 		
matriz4 = matriz4.values
print(matriz4)

label1= ['80%', '60%', '70%']
fig, graph = plt.subplots()
graph.plot(matriz4[0],matriz4[1], 'k-.^',matriz4[2],matriz4[3], 'k-*',matriz4[4], matriz4[5], 'k--o', linewidth = 1 )

graph.axis([-0.0034,-0.0025,1,100])
graph.set_yscale('log')
leyenda = graph.legend(label1, loc='best' , title = '%', frameon = True, borderaxespad=0.8, fontsize='large')

plt.minorticks_on()
plt.tick_params(which='major', length=6, width=1)
plt.tick_params(which='minor', length=3, color='k')
graph.set_xticks([-0.0034, -0.0032, -0.0030, -0.0028, -0.0026])

graph.grid(True, ls='-.', lw=0.25,)
plt.grid(b=True, which='minor', linestyle='-', alpha = 0.1)


#sub_graph = fig.add_axes([0.2,0.55,0.35,0.25], yscale = 'log', facecolor = 'k', title='ZOOM')
#sub_graph.set_xticks([1.5,2.5,3.5,4.5,5.5,6.5],minor=True)





plt.show()