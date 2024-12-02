import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.interpolate import griddata

# Definir as coordenadas dos pontos do contorno
coordenadas_contorno = np.array([
    [0, 0],  [0, 1],  [0, 2],  [0, 3],
    [1, 3],  [2, 3],  [3, 3],  [4, 3],
    [4, 2],  [4, 1],  [4, 0],  [3, 0],
    [2, 0],  [1, 0]
])

# Número de pontos no contorno
n_pontos = len(coordenadas_contorno)

# Definir deslocamentos fornecidos (exemplo de deslocamentos em X e Y)
deslocamentos = np.array([
    [0.0, 0.0], [0.1, 0.2], [0.2, 0.4], [0.3, 0.5],
    [0.4, 0.6], [0.5, 0.7], [0.6, 0.8], [0.7, 0.9],
    [0.8, 1.0], [0.9, 1.1], [1.0, 1.2], [1.1, 1.3],
    [1.2, 1.4], [1.3, 1.5]
])

# Calcular a magnitude dos deslocamentos (distância total)
magnitude_deslocamento = np.linalg.norm(deslocamentos, axis=1)

# Definir uma grade regular para a área da chapa
x_grid = np.linspace(0, 4, 100)  # Intervalo para o eixo X
y_grid = np.linspace(0, 3, 100)  # Intervalo para o eixo Y
x_grid, y_grid = np.meshgrid(x_grid, y_grid)

# Definir o orifício no centro da chapa
raio_orificio = 0.5  # Raio do orifício ajustado para ser proporcional
centro_orificio = (2, 1.5)  # Centro do orifício (no meio da chapa)

# Máscara para o orifício (pontos dentro do orifício serão excluídos)
distancia_do_centro = np.sqrt((x_grid - centro_orificio[0])**2 + (y_grid - centro_orificio[1])**2)
mascara_orificio = distancia_do_centro <= raio_orificio

# Interpolar os deslocamentos nos pontos da grade usando a função griddata
# Interpolação para a magnitude do deslocamento (usando os pontos do contorno)
grid_magnitude = griddata(coordenadas_contorno, magnitude_deslocamento, (x_grid, y_grid), method='cubic')

# Aplicar a máscara do orifício (atribui um valor nulo ou NaN dentro do orifício)
grid_magnitude[mascara_orificio] = np.nan

# Plotar o mapa de calor da magnitude dos deslocamentos
plt.figure(figsize=(8, 6))
plt.title("Mapa de Calor dos Deslocamentos com Orifício no Centro")
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")

# Exibir o mapa de calor
contour = plt.contourf(x_grid, y_grid, grid_magnitude, 50, cmap=cm.viridis)
plt.colorbar(contour, label="Magnitude do Deslocamento")

# Desenhar o orifício no centro (círculo)
circle = plt.Circle(centro_orificio, raio_orificio, color='white', lw=2, fill=False)
plt.gca().add_artist(circle)

# Exibir a trama
plt.show()
