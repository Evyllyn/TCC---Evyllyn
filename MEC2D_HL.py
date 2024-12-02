import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import qmc  # Para Latin Hypercube Sampling

# Parâmetros da viga
L = 8.0  # Vão livre da viga em metros
E_mean = 210e9  # Módulo de elasticidade médio em Pa (210 GPa)
E_std = E_mean * 0.05  # Desvio padrão (5% de variação para o módulo de elasticidade)
q_mean = 27000  # Carga distribuída média em N/m (27 kN/m)
q_std = q_mean * 0.2  # Desvio padrão (10% de variação para a carga)

# Número de simulações
n_simulations = 10000


# Função para calcular o deslocamento máximo
def calculate_displacement(E, q, L):
    I = 0.001246  # Momento de inércia (estimado anteriormente em m^4)
    delta_max = (5 * q * L ** 4) / (384 * E * I)
    return delta_max


# Função de falha g1(D)
def g1(D):
    return 0.022 - D  # Deslocamento limite de 22 mm (L/350)


# Amostragem por Hipercubo Latino
sampler = qmc.LatinHypercube(d=2)  # Duas variáveis: E e q
samples = sampler.random(n_simulations)

# Transformar as amostras em distribuições normais para E e q
E_samples = E_mean + E_std * (samples[:, 0] * 6 - 3)  # Transformando de [0,1] para [-3,3]
q_samples = q_mean + q_std * (samples[:, 1] * 6 - 3)  # Transformando de [0,1] para [-3,3]

# Simulação de Monte Carlo
failure_count = 0
displacements = []

for i in range(n_simulations):
    # Calcular o deslocamento máximo para essa amostra
    D = calculate_displacement(E_samples[i], q_samples[i], L)
    displacements.append(D)

    # Verificar se a função de falha é negativa (indicando falha)
    if g1(D) < 0:
        failure_count += 1

# Probabilidade de falha
failure_probability = failure_count / n_simulations
print(f"Probabilidade de falha: {failure_probability:.6f}")

# Gráfico de dispersão das amostras
plt.scatter(E_samples, q_samples, color='red', alpha=0.3, s=5, label="Rank")  # Aumentar alpha para mais transparência
plt.title('Simulação de Monte Carlo - Hipercubo Latino')
plt.xlabel('$E_i$ (Módulo de Elasticidade)')
plt.ylabel('$q_j$ (Carga Distribuída)')
plt.grid(True)

# Adiciona a legenda
plt.legend()

# Mostra o gráfico
plt.show()