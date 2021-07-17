import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#-------------------Funciones-------------------
def escala_grises_vector(cantidad):
    #cantidad =index.size
    vector = 3
    cantidad_colores = np.linspace(0.6,0.9,cantidad)
    #print(cantidad_colores)
    rgb_p = np.ones((cantidad,vector))
    for i in range(cantidad):
        for j in range(3):
            rgb_p[i,j] = rgb_p[i,j]*cantidad_colores[i]
    print(rgb_p)
    #print(cantidad)
    return rgb_p
#-----------------------------------------------

figura11 = pd.read_excel('Figura11.xlsx', 
		header=0,
		usecols = [0,1,2,3,4],
		dtype={'temperature':str})



matriz11 = figura11.T
matriz11 = matriz11.values
index = np.arange(0,3)
color = escala_grises_vector(4)
leyenda = ['Generator Exergy Destruyed [%]', 'Heat Exchanger Exergy Destroyed [%]', 'Pump Exergy Destroyed [%]', 'Asembly Destroyed [%]']


fig = plt.figure(constrained_layout=True, figsize = [6,12])
graph = fig.add_gridspec(nrows = 4, ncols= 1, wspace= 0.01)

ax1 = fig.add_subplot(graph[0,0])
ax2 = fig.add_subplot(graph[1,0])
ax3 = fig.add_subplot(graph[2,0])
ax4 = fig.add_subplot(graph[3,0])

bar1 = ax1.barh(matriz11[0], matriz11[1], color=color[0],hatch ='\\\\\\\\', label = leyenda[0])
bar2 = ax2.barh(matriz11[0], matriz11[2], color=color[1],hatch ='\\\\\\\\', label = leyenda[1])
bar3 = ax3.barh(matriz11[0], matriz11[3], color=color[2],hatch ='\\\\\\\\', label = leyenda[2])
bar3 = ax4.barh(matriz11[0], matriz11[4], color=color[3],hatch ='\\\\\\\\', label = leyenda[3])

ax1.title.set_text('Generator Exergy Destruyed [%]')
ax2.title.set_text(leyenda[1])

ax3.title.set_text(leyenda[2])
ax4.title.set_text(leyenda[3])

ax1.set_xlim(38.9,39.05)
ax2.set_xlim(6.44,6.68)
ax3.set_xlim(0.0060,0.0065)
ax4.set_xlim(54.3,54.5)

ax1.minorticks_on()
ax2.minorticks_on()
ax3.minorticks_on()
ax4.minorticks_on()

ax1.xaxis.grid(True, ls = '--', lw = 0.5)
ax1.xaxis.grid(True, ls = '--', lw = 0.5, which='minor')
ax2.xaxis.grid(True, ls = '--', lw = 0.5)
ax2.xaxis.grid(True, ls = '--', lw = 0.5, which='minor')
ax3.xaxis.grid(True, ls = '--', lw = 0.5)
ax3.xaxis.grid(True, ls = '--', lw = 0.5, which='minor')
ax4.xaxis.grid(True, ls = '--', lw = 0.5)
ax4.xaxis.grid(True, ls = '--', lw = 0.5, which='minor')

plt.show()


