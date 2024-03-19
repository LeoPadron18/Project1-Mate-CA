#Parte 2 del 1er Proyecto Parcial 1 de Matemáticas Para las Ciencias Aplicadas
#Elaborado por: Ramirez Padron Angel Leonardo
#Programa que evalua la Paradoja del Cumpleaños
#Los parametros son 365 dias (año normal), seguido de 100 personas y en un experimento de 1000 posibles casos
# se deebra tenrer "random" Para ejecutarlo  
import random

def generar_cumpleaños(num_personas):
    cumpleaños = []
    for _ in range(num_personas):
        dia = random.randint(1, 365)  # Suponiendo que el año tiene 365 días
        cumpleaños.append(dia)
    return cumpleaños

def testear_paradoja(num_experimentos, num_personas):
    coincidencias = 0
    for _ in range(num_experimentos):
        cumpleaños = generar_cumpleaños(num_personas)
        if len(cumpleaños) != len(set(cumpleaños)):  # Hay al menos una coincidencia
            coincidencias += 1
    probabilidad = coincidencias / num_experimentos * 100
    return probabilidad

def main():
    num_personas = 100
    num_experimentos = 1000
    probabilidad = testear_paradoja(num_experimentos, num_personas)
    print(f"Después de {num_experimentos} experimentos con {num_personas} personas cada uno:")
    print(f"La probabilidad de que al menos dos personas compartan cumpleaños es aproximadamente del {probabilidad:.2f}%.")

if __name__ == "__main__":
    main()
