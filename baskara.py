#Calculadora de Bhaskára

from math import sqrt
import cmath
a = float(input('Digite o valor de a: '))
b = float(input('Digite o Valor de b: '))
c = float(input('Digite o valor de c: '))
print('A equação ficou assim: {:.0f}x²+{:.0f}x+{:.0f}=0'.format(a, b, c))
complexo = int(input('Deseja receber os resultados em números complexos? Digite sua escolha: \n 1 - sim \n 2 - não \n'))
delta = b**2-4*a*c
if complexo == 1:
     print('O delta é negativo, as raízes são complexas: ')
     deltac = complex(delta)
     x1 = (-b+(cmath.sqrt(deltac))) / (2*a)
     x2 = (-b-(cmath.sqrt(deltac))) / (2*a)
     print("x' vale: {}".format(x1))
     print("x'' vale: {}".format(x2))

elif delta >=0:
    x1 = (-b+(sqrt(delta))) / (2*a)
    x2 = (-b-(sqrt(delta))) / (2*a)
    print('As raízes são reais: ')
    print("X' vale: {:.2f}". format(x1))
    print("x'' vale: {:.2f}".format(x2))
else:
     print('O delta é negativo, portanto as raízes são complexas. Como você optou, elas não serão calculadas')