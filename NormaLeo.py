# 2Da parte proyecto Matemáticas Para las Ciencias Aplicadas II
# Programaa que evaluara si (p>2), y dara la norma euclidiana para p
# Elaborado por: Ramirez Padron Angel Leonardo
# Se debe tener "math" para su funcionamiento


import math

def norma(v, p=2):
    if p == 2:
        return norma_euclidiana(v)
    else:
        suma = sum(abs(x) ** p for x in v)
        return suma ** (1/p)

def norma_euclidiana(v):
    suma_cuadrados = sum(x ** 2 for x in v)
    return math.sqrt(suma_cuadrados)

# Ejemplo de uso
vector = [3, 4]
norma_2 = norma(vector)
norma_3 = norma(vector, 3)

print(f"Norma Euclidiana de {vector}: {norma_2}")
print(f"Norma 3 de {vector}: {norma_3}")
