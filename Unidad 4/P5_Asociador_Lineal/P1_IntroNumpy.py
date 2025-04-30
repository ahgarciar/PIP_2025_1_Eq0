
import numpy as n

a = [[2, 3, 4],[2, 1, 4],[3,2,1]]
print(a)


A = n.array(a)
print("\n")
print(A)

[F, C] = A.shape #orden
print("Filas: ", F, "Columnas: ", C)
