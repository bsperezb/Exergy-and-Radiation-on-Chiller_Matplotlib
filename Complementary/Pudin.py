import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

V=[24, 13, 6, 2] 								#sobresalir el primero
labels = ['Celular', ' Radio', 'Enlase', 'Otros']
colores = ['yellow','green','red','blue']
sobresalir = [0,0,0,0.3]
plt.pie( V, labels=labels, colors=colores, explode = sobresalir, shadow=True, startangle = 180, autopct="%0.1f %%"  )
plt.title('Alarma por tipo de comunicación')
plt.axis('equal')
plt.show()