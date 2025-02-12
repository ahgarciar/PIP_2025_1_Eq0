
archivo = open("../Archivos/calificaciones_con_nombre.csv")
contenido = archivo.readlines()

print(contenido)

datos = [i.split(",") for i in contenido]

print(datos)

datos = [[i[0], list(map(int,i[1:])) ] for i in datos]

print(datos)

#calcular el promedio de cada alumno y agregar el resultado
# a la lista asociada al usuario

datos = [[ i[0], i[1] , sum(i[1])/len(i[1]) ] for i in datos]
print(datos)

#datos.sort(key = lambda x:x[2])

nombres = [i[0] for i in datos]
promedios = [i[2] for i in datos]

#estandariza la instancia...

#z = valor - promedio / desviacion

promedioGrupo = sum(promedios)/len(promedios)

import numpy as np
vector = np.array(promedios)
desviacion = np.std(vector)

print("Promedio Grupo:", promedioGrupo)
print("Desviacion:", desviacion)

promedio_std = [(i-promedioGrupo)/desviacion for i in promedios]
print(promedio_std)

referencia_promedio = [0 for i in range(len(promedios))]

from matplotlib import pyplot as plt
plt.plot(nombres, promedio_std)
plt.plot(nombres, referencia_promedio, color = 'green', marker = '*')
plt.grid(True)
plt.show()