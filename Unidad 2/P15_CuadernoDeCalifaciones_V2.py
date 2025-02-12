
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

datos.sort(key = lambda x:x[2])

nombres = [i[0] for i in datos]
promedios = [i[2] for i in datos]

promedioGrupo = sum(promedios)/len(promedios)
promedioGrupo = [promedioGrupo for i in range(len(promedios))]
print(promedioGrupo)

from matplotlib import pyplot as plt

plt.plot(nombres, promedios, color = 'red', marker = 'X')
plt.plot(nombres, promedioGrupo, color = 'green', marker = '*')
plt.bar(nombres, promedios)

plt.title('Resumen de Calificaciones')
plt.xlabel('Nombre')
plt.ylabel('Promedio')
plt.ylim(0, 12)

plt.show()