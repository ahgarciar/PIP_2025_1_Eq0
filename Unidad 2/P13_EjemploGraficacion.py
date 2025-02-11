
#  y  = mx + b

x = [i for i in range(-5, 5+1, 1)]
print(x)

m  = 3
b = 2


##
y = [i*m+b for i in x]
print(y)

from matplotlib import pyplot as plt
plt.plot(x, y, marker= "X")
plt.show()

#práctica 4....-> Prbar otras maneras de personalizar el diseño de las graficas
# con matplotlib