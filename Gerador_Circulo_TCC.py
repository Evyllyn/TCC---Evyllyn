import math
#Aqui vamos entrar com os dados
n = int(input("entre com o número de nós: "))
radius = float(input("entre com o Raio: "))
F = float(input("entre com a intensidade da força: "))
E = float(input("entre com o módulo de elasticidade: "))
V = float(input("entre com o coeficiente de poisson: "))
SIG = float(input("entre com i SIGMAXMAT: "))
b = 2 * n

# Abre o arquivo "Circulo1.txt" em modo de escrita ("wt")
arquivoS = open("Exemplo_1_1.txt", "wt")
# Escreve informações sobre o coeficiente de Poisson, elasticidade e SIGMAXMAT no arquivo
arquivoS.write("%POISSON \n")
arquivoS.write("%f \n\n" % V)
arquivoS.write("%ELASTICITY \n")
arquivoS.write("%f \n\n" % E)
arquivoS.write("%SIGMAMAXMAT \n")
arquivoS.write("%f \n\n" % SIG)

# Escreve o número de bordas (limite) do círculo no arquivo
arquivoS.write("%NODE.BOUND \n")
arquivoS.write("%f \n" % b)

coordinates = []  # Inicializa uma lista vazia para armazenar as coordenadas dos nós
angle_increment = 360 / n  # Calcula o incremento do ângulo para distribuir os nós uniformemente

arquivoS.write("1 %4f 0 \n" %radius)

# Loop para calcular as coordenadas dos nós no círculo
for i in range(n):
    angle_degress = (i * angle_increment) % 360  # Calcula o ângulo para este nó
    angle_radians = math.radians(angle_degress)  # Converte o ângulo de graus para radianos
    x = radius * math.cos(angle_radians)  # Calcula a coordenada x do nó
    y = radius * math.sin(angle_radians)  # Calcula a coordenada y do nó
    coordinates.append((x, y))  # Adiciona as coordenadas do nó à lista de coordenadas
e = 2
# Loop para escrever as coordenadas dos nós no arquivo
for i, (x, y) in enumerate(coordinates[1:], start=2):
    arquivoS.write(f"{e} {x:.4f} {y:.4f}\n") # interação 1 i = 2, i = 3, i =4
    arquivoS.write(f"{e+1} {x:.4f} {y:.4f}\n") # i+1 = 3, i +1 = 4 , i = 5
    e = e + 2

arquivoS.write("16 %f 0 \n" %radius)

#Aqui vem a lógica para os nós internos
arquivoS.write("%NODE.IN \n")
arquivoS.write("5 \n")
arquivoS.write("1 12 0 \n")
arquivoS.write("2 16 0 \n")
arquivoS.write("3 18 0 \n")
arquivoS.write("4 20 0 \n")
arquivoS.write("5 24 0 \n")

#Aqui vem a lógica do elemento
arquivoS.write("%ELEMENT \n")
arquivoS.write("%f \n" %(n))
v = 1
e = 2
for i in range (1, n + 1):
    arquivoS.write(f"{i} {e} {v}\n")
    e = e + 2
    v = v + 2


#Aqui vem a de elemento de contorno e valor da força
arquivoS.write("%CODE  \n")
arquivoS.write("Coord     Cód     val \n")

m = 2

coordinatess = []  # Inicializa uma lista vazia para armazenar as coordenadas dos nós
angle_increment = 360 / n  # Calcula o incremento do ângulo para distribuir os nós uniformemente

# Loop para calcular as coordenadas dos nós com a força aplicada
for i in range(n):
    angle_degrees = (i * angle_increment) % 360
    angle_radians = math.radians(angle_degrees)
    x = F * math.cos(angle_radians)
    y = F * math.sin(angle_radians)
    coordinatess.append((x, y))  # Adiciona as coordenadas do nó à lista de coordenadas
    
arquivoS.write("1 1 %4f \n" %F)
arquivoS.write("2 1 0 \n")

# Loop para escrever as coordenadas dos nós no arquivo, a partir do segundo nó
for i, (x, y) in enumerate(coordinatess[1:], start=3):
    arquivoS.write(f"{m} 1 {x:.4f}\n")
    arquivoS.write(f"{m+1} 1 {y:.4f}\n")
    arquivoS.write(f"{m+2} 1 {x:.4f}\n")
    arquivoS.write(f"{m + 3} 1 {y:.4f}\n")
    m = m + 4
    
arquivoS.write("31 1 %4f \n" %F)
arquivoS.write("32 1 0 \n")

# Fecha o arquivo
arquivoS.close()

