import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parâmetros da viga
L_mean = 8.0          # Comprimento médio da viga em metros
h = 0.4               # Altura da seção em metros
E_mean = 210e9        # Módulo de elasticidade em Pa (210 GPa)
w_mean = 27e3         # Carga distribuída em N/m (27 kN/m)
n_simulations = 1127   # Número de simulações
n_factors = 3         # Número de variáveis (E, w e L)

# Desvios padrão (assumindo 10% para E, 5% para w e 5% para L)
E_std = 0.15 * E_mean  # 10% de desvio padrão
w_std = 0.1 * w_mean    # 5% de desvio padrão
L_std = 0.4 * L_mean    # 5% de desvio padrão

# Critério de resistência
criterion = 0.22  # mm

# Função para calcular deslocamento máximo
def max_displacement(E, w, L):
    return (5 * w * L**4) / (384 * E * (h**3))

# Gerar pontos do hipercubo latino
def latin_hypercube_sampling(n_samples, n_factors):
    samples = np.zeros((n_samples, n_factors))
    for i in range(n_factors):
        samples[:, i] = np.linspace(0, 1, n_samples)
        np.random.shuffle(samples[:, i])  # Embaralha cada coluna individualmente
    return samples

# Gerar amostras do hipercubo latino
samples = latin_hypercube_sampling(n_simulations, n_factors)

# Transformar amostras uniformes em amostras normais para E e w
E_samples = norm.ppf(samples[:, 0], loc=E_mean, scale=E_std)
w_samples = norm.ppf(samples[:, 1], loc=w_mean, scale=w_std)

# Gerar amostras de L a partir de uma distribuição lognormal
sigma_L = np.log(1 + (L_std / L_mean)**2) ** 0.5  # Cálculo do desvio padrão da lognormal
mu_L = np.log(L_mean) - 0.5 * sigma_L**2  # Cálculo da média da lognormal
L_samples = np.random.lognormal(mean=mu_L, sigma=sigma_L, size=n_simulations)

# Verificar se as amostras são válidas
E_samples[E_samples < 0] = np.nan  # Substituir valores negativos por NaN
w_samples[w_samples < 0] = np.nan  # Substituir valores negativos por NaN
# Não há necessidade de verificar L_samples, pois a lognormal sempre produz valores positivos

# Remover amostras inválidas
valid_indices = ~np.isnan(E_samples) & ~np.isnan(w_samples)
E_samples = E_samples[valid_indices]
w_samples = w_samples[valid_indices]
L_samples = L_samples[valid_indices]

# Calcular deslocamentos máximos
displacements = [max_displacement(E, w, L) * 1000 for E, w, L in zip(E_samples, w_samples, L_samples)]  # m para mm

# Análise de falha
failures = np.sum(np.array(displacements) > criterion)
probability_of_failure = failures / len(displacements)

# Resultados
print(f"Probabilidade de Falha: {probability_of_failure * 100:.2f}%")
print(f"Deslocamentos máximos (mm): Média = {np.mean(displacements):.4f}, Mínimo = {np.min(displacements):.4f}, Máximo = {np.max(displacements):.4f}")

# Gráfico de dispersão (E_samples vs w_samples)
plt.scatter(E_samples, w_samples, color='red', label='Rank')
plt.xlabel('E (Módulo de Elasticidade)')
plt.ylabel('w (Carga Distribuída)')
plt.title('Simulação de Monte Carlo - Hipercubo Latino')
plt.legend()
plt.grid(True)
plt.show()