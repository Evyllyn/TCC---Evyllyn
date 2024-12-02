import math
#Aqui vamos entrar com os dados
F = float(input("entre com a intensidade da força: "))
E = float(input("entre com o módulo de elasticidade: "))
V = float(input("entre com o coeficiente de poisson: "))
SIG = float(input("entre com i SIGMAXMAT: "))
b=40
m = 44/48
L = ((48)**2+(44)**2)**(1/2)
n = L/6

# Abre o arquivo "Circulo1.txt" em modo de escrita ("wt")
arquivoS = open("Cook_test.txt", "wt")
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

arquivoS.write("1 0 0 \n")

c = 2
for i in range(1,7):
    y = i * (44/6)
    x = i * (48/6)
    arquivoS.write(f"{c} {x} {y}\n") # interação 1 i = 2, i = 3, i =4
    arquivoS.write(f"{c+1} {x} {y}\n") # interação 1 i = 2, i = 3, i =4
    c = c + 2

arquivoS.write("16 48 44 \n")
arquivoS.write("17 48 44 \n")
arquivoS.write("18 48 52 \n")
arquivoS.write("19 48 52 \n")
arquivoS.write("20 48 60 \n")
arquivoS.write("21 48 60 \n")

c = 21
a = 48
for i in range (1,8):
    y = a * math.sin(42.51)
    x = a * math.cos(42.51)
    arquivoS.write(f"{c} {x} {-y}\n") # interação 1 i = 2, i = 3, i =4
    a = a - 6
    arquivoS.write(f"{c+1} {x} {-y}\n") # interação 1 i = 2, i = 3, i =4
    c = c+2

arquivoS.write("37 0 22 \n")
arquivoS.write("38 0 22 \n")
arquivoS.write("39 0 0 \n")