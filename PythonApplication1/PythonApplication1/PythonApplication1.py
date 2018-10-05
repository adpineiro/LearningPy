#este es un fichero de prueba de python
#primer comentario
import math

frase="hola mundo"
print(frase)
rango=range(0,10,1)
for i in rango:
    print(i)
j=range(2)
lista=list(j)
print(lista)
"""l=math.e
print(l)
input()
j= int
m=1
while m<10:
    m+=1
    print("dentro del while")
print("Salida del while")"""
def suma(sum1, sum2):
    sumatorio=sum1+sum2
    print(sumatorio)


def factorial_numero(numero):
    factorial = 1
    while numero > 0:
        factorial = factorial*numero
        numero -= 1
    return factorial


resultado = factorial_numero(5)
print("Cálculo del factorial")
print(resultado)
print("Suma")
suma(2, 5)
input()



    
