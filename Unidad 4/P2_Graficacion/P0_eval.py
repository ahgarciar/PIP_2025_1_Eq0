
cadena = "3+5/2"
a = eval(cadena)
print(a)

import math

cadena = "math.pow(2,3)"
a = eval(cadena)
print(a)


valores_x = [i for i in range(-10, 10, 1)]
#x = 5
y = "x**2"
#y = "math.pow(x,2)"
#y = "x*x"

#valores_y = eval(y)
valores_y = [eval(y) for x in valores_x]
print(valores_y)

from matplotlib import pyplot as plt
plt.plot(valores_x, valores_y)
plt.show()