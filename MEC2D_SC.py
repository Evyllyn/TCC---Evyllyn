import numpy as np
import math
import matplotlib.pyplot as plt
from time import process_time
from scipy.stats import norm, lognorm

class DadosMaterial:
    def __init__(self, caminho_arquivo, v_sc):
        self.caminho_arquivo = caminho_arquivo
        self.Num_elem = 0
        self.v = v_sc
        self.E = 0
        self.tensao_vm = []
        self.X_int, self.Y_int = [], []
        self.X_cont, self.Y_cont = [], []
        self.conect = []
        self.codigo, self.valor, self.v_s = [], [], []
        self.Num_P_int = 0
        self.sigmaMaxMat = 0
        self.OME = []
        self.GI = []
        self.Gc = 0
        (
            self.Ksi,
            self.Fi_1,
            self.Fi_2,
            self.h,
            self.Delta,
            self.Dh,
            self.Dg,
            self.Se,
            self.Co,
            self.eta,
            self.ponto,
        ) = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

        self.H, self.G, self.A, self.B = [], [], [], []

        self.FD = []
        self.Num_P_int = 0
        (
            self.D_int,
            self.Tens_Int,
            self.Tens_P,
            self.sigmaMaxMat,
            self.sigmaPontoMax,
            self.pontoMax,
            self.DeslocYMax,
            self.pontoDMax,
            self.Teta_P,
            self.sigmaYMax,
        ) = [], [], [], [], [], [], [], [], [], []

    def ler_dados(self):
        # print('... Ler dados ...')
        with open(self.caminho_arquivo, "r") as arquivo:
            # Entrada de dados
            while True:
                line = arquivo.readline()
                if not line:
                    break

                # Verifica se a linha não está vazia antes de tentar acessar o índice 0
                if line.strip():
                    aux = (
                        line.split()
                    )  # Variável auxiliar para leitura das strings do arquivo
                else:
                    continue

                # Leitura do valor do Coeficiente de Poisson

                #if aux and aux[0] == "%POISSON":
                    #self.v = float(arquivo.readline())
                    # print(f"DEBUG: V={self.v}")

                # Leitura do valor do Módulo de Elasticidade
                if aux and aux[0] == "%ELASTICITY":
                    self.E = float(arquivo.readline())
                    # print(f"DEBUG: E={self.E}")

                # Leitura do valor máximo do sigma do Material
                elif aux and aux[0] == "%SIGMAMAXMAT":
                    self.sigmaMaxMat = float(arquivo.readline())
                    # print(f"DEBUG: sigmaMaxMat={self.sigmaMaxMat}")

                # Leitura dos Pontos de Contorno
                elif aux and aux[0] == "%NODE.BOUND":
                    self.Num_P_cont = int(arquivo.readline())
                    self.X_cont, self.Y_cont = [], []
                    # print(f"DEBUG: Num_P_cont={self.Num_P_cont}")
                    for j in range(self.Num_P_cont):
                        line_cont = arquivo.readline().split()
                        if len(line_cont) >= 2:
                            try:
                                self.X_cont.append(float(line_cont[1]))
                                self.Y_cont.append(float(line_cont[2]))
                                # print(f"DEBUG: Num_P_cont = {self.Num_P_cont} y_cont={self.Y_cont}")
                            except ValueError:
                                print("Error reading contour point. Skipping.")
                        else:
                            print("Error reading contour point. Skipping.")

                # Leitura dos Pontos Internos
                elif aux and aux[0] == "%NODE.IN":
                    self.Num_P_int = int(arquivo.readline())
                    self.X_int, self.Y_int = [], []

                    for i in range(self.Num_P_int):
                        line_int = arquivo.readline().split()
                        if len(line_int) >= 2:
                            self.X_int.append(float(line_int[1]))
                            self.Y_int.append(float(line_int[2]))
                            # print(f"DEBUG: Num_P_int={self.Num_P_int} y_int={self.Y_int}")
                        else:
                            print("Error reading internal point. Skipping.")

                # Conectividade dos Elementos
                elif aux and aux[0] == "%ELEMENT":
                    self.Num_elem = int(arquivo.readline())
                    self.conect = []
                    # print(f"DEBUG: self. Num_elem={self.Num_elem}")
                    for lin in range(self.Num_elem):
                        line_elem = arquivo.readline().split()
                        if len(line_elem) >= 2:
                            try:
                                self.conect.append(
                                    [int(line_elem[1]), int(line_elem[2])]
                                )
                                # print(f"DEBUG: self. conect={self.conect}")
                            except ValueError:
                                print("Error reading element connectivity. Skipping.")
                        else:
                            print("Error reading element connectivity. Skipping.")
                    codigo = []  # Certifique-se de inicializar a lista código

                # Leitura das condições de contorno
                elif aux and aux[0] == "%CODE":
                    self.codigo = [0] * (4 * self.Num_elem)
                    self.valor = [0.0] * (4 * self.Num_elem)
                    self.v_s = [0.0] * (4 * self.Num_elem)

                    # Variável para ler as strings do arquivo que não serão utilizadas no programa
                    lixo = arquivo.readline().split()[:3]

                    for i in range(4 * self.Num_elem):
                        line_code = arquivo.readline().split()

                        if len(line_code) >= 3:  # Ajuste para 3 valores por linha
                            try:
                                self.codigo[i] = int(line_code[1])
                                self.valor[i] = float(line_code[2])
                                self.v_s[i] = self.valor[i]
                                # print(f"DEBUG: self. codigo={self.codigo}, self.Valor={self.valor}, Self.v_s = {self.v_s}")
                            except (ValueError, IndexError):
                                print("Error reading boundary condition. Skipping.")

                elif aux and aux[0] == "%END":
                    break

            arquivo.close()

    def comprimento(self, j, k):
        L = np.sqrt(
            (self.X_cont[k] - self.X_cont[j]) ** 2
            + (self.Y_cont[k] - self.Y_cont[j]) ** 2
        )
        return L

    def obter_pontos_de_gauss(self):
        # print('... pontos de gauss ...')
        # Inicialização das variáveis globais
        self.GI = np.zeros(24)
        self.OME = np.zeros(24)

        # 2 pontos
        self.GI[0] = 0.577350269189626
        self.OME[0] = 1.000000000000000
        self.GI[1] = -0.577350269189626
        self.OME[1] = 1.000000000000000

        # 4 pontos
        self.GI[2] = 0.339981043584856
        self.OME[2] = 0.652145154862546
        self.GI[3] = -0.339981043584856
        self.OME[3] = 0.652145154862546
        self.GI[4] = 0.861136311594053
        self.OME[4] = 0.347854845137454
        self.GI[5] = -0.861136311594053
        self.OME[5] = 0.347854845137454

        # 6 pontos
        self.GI[6] = 0.238619186083197
        self.OME[6] = 0.467913934572691
        self.GI[7] = -0.238619186083197
        self.OME[7] = 0.467913934572691
        self.GI[8] = 0.661209386466265
        self.OME[8] = 0.360761573048139
        self.GI[9] = -0.661209386466265
        self.OME[9] = 0.360761573048139
        self.GI[10] = 0.932469514203152
        self.OME[10] = 0.171324492379170
        self.GI[11] = -0.932469514203152
        self.OME[11] = 0.171324492379170

        # 12 pontos
        self.GI[12] = 0.125233408511469
        self.OME[12] = 0.249147045813403
        self.GI[13] = -0.125233408511469
        self.OME[13] = 0.249147045813403
        self.GI[14] = 0.367831498998180
        self.OME[14] = 0.233492536538355
        self.GI[15] = -0.367831498998180
        self.OME[15] = 0.233492536538355
        self.GI[16] = 0.587317954286617
        self.OME[16] = 0.203167426723066
        self.GI[17] = -0.587317954286617
        self.OME[17] = 0.203167426723066
        self.GI[18] = 0.769902674194305
        self.OME[18] = 0.160078328543346
        self.GI[19] = -0.769902674194305
        self.OME[19] = 0.160078328543346
        self.GI[20] = 0.904117256370475
        self.OME[20] = 0.106939325995318
        self.GI[21] = -0.904117256370475
        self.OME[21] = 0.106939325995318
        self.GI[22] = 0.981560634246719
        self.OME[22] = 0.047175336386512
        self.GI[23] = -0.981560634246719
        self.OME[23] = 0.047175336386512

        return self.GI, self.OME

    def matrizes_auxiliares(self):
        self.Gc = self.E / (2 * (1 + self.v))

        # Valores para qsi_1 e qsi_2
        qsi_1 = -0.5
        qsi_2 = 0.5
        self.Ksi = [qsi_1, qsi_2]

        # Cálculo das funções de aproximação
        h1 = (1 - qsi_1) / 4
        h2 = (1 + qsi_1) / 4

        self.Fi_1 = np.zeros((2, 2))
        self.Fi_2 = np.zeros((2, 2))
        self.Fi_1[0, 0] = (1 - qsi_1) / 2
        self.Fi_2[0, 0] = (1 + qsi_1) / 2
        self.Fi_1[0, 1] = (1 + qsi_1) / 2
        self.Fi_2[0, 1] = (1 - qsi_1) / 2
        self.Fi_1[1, 0] = (1 - qsi_2) / 2
        self.Fi_2[1, 0] = (1 + qsi_2) / 2
        self.Fi_1[1, 1] = (1 + qsi_2) / 2
        self.Fi_2[1, 1] = (1 - qsi_2) / 2
        # print(f"DEBUG: Fi_1={self.Fi_1}")
        # print(f"DEBUG: Fi_2={self.Fi_2}")

        self.h = np.zeros((4, 4))
        self.h[0, 0] = h1
        self.h[0, 2] = h2
        self.h[1, 1] = h1
        self.h[1, 3] = h2
        self.h[2, 0] = h2
        self.h[2, 2] = h1
        self.h[3, 1] = h2
        self.h[3, 3] = h1

        # print(f"DEBUG h={self.h}")

        # Constantes do integrando
        K1 = 1 / (8 * np.pi * self.Gc * (1 - self.v))
        K2 = (1 - 2 * self.v) / (4 * np.pi * (1 - self.v))
        C3 = 3 - 4 * self.v
        C2 = 1 - 2 * self.v
        # print(f"DEBUG: K1={K1},  K2={K2},  C3={C3},  C2={C2}")

    def integral_numerica(self, Xi, Yi, elem_j):
        j = self.conect[elem_j - 1][0] - 1  # N� 1 do elemento j
        k = self.conect[elem_j - 1][1] - 1  # N� 2 do elemento j

        L = self.comprimento(j, k)

        Ax = (
            self.X_cont[k] - self.X_cont[j]
        ) / 2  # Proje��o do elemento j no eixo x, dividido por 2
        Ay = (
            self.Y_cont[k] - self.Y_cont[j]
        ) / 2  # Proje��o do elemento j no eixo y, dividido por 2
        Bx = (
            self.X_cont[k] + self.X_cont[j]
        ) / 2  # Ponto m�dio da proje��o do elemento j no eixo x
        By = (
            self.Y_cont[k] + self.Y_cont[j]
        ) / 2  # Ponto m�dio da proje��o do elemento j no eixo y

        C1 = 1 - 2 * self.v
        C2 = 3 - 4 * self.v

        Delta = np.eye(2)

        Dh = (-L) / (
            8 * np.pi * (1 - self.v)
        )  # Parte constante da sol.fund. f. de super.
        Dg = Dh / (2 * self.Gc)  # Parte constante da sol.fund.do desloc.

        self.eta = np.array([self.Se[elem_j - 1], -self.Co[elem_j - 1]])
        self.obter_pontos_de_gauss()
        Pg_1 = 13
        Pg_2 = 24

        self.A = np.zeros((2, 4))
        self.B = np.zeros((2, 4))

        for indi in range(2):
            for indj in range(2):
                for ig in range(Pg_1 - 1, Pg_2):
                    X = Bx + self.GI[ig] * Ax  # Coordenada x do ponto campo
                    Y = By + self.GI[ig] * Ay  # Coordenada y do ponto campo

                    R = np.sqrt((X - Xi) ** 2 + (Y - Yi) ** 2)  # Norma de r
                    R_ij = np.array(
                        [(X - Xi) / R, (Y - Yi) / R]
                    )  # Derivada de r na dire��o x e y
                    D_i = R_ij[indi]
                    D_j = R_ij[indj]
                    Etai = self.eta[indi]
                    Etaj = self.eta[indj]
                    Dij = Delta[indi, indj]
                    Deriv_n = ((X - Xi) / R) * self.Se[elem_j - 1] - (
                        (Y - Yi) / R
                    ) * self.Co[elem_j - 1]

                    G = Dg * (C2 * np.log(R) * Dij - D_i * D_j) * self.OME[ig]
                    H = (
                        Dh
                        * (
                            (C1 * Dij + 2 * D_i * D_j) * Deriv_n
                            - C1 * (D_i * Etaj - D_j * Etai)
                        )
                        * self.OME[ig]
                        / R
                    )

                    aux = 2 * indj
                    # print(f"DEBUG: A={self.A}, B={self.B}")
                    self.A[indi, aux] += (1 - self.GI[ig]) * H / 2
                    self.A[indi, aux + 1] += (1 + self.GI[ig]) * H / 2
                    self.B[indi, aux] += (1 - self.GI[ig]) * G / 2
                    self.B[indi, aux + 1] += (1 + self.GI[ig]) * G / 2

        return

    def Integral_elem_nao_singular(self, elem_i, elem_j):
        j = self.conect[elem_i - 1][0] - 1
        k = self.conect[elem_i - 1][1] - 1

        # print(f"DEBUG(Não sinfular): j={j} k={k}")

        self.matrizes_auxiliares()

        for self.ponto in range(1, 3):
            Xi = (0.5 + self.Ksi[self.ponto - 1] / 2) * self.X_cont[k] + (
                0.5 - self.Ksi[self.ponto - 1] / 2
            ) * self.X_cont[j]
            Yi = (0.5 + self.Ksi[self.ponto - 1] / 2) * self.Y_cont[k] + (
                0.5 - self.Ksi[self.ponto - 1] / 2
            ) * self.Y_cont[j]

            self.integral_numerica(Xi, Yi, elem_j)

            i = 4 * (elem_i) - 5 + 2 * (self.ponto)
            c = 4 * (elem_j) - 3
            # print(f"DEBUG (integral numerica): Xi={Xi}, Yi={Yi}, i={i}, c={c}")

            self.H[i - 1, c - 1] += self.A[0, 0]
            self.H[i - 1, c] += self.A[0, 2]
            self.H[i - 1, c + 1] += self.A[0, 1]
            self.H[i - 1, c + 2] += self.A[0, 3]
            self.H[i, c - 1] += self.A[1, 0]
            self.H[i, c] += self.A[1, 2]
            self.H[i, c + 1] += self.A[1, 1]
            self.H[i, c + 2] += self.A[1, 3]
            p = 1
            self.G[i - 1, c - 1] += self.B[0, 0]
            self.G[i - 1, c] += self.B[0, 2]
            self.G[i - 1, c + 1] += self.B[0, 1]
            self.G[i - 1, c + 2] += self.B[0, 3]
            self.G[i, c - 1] += self.B[1, 0]
            self.G[i, c] += self.B[1, 2]
            self.G[i, c + 1] += self.B[1, 1]
            self.G[i, c + 2] += self.B[1, 3]

        # print(f"DEBUG (integral numerica): G={self.G}")
        return

    def Integral_elem_singular(self, elem_i):
        j = self.conect[elem_i - 1][0] - 1
        k = self.conect[elem_i - 1][1] - 1

        L = self.comprimento(j, k)
        # print ("Comprimento:", L)

        self.matrizes_auxiliares()
        # print(f"DEBUG: Gc={Gc}, K1={K1}, K2={K2},C2={C2},C3={C3},h={h},fi_1={Fi_1},fi_2={Fi_2}")

        Dh = (1 - 2 * self.v) / (4 * np.pi * (1 - self.v))
        Dg = -L / (8 * np.pi * self.Gc * (1 - self.v))
        C1 = 3 - 4 * self.v
        Eta = np.array([self.Se[elem_i - 1], -self.Co[elem_i - 1]])
        Di = np.array([self.Co[elem_i - 1], self.Se[elem_i - 1]])
        Delta = np.eye(2)

        temp_G = np.zeros_like(self.G)
        # print(f"DEBUG: C1={C1}, Dh={Dh}, Dg={Dg},C1={C1},ETA={Eta},Di={Di}")

        lin = None
        col = None

        for m in range(1, 3):
            for i in range(1, 3):
                for j in range(1, 3):
                    for k in range(1, 3):
                        F1 = self.Fi_1[m - 1, k - 1]
                        F2 = self.Fi_2[m - 1, k - 1]
                        Fk = F1
                        lin = 4 * (elem_i) + 2 * m + i - 6
                        col = 4 * (elem_i) + 2 * k + j - 6
                        self.G[lin - 1, col - 1] = Dg * (
                            C1
                            * (
                                F1**2 / 2 * math.log(L * F1)
                                + math.log(L * F2) * (F1 * F2 + F2**2 / 2)
                                - 3 * F1**2 / 4
                                - F1 * F2
                                - F2**2 / 4
                            )
                            * Delta[i - 1, j - 1]
                            + Di[i - 1]
                            * Di[j - 1]
                            * (-1 * (F1**2 / 2) - F1 * F2 - F2**2 / 2)
                        )
                        F1 = self.Fi_1[m - 1, 0]
                        F2 = self.Fi_2[m - 1, 0]
                        if k == 2:
                            Fk = F2

                        self.H[lin - 1, col - 1] = Dh * (
                            (Di[i - 1] * Eta[j - 1] - Di[j - 1] * Eta[i - 1])
                            * (Fk * math.log(F1 / F2) - (3 - 2 * k) * (F1 + F2))
                        )
        lin = lin - 4
        col = col - 4
        for i in range(1, 5):
            for j in range(1, 5):
                self.H[lin + i - 1, col + j - 1] = (
                    self.H[lin + i - 1, col + j - 1] + self.h[i - 1, j - 1]
                )

        return

    def tensoes_internas(self, Xi, Yi, elem_j):
        # Recupera dados necessários
        j = self.conect[elem_j - 1][0] - 1  # Nó 1 do elemento j
        k = self.conect[elem_j - 1][1] - 1  # Nó 2 do elemento j

        L = self.comprimento(j, k)

        Ax = (
            self.X_cont[k] - self.X_cont[j]
        ) / 2  # Projeção do elemento j no eixo x, dividido por 2
        Ay = (
            self.Y_cont[k] - self.Y_cont[j]
        ) / 2  # Projeção do elemento j no eixo y, dividido por 2
        Bx = (
            self.X_cont[k] + self.X_cont[j]
        ) / 2  # Ponto médio da projeção do elemento j no eixo x
        By = (
            self.Y_cont[k] + self.Y_cont[j]
        ) / 2  # Ponto médio da projeção do elemento j no eixo y

        C1 = 1 - 2 * self.v_int
        C2 = 1 - 4 * self.v_int

        Delta = np.eye(2)
        Delta[0, 0] = 1
        Delta[1, 1] = 1
        Dds = L / (8 * np.pi * (1 - self.v_int))

        Eta = np.array([self.Se[elem_j - 1], -self.Co[elem_j - 1]])
        self.obter_pontos_de_gauss()
        Pg_1 = 13
        Pg_2 = 24

        self.A = np.zeros((3, 4))
        self.B = np.zeros((3, 4))

        jj = 0
        for indi in range(1, 3):
            for indj in range(indi, 3):
                jj += 1
                for indk in range(1, 3):
                    for ig in range(Pg_1, Pg_2 + 1):
                        X = Bx + self.GI[ig - 1] * Ax
                        Y = By + self.GI[ig - 1] * Ay

                        R = np.sqrt((X - Xi) ** 2 + (Y - Yi) ** 2)
                        R_ijk = np.array([(X - Xi) / R, (Y - Yi) / R])
                        D_i, D_j, D_k = (
                            R_ijk[indi - 1],
                            R_ijk[indj - 1],
                            R_ijk[indk - 1],
                        )
                        Etai, Etaj, Etak = Eta[indi - 1], Eta[indj - 1], Eta[indk - 1]
                        Dij, Dik, Djk = (
                            Delta[indi - 1, indj - 1],
                            Delta[indi - 1, indk - 1],
                            Delta[indj - 1, indk - 1],
                        )
                        Deriv_n = ((X - Xi) / R) * self.Se[elem_j - 1] - (
                            (Y - Yi) / R
                        ) * self.Co[elem_j - 1]

                        G = (
                            (Dds / R)
                            * (
                                C1 * (Dik * D_j + Djk * D_i - Dij * D_k)
                                + 2 * D_i * D_j * D_k
                            )
                            * self.OME[ig - 1]
                        )
                        H = (
                            (2 * self.Gc * Dds / R**2)
                            * (
                                2
                                * Deriv_n
                                * (
                                    C1 * Dij * D_k
                                    + self.v_int * (Dik * D_j + Djk * D_i)
                                    - 4 * D_i * D_j * D_k
                                )
                                + 2 * self.v_int * (Etai * D_j * D_k + Etaj * D_i * D_k)
                                + C1 * (2 * Etak * D_i * D_j + Etaj * Dik + Etai * Djk)
                                - C2 * Etak * Dij
                            )
                            * self.OME[ig - 1]
                        )
                        # print(f"DEBUG (integral numerica): H={H}, G={G}")
                        aux = (2 * indk) - 1
                        self.A[jj - 1, aux - 1] += (1 - self.GI[ig - 1]) * H / 2
                        self.A[jj - 1, aux] += (1 + self.GI[ig - 1]) * H / 2
                        self.B[jj - 1, aux - 1] += (1 - self.GI[ig - 1]) * G / 2
                        self.B[jj - 1, aux] += (1 + self.GI[ig - 1]) * G / 2
                        # print(f"DEBUG (integral numerica): A={self.A}")
        return

    def Monta_Matrizes_G_H(self):
        # print('... Montagem das matrizes [G] e [H] ...')

        self.H = np.zeros((4 * self.Num_elem, 4 * self.Num_elem))
        self.G = np.zeros((4 * self.Num_elem, 4 * self.Num_elem))
        self.Se = np.zeros(self.Num_elem)
        self.Co = np.zeros(self.Num_elem)

        self.obter_pontos_de_gauss()

        # print(f"PRIMEIRO G={self.G} or H={self.H} for element {self.Num_elem}")
        j_values = []
        k_values = []

        for elem in range(self.Num_elem):
            j = self.conect[elem][0] - 1
            k = self.conect[elem][1] - 1
            L = self.comprimento(j, k)

            self.Se[elem] = (self.Y_cont[k] - self.Y_cont[j]) / L
            self.Co[elem] = (self.X_cont[k] - self.X_cont[j]) / L

        # Estrutura de repeti��o para montagem das matrizes G e H
        for elem_i in range(1, self.Num_elem + 1):
            for elem_j in range(1, self.Num_elem + 1):
                if elem_i == elem_j:
                    self.matrizes_auxiliares()
                    self.Integral_elem_singular(
                        elem_i
                    )  # Chama a função para integração singular

                else:
                    self.Integral_elem_nao_singular(
                        elem_i, elem_j
                    )  # Chama a função para integração numérica

        for ponto in range(1, 4 * self.Num_elem + 1):
            if self.codigo[ponto - 1] > 0:
                for lin in range(1, 4 * self.Num_elem + 1):
                    aux = self.G[lin - 1, ponto - 1]
                    self.G[lin - 1, ponto - 1] = (-1) * self.H[lin - 1, ponto - 1]
                    self.H[lin - 1, ponto - 1] = (-1) * aux
                    # print(f"DEBUG (integral numerica): H={self.H}")
                    # print(f"DEBUG (integral numerica): G={self.G}")
                p = 1
            else:
                for lin in range(1, 4 * self.Num_elem + 1):
                    self.G[lin - 1, ponto - 1] = self.G[lin - 1, ponto - 1] * self.Gc
                    # print(f"DEBUG (integral numerica): G={self.G}")

        return

    def Vetor_Valores_Prescritos(self):
        self.FD = np.zeros(4 * self.Num_elem)  # Vetor de valores prescritos

        for lin in range(1, 4 * self.Num_elem + 1):
            for col in range(1, 4 * self.Num_elem + 1):
                self.FD[lin - 1] += self.H[lin - 1, col - 1] * self.valor[col - 1]

        return

    def Resolucao_Sistema(self):
        # print('... Resolução do sistema linear ...')

        self.C = np.linalg.solve(self.G, self.FD)
        # print(f"C={self.C}")

        for lin in range(1, (4 * self.Num_elem) + 1):
            self.FD[lin - 1] = self.C[lin - 1]

            if self.codigo[lin - 1] == 0:
                aux = self.valor[lin - 1]
                self.valor[lin - 1] = round(self.FD[lin - 1] * self.Gc, 5)
                self.FD[lin - 1] = round(aux * self.Gc, 5)
        return

    def Pontos_Internos2(self):
        self.Monta_Matrizes_G_H()

        # print('... Cálculo nos pontos internos ...')

        self.D_Int = np.zeros((self.Num_P_int, 2))
        self.Tens_Int = np.zeros((self.Num_P_int, 3))
        self.Tens_P = np.zeros((self.Num_P_int, 4))
        self.Teta_P = np.zeros((self.Num_P_int, 2))

        self.v_int = self.v / (1 + self.v)

        for ponto in range(self.Num_P_int):
            for elem in range(self.Num_elem):
                self.integral_numerica(self.X_int[ponto], self.Y_int[ponto], elem + 1)
                lin = 4 * (elem + 1) - 4
                self.D_Int[ponto, 0] = (
                    self.D_Int[ponto, 0]
                    + self.valor[lin] * self.B[0, 0]
                    - self.FD[lin] * self.A[0, 0]
                    + self.valor[lin + 1] * self.B[0, 2]
                    - self.FD[lin + 1] * self.A[0, 2]
                    + self.valor[lin + 2] * self.B[0, 1]
                    - self.FD[lin + 2] * self.A[0, 1]
                    + self.valor[lin + 3] * self.B[0, 3]
                    - self.FD[lin + 3] * self.A[0, 3]
                )
                self.D_Int[ponto, 1] = (
                    self.D_Int[ponto, 1]
                    + self.valor[lin] * self.B[1, 0]
                    - self.FD[lin] * self.A[1, 0]
                    + self.valor[lin + 1] * self.B[1, 2]
                    - self.FD[lin + 1] * self.A[1, 2]
                    + self.valor[lin + 2] * self.B[1, 1]
                    - self.FD[lin + 2] * self.A[1, 1]
                    + self.valor[lin + 3] * self.B[1, 3]
                    - self.FD[lin + 3] * self.A[1, 3]
                )
                self.tensoes_internas(self.X_int[ponto], self.Y_int[ponto], elem + 1)
                self.Tens_Int[ponto, 0] += (
                    self.valor[lin] * self.B[0, 0]
                    - self.FD[lin] * self.A[0, 0]
                    + self.valor[lin + 1] * self.B[0, 2]
                    - self.FD[lin + 1] * self.A[0, 2]
                    + self.valor[lin + 2] * self.B[0, 1]
                    - self.FD[lin + 2] * self.A[0, 1]
                    + self.valor[lin + 3] * self.B[0, 3]
                    - self.FD[lin + 3] * self.A[0, 3]
                )
                self.Tens_Int[ponto, 1] += (
                    self.valor[lin] * self.B[1, 0]
                    - self.FD[lin] * self.A[1, 0]
                    + self.valor[lin + 1] * self.B[1, 2]
                    - self.FD[lin + 1] * self.A[1, 2]
                    + self.valor[lin + 2] * self.B[1, 1]
                    - self.FD[lin + 2] * self.A[1, 1]
                    + self.valor[lin + 3] * self.B[1, 3]
                    - self.FD[lin + 3] * self.A[1, 3]
                )
                self.Tens_Int[ponto, 2] += (
                    self.valor[lin] * self.B[2, 0]
                    - self.FD[lin] * self.A[2, 0]
                    + self.valor[lin + 1] * self.B[2, 2]
                    - self.FD[lin + 1] * self.A[2, 2]
                    + self.valor[lin + 2] * self.B[2, 1]
                    - self.FD[lin + 2] * self.A[2, 1]
                    + self.valor[lin + 3] * self.B[2, 3]
                    - self.FD[lin + 3] * self.A[2, 3]
                )
            teta1 = (
                np.arctan(
                    2
                    * self.Tens_Int[ponto, 1]
                    / (self.Tens_Int[ponto, 0] - self.Tens_Int[ponto, 2])
                )
                / 2
            )
            teta2 = teta1 + np.pi / 2
            self.Tens_P[ponto, 0] = (
                self.Tens_Int[ponto, 0] * (np.cos(teta1)) ** 2
                + self.Tens_Int[ponto, 2] * (np.sin(teta1)) ** 2
                + self.Tens_Int[ponto, 1] * np.cos(2 * teta1)
            )
            self.Tens_P[ponto, 1] = (
                self.Tens_Int[ponto, 0] * (np.cos(teta2)) ** 2
                + self.Tens_Int[ponto, 2] * (np.sin(teta2)) ** 2
                + self.Tens_Int[ponto, 1] * np.cos(2 * teta2)
            )
            self.Teta_P[ponto][0] = teta1
            self.Teta_P[ponto][1] = teta2

            # Procura de ponto mais solicitado por tensões de compressão em Y
            sigma3teste = [t for t in self.Tens_Int[:, 2]]
            deslocYteste = [d for d in self.D_Int[:, 1]]

            sigma3max = max(sigma3teste, key=abs)
            Desloc3max = max(deslocYteste, key=abs)
            self.pontoMax = sigma3teste.index(sigma3max)
            self.pontoDMax = deslocYteste.index(Desloc3max)

            # Valores das tensões a partir de zero de carga, até o colapso
            valorColapso = self.sigmaMaxMat / sigma3teste[self.pontoMax]
            Desloc3maxM = deslocYteste[self.pontoDMax] * self.sigmaMaxMat
            deltaValor = valorColapso / 20
            deltaDesloc = Desloc3maxM / 20
            deltasigmaYMax = self.sigmaMaxMat / 20

            self.sigmaPontoMax = [deltaValor * (i - 1) for i in range(1, 22)]
            self.DeslocYMax = [deltaDesloc * (i - 1) for i in range(1, 22)]
            self.sigmaYMax = [deltasigmaYMax * (i - 1) for i in range(1, 22)]
        return

    def Calcula_VM(self):

        for i in range(1, self.Num_P_int + 1):
            self.tensao_vm.append(((self.Tens_Int[i - 1][0]) ** 2 + (self.Tens_Int[i - 1][2]) ** 2 - (
                        (self.Tens_Int[i - 1][0]) * (self.Tens_Int[i - 1][2]))) ** (1 / 2))

    def plot_desenho(self):
        
        plt.figure(figsize=(10, 10))
        
        # Plotar pontos de contorno
        if self.X_cont and self.Y_cont:
            plt.plot(self.X_cont, self.Y_cont, 'bo-', label="Pontos de Contorno")
        
        # Plotar pontos internos
        if self.X_int and self.Y_int:
            plt.plot(self.X_int, self.Y_int, 'ro', label="Pontos Internos")

        # Adicionando condições de contorno e forças
        for i, (x, y) in enumerate(zip(self.X_cont, self.Y_cont)):
            condition_x = self.codigo[2*i]
            force_x = self.valor[2*i]
            condition_y = self.codigo[2*i + 1]
            force_y = self.valor[2*i + 1]
            
            # Condições de contorno
            if condition_x == 0 and condition_y == 0:
                plt.plot(x, y, 'ks', markersize=10, label="Engaste" if 'Engaste' not in plt.gca().get_legend_handles_labels()[1] else "")
            elif condition_x == 0 and condition_y == 1:
                plt.plot(x, y, 'ms', markersize=10, label="Apoio 1º Gênero" if 'Apoio 1º Gênero' not in plt.gca().get_legend_handles_labels()[1] else "")
            elif condition_x == 1 and condition_y == 0:
                plt.plot(x, y, 'gs', markersize=10, label="Apoio 2º Gênero" if 'Apoio 2º Gênero' not in plt.gca().get_legend_handles_labels()[1] else "")

            # Forças aplicadas
            if force_x != 0:
                plt.arrow(x, y, force_x * 0.1, 0, head_width=0.05, head_length=0.1, fc='green', ec='green', label="Força X" if 'Força X' not in plt.gca().get_legend_handles_labels()[1] else "")
            if force_y != 0:
                plt.arrow(x, y, 0, force_y * 0.1, head_width=0.05, head_length=0.1, fc='blue', ec='blue', label="Força Y" if 'Força Y' not in plt.gca().get_legend_handles_labels()[1] else "")
        
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Desenho dos Pontos")
        plt.legend()
        plt.grid(True)
        plt.axis('equal')
        plt.show()
        
    def Saida_dados(self):
        arquivoS = open("Saida_Exemplo_1_64.txt", "wt")
        # print(len(self.X_int), len(self.Y_int), len(self.D_Int), len(self.Tens_Int), len(self.Tens_P), len(self.Teta_P))

        # Saída de dados
        arquivoS.write("ARQUIVO DE SAIDA DE DADOS E RESULTADOS \n\n")
        arquivoS.write("Dados de entrada do problema 2D elastostatico \n")
        arquivoS.write("Modulo de elasticidade longitudinal %10.4f \n" % self.E)
        arquivoS.write("Modulo de elasticidade transversal %10.4f \n" % self.Gc)
        # Adicione uma verificação para self.Gc antes de tentar escrevê-lo
        arquivoS.write("Coeficiente de Poisson              %10.4f \n" % self.v)
        arquivoS.write("Resistencia aa Compressao do Material %10.4f \n" % self.sigmaMaxMat)
        arquivoS.write("Numero de elementos          %10d \n" % self.Num_elem)
        arquivoS.write("Numero de contornos          %10d \n" % self.Num_P_cont)
        arquivoS.write("Numero de nos Interno        %10d \n" % self.Num_P_int)
        arquivoS.write("Coordenadas X e Y dosuNos do Contorno:\n")
        arquivoS.write("\n No    Coord-X    Coord-Y \n")
        for i in range(1, self.Num_P_cont + 1):
            arquivoS.write(
                "%4d %10.4f %10.4f\n" % (i, self.X_cont[i - 1], self.Y_cont[i - 1])
            )

        arquivoS.write("\n Conectividade dos Elementos\n")
        arquivoS.write("\n Elemento  No Inicial    No Final \n")
        for i in range(1, self.Num_elem + 1):
            arquivoS.write(
                "%8d %12d %12d \n" % (i, self.conect[i - 1][0], self.conect[i - 1][1])
            )

        arquivoS.write("\n Resultados Encontrados \n")
        arquivoS.write("\n *** PONTOS DO CONTORNO *** \n")
        arquivoS.write(
            "\n LPoint    Desloc-X   Desloc-Y       FSuperf-X   FSuperf-Y \n"
        )
        for i in range(1, self.Num_P_cont + 1):
            arquivoS.write(
                "%4d %14.4f %10.4f %15.4f %10.4f\n"
                % (
                    i,
                    self.FD[2 * i - 2],
                    self.FD[2 * i - 1],
                    self.valor[2 * i - 2],
                    self.valor[2 * i - 1],
                )
            )

        arquivoS.write("\n *** PONTOS INTERNOS *** \n")
        arquivoS.write(
            "\n P_int   Coord-X   Coord-Y        Desloc-X   Desloc-Y       Tensao-X   Tensao-Y   Tensao_XY      Sigma1    Sigma2    Teta1  Teta2\n"
        )
        for i in range(1, self.Num_P_int + 1):
            arquivoS.write(
                "%4d %10.4f %10.4f %14.4f %10.4f %15.4f %10.4f %10.4f %12.4f %10.4f %6.1f %6.1f\n"
                % (
                    i - 1,
                    self.X_int[i - 1],
                    self.Y_int[i - 1],
                    self.D_Int[i - 1][0],
                    self.D_Int[i - 1][1],
                    self.Tens_Int[i - 1][0],
                    self.Tens_Int[i - 1][2],
                    self.Tens_Int[i - 1][1],
                    self.Tens_P[i - 1][0],
                    self.Tens_P[i - 1][1],
                    (self.Teta_P[i - 1][0] * 180 / np.pi),
                    (self.Teta_P[i - 1][1] * 180 / np.pi),
                )
            )
        arquivoS.write(
            "\n *** PROC. ITERATIVO: PONTOS INTERNOS sigmaMax E DeslMax *** \n"
        )
        arquivoS.write(
            "\n Passo de Carga P_int   Coord-X   Coord-Y       F.Superf.       Tensao-Y\n"
        )
        for i in range(1, 22):
            arquivoS.write(
                "%15d %4d %10.4f %10.4f %14.8f %14.8f \n"
                % (
                    i,
                    self.pontoMax,
                    self.X_int[self.pontoMax],
                    self.Y_int[self.pontoMax],
                    self.sigmaPontoMax[i - 1],
                    self.sigmaYMax[i - 1],
                )
            )

        arquivoS.write(
            "\n Passo de Carga P_int   Coord-X   Coord-Y        Desloc-Y      F.Superf.\n"
        )
        for i in range(1, 22):
            arquivoS.write(
                "%15d %4d %10.4f %10.4f %14.8f %14.8f \n"
                % (
                    i,
                    self.pontoDMax,
                    self.X_int[self.pontoDMax],
                    self.Y_int[self.pontoDMax],
                    self.DeslocYMax[i - 1],
                    self.sigmaPontoMax[i - 1],
                )
            )

        arquivoS.close()
        
    def principalMEC2DSingle2(self):
        t0 = process_time()
        self.ler_dados()
        self.Monta_Matrizes_G_H()
        self.Vetor_Valores_Prescritos()
        self.Resolucao_Sistema()
        self.Pontos_Internos2()
        self.Calcula_VM()

        return max(self.tensao_vm)

