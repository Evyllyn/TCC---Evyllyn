import matplotlib.pyplot as plt
import numpy as np

def plot_viga_biapoiada():
    # Parâmetros do problema
    comprimento = 8  # Comprimento da viga (m)
    carga_distribuida = 27  # Carregamento distribuído (kN/m)
    largura = 0.4  # Largura da seção transversal (m)
    altura = 0.4  # Altura da seção transversal (m)
    num_nos = 10  # Número total de nós (5 no superior, 5 no inferior)

    # Coordenadas dos nós
    x_nos = np.linspace(0, comprimento, num_nos // 2)  # Nós igualmente espaçados ao longo do comprimento
    y_superior = np.full_like(x_nos, altura / 2)  # Nós na borda superior
    y_inferior = np.full_like(x_nos, -altura / 2)  # Nós na borda inferior

    # Configuração do gráfico
    plt.figure(figsize=(12, 6))
    plt.title("Visualização da Malha Discretizada", fontsize=14)

    # Conectar os nós superiores e inferiores para formar os elementos da viga
    for i in range(len(x_nos) - 1):
        # Conectar nós superiores
        plt.plot([x_nos[i], x_nos[i + 1]], [y_superior[i], y_superior[i + 1]], 'b-', linewidth=1)
        # Conectar nós inferiores
        plt.plot([x_nos[i], x_nos[i + 1]], [y_inferior[i], y_inferior[i + 1]], 'b-', linewidth=1)
        # Conectar os nós superior-inferior em cada extremidade
        plt.plot([x_nos[i], x_nos[i]], [y_inferior[i], y_superior[i]], 'b-', linewidth=1)

    # Plotar os nós
    plt.scatter(x_nos, y_superior, c='blue', label="Nós Superiores")
    plt.scatter(x_nos, y_inferior, c='cyan', label="Nós Inferiores")

    # Apoios nas extremidades da face inferior
    plt.plot(x_nos[0], y_inferior[0], 'ks', markersize=10, label="Apoio Segundo Gênero")
    plt.plot(x_nos[-1], y_inferior[-1], 'gs', markersize=10, label="Apoio Primeiro Gênero")

    # Adicionar o carregamento distribuído na face superior (apontando para baixo)
    num_setas = len(x_nos)  # Uma seta para cada nó superior
    for i in range(num_setas):
        plt.arrow(x_nos[i], y_superior[i], 0, -0.2, head_width=0.15, head_length=0.1, fc='magenta', ec='magenta')

    # Texto indicando o carregamento distribuído
    plt.text(comprimento / 2, altura / 2 + 0.1, f"q = {carga_distribuida} kN/m", fontsize=10, color='magenta', ha='center')

    # Configurações do gráfico
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axhline(0, color='black', linewidth=0.8, linestyle="--")
    plt.grid(True)
    plt.legend(loc="upper left", fontsize=10)
    plt.axis('equal')

    # Mostrar o gráfico
    plt.show()

# Chamar a função para plotar
plot_viga_biapoiada()
