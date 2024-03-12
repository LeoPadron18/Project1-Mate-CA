import matplotlib.pyplot as plt
import numpy as np

# Define la función de la métrica
def metric_function(BW, Load, Delay, REL, K1, K2, K3, K4, K5):
    return (K1 * BW + K2 * BW) / (256 - Load + K3 * Delay * K5 / (K4 + REL))

# Asigna valores a los parámetros y variables
BW_values = np.linspace(1, 100, 100)  # Ejemplo: valores de ancho de banda de 1 a 100
Load_value = 70 # Ejemplo: valor de carga
Delay_value = 70 # Ejemplo: valor de retardo
REL_value = 60  # Ejemplo: valor de REL
K1_value = 3
K2_value = 6
K3_value = 1.5
K4_value = 2.2
K5_value = 4.8

# Calcula los valores de la métrica para cada valor de BW
metric_values = [metric_function(BW, Load_value, Delay_value, REL_value, K1_value, K2_value, K3_value, K4_value, K5_value) for BW in BW_values]

# Grafica la métrica
plt.plot(BW_values, metric_values, label='Metrica')
plt.xlabel('Ancho de Banda (BW)')
plt.ylabel('Valor de la Métrica')
plt.title('Gráfico de la Métrica en función del Ancho de Banda')
plt.legend()
plt.show()