# Criar uma instância da classe e chamar o método principalMEC2DSingle2
caminho_do_arquivo = "Exemplo_1_32.txt"

t0 = process_time()

v_med = 0.33
MONTE_CARLO_REP = 100
monte_carlo_v = norm.rvs(size=MONTE_CARLO_REP, loc=1.1 * v_med, scale=1.1 * .1 * v_med)
Pf = 0
passou = True
TENSAO_ESCOAMENTO = 450 * (10 ** 6)

p2 = math.sqrt(math.log(((.063 * 1.03 * TENSAO_ESCOAMENTO) ** 2 / (1.03 * TENSAO_ESCOAMENTO) ** 2) + 1))
p1 = math.log(1.03 * TENSAO_ESCOAMENTO) - (p2 ** 2) / 2
monte_carlo_T_E = lognorm.rvs(s=p2, size=MONTE_CARLO_REP, loc=0, scale=math.exp(p1))

def evento_falhou(tensao_escoamento, tensao_vm):
    return (tensao_vm > tensao_escoamento)

# Para plotar o gráfico
resistencia_sem_falha = []
solicitacao_sem_falha = []
resistencia_com_falha = []
solicitacao_com_falha = []

for i in range(MONTE_CARLO_REP):
    dados_material_instancia = DadosMaterial(caminho_arquivo=caminho_do_arquivo, v_sc=monte_carlo_v[i])
    tensao_vm = dados_material_instancia.principalMEC2DSingle2()
    print(f'TENSAO_VM: {tensao_vm}, Força: {monte_carlo_v[i]} ')
    print(f'TENSAO_ESCOAMENTO: {monte_carlo_T_E[i]}')

    if evento_falhou(monte_carlo_T_E[i], tensao_vm):
        Pf = Pf + 1 / MONTE_CARLO_REP
        resistencia_com_falha.append(monte_carlo_T_E[i])  # Resistência no evento de falha
        solicitacao_com_falha.append(tensao_vm)  # Solicitação (tensão von Mises) no evento de falha
        print(f'TENSAO_ESCOAMENTO: {monte_carlo_T_E[i]}')

    else:
        resistencia_sem_falha.append(monte_carlo_T_E[i])
        solicitacao_sem_falha.append(tensao_vm)

# Imprimir a probabilidade de falha
print(f"Probabilidade de falha: {Pf}")

dtempo = process_time() - t0
print(f"... Tempo Gasto... {dtempo:.10f}")

# Plotar o gráfico
plt.figure(figsize=(8, 6))

# Eventos sem falha
plt.scatter(resistencia_sem_falha, solicitacao_sem_falha, color='black', label='Eventos sem falha')

# Eventos com falha
plt.scatter(resistencia_com_falha, solicitacao_com_falha, color='red', label='Eventos com falha')

# Plotar a linha de falha G(R,S)=0 (onde a solicitação é igual à resistência)
limite_max = max(max(monte_carlo_T_E), max(monte_carlo_v))
plt.plot([0, limite_max], [0, limite_max], color='red', label='G(R, S) = R - S = 0')

# Título e rótulos dos eixos
plt.title('Simulação de Monte Carlo - Resistência vs Solicitação')
plt.xlabel('Resistência (Tensão von Mises)')
plt.ylabel('Solicitação (Força aplicada)')

# Adicionar legenda e grade
plt.legend()
plt.grid(True)

# Mostrar o gráfico
plt.show()
