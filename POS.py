import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# Definir os dados de contorno (ajustar conforme seus dados reais)
# Exemplificando com uma forma de anel (contorno circular)
# Aqui vamos assumir que você tem um círculo com um furo no meio (um anel)

# Pontos de contorno (exemplo circular)
num_points = 33  # número de pontos de contorno
r_outer = 10  # Raio externo do tubo
r_inner = 4    # Raio do furo no centro

# Gerar os pontos no contorno (circular) com um furo no meio
theta = np.linspace(0, 2 * np.pi, num_points)
contour_nodes = np.array([
    [r_outer * np.cos(t), r_outer * np.sin(t)] for t in theta
] + [
    [r_inner * np.cos(t), r_inner * np.sin(t)] for t in theta
])

# Valores de deslocamento associados a cada ponto de contorno (substituir com seus dados reais)
displacement_magnitude = np.random.rand(len(contour_nodes))

# Verificar se o número de pontos e valores é igual
if len(contour_nodes) != len(displacement_magnitude):
    print("Erro: O número de pontos e valores não é igual!")
    # Ajustar os dados
    if len(contour_nodes) > len(displacement_magnitude):
        contour_nodes = contour_nodes[:-1]
    elif len(displacement_magnitude) > len(contour_nodes):
        displacement_magnitude = displacement_magnitude[:-1]
    print(f"Contagem corrigida de pontos: {len(contour_nodes)}")
    print(f"Contagem corrigida de valores: {len(displacement_magnitude)}")

# Gerar uma grade para interpolação dentro do círculo (definir limites da área de interesse)
grid_x, grid_y = np.meshgrid(np.linspace(-r_outer, r_outer, 100),
                             np.linspace(-r_outer, r_outer, 100))

# Calcular a distância radial para cada ponto na grade
radius = np.sqrt(grid_x**2 + grid_y**2)

# Filtrar pontos dentro do anel (círculo externo com furo interno)
mask = (radius >= r_inner) & (radius <= r_outer)

# Aplicar interpolação para obter os valores de deslocamento na grade
grid_z = griddata(contour_nodes, displacement_magnitude, (grid_x, grid_y), method='cubic')

# Definir a área fora do anel como NaN para não aparecer na visualização
grid_z[~mask] = np.nan

# Plotar os resultados
plt.figure(figsize=(8, 6))
plt.contourf(grid_x, grid_y, grid_z, levels=20, cmap='viridis')  # Contorno da interpolação
plt.colorbar(label='Magnitude de Deslocamento')  # Barra de cores para os valores de deslocamento
plt.scatter(contour_nodes[:, 0], contour_nodes[:, 1], c=displacement_magnitude, cmap='viridis', edgecolors='k')  # Pontos de contorno
plt.title('Distribuição do Deslocamento no Tubo com Furo')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.gca().set_aspect('equal', adjustable='box')  # Para manter a proporção correta
plt.show()
