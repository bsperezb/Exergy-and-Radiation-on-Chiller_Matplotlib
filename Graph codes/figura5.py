import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#------------------		Funciones 	-----------------
def escala_grises_vector(cantidad):
    #cantidad =index.size
    vector = 3
    cantidad_colores = np.linspace(0.7,0.9,cantidad)
    #print(cantidad_colores)
    rgb_p = np.ones((cantidad,vector))
    for i in range(cantidad):
        for j in range(3):
            rgb_p[i,j] = rgb_p[i,j]*cantidad_colores[i]
    print(rgb_p)
    #print(cantidad)
    return rgb_p
#----------------------------------------------------

figura5 = pd.read_excel('Figura5.xlsx',
		header = 0,
		dtype = {'Month': str ,'Qg':float, 'Qc':float, 'Qa':float, 'Qe':float },
		usecols = [0,1,2,3,4])

matriz5 = figura5.T
matriz5 = matriz5.values
print(matriz5)

fig = plt.figure(5, figsize = [6,12])
#graf1 = fig.add_subplot()
#graf2 = fig.add_subplot()
#graf3 = fig.add_subplot()
#graf4 = fig.add_subplot()

index = np.arange(0,12)

bw=0.23
leyenda = ['$\dot{Q}g$', '$\dot{Q}c$', '$\dot{Q}a$', '$\dot{Q}e$']
color = escala_grises_vector(4)
print(color)


bar1 = plt.barh(index, matriz5[1],bw, color=color[0], hatch ='\\\\\\\\', label = leyenda[0])
bar2 = plt.barh(index+bw, matriz5[2],bw, color=color[1], hatch ='ooo', label = leyenda[1])
bar3 = plt.barh(index+bw*2, matriz5[3],bw, color=color[2], hatch ='xxx', label = leyenda[2])
bar3 = plt.barh(index+bw*3, matriz5[4],bw, color=color[3], hatch ='//////', label = leyenda[3])

#plt.title('$Enegy\ Flow$', fontsize= 30)
plt.axis([0,28,-0.2,12])
plt.yticks(index+bw*1.5, matriz5[0], fontsize = 12)
plt.minorticks_on()
plt.grid(True, which = 'major',ls='-.', lw=0.25)
plt.grid(True, which = 'minor',ls='-.', lw=0.25)
plt.legend(fontsize = 12)
plt.show()

