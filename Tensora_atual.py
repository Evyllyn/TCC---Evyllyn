# =-=-=-=-=-=-=-= [ IMPORTANTO OS PACOTES NECESSÁRIOS PARA O PROGRAMA ] =-=-=-=-=-=-=-= #

from PyQt5 import QtCore, QtGui, QtWidgets #Interface Gráfica
import numpy as np # Operação com matrizes
from math import * # Operações Matemáticas
import matplotlib.pyplot as plt #Gráficos
from matplotlib.patches import Arc #Gráficos

# =-=-=-=-=-=-=-= [ CÓDIGO DA INTERFACE GRÁFICA ] =-=-=-=-=-=-=-= #

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(984, 615)
        icon = QtGui.QIcon.fromTheme("PlaneStr2")
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 241, 561))
        self.frame.setStyleSheet("background-color: #EB3438 ;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setEnabled(True)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 221, 541))
        self.frame_2.setStyleSheet("border: 1px solid white;\n"
"background-color: transparent;\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(50, 90, 121, 121))
        self.label.setStyleSheet("border-radius: 60px;\n"
"background-color: white;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(40, 80, 141, 141))
        self.frame_3.setStyleSheet("border-radius: 70px;\n"
"border: 2px solid white;\n"
"background-color: transparent;\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border: transparent")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(50, 400, 121, 141))
        self.label_3.setStyleSheet("border:transparent")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("ufal branco.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(70, 50, 91, 16))
        self.label_4.setStyleSheet("border:transparent")
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(10, 230, 201, 101))
        self.label_5.setStyleSheet("border:none")
        self.label_5.setScaledContents(True)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(20, 310, 201, 71))
        self.label_6.setStyleSheet("border:none")
        self.label_6.setScaledContents(True)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(10, 370, 201, 71))
        self.label_7.setStyleSheet("border:none")
        self.label_7.setScaledContents(True)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.frame_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(250, 0, 711, 561))
        self.tabWidget.setStyleSheet("QTabBar::tab:selected {\n"
"    background-color: #EB3438 ;\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(330, 30, 20, 481))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.frame_4 = QtWidgets.QFrame(self.tab)
        self.frame_4.setGeometry(QtCore.QRect(10, 20, 151, 21))
        self.frame_4.setStyleSheet("background-color: #EB3438 ;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setGeometry(QtCore.QRect(10, 0, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("border: transparent")
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setScaledContents(True)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_8.setWordWrap(False)
        self.label_8.setObjectName("label_8")
        self.frame_5 = QtWidgets.QFrame(self.tab)
        self.frame_5.setGeometry(QtCore.QRect(10, 20, 311, 191))
        self.frame_5.setStyleSheet("border: 2px solid #EB3438;\n"
"border-style: dashed;\n"
"background-color: transparent;\n"
"")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.line_2 = QtWidgets.QFrame(self.frame_5)
        self.line_2.setGeometry(QtCore.QRect(110, 50, 161, 101))
        self.line_2.setStyleSheet("QFrame {\n"
"    border: 1px solid black;\n"
"}\n"
"")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_11 = QtWidgets.QLabel(self.frame_5)
        self.label_11.setGeometry(QtCore.QRect(30, 80, 61, 41))
        self.label_11.setStyleSheet("border: none;\n"
"")
        self.label_11.setObjectName("label_11")
        self.lineEdit_sigmaxx = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_sigmaxx.setGeometry(QtCore.QRect(120, 60, 41, 21))
        self.lineEdit_sigmaxx.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_sigmaxx.setFrame(True)
        self.lineEdit_sigmaxx.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_sigmaxx.setObjectName("lineEdit_sigmaxx")
        self.lineEdit_sigmaxy = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_sigmaxy.setGeometry(QtCore.QRect(170, 60, 41, 21))
        self.lineEdit_sigmaxy.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_sigmaxy.setFrame(True)
        self.lineEdit_sigmaxy.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_sigmaxy.setObjectName("lineEdit_sigmaxy")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(220, 60, 41, 21))
        self.lineEdit_3.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_3.setFrame(True)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_sigmayx = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_sigmayx.setGeometry(QtCore.QRect(120, 90, 41, 21))
        self.lineEdit_sigmayx.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_sigmayx.setFrame(True)
        self.lineEdit_sigmayx.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_sigmayx.setObjectName("lineEdit_sigmayx")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 120, 41, 21))
        self.lineEdit_5.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_5.setFrame(True)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setPlaceholderText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_sigmayy = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_sigmayy.setGeometry(QtCore.QRect(170, 90, 41, 21))
        self.lineEdit_sigmayy.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_sigmayy.setFrame(True)
        self.lineEdit_sigmayy.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_sigmayy.setObjectName("lineEdit_sigmayy")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_7.setGeometry(QtCore.QRect(220, 90, 41, 21))
        self.lineEdit_7.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_7.setFrame(True)
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_8.setEnabled(False)
        self.lineEdit_8.setGeometry(QtCore.QRect(170, 120, 41, 21))
        self.lineEdit_8.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_8.setFrame(True)
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_sigmazz = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_sigmazz.setGeometry(QtCore.QRect(220, 120, 41, 21))
        self.lineEdit_sigmazz.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_sigmazz.setFrame(True)
        self.lineEdit_sigmazz.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_sigmazz.setObjectName("lineEdit_sigmazz")
        self.label_12 = QtWidgets.QLabel(self.frame_5)
        self.label_12.setGeometry(QtCore.QRect(20, 0, 291, 71))
        self.label_12.setStyleSheet("border:none")
        self.label_12.setScaledContents(True)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.frame_6 = QtWidgets.QFrame(self.tab)
        self.frame_6.setGeometry(QtCore.QRect(10, 250, 201, 21))
        self.frame_6.setStyleSheet("background-color: #EB3438 ;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_9 = QtWidgets.QLabel(self.frame_6)
        self.label_9.setGeometry(QtCore.QRect(10, 0, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("border: transparent")
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setScaledContents(True)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_9.setWordWrap(False)
        self.label_9.setObjectName("label_9")
        self.frame_7 = QtWidgets.QFrame(self.tab)
        self.frame_7.setGeometry(QtCore.QRect(10, 390, 201, 21))
        self.frame_7.setStyleSheet("background-color: #EB3438 ;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_10 = QtWidgets.QLabel(self.frame_7)
        self.label_10.setGeometry(QtCore.QRect(10, 0, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("border: transparent")
        self.label_10.setTextFormat(QtCore.Qt.AutoText)
        self.label_10.setScaledContents(True)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_10.setWordWrap(False)
        self.label_10.setObjectName("label_10")
        self.pushButton_calculartensoes = QtWidgets.QPushButton(self.tab)
        self.pushButton_calculartensoes.setGeometry(QtCore.QRect(110, 190, 111, 41))
        self.pushButton_calculartensoes.setObjectName("pushButton_calculartensoes")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(20, 310, 81, 41))
        self.label_13.setStyleSheet("border: none;\n"
"")
        self.label_13.setObjectName("label_13")
        self.line_3 = QtWidgets.QFrame(self.tab)
        self.line_3.setGeometry(QtCore.QRect(120, 280, 161, 101))
        self.line_3.setStyleSheet("QFrame {\n"
"    border: 1px solid black;\n"
"}\n"
"")
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(20, 450, 81, 41))
        self.label_14.setStyleSheet("border: none;\n"
"")
        self.label_14.setObjectName("label_14")
        self.line_4 = QtWidgets.QFrame(self.tab)
        self.line_4.setGeometry(QtCore.QRect(120, 420, 161, 101))
        self.line_4.setStyleSheet("QFrame {\n"
"    border: 1px solid black;\n"
"}\n"
"")
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.lineEdit_sigmamxx = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_sigmamxx.setEnabled(False)
        self.lineEdit_sigmamxx.setGeometry(QtCore.QRect(130, 290, 41, 21))
        self.lineEdit_sigmamxx.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_sigmamxx.setFrame(True)
        self.lineEdit_sigmamxx.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_sigmamxx.setObjectName("lineEdit_sigmamxx")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_6.setGeometry(QtCore.QRect(230, 290, 41, 21))
        self.lineEdit_6.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_6.setFrame(True)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_9.setEnabled(False)
        self.lineEdit_9.setGeometry(QtCore.QRect(180, 290, 41, 21))
        self.lineEdit_9.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_9.setFrame(True)
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_10.setEnabled(False)
        self.lineEdit_10.setGeometry(QtCore.QRect(130, 320, 41, 21))
        self.lineEdit_10.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_10.setFrame(True)
        self.lineEdit_10.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_11.setEnabled(False)
        self.lineEdit_11.setGeometry(QtCore.QRect(130, 350, 41, 21))
        self.lineEdit_11.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_11.setFrame(True)
        self.lineEdit_11.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_12.setEnabled(False)
        self.lineEdit_12.setGeometry(QtCore.QRect(180, 350, 41, 21))
        self.lineEdit_12.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_12.setFrame(True)
        self.lineEdit_12.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_13.setEnabled(False)
        self.lineEdit_13.setGeometry(QtCore.QRect(230, 320, 41, 21))
        self.lineEdit_13.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_13.setFrame(True)
        self.lineEdit_13.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_sigmamyy = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_sigmamyy.setEnabled(False)
        self.lineEdit_sigmamyy.setGeometry(QtCore.QRect(180, 320, 41, 21))
        self.lineEdit_sigmamyy.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_sigmamyy.setFrame(True)
        self.lineEdit_sigmamyy.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_sigmamyy.setObjectName("lineEdit_sigmamyy")
        self.lineEdit_sigmamzz = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_sigmamzz.setEnabled(False)
        self.lineEdit_sigmamzz.setGeometry(QtCore.QRect(230, 350, 41, 21))
        self.lineEdit_sigmamzz.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_sigmamzz.setFrame(True)
        self.lineEdit_sigmamzz.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_sigmamzz.setObjectName("lineEdit_sigmamzz")
        self.lineEdit_sigmasxx = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_sigmasxx.setEnabled(False)
        self.lineEdit_sigmasxx.setGeometry(QtCore.QRect(130, 430, 41, 21))
        self.lineEdit_sigmasxx.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_sigmasxx.setFrame(True)
        self.lineEdit_sigmasxx.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_sigmasxx.setObjectName("lineEdit_sigmasxx")
        self.lineEdit_sigmasxy = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_sigmasxy.setEnabled(False)
        self.lineEdit_sigmasxy.setGeometry(QtCore.QRect(180, 430, 41, 21))
        self.lineEdit_sigmasxy.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_sigmasxy.setFrame(True)
        self.lineEdit_sigmasxy.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_sigmasxy.setObjectName("lineEdit_sigmasxy")
        self.lineEdit_sigmasyx = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_sigmasyx.setEnabled(False)
        self.lineEdit_sigmasyx.setGeometry(QtCore.QRect(130, 460, 41, 21))
        self.lineEdit_sigmasyx.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_sigmasyx.setFrame(True)
        self.lineEdit_sigmasyx.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_sigmasyx.setObjectName("lineEdit_sigmasyx")
        self.lineEdit_sigmasyy = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_sigmasyy.setEnabled(False)
        self.lineEdit_sigmasyy.setGeometry(QtCore.QRect(180, 460, 41, 21))
        self.lineEdit_sigmasyy.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_sigmasyy.setFrame(True)
        self.lineEdit_sigmasyy.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_sigmasyy.setObjectName("lineEdit_sigmasyy")
        self.lineEdit_sigmaszz = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_sigmaszz.setEnabled(False)
        self.lineEdit_sigmaszz.setGeometry(QtCore.QRect(230, 490, 41, 21))
        self.lineEdit_sigmaszz.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_sigmaszz.setFrame(True)
        self.lineEdit_sigmaszz.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_sigmaszz.setObjectName("lineEdit_sigmaszz")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_15.setEnabled(False)
        self.lineEdit_15.setGeometry(QtCore.QRect(230, 430, 41, 21))
        self.lineEdit_15.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_15.setFrame(True)
        self.lineEdit_15.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_16.setEnabled(False)
        self.lineEdit_16.setGeometry(QtCore.QRect(230, 460, 41, 21))
        self.lineEdit_16.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_16.setFrame(True)
        self.lineEdit_16.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_17.setEnabled(False)
        self.lineEdit_17.setGeometry(QtCore.QRect(130, 490, 41, 21))
        self.lineEdit_17.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_17.setFrame(True)
        self.lineEdit_17.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_18.setEnabled(False)
        self.lineEdit_18.setGeometry(QtCore.QRect(180, 490, 41, 21))
        self.lineEdit_18.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_18.setFrame(True)
        self.lineEdit_18.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_textoiso = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_textoiso.setEnabled(False)
        self.lineEdit_textoiso.setGeometry(QtCore.QRect(220, 250, 113, 20))
        self.lineEdit_textoiso.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_textoiso.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_textoiso.setObjectName("lineEdit_textoiso")
        self.lineEdit_textos = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_textos.setEnabled(False)
        self.lineEdit_textos.setGeometry(QtCore.QRect(220, 390, 113, 20))
        self.lineEdit_textos.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_textos.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_textos.setObjectName("lineEdit_textos")
        self.frame_8 = QtWidgets.QFrame(self.tab)
        self.frame_8.setGeometry(QtCore.QRect(350, 20, 231, 21))
        self.frame_8.setStyleSheet("background-color: #EB3438 ;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.label_16 = QtWidgets.QLabel(self.frame_8)
        self.label_16.setGeometry(QtCore.QRect(10, 0, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("border: transparent")
        self.label_16.setTextFormat(QtCore.Qt.AutoText)
        self.label_16.setScaledContents(True)
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_16.setWordWrap(False)
        self.label_16.setObjectName("label_16")
        self.lineEdit_sigmamedio = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_sigmamedio.setEnabled(False)
        self.lineEdit_sigmamedio.setGeometry(QtCore.QRect(430, 70, 81, 31))
        self.lineEdit_sigmamedio.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_sigmamedio.setText("")
        self.lineEdit_sigmamedio.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_sigmamedio.setObjectName("lineEdit_sigmamedio")
        self.lineEdit_raio = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_raio.setEnabled(False)
        self.lineEdit_raio.setGeometry(QtCore.QRect(590, 70, 81, 31))
        self.lineEdit_raio.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_raio.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_raio.setObjectName("lineEdit_raio")
        self.label_17 = QtWidgets.QLabel(self.tab)
        self.label_17.setGeometry(QtCore.QRect(360, 70, 51, 31))
        self.label_17.setStyleSheet("border: none;\n"
"")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.tab)
        self.label_18.setGeometry(QtCore.QRect(530, 70, 51, 31))
        self.label_18.setStyleSheet("border: none;\n"
"")
        self.label_18.setObjectName("label_18")
        self.label_20 = QtWidgets.QLabel(self.tab)
        self.label_20.setGeometry(QtCore.QRect(360, 120, 61, 31))
        self.label_20.setStyleSheet("border: none;\n"
"")
        self.label_20.setObjectName("label_20")
        self.lineEdit_sigma1 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_sigma1.setEnabled(False)
        self.lineEdit_sigma1.setGeometry(QtCore.QRect(430, 120, 81, 31))
        self.lineEdit_sigma1.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_sigma1.setText("")
        self.lineEdit_sigma1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_sigma1.setObjectName("lineEdit_sigma1")
        self.label_21 = QtWidgets.QLabel(self.tab)
        self.label_21.setGeometry(QtCore.QRect(530, 120, 51, 31))
        self.label_21.setStyleSheet("border: none;\n"
"")
        self.label_21.setObjectName("label_21")
        self.lineEdit_teta1 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_teta1.setEnabled(False)
        self.lineEdit_teta1.setGeometry(QtCore.QRect(590, 120, 81, 31))
        self.lineEdit_teta1.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_teta1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_teta1.setObjectName("lineEdit_teta1")
        self.label_22 = QtWidgets.QLabel(self.tab)
        self.label_22.setGeometry(QtCore.QRect(360, 170, 61, 31))
        self.label_22.setStyleSheet("border: none;\n"
"")
        self.label_22.setObjectName("label_22")
        self.lineEdit_sigma2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_sigma2.setEnabled(False)
        self.lineEdit_sigma2.setGeometry(QtCore.QRect(430, 170, 81, 31))
        self.lineEdit_sigma2.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_sigma2.setText("")
        self.lineEdit_sigma2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_sigma2.setObjectName("lineEdit_sigma2")
        self.label_23 = QtWidgets.QLabel(self.tab)
        self.label_23.setGeometry(QtCore.QRect(530, 170, 51, 31))
        self.label_23.setStyleSheet("border: none;\n"
"")
        self.label_23.setObjectName("label_23")
        self.lineEdit_teta2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_teta2.setEnabled(False)
        self.lineEdit_teta2.setGeometry(QtCore.QRect(590, 170, 81, 31))
        self.lineEdit_teta2.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_teta2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_teta2.setObjectName("lineEdit_teta2")
        self.label_25 = QtWidgets.QLabel(self.tab)
        self.label_25.setGeometry(QtCore.QRect(530, 330, 51, 31))
        self.label_25.setStyleSheet("border: none;\n"
"")
        self.label_25.setObjectName("label_25")
        self.lineEdit_tetacismmax = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_tetacismmax.setEnabled(False)
        self.lineEdit_tetacismmax.setGeometry(QtCore.QRect(590, 330, 81, 31))
        self.lineEdit_tetacismmax.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_tetacismmax.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_tetacismmax.setObjectName("lineEdit_tetacismmax")
        self.lineEdit_cismax = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_cismax.setEnabled(False)
        self.lineEdit_cismax.setGeometry(QtCore.QRect(430, 330, 81, 31))
        self.lineEdit_cismax.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_cismax.setText("")
        self.lineEdit_cismax.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_cismax.setObjectName("lineEdit_cismax")
        self.lineEdit_cismin = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_cismin.setEnabled(False)
        self.lineEdit_cismin.setGeometry(QtCore.QRect(430, 370, 81, 31))
        self.lineEdit_cismin.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_cismin.setText("")
        self.lineEdit_cismin.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_cismin.setObjectName("lineEdit_cismin")
        self.label_27 = QtWidgets.QLabel(self.tab)
        self.label_27.setGeometry(QtCore.QRect(530, 370, 51, 31))
        self.label_27.setStyleSheet("border: none;\n"
"")
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.tab)
        self.label_28.setGeometry(QtCore.QRect(360, 330, 61, 31))
        self.label_28.setStyleSheet("border: none;\n"
"")
        self.label_28.setObjectName("label_28")
        self.lineEdit_tetacismin = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_tetacismin.setEnabled(False)
        self.lineEdit_tetacismin.setGeometry(QtCore.QRect(590, 370, 81, 31))
        self.lineEdit_tetacismin.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_tetacismin.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_tetacismin.setObjectName("lineEdit_tetacismin")
        self.label_29 = QtWidgets.QLabel(self.tab)
        self.label_29.setGeometry(QtCore.QRect(360, 370, 61, 31))
        self.label_29.setStyleSheet("border: none;\n"
"")
        self.label_29.setObjectName("label_29")
        self.frame_9 = QtWidgets.QFrame(self.tab)
        self.frame_9.setGeometry(QtCore.QRect(350, 290, 281, 21))
        self.frame_9.setStyleSheet("background-color: #EB3438 ;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.label_30 = QtWidgets.QLabel(self.frame_9)
        self.label_30.setGeometry(QtCore.QRect(10, 0, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("border: transparent")
        self.label_30.setTextFormat(QtCore.Qt.AutoText)
        self.label_30.setScaledContents(True)
        self.label_30.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_30.setWordWrap(False)
        self.label_30.setObjectName("label_30")
        self.pushButton_graficonormal = QtWidgets.QPushButton(self.tab)
        self.pushButton_graficonormal.setGeometry(QtCore.QRect(430, 220, 201, 41))
        self.pushButton_graficonormal.setObjectName("pushButton_graficonormal")
        self.pushButton_graficocis = QtWidgets.QPushButton(self.tab)
        self.pushButton_graficocis.setGeometry(QtCore.QRect(430, 420, 201, 41))
        self.pushButton_graficocis.setObjectName("pushButton_graficocis")
        self.frame_5.raise_()
        self.line.raise_()
        self.frame_4.raise_()
        self.frame_6.raise_()
        self.frame_7.raise_()
        self.pushButton_calculartensoes.raise_()
        self.label_13.raise_()
        self.line_3.raise_()
        self.label_14.raise_()
        self.line_4.raise_()
        self.lineEdit_sigmamxx.raise_()
        self.lineEdit_6.raise_()
        self.lineEdit_9.raise_()
        self.lineEdit_10.raise_()
        self.lineEdit_11.raise_()
        self.lineEdit_12.raise_()
        self.lineEdit_13.raise_()
        self.lineEdit_sigmamyy.raise_()
        self.lineEdit_sigmamzz.raise_()
        self.lineEdit_sigmasxx.raise_()
        self.lineEdit_sigmasxy.raise_()
        self.lineEdit_sigmasyx.raise_()
        self.lineEdit_sigmasyy.raise_()
        self.lineEdit_sigmaszz.raise_()
        self.lineEdit_15.raise_()
        self.lineEdit_16.raise_()
        self.lineEdit_17.raise_()
        self.lineEdit_18.raise_()
        self.lineEdit_textoiso.raise_()
        self.lineEdit_textos.raise_()
        self.frame_8.raise_()
        self.lineEdit_sigmamedio.raise_()
        self.lineEdit_raio.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.label_20.raise_()
        self.lineEdit_sigma1.raise_()
        self.label_21.raise_()
        self.lineEdit_teta1.raise_()
        self.label_22.raise_()
        self.lineEdit_sigma2.raise_()
        self.label_23.raise_()
        self.lineEdit_teta2.raise_()
        self.label_25.raise_()
        self.lineEdit_tetacismmax.raise_()
        self.lineEdit_cismax.raise_()
        self.lineEdit_cismin.raise_()
        self.label_27.raise_()
        self.label_28.raise_()
        self.lineEdit_tetacismin.raise_()
        self.label_29.raise_()
        self.frame_9.raise_()
        self.pushButton_graficonormal.raise_()
        self.pushButton_graficocis.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.frame_24 = QtWidgets.QFrame(self.tab_3)
        self.frame_24.setGeometry(QtCore.QRect(10, 20, 311, 191))
        self.frame_24.setStyleSheet("border: 2px solid #EB3438;\n"
"border-style: dashed;\n"
"background-color: transparent;\n"
"")
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.line_9 = QtWidgets.QFrame(self.frame_24)
        self.line_9.setGeometry(QtCore.QRect(110, 50, 161, 101))
        self.line_9.setStyleSheet("QFrame {\n"
"    border: 1px solid black;\n"
"}\n"
"")
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.label_60 = QtWidgets.QLabel(self.frame_24)
        self.label_60.setGeometry(QtCore.QRect(20, 80, 61, 41))
        self.label_60.setStyleSheet("border: none;\n"
"")
        self.label_60.setObjectName("label_60")
        self.lineEdit_epsilonxx = QtWidgets.QLineEdit(self.frame_24)
        self.lineEdit_epsilonxx.setGeometry(QtCore.QRect(120, 60, 41, 21))
        self.lineEdit_epsilonxx.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_epsilonxx.setFrame(True)
        self.lineEdit_epsilonxx.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_epsilonxx.setObjectName("lineEdit_epsilonxx")
        self.lineEdit_epsilonxy = QtWidgets.QLineEdit(self.frame_24)
        self.lineEdit_epsilonxy.setGeometry(QtCore.QRect(170, 60, 41, 21))
        self.lineEdit_epsilonxy.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_epsilonxy.setFrame(True)
        self.lineEdit_epsilonxy.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_epsilonxy.setObjectName("lineEdit_epsilonxy")
        self.lineEdit_31 = QtWidgets.QLineEdit(self.frame_24)
        self.lineEdit_31.setEnabled(False)
        self.lineEdit_31.setGeometry(QtCore.QRect(220, 60, 41, 21))
        self.lineEdit_31.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_31.setFrame(True)
        self.lineEdit_31.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.lineEdit_epsilonyx = QtWidgets.QLineEdit(self.frame_24)
        self.lineEdit_epsilonyx.setGeometry(QtCore.QRect(120, 90, 41, 21))
        self.lineEdit_epsilonyx.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_epsilonyx.setFrame(True)
        self.lineEdit_epsilonyx.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_epsilonyx.setObjectName("lineEdit_epsilonyx")
        self.lineEdit_32 = QtWidgets.QLineEdit(self.frame_24)
        self.lineEdit_32.setEnabled(False)
        self.lineEdit_32.setGeometry(QtCore.QRect(120, 120, 41, 21))
        self.lineEdit_32.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_32.setFrame(True)
        self.lineEdit_32.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_32.setPlaceholderText("")
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.lineEdit_epsilonyy = QtWidgets.QLineEdit(self.frame_24)
        self.lineEdit_epsilonyy.setGeometry(QtCore.QRect(170, 90, 41, 21))
        self.lineEdit_epsilonyy.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_epsilonyy.setFrame(True)
        self.lineEdit_epsilonyy.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_epsilonyy.setObjectName("lineEdit_epsilonyy")
        self.lineEdit_33 = QtWidgets.QLineEdit(self.frame_24)
        self.lineEdit_33.setEnabled(False)
        self.lineEdit_33.setGeometry(QtCore.QRect(220, 90, 41, 21))
        self.lineEdit_33.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_33.setFrame(True)
        self.lineEdit_33.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.lineEdit_34 = QtWidgets.QLineEdit(self.frame_24)
        self.lineEdit_34.setEnabled(False)
        self.lineEdit_34.setGeometry(QtCore.QRect(170, 120, 41, 21))
        self.lineEdit_34.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_34.setFrame(True)
        self.lineEdit_34.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.lineEdit_epsilonzz = QtWidgets.QLineEdit(self.frame_24)
        self.lineEdit_epsilonzz.setGeometry(QtCore.QRect(220, 120, 41, 21))
        self.lineEdit_epsilonzz.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_epsilonzz.setFrame(True)
        self.lineEdit_epsilonzz.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_epsilonzz.setObjectName("lineEdit_epsilonzz")
        self.label_61 = QtWidgets.QLabel(self.frame_24)
        self.label_61.setGeometry(QtCore.QRect(10, 0, 291, 71))
        self.label_61.setStyleSheet("border:none")
        self.label_61.setScaledContents(True)
        self.label_61.setWordWrap(True)
        self.label_61.setObjectName("label_61")
        self.frame_25 = QtWidgets.QFrame(self.frame_24)
        self.frame_25.setGeometry(QtCore.QRect(0, 0, 151, 21))
        self.frame_25.setStyleSheet("background-color: #EB3438 ;")
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.label_62 = QtWidgets.QLabel(self.frame_25)
        self.label_62.setGeometry(QtCore.QRect(10, 0, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        self.label_62.setFont(font)
        self.label_62.setStyleSheet("border: transparent")
        self.label_62.setTextFormat(QtCore.Qt.AutoText)
        self.label_62.setScaledContents(True)
        self.label_62.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_62.setWordWrap(False)
        self.label_62.setObjectName("label_62")
        self.pushButton_calcular_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_calcular_3.setGeometry(QtCore.QRect(110, 190, 111, 41))
        self.pushButton_calcular_3.setObjectName("pushButton_calcular_3")
        self.frame_26 = QtWidgets.QFrame(self.tab_3)
        self.frame_26.setGeometry(QtCore.QRect(10, 250, 201, 21))
        self.frame_26.setStyleSheet("background-color: #EB3438 ;")
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.label_19 = QtWidgets.QLabel(self.frame_26)
        self.label_19.setGeometry(QtCore.QRect(10, 0, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("border: transparent")
        self.label_19.setTextFormat(QtCore.Qt.AutoText)
        self.label_19.setScaledContents(True)
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_19.setWordWrap(False)
        self.label_19.setObjectName("label_19")
        self.lineEdit_textoiso_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_textoiso_3.setEnabled(False)
        self.lineEdit_textoiso_3.setGeometry(QtCore.QRect(220, 250, 113, 20))
        self.lineEdit_textoiso_3.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_textoiso_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_textoiso_3.setObjectName("lineEdit_textoiso_3")
        self.line_10 = QtWidgets.QFrame(self.tab_3)
        self.line_10.setGeometry(QtCore.QRect(330, 30, 20, 481))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.label_24 = QtWidgets.QLabel(self.tab_3)
        self.label_24.setGeometry(QtCore.QRect(20, 310, 81, 41))
        self.label_24.setStyleSheet("border: none;\n"
"")
        self.label_24.setObjectName("label_24")
        self.line_11 = QtWidgets.QFrame(self.tab_3)
        self.line_11.setGeometry(QtCore.QRect(120, 280, 161, 101))
        self.line_11.setStyleSheet("QFrame {\n"
"    border: 1px solid black;\n"
"}\n"
"")
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.lineEdit_epsilonmedxx = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_epsilonmedxx.setEnabled(False)
        self.lineEdit_epsilonmedxx.setGeometry(QtCore.QRect(130, 290, 41, 21))
        self.lineEdit_epsilonmedxx.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_epsilonmedxx.setFrame(True)
        self.lineEdit_epsilonmedxx.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_epsilonmedxx.setObjectName("lineEdit_epsilonmedxx")
        self.lineEdit_35 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_35.setEnabled(False)
        self.lineEdit_35.setGeometry(QtCore.QRect(180, 290, 41, 21))
        self.lineEdit_35.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_35.setFrame(True)
        self.lineEdit_35.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.lineEdit_36 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_36.setEnabled(False)
        self.lineEdit_36.setGeometry(QtCore.QRect(230, 290, 41, 21))
        self.lineEdit_36.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_36.setFrame(True)
        self.lineEdit_36.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.lineEdit_37 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_37.setEnabled(False)
        self.lineEdit_37.setGeometry(QtCore.QRect(130, 320, 41, 21))
        self.lineEdit_37.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_37.setFrame(True)
        self.lineEdit_37.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.lineEdit_epsilonmedxy = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_epsilonmedxy.setEnabled(False)
        self.lineEdit_epsilonmedxy.setGeometry(QtCore.QRect(180, 320, 41, 21))
        self.lineEdit_epsilonmedxy.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_epsilonmedxy.setFrame(True)
        self.lineEdit_epsilonmedxy.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_epsilonmedxy.setObjectName("lineEdit_epsilonmedxy")
        self.lineEdit_38 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_38.setEnabled(False)
        self.lineEdit_38.setGeometry(QtCore.QRect(230, 320, 41, 21))
        self.lineEdit_38.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_38.setFrame(True)
        self.lineEdit_38.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.lineEdit_39 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_39.setEnabled(False)
        self.lineEdit_39.setGeometry(QtCore.QRect(130, 350, 41, 21))
        self.lineEdit_39.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_39.setFrame(True)
        self.lineEdit_39.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.lineEdit_40 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_40.setEnabled(False)
        self.lineEdit_40.setGeometry(QtCore.QRect(180, 350, 41, 21))
        self.lineEdit_40.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_40.setFrame(True)
        self.lineEdit_40.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.lineEdit_epsilonmedyy = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_epsilonmedyy.setEnabled(False)
        self.lineEdit_epsilonmedyy.setGeometry(QtCore.QRect(230, 350, 41, 21))
        self.lineEdit_epsilonmedyy.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_epsilonmedyy.setFrame(True)
        self.lineEdit_epsilonmedyy.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_epsilonmedyy.setObjectName("lineEdit_epsilonmedyy")
        self.frame_27 = QtWidgets.QFrame(self.tab_3)
        self.frame_27.setGeometry(QtCore.QRect(10, 390, 201, 21))
        self.frame_27.setStyleSheet("background-color: #EB3438 ;")
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.label_63 = QtWidgets.QLabel(self.frame_27)
        self.label_63.setGeometry(QtCore.QRect(10, 0, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        self.label_63.setFont(font)
        self.label_63.setStyleSheet("border: transparent")
        self.label_63.setTextFormat(QtCore.Qt.AutoText)
        self.label_63.setScaledContents(True)
        self.label_63.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_63.setWordWrap(False)
        self.label_63.setObjectName("label_63")
        self.lineEdit_textoiso_4 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_textoiso_4.setEnabled(False)
        self.lineEdit_textoiso_4.setGeometry(QtCore.QRect(220, 390, 113, 20))
        self.lineEdit_textoiso_4.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_textoiso_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_textoiso_4.setObjectName("lineEdit_textoiso_4")
        self.label_64 = QtWidgets.QLabel(self.tab_3)
        self.label_64.setGeometry(QtCore.QRect(20, 450, 81, 41))
        self.label_64.setStyleSheet("border: none;\n"
"")
        self.label_64.setObjectName("label_64")
        self.line_12 = QtWidgets.QFrame(self.tab_3)
        self.line_12.setGeometry(QtCore.QRect(120, 420, 161, 101))
        self.line_12.setStyleSheet("QFrame {\n"
"    border: 1px solid black;\n"
"}\n"
"")
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.lineEdit_epsiloxx = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_epsiloxx.setEnabled(False)
        self.lineEdit_epsiloxx.setGeometry(QtCore.QRect(130, 430, 41, 21))
        self.lineEdit_epsiloxx.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_epsiloxx.setFrame(True)
        self.lineEdit_epsiloxx.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_epsiloxx.setObjectName("lineEdit_epsiloxx")
        self.lineEdit_epsiloxy = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_epsiloxy.setEnabled(False)
        self.lineEdit_epsiloxy.setGeometry(QtCore.QRect(180, 430, 41, 21))
        self.lineEdit_epsiloxy.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_epsiloxy.setFrame(True)
        self.lineEdit_epsiloxy.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_epsiloxy.setObjectName("lineEdit_epsiloxy")
        self.lineEdit_41 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_41.setEnabled(False)
        self.lineEdit_41.setGeometry(QtCore.QRect(230, 430, 41, 21))
        self.lineEdit_41.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_41.setFrame(True)
        self.lineEdit_41.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_41.setObjectName("lineEdit_41")
        self.lineEdit_epsiloyx = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_epsiloyx.setEnabled(False)
        self.lineEdit_epsiloyx.setGeometry(QtCore.QRect(130, 460, 41, 21))
        self.lineEdit_epsiloyx.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_epsiloyx.setFrame(True)
        self.lineEdit_epsiloyx.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_epsiloyx.setObjectName("lineEdit_epsiloyx")
        self.lineEdit_epsiloyy = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_epsiloyy.setEnabled(False)
        self.lineEdit_epsiloyy.setGeometry(QtCore.QRect(180, 460, 41, 21))
        self.lineEdit_epsiloyy.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_epsiloyy.setFrame(True)
        self.lineEdit_epsiloyy.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_epsiloyy.setObjectName("lineEdit_epsiloyy")
        self.lineEdit_42 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_42.setEnabled(False)
        self.lineEdit_42.setGeometry(QtCore.QRect(230, 460, 41, 21))
        self.lineEdit_42.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_42.setFrame(True)
        self.lineEdit_42.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.lineEdit_43 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_43.setEnabled(False)
        self.lineEdit_43.setGeometry(QtCore.QRect(130, 490, 41, 21))
        self.lineEdit_43.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_43.setFrame(True)
        self.lineEdit_43.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_43.setObjectName("lineEdit_43")
        self.lineEdit_44 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_44.setEnabled(False)
        self.lineEdit_44.setGeometry(QtCore.QRect(180, 490, 41, 21))
        self.lineEdit_44.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_44.setFrame(True)
        self.lineEdit_44.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_44.setObjectName("lineEdit_44")
        self.lineEdit_epsilozz = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_epsilozz.setEnabled(False)
        self.lineEdit_epsilozz.setGeometry(QtCore.QRect(230, 490, 41, 21))
        self.lineEdit_epsilozz.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_epsilozz.setFrame(True)
        self.lineEdit_epsilozz.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_epsilozz.setObjectName("lineEdit_epsilozz")
        self.frame_28 = QtWidgets.QFrame(self.tab_3)
        self.frame_28.setGeometry(QtCore.QRect(350, 20, 271, 21))
        self.frame_28.setStyleSheet("background-color: #EB3438 ;")
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.label_65 = QtWidgets.QLabel(self.frame_28)
        self.label_65.setGeometry(QtCore.QRect(10, 0, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        self.label_65.setFont(font)
        self.label_65.setStyleSheet("border: transparent")
        self.label_65.setTextFormat(QtCore.Qt.AutoText)
        self.label_65.setScaledContents(True)
        self.label_65.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_65.setWordWrap(False)
        self.label_65.setObjectName("label_65")
        self.label_66 = QtWidgets.QLabel(self.tab_3)
        self.label_66.setGeometry(QtCore.QRect(360, 70, 51, 31))
        self.label_66.setStyleSheet("border: none;\n"
"")
        self.label_66.setObjectName("label_66")
        self.lineEdit_epsilonmedio = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_epsilonmedio.setEnabled(False)
        self.lineEdit_epsilonmedio.setGeometry(QtCore.QRect(430, 70, 81, 31))
        self.lineEdit_epsilonmedio.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_epsilonmedio.setText("")
        self.lineEdit_epsilonmedio.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_epsilonmedio.setObjectName("lineEdit_epsilonmedio")
        self.label_67 = QtWidgets.QLabel(self.tab_3)
        self.label_67.setGeometry(QtCore.QRect(530, 70, 51, 31))
        self.label_67.setStyleSheet("border: none;\n"
"")
        self.label_67.setObjectName("label_67")
        self.lineEdit_raio1_e = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_raio1_e.setEnabled(False)
        self.lineEdit_raio1_e.setGeometry(QtCore.QRect(590, 70, 81, 31))
        self.lineEdit_raio1_e.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_raio1_e.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_raio1_e.setObjectName("lineEdit_raio1_e")
        self.label_68 = QtWidgets.QLabel(self.tab_3)
        self.label_68.setGeometry(QtCore.QRect(360, 120, 71, 31))
        self.label_68.setStyleSheet("border: none;\n"
"")
        self.label_68.setObjectName("label_68")
        self.lineEdit_epsilon1 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_epsilon1.setEnabled(False)
        self.lineEdit_epsilon1.setGeometry(QtCore.QRect(430, 120, 81, 31))
        self.lineEdit_epsilon1.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_epsilon1.setText("")
        self.lineEdit_epsilon1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_epsilon1.setObjectName("lineEdit_epsilon1")
        self.label_69 = QtWidgets.QLabel(self.tab_3)
        self.label_69.setGeometry(QtCore.QRect(530, 120, 51, 31))
        self.label_69.setStyleSheet("border: none;\n"
"")
        self.label_69.setObjectName("label_69")
        self.lineEdit_teta1_e = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_teta1_e.setEnabled(False)
        self.lineEdit_teta1_e.setGeometry(QtCore.QRect(590, 120, 81, 31))
        self.lineEdit_teta1_e.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_teta1_e.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_teta1_e.setObjectName("lineEdit_teta1_e")
        self.label_70 = QtWidgets.QLabel(self.tab_3)
        self.label_70.setGeometry(QtCore.QRect(360, 170, 61, 31))
        self.label_70.setStyleSheet("border: none;\n"
"")
        self.label_70.setObjectName("label_70")
        self.lineEdit_epsilon2 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_epsilon2.setEnabled(False)
        self.lineEdit_epsilon2.setGeometry(QtCore.QRect(430, 170, 81, 31))
        self.lineEdit_epsilon2.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_epsilon2.setText("")
        self.lineEdit_epsilon2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_epsilon2.setObjectName("lineEdit_epsilon2")
        self.label_71 = QtWidgets.QLabel(self.tab_3)
        self.label_71.setGeometry(QtCore.QRect(530, 170, 51, 31))
        self.label_71.setStyleSheet("border: none;\n"
"")
        self.label_71.setObjectName("label_71")
        self.lineEdit_teta2_e = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_teta2_e.setEnabled(False)
        self.lineEdit_teta2_e.setGeometry(QtCore.QRect(590, 170, 81, 31))
        self.lineEdit_teta2_e.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_teta2_e.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_teta2_e.setObjectName("lineEdit_teta2_e")
        self.pushButton_graficonormal_4 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_graficonormal_4.setGeometry(QtCore.QRect(430, 220, 201, 41))
        self.pushButton_graficonormal_4.setObjectName("pushButton_graficonormal_4")
        self.frame_29 = QtWidgets.QFrame(self.tab_3)
        self.frame_29.setGeometry(QtCore.QRect(350, 290, 261, 21))
        self.frame_29.setStyleSheet("background-color: #EB3438 ;")
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.label_72 = QtWidgets.QLabel(self.frame_29)
        self.label_72.setGeometry(QtCore.QRect(10, 0, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        self.label_72.setFont(font)
        self.label_72.setStyleSheet("border: transparent")
        self.label_72.setTextFormat(QtCore.Qt.AutoText)
        self.label_72.setScaledContents(True)
        self.label_72.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_72.setWordWrap(False)
        self.label_72.setObjectName("label_72")
        self.label_73 = QtWidgets.QLabel(self.tab_3)
        self.label_73.setGeometry(QtCore.QRect(360, 330, 61, 31))
        self.label_73.setStyleSheet("border: none;\n"
"")
        self.label_73.setObjectName("label_73")
        self.lineEdit_angmax = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_angmax.setEnabled(False)
        self.lineEdit_angmax.setGeometry(QtCore.QRect(430, 330, 81, 31))
        self.lineEdit_angmax.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_angmax.setText("")
        self.lineEdit_angmax.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_angmax.setObjectName("lineEdit_angmax")
        self.label_74 = QtWidgets.QLabel(self.tab_3)
        self.label_74.setGeometry(QtCore.QRect(360, 370, 61, 31))
        self.label_74.setStyleSheet("border: none;\n"
"")
        self.label_74.setObjectName("label_74")
        self.lineEdit_angmin = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_angmin.setEnabled(False)
        self.lineEdit_angmin.setGeometry(QtCore.QRect(430, 370, 81, 31))
        self.lineEdit_angmin.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_angmin.setText("")
        self.lineEdit_angmin.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_angmin.setObjectName("lineEdit_angmin")
        self.label_75 = QtWidgets.QLabel(self.tab_3)
        self.label_75.setGeometry(QtCore.QRect(530, 330, 51, 31))
        self.label_75.setStyleSheet("border: none;\n"
"")
        self.label_75.setObjectName("label_75")
        self.lineEdit_tetaangmmax = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_tetaangmmax.setEnabled(False)
        self.lineEdit_tetaangmmax.setGeometry(QtCore.QRect(590, 330, 81, 31))
        self.lineEdit_tetaangmmax.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_tetaangmmax.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_tetaangmmax.setObjectName("lineEdit_tetaangmmax")
        self.label_76 = QtWidgets.QLabel(self.tab_3)
        self.label_76.setGeometry(QtCore.QRect(530, 370, 51, 31))
        self.label_76.setStyleSheet("border: none;\n"
"")
        self.label_76.setObjectName("label_76")
        self.lineEdit_tetaangmin_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_tetaangmin_3.setEnabled(False)
        self.lineEdit_tetaangmin_3.setGeometry(QtCore.QRect(590, 370, 81, 31))
        self.lineEdit_tetaangmin_3.setStyleSheet("border: 1px solid #D3D3D3;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"\n"
"")
        self.lineEdit_tetaangmin_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_tetaangmin_3.setObjectName("lineEdit_tetaangmin_3")
        self.pushButton_graficocis_4 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_graficocis_4.setGeometry(QtCore.QRect(430, 420, 201, 41))
        self.pushButton_graficocis_4.setObjectName("pushButton_graficocis_4")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.frame_13 = QtWidgets.QFrame(self.tab_2)
        self.frame_13.setGeometry(QtCore.QRect(0, 0, 701, 521))
        self.frame_13.setStyleSheet("border: 2px solid #EB3438;\n"
"border-style: dashed;\n"
"background-color: transparent;\n"
"")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_13.setObjectName("frame_13")
        self.label_46 = QtWidgets.QLabel(self.frame_13)
        self.label_46.setGeometry(QtCore.QRect(10, 90, 321, 421))
        self.label_46.setMinimumSize(QtCore.QSize(0, 400))
        self.label_46.setStyleSheet("border:none")
        self.label_46.setFrameShape(QtWidgets.QFrame.Box)
        self.label_46.setScaledContents(True)
        self.label_46.setWordWrap(True)
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(self.frame_13)
        self.label_47.setGeometry(QtCore.QRect(360, 100, 311, 400))
        self.label_47.setMinimumSize(QtCore.QSize(0, 400))
        self.label_47.setStyleSheet("border:none")
        self.label_47.setFrameShape(QtWidgets.QFrame.Box)
        self.label_47.setScaledContents(True)
        self.label_47.setWordWrap(True)
        self.label_47.setObjectName("label_47")
        self.frame_11 = QtWidgets.QFrame(self.frame_13)
        self.frame_11.setGeometry(QtCore.QRect(360, 60, 321, 21))
        self.frame_11.setStyleSheet("background-color: #EB3438 ;")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.label_31 = QtWidgets.QLabel(self.frame_11)
        self.label_31.setGeometry(QtCore.QRect(30, 0, 401, 21))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(8)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("border: transparent")
        self.label_31.setTextFormat(QtCore.Qt.AutoText)
        self.label_31.setScaledContents(True)
        self.label_31.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_31.setWordWrap(False)
        self.label_31.setObjectName("label_31")
        self.frame_10 = QtWidgets.QFrame(self.frame_13)
        self.frame_10.setGeometry(QtCore.QRect(10, 60, 311, 21))
        self.frame_10.setStyleSheet("background-color: #EB3438 ;")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.label_26 = QtWidgets.QLabel(self.frame_10)
        self.label_26.setGeometry(QtCore.QRect(50, 0, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("border: transparent")
        self.label_26.setTextFormat(QtCore.Qt.AutoText)
        self.label_26.setScaledContents(True)
        self.label_26.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_26.setWordWrap(False)
        self.label_26.setObjectName("label_26")
        self.frame_17 = QtWidgets.QFrame(self.frame_13)
        self.frame_17.setGeometry(QtCore.QRect(220, 0, 251, 41))
        self.frame_17.setStyleSheet("background-color: #EB3438 ;")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.label_45 = QtWidgets.QLabel(self.frame_17)
        self.label_45.setGeometry(QtCore.QRect(50, 0, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("border: transparent")
        self.label_45.setTextFormat(QtCore.Qt.AutoText)
        self.label_45.setScaledContents(True)
        self.label_45.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_45.setWordWrap(False)
        self.label_45.setObjectName("label_45")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 984, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # [ PROGRAMAÇÃO DOS BOTÕES] ------------------------------------------------------------------------------------
        self.pushButton_calculartensoes.clicked.connect(self.dirprin)
        self.pushButton_graficonormal.clicked.connect(self.pltnormal)
        self.pushButton_graficocis.clicked.connect(self.pltcis)
        self.pushButton_calcular_3.clicked.connect(self.dirprin1)
        self.pushButton_graficonormal_4.clicked.connect(self.pltang)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PlaneStr2"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">PlaneStr2</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; color:#ffffff;\">(Versão 1.0)</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" color:#ffffff;\">Ferramenta para suporte de tensões e deformações em estado plano.</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-weight:600; color:#ffffff;\">AUTORES:</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Evyllyn dos Santos Vieira</span></p><p align=\"center\"><span style=\" color:#ffffff;\">João Victor Rosa Cruz</span></p><p align=\"center\"><span style=\" color:#ffffff;\">Eduardo Toledo de Lima Junior</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">DADOS DE ENTRADA</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">[ σ ] =</span></p></body></html>"))
        self.lineEdit_sigmaxx.setPlaceholderText(_translate("MainWindow", "σxx"))
        self.lineEdit_sigmaxy.setPlaceholderText(_translate("MainWindow", "σxy"))
        self.lineEdit_3.setText(_translate("MainWindow", "0"))
        self.lineEdit_sigmayx.setPlaceholderText(_translate("MainWindow", "σyx"))
        self.lineEdit_5.setText(_translate("MainWindow", "0"))
        self.lineEdit_sigmayy.setPlaceholderText(_translate("MainWindow", "σyy"))
        self.lineEdit_7.setText(_translate("MainWindow", "0"))
        self.lineEdit_8.setText(_translate("MainWindow", "0"))
        self.lineEdit_sigmazz.setPlaceholderText(_translate("MainWindow", "σzz"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" color:#000000;\">Insira abaixo os componentes </span>σxx, σxy = σyx, σyy e σzz.</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">COMPONENTE ISOTRÓPICO</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">COMPONENTE DESVIADOR</span></p></body></html>"))
        self.pushButton_calculartensoes.setText(_translate("MainWindow", "Calcular Tensões"))
        self.label_13.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">[ σ</span><span style=\" font-size:14pt; font-weight:600; vertical-align:sub;\">m</span><span style=\" font-size:14pt; font-weight:600;\"> ] =</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">[ σ</span><span style=\" font-size:14pt; font-weight:600; vertical-align:sub;\">s</span><span style=\" font-size:14pt; font-weight:600;\"> ] =</span></p></body></html>"))
        self.lineEdit_sigmamxx.setPlaceholderText(_translate("MainWindow", "σm"))
        self.lineEdit_6.setText(_translate("MainWindow", "0"))
        self.lineEdit_9.setText(_translate("MainWindow", "0"))
        self.lineEdit_10.setText(_translate("MainWindow", "0"))
        self.lineEdit_11.setText(_translate("MainWindow", "0"))
        self.lineEdit_12.setText(_translate("MainWindow", "0"))
        self.lineEdit_13.setText(_translate("MainWindow", "0"))
        self.lineEdit_sigmamyy.setPlaceholderText(_translate("MainWindow", "σm"))
        self.lineEdit_sigmamzz.setPlaceholderText(_translate("MainWindow", "σm"))
        self.lineEdit_sigmasxx.setPlaceholderText(_translate("MainWindow", "σxx"))
        self.lineEdit_sigmasxy.setPlaceholderText(_translate("MainWindow", "σxy"))
        self.lineEdit_sigmasyx.setPlaceholderText(_translate("MainWindow", "σyx"))
        self.lineEdit_sigmasyy.setPlaceholderText(_translate("MainWindow", "σyy"))
        self.lineEdit_sigmaszz.setPlaceholderText(_translate("MainWindow", "σzz"))
        self.lineEdit_15.setText(_translate("MainWindow", "0"))
        self.lineEdit_16.setText(_translate("MainWindow", "0"))
        self.lineEdit_17.setText(_translate("MainWindow", "0"))
        self.lineEdit_18.setText(_translate("MainWindow", "0"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">ESTADO PRINCIPAL DE TENSÕES</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#eb3438;\">σ</span><span style=\" font-size:12pt; font-weight:600; color:#eb3438; vertical-align:sub;\">médio</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#eb3438; vertical-align:sub;\">Raio (R)</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#eb3438;\">σ</span><span style=\" font-size:12pt; font-weight:600; color:#eb3438; vertical-align:sub;\">1 (máx)</span></p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#eb3438;\">θ</span><span style=\" font-size:12pt; font-weight:600; color:#eb3438; vertical-align:sub;\">1 (º)</span></p></body></html>"))
        self.label_22.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#eb3438;\">σ</span><span style=\" font-size:12pt; font-weight:600; color:#eb3438; vertical-align:sub;\">2 (mín)</span></p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#eb3438;\">θ</span><span style=\" font-size:12pt; font-weight:600; color:#eb3438; vertical-align:sub;\">2 (º)</span></p></body></html>"))
        self.label_25.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#eb3438;\">θ </span><span style=\" font-size:10pt; font-weight:600; color:#eb3438; vertical-align:sub;\">τ1</span><span style=\" font-size:12pt; font-weight:600; color:#eb3438; vertical-align:sub;\"> (º)</span></p></body></html>"))
        self.label_27.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#eb3438;\">θ </span><span style=\" font-size:10pt; font-weight:600; color:#eb3438; vertical-align:sub;\">τ2</span><span style=\" font-size:12pt; font-weight:600; color:#eb3438; vertical-align:sub;\"> (º)</span></p></body></html>"))
        self.label_28.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#eb3438;\">τ</span><span style=\" font-size:12pt; font-weight:600; color:#eb3438; vertical-align:sub;\"> (máx)</span></p></body></html>"))
        self.label_29.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#eb3438;\">τ</span><span style=\" font-size:12pt; font-weight:600; color:#eb3438; vertical-align:sub;\"> (mín)</span></p></body></html>"))
        self.label_30.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">TENSÕES EXTREMAS DE CISALHAMENTO</span></p></body></html>"))
        self.pushButton_graficonormal.setText(_translate("MainWindow", "Representação gráfica"))
        self.pushButton_graficocis.setText(_translate("MainWindow", "Representação gráfica"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Análise de Tensões"))
        self.label_60.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">[</span><a name=\"docs-internal-guid-66aa84bc-7fff-9ba6-03ea-03f571a11dfd\"/><span style=\" font-family:\'Arial,sans-serif\'; font-size:14pt; font-weight:600; color:#000000; background-color:transparent;\">Ɛ</span><span style=\" font-size:14pt; font-weight:600;\">] =</span></p><p><span style=\" font-weight:600;\"><br/></span></p></body></html>"))
        self.lineEdit_epsilonxx.setPlaceholderText(_translate("MainWindow", "Ɛxx"))
        self.lineEdit_epsilonxy.setPlaceholderText(_translate("MainWindow", "Ɛxy"))
        self.lineEdit_31.setText(_translate("MainWindow", "0"))
        self.lineEdit_epsilonyx.setPlaceholderText(_translate("MainWindow", "Ɛyx"))
        self.lineEdit_32.setText(_translate("MainWindow", "0"))
        self.lineEdit_epsilonyy.setPlaceholderText(_translate("MainWindow", "Ɛyy"))
        self.lineEdit_33.setText(_translate("MainWindow", "0"))
        self.lineEdit_34.setText(_translate("MainWindow", "0"))
        self.lineEdit_epsilonzz.setPlaceholderText(_translate("MainWindow", "Ɛzz"))
        self.label_61.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" color:#000000;\">Insira abaixo os componentes </span><a name=\"docs-internal-guid-66aa84bc-7fff-9ba6-03ea-03f571a11dfd\"/><span style=\" font-family:\'Arial,sans-serif\'; color:#000000; background-color:transparent;\">Ɛ</span>xx, <a name=\"docs-internal-guid-66aa84bc-7fff-9ba6-03ea-03f571a11dfd\"/><span style=\" font-family:\'Arial,sans-serif\'; color:#000000; background-color:transparent;\">Ɛ</span>xy = <a name=\"docs-internal-guid-66aa84bc-7fff-9ba6-03ea-03f571a11dfd\"/><span style=\" font-family:\'Arial,sans-serif\'; color:#000000; background-color:transparent;\">Ɛ</span>yx, <a name=\"docs-internal-guid-66aa84bc-7fff-9ba6-03ea-03f571a11dfd\"/><span style=\" font-family:\'Arial,sans-serif\'; color:#000000; background-color:transparent;\">Ɛ</span>yy e <a name=\"docs-internal-guid-66aa84bc-7fff-9ba6-03ea-03f571a11dfd\"/><span style=\" font-family:\'Arial,sans-serif\'; color:#000000; background-color:transparent;\">Ɛ</span>zz.</p></body></html>"))
        self.label_62.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">DADOS DE ENTRADA</span></p></body></html>"))
        self.pushButton_calcular_3.setText(_translate("MainWindow", "Calcular"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">COMPONENTE ISOTRÓPICO</span></p></body></html>"))
        self.label_24.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">[ </span><a name=\"docs-internal-guid-66aa84bc-7fff-9ba6-03ea-03f571a11dfd\"></a><span style=\" font-family:\'Arial,sans-serif\'; font-size:14pt; font-weight:600; color:#000000; background-color:transparent;\">Ɛ</span><span style=\" font-size:14pt; font-weight:600; vertical-align:sub;\">m</span><span style=\" font-size:14pt; font-weight:600;\"> ] =</span></p></body></html>"))
        self.lineEdit_epsilonmedxx.setPlaceholderText(_translate("MainWindow", "Ɛm"))
        self.lineEdit_35.setText(_translate("MainWindow", "0"))
        self.lineEdit_36.setText(_translate("MainWindow", "0"))
        self.lineEdit_37.setText(_translate("MainWindow", "0"))
        self.lineEdit_epsilonmedxy.setPlaceholderText(_translate("MainWindow", "Ɛm"))
        self.lineEdit_38.setText(_translate("MainWindow", "0"))
        self.lineEdit_39.setText(_translate("MainWindow", "0"))
        self.lineEdit_40.setText(_translate("MainWindow", "0"))
        self.lineEdit_epsilonmedyy.setPlaceholderText(_translate("MainWindow", "Ɛm"))
        self.label_63.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">COMPONENTE DESVIADOR</span></p></body></html>"))
        self.label_64.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">[ </span><a name=\"docs-internal-guid-66aa84bc-7fff-9ba6-03ea-03f571a11dfd\"></a><span style=\" font-family:\'Arial,sans-serif\'; font-size:14pt; font-weight:600; color:#000000; background-color:transparent;\">Ɛ</span><span style=\" font-size:14pt; font-weight:600; vertical-align:sub;\">s</span><span style=\" font-size:14pt; font-weight:600;\"> ] =</span></p></body></html>"))
        self.lineEdit_epsiloxx.setPlaceholderText(_translate("MainWindow", "Ɛxx"))
        self.lineEdit_epsiloxy.setPlaceholderText(_translate("MainWindow", "Ɛxy"))
        self.lineEdit_41.setText(_translate("MainWindow", "0"))
        self.lineEdit_epsiloyx.setPlaceholderText(_translate("MainWindow", "Ɛyx"))
        self.lineEdit_epsiloyy.setPlaceholderText(_translate("MainWindow", "Ɛyy"))
        self.lineEdit_42.setText(_translate("MainWindow", "0"))
        self.lineEdit_43.setText(_translate("MainWindow", "0"))
        self.lineEdit_44.setText(_translate("MainWindow", "0"))
        self.lineEdit_epsilozz.setPlaceholderText(_translate("MainWindow", "Ɛzz"))
        self.label_65.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">ESTADO PRINCIPAL DE DEFORMAÇÕES</span></p></body></html>"))
        self.label_66.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"docs-internal-guid-66aa84bc-7fff-9ba6-03ea-03f571a11dfd\"></a><span style=\" font-family:\'Arial,sans-serif\'; font-size:14pt; font-weight:600; color:#eb3438; background-color:transparent;\">Ɛ</span><span style=\" font-size:12pt; font-weight:600; color:#eb3438; vertical-align:sub;\">médio</span></p></body></html>"))
        self.label_67.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#eb3438; vertical-align:sub;\">Raio (R)</span></p></body></html>"))
        self.label_68.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"docs-internal-guid-66aa84bc-7fff-9ba6-03ea-03f571a11dfd\"></a><span style=\" font-family:\'Arial,sans-serif\'; font-size:14pt; font-weight:600; color:#eb3438; background-color:transparent;\">Ɛ</span><span style=\" font-size:12pt; font-weight:600; color:#eb3438; vertical-align:sub;\">1 (máx)</span></p></body></html>"))
        self.label_69.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#eb3438;\">θ</span><span style=\" font-size:12pt; font-weight:600; color:#eb3438; vertical-align:sub;\">1 (º)</span></p></body></html>"))
        self.label_70.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"docs-internal-guid-66aa84bc-7fff-9ba6-03ea-03f571a11dfd\"></a><span style=\" font-family:\'Arial,sans-serif\'; font-size:14pt; font-weight:600; color:#eb3438; background-color:transparent;\">Ɛ</span><span style=\" font-size:12pt; font-weight:600; color:#eb3438; vertical-align:sub;\">2 (mín)</span></p></body></html>"))
        self.label_71.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#eb3438;\">θ</span><span style=\" font-size:12pt; font-weight:600; color:#eb3438; vertical-align:sub;\">2 (º)</span></p></body></html>"))
        self.pushButton_graficonormal_4.setText(_translate("MainWindow", "Representação gráfica"))
        self.label_72.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">DEFORMAÇÕES EXTREMAS ANGULAR</span></p></body></html>"))
        self.label_73.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"docs-internal-guid-45daea5f-7fff-8cff-c16e-2e854b7ace69\"></a><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600; color:#eb3438; background-color:transparent;\">Ƴ</span><span style=\" font-size:12pt; font-weight:600; color:#eb3438; vertical-align:sub;\">(máx)</span></p></body></html>"))
        self.label_74.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"docs-internal-guid-45daea5f-7fff-8cff-c16e-2e854b7ace69\"></a><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600; color:#eb3438; background-color:transparent;\">Ƴ</span><span style=\" font-size:12pt; font-weight:600; color:#eb3438; vertical-align:sub;\"> (mín)</span></p></body></html>"))
        self.label_75.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#eb3438;\">θ </span><span style=\" font-size:10pt; font-weight:600; color:#eb3438; vertical-align:sub;\">τ1</span><span style=\" font-size:12pt; font-weight:600; color:#eb3438; vertical-align:sub;\"> (º)</span></p></body></html>"))
        self.label_76.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#eb3438;\">θ </span><span style=\" font-size:10pt; font-weight:600; color:#eb3438; vertical-align:sub;\">τ2</span><span style=\" font-size:12pt; font-weight:600; color:#eb3438; vertical-align:sub;\"> (º)</span></p></body></html>"))
        self.pushButton_graficocis_4.setText(_translate("MainWindow", "Representação gráfica"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Análise de Deformações"))
        self.label_46.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><a name=\"docs-internal-guid-91adfff4-7fff-b3bf-0d12-4096424de490\"/><span style=\" font-family:\'Arial\'; color:#000000; background-color:transparent;\">-</span><span style=\" font-family:\'Arial\'; color:#000000; background-color:transparent;\"> Por tensão, entende-se uma extensão dessa idéia para os casos em que a força por unidade de área pode não ser, necessariamente, normal.</span></p><p align=\"justify\"><span style=\" font-family:\'Arial\'; color:#000000; background-color:transparent;\">- </span><a name=\"docs-internal-guid-06a85955-7fff-c70d-803f-a2be4c309450\"/><span style=\" font-family:\'Arial\'; color:#000000; background-color:transparent;\">O</span><span style=\" font-family:\'Arial\'; color:#000000; background-color:transparent;\"> Estado Plano de tensão trata-se de um estado de tensão mais geral num elemento onde não só atua tensão normal em uma direção mas em duas direções. Tal situação é conhecida como tensões biaxiais.</span></p><p align=\"justify\"><span style=\" font-family:\'Arial\'; color:#000000; background-color:transparent;\">- </span><a name=\"docs-internal-guid-dc292d45-7fff-687d-60a6-726603444e6d\"/><span style=\" font-family:\'Arial\'; color:#000000; background-color:transparent;\">N</span><span style=\" font-family:\'Arial\'; color:#000000; background-color:transparent;\">esse sentido, usamos algumas fórmulas para calcular suas propriedades bidimensional no plano XY, tais como:</span></p><p align=\"center\"><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent;\">σ</span><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent; vertical-align:sub;\">med</span><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent;\"> = (σ</span><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent; vertical-align:sub;\">xx</span><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent;\">+ σ</span><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent; vertical-align:sub;\">yy</span><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent;\">)/2</span></p><p align=\"center\"><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent;\">R=(σ</span><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent; vertical-align:sub;\">xx-</span><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent;\"> - σ</span><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent; vertical-align:sub;\">yy</span><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent;\">)/2)²+σ</span><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent; vertical-align:sub;\">yy</span></p><p align=\"center\"><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent;\">σ</span><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent; vertical-align:sub;\">máx</span><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent;\"> =σ</span><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent; vertical-align:sub;\">med</span><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent;\"> +R </span></p><p align=\"center\"><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent;\">σ</span><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent; vertical-align:sub;\">min</span><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent;\"> =σ</span><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent; vertical-align:sub;\">med</span><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent;\"> -R</span></p><p align=\"center\"><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent;\">tg20p=(2*σxy)/(σxx- σyy)</span></p><p><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent;\">σ</span><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent; vertical-align:sub;\">med</span><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent;\"> = </span><span style=\" font-family:\'Arial\'; color:#000000; background-color:transparent;\">Tensão média; </span><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent;\">R = </span><span style=\" font-family:\'Arial\'; color:#000000; background-color:transparent;\">Raio; </span><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent;\">σ</span><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent; vertical-align:sub;\">máx</span><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent;\"> = </span><span style=\" font-family:\'Arial\'; color:#000000; background-color:transparent;\">Tensão máxima; </span><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent;\">σ</span><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent; vertical-align:sub;\">min</span><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent;\"> = </span><span style=\" font-family:\'Arial\'; color:#000000; background-color:transparent;\">Tensão mínima; </span><span style=\" font-size:10pt;\">0</span><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent;\">= </span><span style=\" font-family:\'Arial\'; color:#000000; background-color:transparent;\">Ângulo teta de rotação.</span></p></body></html>"))
        self.label_47.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%;\"><a name=\"docs-internal-guid-8f776fb3-7fff-f777-30a9-f2e70fff721a\"></a><span style=\" font-family:\'Arial\'; color:#000000; background-color:transparent;\">-</span><span style=\" font-family:\'Arial\'; color:#000000; background-color:transparent;\"> A intensidade da força, ou força por unidade de área, que age tangente a ΔA, é denominada tensão de cisalhamento é denominada tensão de cisalhamento T (tau).</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%; font-family:\'Arial\'; color:#000000;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%;\"><span style=\" font-family:\'Arial\'; color:#000000; background-color:transparent;\">- Ao analisarmos o circulo de Mohr, percebe-se que há pontos extremos, logo há pontos em que a tensão cisalhante é extrema, sendo assim:</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%; font-family:\'Arial\'; color:#000000;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%;\"><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent;\">T</span><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent; vertical-align:sub;\">min</span><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent;\"> = -R e T</span><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent; vertical-align:sub;\">máx</span><span style=\" font-family:\'Arial\'; font-size:10pt; color:#000000; background-color:transparent;\"> = R.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_31.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">TENSÇOES EXTREMAS DE CISALHAMENTO</span></p></body></html>"))
        self.label_26.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">ESTADO PRINCIPAL DE TENSÕES</span></p></body></html>"))
        self.label_45.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\"> FORMULAÇÃO</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Informações Gerais"))

# =-=-=-=-=-=-=-= [ MÓDULO PARA CALCULAR OS DADOS DAS DIREÇÕES PRINCIPAIS ] =-=-=-=-=-=-=-= #

    def dirprin(self):

        # [ ENTRADA DE DADOS DO USUÁRIO ] ------------------------------------------------------------------------------

        sigma_xx = float(self.lineEdit_sigmaxx.text())
        sigma_yy = float(self.lineEdit_sigmayy.text())
        sigma_zz = float(self.lineEdit_sigmazz.text())
        sigma_xy = float(self.lineEdit_sigmaxy.text())

        # [ CRIAÇÃO DO TENSOR DE TENSÃO ] ------------------------------------------------------------------------------

        sigma = np.array([[sigma_xx, sigma_xy, 0], [sigma_xy, sigma_yy, 0], [0, 0, sigma_zz]])

        # [ COMPONENTES PARA O CÁLCULO DAS DIREÇÕES PRINCIPAIS ] -------------------------------------------------------
        
        sigma_med = (sigma_xx + sigma_yy) / 2
        R = sqrt((((sigma_xx - sigma_yy) / 2) ** 2) + (sigma_xy) ** 2)
        sigma_1 = sigma_med + R
        sigma_2 = sigma_med - R
        teta_2p = np.degrees(np.arctan(2 * sigma_xy / (sigma_xx - sigma_yy)))

        if teta_2p < 0:
                teta_2p = teta_2p + 180
        if sigma_xy > 0:
                teta_1 = teta_2p / 2
        if sigma_xy < 0:
                teta_1 = (teta_2p + 180) / 2

        teta_2 = teta_1 + 90

        cis_min = -R
        cis_max = R
        teta_cis_min = teta_1 + 45
        teta_cis_max = teta_1 + 135
        
        # [ COMPONENTE ISOTRÓPICO E DESVIADOR DO TENSOR DE TENSÃO ] ----------------------------------------------------

        # Isotrópico #
        sigma_m = (sigma_xx + sigma_yy + sigma_zz) / 3
        sigma_iso = np.array([[sigma_m, 0, 0], [0, sigma_m, 0], [0, 0, sigma_m]])

        if sigma_m > 0:
                texto_iso = "Ocorre Expansão!"
        else:
                texto_iso = "Ocorre Contração!"

        # Desviador #
        sigma_s = sigma - sigma_iso

        # Loop para verificar se existe algum elemento da matriz diferente de zero
        for i in range(0, len(sigma_s)):
                for j in range(0, len(sigma_s)):
                        if (sigma_s[i, j]) != 0:
                                texto_s = "Ocorre Distorção!"
                                break

        # [ SAÍDA DE DADOS NA INTERFACE GRÁFICA] -----------------------------------------------------------------------

        # COMPONENTE ISOTRÓPICO #
        self.lineEdit_sigmamxx.setText(str(round(sigma_m,2)))
        self.lineEdit_sigmamyy.setText(str(round(sigma_m,2)))
        self.lineEdit_sigmamzz.setText(str(round(sigma_m,2)))
        self.lineEdit_textoiso.setText(str(texto_iso))

        # COMPONENTE DESVIADOR #
        self.lineEdit_sigmasxx.setText(str(round(sigma_s[0][0],2)))
        self.lineEdit_sigmasxy.setText(str(round(sigma_s[0][1],2)))
        self.lineEdit_sigmasyx.setText(str(round(sigma_s[1][0],2)))
        self.lineEdit_sigmasyy.setText(str(round(sigma_s[1][1],2)))
        self.lineEdit_sigmaszz.setText(str(round(sigma_s[2][2],2)))
        self.lineEdit_textos.setText(str(texto_s))

        # DADOS DE SAÍDA (DIREÇÕES PRINCIPAIS) #
        self.lineEdit_sigmamedio.setText(str(round(sigma_med,2)))
        self.lineEdit_raio.setText(str(round(R,2)))
        self.lineEdit_sigma1.setText(str(round(sigma_1,2)))
        self.lineEdit_sigma2.setText(str(round(sigma_2,2)))
        self.lineEdit_teta1.setText(str(round(teta_1,2)))
        self.lineEdit_teta2.setText(str(round(teta_2,2)))
        self.lineEdit_cismax.setText(str(round(cis_max,2)))
        self.lineEdit_cismin.setText(str(round(cis_min,2)))
        self.lineEdit_tetacismmax.setText(str(round(teta_cis_max,2)))
        self.lineEdit_tetacismin.setText(str(round(teta_cis_min,2)))
        
# ------ DEFORMAÇÕES CÁLCULO------
        
    def dirprin1(self):

        # [ ENTRADA DE DADOS DO USUÁRIO ] ------------------------------------------------------------------------------
        
        epsilon_xx = float(self.lineEdit_epsilonxx.text())
        epsilon_yy = float(self.lineEdit_epsilonyy.text())
        epsilon_zz = float(self.lineEdit_epsilonzz.text())
        epsilon_xy = float(self.lineEdit_epsilonxy.text())

        # [ CRIAÇÃO DO TENSOR DE TENSÃO ] ------------------------------------------------------------------------------

        epsilon = np.array([[epsilon_xx, epsilon_xy, 0], [epsilon_xy, epsilon_yy, 0], [0, 0, epsilon_zz]])

        # [ COMPONENTES PARA O CÁLCULO DAS DIREÇÕES PRINCIPAIS ] -------------------------------------------------------
        
        epsilon_med = (epsilon_xx + epsilon_yy) / 2
        R1 = sqrt((((epsilon_xx - epsilon_yy) / 2) ** 2) + (epsilon_xy) ** 2)
        epsilon_11 = epsilon_med + R1
        epsilon_21 = epsilon_med - R1
        teta_2pp = np.degrees(np.arctan(2 * epsilon_xy / (epsilon_xx - epsilon_yy)))

        if teta_2pp < 0:
                teta_2pp = teta_2pp + 180
        if epsilon_xy > 0:
                teta_11 = teta_2pp / 2
        if epsilon_xy < 0:
                teta_11 = (teta_2pp + 180) / 2

        teta_21 = teta_11 + 90

        ang_min = -R1
        ang_max = R1
        teta_ang_min = teta_11 + 45
        teta_ang_max = teta_11 + 135
        
        # [ COMPONENTE ISOTRÓPICO E DESVIADOR DO TENSOR DE TENSÃO ] ---------------------------------------------------

        # Isotrópico #
        epsilon_m = (epsilon_xx + epsilon_yy + epsilon_zz) / 3
        epsilon_iso = np.array([[epsilon_m, 0, 0], [0, epsilon_m, 0], [0, 0, epsilon_m]])

        if epsilon_m > 0:
                texto_iso1 = "Ocorre Expansão!"
        else:
                texto_iso1 = "Ocorre Contração!"

        # Desviador #
        
        epsilon_s = epsilon - epsilon_iso

        # Loop para verificar se existe algum elemento da matriz diferente de zero
        for i in range(0, len(epsilon_s)):
                for j in range(0, len(epsilon_s)):
                        if (epsilon_s[i, j]) != 0:
                                texto_s1 = "Ocorre Distorção!"
                                break
        # [ SAÍDA DE DADOS NA INTERFACE GRÁFICA] -----------------------------------------------------------------------
        # COMPONENTE ISOTRÓPICO #
        self.lineEdit_epsilonmedxx.setText(str(round(epsilon_m,2)))
        self.lineEdit_epsilonmedxy.setText(str(round(epsilon_m,2)))
        self.lineEdit_epsilonmedyy.setText(str(round(epsilon_m,2)))
        self.lineEdit_textoiso_3.setText(str(texto_iso1))

        # COMPONENTE DESVIADOR #
        self.lineEdit_epsiloxx.setText(str(round(epsilon_s[0][0],2)))
        self.lineEdit_epsiloxy.setText(str(round(epsilon_s[0][1],2)))
        self.lineEdit_epsiloyx.setText(str(round(epsilon_s[1][0],2)))
        self.lineEdit_epsiloyy.setText(str(round(epsilon_s[1][1],2)))
        self.lineEdit_epsilozz.setText(str(round(epsilon_s[2][2],2)))
        self.lineEdit_textoiso_4.setText(str(texto_s1))

        # DADOS DE SAÍDA (DIREÇÕES PRINCIPAIS) #
        self.lineEdit_epsilonmedio.setText(str(round(epsilon_med,2)))
        self.lineEdit_raio1_e.setText(str(round(R1,2)))
        self.lineEdit_epsilon1.setText(str(round(epsilon_11,2)))
        self.lineEdit_epsilon2.setText(str(round(epsilon_21,2)))
        self.lineEdit_teta1_e.setText(str(round(teta_11,2)))
        self.lineEdit_teta2_e.setText(str(round(teta_21,2)))
        self.lineEdit_angmax.setText(str(round(ang_max,2)))
        self.lineEdit_angmin.setText(str(round(ang_min,2)))
        self.lineEdit_tetaangmmax.setText(str(round(teta_ang_max,2)))
        self.lineEdit_tetaangmin_3.setText(str(round(teta_ang_min,2)))

# =-=-=-=-=-=-=-= [ MÓDULO PARA PLOTAR O GRÁFICO DAS TENSÕES NORMAIS MÁXIMAS ] =-=-=-=-=-=-=-= #

    def pltnormal(self):

        # [ FUNÇÃO QUE GERA OS VETORES ]

        def plot_arrow(ax, x, y, dx, dy):
                ax.arrow(x, y, dx, dy, head_width=0.05, head_length=0.1, fc='k', ec='k')

        # [ CAPTURA O ÂNGULO TETA_1 GERADO ]

        angle = float(self.lineEdit_teta1.text())
        theta = np.radians(angle) # Conversão para radianos

        # [ CRIAÇÃO DAS COORDENADAS DOS PONTOS DO QUADRADO]

        vertices = np.array([[-0.5, -0.5], [0.5, -0.5], [0.5, 0.5], [-0.5, 0.5], [-0.5, -0.5]])

        # [ MATRIZ DE ROTAÇÃO E ROTAÇÃO DO QUADRADO ]

        Rot = np.array([[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]])
        rotated_vertices = np.dot(vertices, Rot)

        # [ PLOTAGEM DO QUADRADO ]

        fig, ax = plt.subplots()

        # [ PLOTAGEM DOS EIXOS X E Y TRACEJADOS ]

        ax.plot([-1.8, 1.8], [0, 0], linestyle='--', color='salmon', zorder=0)
        ax.plot([0, 0], [-1.8, 1.8], linestyle='--', color='salmon', zorder=0)

        # [ PLOTAGEM DO TENSOR DE TENSÃO NO GRÁFICO E NOME DO SOFTWARE]

        sigma_xxplt = float(self.lineEdit_sigmaxx.text())
        sigma_yyplt = float(self.lineEdit_sigmayy.text())
        sigma_zzplt = float(self.lineEdit_sigmazz.text())
        sigma_xyplt = float(self.lineEdit_sigmaxy.text())

        ax.plot([-1.8, -1.8], [-1.75, -1.25], linestyle='solid', color='black', zorder=4)
        ax.plot([-0.7, -0.7], [-1.75, -1.25], linestyle='solid', color='black', zorder=4)
        ax.plot([-1.8, -1.75], [-1.25, -1.25], linestyle='solid', color='black', zorder=4)
        ax.plot([-1.8, -1.75], [-1.75, -1.75], linestyle='solid', color='black', zorder=4)
        ax.plot([-0.7, -0.75], [-1.25, -1.25], linestyle='solid', color='black', zorder=4)
        ax.plot([-0.7, -0.75], [-1.75, -1.75], linestyle='solid', color='black', zorder=4)
        ax.plot([-1.85, -1.915], [-1.48, -1.48], linestyle='solid', color='black', zorder=4)
        ax.plot([-1.85, -1.915], [-1.52, -1.52], linestyle='solid', color='black', zorder=4)
        plt.text(-2.1, -1.5, "[ σ ]", ha='center', va='center', color='black', weight='bold', zorder=4)
        plt.text(-1.6, -1.35, "{}".format(round(sigma_xxplt,2)), ha='center', va='center', color='black', fontsize=7, zorder=4)  # sigmaxx
        plt.text(-1.250, -1.35, "{}".format(round(sigma_xyplt,2)), ha='center', va='center', color='black', fontsize=7, zorder=4)  # sigmaxy
        plt.text(-0.9, -1.35, "0", ha='center', va='center', color='black', fontsize=7, zorder=4)  # sigmaxz
        plt.text(-1.6, -1.52, "{}".format(round(sigma_xyplt,2)), ha='center', va='center', color='black', fontsize=7, zorder=4)  # sigmayx
        plt.text(-1.250, -1.52, "{}".format(round(sigma_yyplt,2)), ha='center', va='center', color='black', fontsize=7, zorder=4)  # sigmayy
        plt.text(-0.9, -1.52, "0", ha='center', va='center', color='black', fontsize=7, zorder=4)  # sigmayz
        plt.text(-1.6, -1.65, "0", ha='center', va='center', color='black', fontsize=7, zorder=4)  # sigmazx
        plt.text(-1.250, -1.65, "0", ha='center', va='center', color='black', fontsize=7, zorder=4)  # sigmazy
        plt.text(-0.9, -1.65, "{}".format(round(sigma_zzplt,2)), ha='center', va='center', color='black', fontsize=7, zorder=4)  # sigmazz
        plt.text(-1.65, -1.11, "* Tensor de tensão de origem ", ha='center', va='center', color='black', fontsize=7, zorder=4)
        plt.text(-1.137, 1.83, "PlaneStr2 © - (Versão 1.0)  ", ha='center', va='center', color='black', fontsize=10, zorder=4)
        
        # [ DEFINIÇÃO DOS LIMITES DOS EIXOS ]

        ax.set_xlim(-2, 2)
        ax.set_ylim(-2, 2)

        # [ DESENHO E PREENCHIMENTO DO QUADRADO ]

        ax.fill(rotated_vertices[:, 0], rotated_vertices[:, 1], color='red', zorder=1)

        # [ APLICAÇÃO DOS VETORES NO PONTO MÉDIO DE CADA UMA DAS FACES DO QUADRADO DE TENSÃO ]

        sigma_1plt = float(self.lineEdit_sigma1.text())
        sigma_2plt = float(self.lineEdit_sigma2.text())

        # FACES DO TETA 1 E SIGMA 1 ------------------------------------------------------------------------------------

        if sigma_1plt < 0:
                left_midpoint = (vertices[0] + vertices[3]) / 2
                right_midpoint = (vertices[1] + vertices[2]) / 2
                midpoints = [left_midpoint, right_midpoint]
                for midpoint in midpoints:
                        rotated_midpoint = np.dot(midpoint, Rot)
                        dx = rotated_midpoint[0]
                        dy = rotated_midpoint[1]
                        plot_arrow(ax, rotated_midpoint[0] + 1.2 * dx, rotated_midpoint[1] + 1.2 * dy, -dx, -dy)

        else:
                left_midpoint = (vertices[0] + vertices[3]) / 2
                right_midpoint = (vertices[1] + vertices[2]) / 2
                midpoints = [left_midpoint, right_midpoint]
                for midpoint in midpoints:
                        rotated_midpoint = np.dot(midpoint, Rot)
                        dx = rotated_midpoint[0]
                        dy = rotated_midpoint[1]
                        plot_arrow(ax, rotated_midpoint[0], rotated_midpoint[1], dx, dy)

        # FACES DO TETA 2 E SIGMA 2 ------------------------------------------------------------------------------------

        if sigma_2plt < 0:
                top_midpoint = (vertices[0] + vertices[1]) / 2
                bottom_midpoint = (vertices[2] + vertices[3]) / 2
                midpoints = [top_midpoint, bottom_midpoint]
                for midpoint in midpoints:
                        rotated_midpoint = np.dot(midpoint, Rot)
                        dx = rotated_midpoint[0]
                        dy = rotated_midpoint[1]
                        plot_arrow(ax, rotated_midpoint[0] + 1.2 * dx, rotated_midpoint[1] + 1.2 * dy, -dx, -dy)

        else:
                top_midpoint = (vertices[0] + vertices[1]) / 2
                bottom_midpoint = (vertices[2] + vertices[3]) / 2
                midpoints = [top_midpoint, bottom_midpoint]
                for midpoint in midpoints:
                        rotated_midpoint = np.dot(midpoint, Rot)
                        dx = rotated_midpoint[0]
                        dy = rotated_midpoint[1]
                        plot_arrow(ax, rotated_midpoint[0], rotated_midpoint[1], dx, dy)
          
        # [ LEGENDAS GERAIS ]

        plt.text(1, -1.6, "σ1 = {}".format(round(sigma_1plt,2)), ha='center', va='center', color='indianred',
                 weight='bold', zorder=4)  # VALOR DO SIGMA 1
        plt.text(1, -1.8, "σ2 = {}".format(round(sigma_2plt,2)), ha='center', va='center', color='darkred',
                 weight='bold', zorder=4)  # VALOR DO SIGMA 2
        plt.text(1.65, -0.2, "eixo x", ha='center', va='center', color='salmon', weight='bold', zorder=4)  # EIXO X
        plt.text(-0.13, 1.65, "eixo y", ha='center', va='center', color='salmon', weight='bold', zorder=4,
                 rotation=90)  # EIXO Y
        plt.text(0, 2.3, "[ ESTADO PARA O QUAL AS TENSÕES NORMAIS SÃO MÁXIMAS ]", ha='center', va='center',
                 color='black', weight='bold', zorder=4)  # TÍTULO

        # [ SEGMENTO DE CIRCUNFERÊNCIA TETA 1 ]

        arc = Arc([0, 0], 2.3, 2.3, theta1=0, theta2=angle, edgecolor='indianred', linewidth=1.5, zorder=3)
        ax.add_patch(arc)
        plt.plot([], [], label="θ1 = {} graus".format(round(angle,2)), color='indianred', linestyle='solid')
        plt.legend()

        # [ SEGMENTO DE CIRCUNFERÊNCIA TETA 2 ]

        arc = Arc([0, 0], 2.6, 2.6, theta1=0, theta2=(angle + 90), edgecolor='darkred', linewidth=1.5, zorder=3)
        ax.add_patch(arc)
        plt.plot([], [], label="θ2 = {} graus".format(round((angle + 90),2)), color='darkred', linestyle='solid')
        plt.legend()

        # [ PLOTAGEM DO GRÁFICO COM O MATPLOTLIB ]

        plt.axis('off') #esconder os eixos
        plt.show()

# =-=-=-=-=-=-=-= [ MÓDULO PARA PLOTAR O GRÁFICO DAS TENSÕES DE CISALHAMENTO EXTREMAS  ] =-=-=-=-=-=-=-= #

    def pltcis(self):

        # [ FUNÇÃO QUE GERA OS VETORES ]

        def plot_arrow(ax, x, y, dx, dy):
                ax.arrow(x, y, dx, dy, head_width=0.05, head_length=0.1, fc='k', ec='k')

        # [ CAPTURA O ÂNGULO TETA_1 GERADO ]

        angle = float(self.lineEdit_tetacismin.text())
        theta = np.radians(angle)  # Conversão para radianos

        # [ CRIAÇÃO DAS COORDENADAS DOS PONTOS DO QUADRADO]

        vertices = np.array([[-0.5, -0.5], [0.5, -0.5], [0.5, 0.5], [-0.5, 0.5], [-0.5, -0.5]])

        # [ MATRIZ DE ROTAÇÃO E ROTAÇÃO DO QUADRADO ]

        Rot = np.array([[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]])
        rotated_vertices = np.dot(vertices, Rot)

        # [ PLOTAGEM DO QUADRADO ]

        fig, ax = plt.subplots()

        # [ PLOTAGEM DOS EIXOS X E Y TRACEJADOS ]

        ax.plot([-1.8, 1.8], [0, 0], linestyle='--', color='salmon', zorder=0)
        ax.plot([0, 0], [-1.8, 1.8], linestyle='--', color='salmon', zorder=0)

        # [ PLOTAGEM DO TENSOR DE TENSÃO NO GRÁFICO E NOME DO SOFTWARE]

        sigma_xxplt = float(self.lineEdit_sigmaxx.text())
        sigma_yyplt = float(self.lineEdit_sigmayy.text())
        sigma_zzplt = float(self.lineEdit_sigmazz.text())
        sigma_xyplt = float(self.lineEdit_sigmaxy.text())

        ax.plot([-1.8, -1.8], [-1.75, -1.25], linestyle='solid', color='black', zorder=4)
        ax.plot([-0.7, -0.7], [-1.75, -1.25], linestyle='solid', color='black', zorder=4)
        ax.plot([-1.8, -1.75], [-1.25, -1.25], linestyle='solid', color='black', zorder=4)
        ax.plot([-1.8, -1.75], [-1.75, -1.75], linestyle='solid', color='black', zorder=4)
        ax.plot([-0.7, -0.75], [-1.25, -1.25], linestyle='solid', color='black', zorder=4)
        ax.plot([-0.7, -0.75], [-1.75, -1.75], linestyle='solid', color='black', zorder=4)
        ax.plot([-1.85, -1.915], [-1.48, -1.48], linestyle='solid', color='black', zorder=4)
        ax.plot([-1.85, -1.915], [-1.52, -1.52], linestyle='solid', color='black', zorder=4)
        plt.text(-2.1, -1.5, "[ σ ]", ha='center', va='center', color='black', weight='bold', zorder=4)
        plt.text(-1.6, -1.35, "{}".format(round(sigma_xxplt, 2)), ha='center', va='center', color='black', fontsize=7,
                 zorder=4)  # sigmaxx
        plt.text(-1.250, -1.35, "{}".format(round(sigma_xyplt, 2)), ha='center', va='center', color='black', fontsize=7,
                 zorder=4)  # sigmaxy
        plt.text(-0.9, -1.35, "0", ha='center', va='center', color='black', fontsize=7, zorder=4)  # sigmaxz
        plt.text(-1.6, -1.52, "{}".format(round(sigma_xyplt, 2)), ha='center', va='center', color='black', fontsize=7,
                 zorder=4)  # sigmayx
        plt.text(-1.250, -1.52, "{}".format(round(sigma_yyplt, 2)), ha='center', va='center', color='black', fontsize=7,
                 zorder=4)  # sigmayy
        plt.text(-0.9, -1.52, "0", ha='center', va='center', color='black', fontsize=7, zorder=4)  # sigmayz
        plt.text(-1.6, -1.65, "0", ha='center', va='center', color='black', fontsize=7, zorder=4)  # sigmazx
        plt.text(-1.250, -1.65, "0", ha='center', va='center', color='black', fontsize=7, zorder=4)  # sigmazy
        plt.text(-0.9, -1.65, "{}".format(round(sigma_zzplt, 2)), ha='center', va='center', color='black', fontsize=7,
                 zorder=4)  # sigmazz
        plt.text(-1.65, -1.11, "* Tensor de tensão de origem ", ha='center', va='center', color='black', fontsize=7,
                 zorder=4)
        plt.text(-1.137, 1.83, "PlaneStr2 © - (Versão 1.0)  ", ha='center', va='center', color='black', fontsize=10,
                 zorder=4)

        # [ DEFINIÇÃO DOS LIMITES DOS EIXOS ]

        ax.set_xlim(-2, 2)
        ax.set_ylim(-2, 2)

        # [ DESENHO E PREENCHIMENTO DO QUADRADO ]

        ax.fill(rotated_vertices[:, 0], rotated_vertices[:, 1], color='red', zorder=1)

        # [ APLICAÇÃO DOS VETORES NO PONTO MÉDIO DE CADA UMA DAS FACES DO QUADRADO ]

        sigma_medplt = float(self.lineEdit_sigmamedio.text())

        # FACES LATERAIS -----------------------------------------------------------------------------------------------

        if sigma_medplt < 0:
                left_midpoint = (vertices[0] + vertices[3]) / 2
                right_midpoint = (vertices[1] + vertices[2]) / 2
                midpoints = [left_midpoint, right_midpoint]
                for midpoint in midpoints:
                        rotated_midpoint = np.dot(midpoint, Rot)
                        dx = rotated_midpoint[0]
                        dy = rotated_midpoint[1]
                        plot_arrow(ax, rotated_midpoint[0] + 1.2 * dx, rotated_midpoint[1] + 1.2 * dy, -dx, -dy)

        else:
                left_midpoint = (vertices[0] + vertices[3]) / 2
                right_midpoint = (vertices[1] + vertices[2]) / 2
                midpoints = [left_midpoint, right_midpoint]
                for midpoint in midpoints:
                        rotated_midpoint = np.dot(midpoint, Rot)
                        dx = rotated_midpoint[0]
                        dy = rotated_midpoint[1]
                        plot_arrow(ax, rotated_midpoint[0], rotated_midpoint[1], dx, dy)

        # FACES SUPERIORES E INFERIORES --------------------------------------------------------------------------------

        if sigma_medplt < 0:
                top_midpoint = (vertices[0] + vertices[1]) / 2
                bottom_midpoint = (vertices[2] + vertices[3]) / 2
                midpoints = [top_midpoint, bottom_midpoint]
                for midpoint in midpoints:
                        rotated_midpoint = np.dot(midpoint, Rot)
                        dx = rotated_midpoint[0]
                        dy = rotated_midpoint[1]
                        plot_arrow(ax, rotated_midpoint[0] + 1.2 * dx, rotated_midpoint[1] + 1.2 * dy, -dx, -dy)

        else:
                top_midpoint = (vertices[0] + vertices[1]) / 2
                bottom_midpoint = (vertices[2] + vertices[3]) / 2
                midpoints = [top_midpoint, bottom_midpoint]
                for midpoint in midpoints:
                        rotated_midpoint = np.dot(midpoint, Rot)
                        dx = rotated_midpoint[0]
                        dy = rotated_midpoint[1]
                        plot_arrow(ax, rotated_midpoint[0], rotated_midpoint[1], dx, dy)

        # [ LEGENDAS GERAIS ]

        cismaxplt = float(self.lineEdit_cismax.text())
        cisminplt = float(self.lineEdit_cismin.text())

        plt.text(1, -1.6, "σméd = {}".format(round(sigma_medplt, 2)), ha='center', va='center', color='black',
                 weight='bold', zorder=4)  # VALOR DO SIGMA MÉDIO
        plt.text(1, -1.8, "Cis máx = {}".format(round(cismaxplt, 2)), ha='center', va='center', color='black',
                 weight='bold', zorder=4)  # VALOR DO SIGMA MÉDIO
        plt.text(1, -2, "Cis mín = {}".format(round(cisminplt , 2)), ha='center', va='center', color='black',
                 weight='bold', zorder=4)  # VALOR DO SIGMA MÉDIO
        plt.text(1.65, -0.2, "eixo x", ha='center', va='center', color='salmon', weight='bold', zorder=4)  # EIXO X
        plt.text(-0.13, 1.65, "eixo y", ha='center', va='center', color='salmon', weight='bold', zorder=4,
                 rotation=90)  # EIXO Y
        plt.text(0, 2.3, "[ ESTADO PARA O QUAL AS TENSÕES CISALHANTES SÃO MÁXIMAS ]", ha='center', va='center',
                 color='black', weight='bold', zorder=4)  # TÍTULO

        # [ SEGMENTO DE CIRCUNFERÊNCIA CIS MAX  ]

        arc = Arc([0, 0], 2.3, 2.3, theta1=0, theta2=angle, edgecolor='indianred', linewidth=1.5, zorder=3)
        ax.add_patch(arc)
        plt.plot([], [], label="θ cis máx = {} graus".format(round(angle+90, 2)), color='darkred', linestyle='solid')
        plt.legend()

        # [ SEGMENTO DE CIRCUNFERÊNCIA CIS MIN ]

        arc = Arc([0, 0], 2.6, 2.6, theta1=0, theta2=(angle + 90), edgecolor='darkred', linewidth=1.5, zorder=3)
        ax.add_patch(arc)
        plt.plot([], [], label="θ cis mín = {} graus".format(round((angle), 2)), color='indianred', linestyle='solid')
        plt.legend()

        # [ PLOTAGEM DOS VETORES DE CISALHAMENTO ]

        # CIS MÍNIMO 1
        plot_arrow(ax, rotated_vertices[0][0] - 0.1 * np.cos(theta), rotated_vertices[0][1] - 0.1 * np.sin(theta),
                   rotated_vertices[3][0] - rotated_vertices[0][0], rotated_vertices[3][1] - rotated_vertices[0][1])

        # CIS MÁXIMO 1
        plot_arrow(ax, rotated_vertices[2][0] - 0.15 * np.sin(theta), rotated_vertices[2][1] + 0.15 * np.cos(theta),
                   rotated_vertices[3][0] - rotated_vertices[2][0], rotated_vertices[3][1] - rotated_vertices[2][1])

        # CIS MÍNIMO 2
        plot_arrow(ax, rotated_vertices[2][0] + 0.1 * np.cos(theta), rotated_vertices[2][1] + 0.1 * np.sin(theta),
                   rotated_vertices[1][0] - rotated_vertices[2][0], rotated_vertices[1][1] - rotated_vertices[2][1])

        # CIS MÁXIMO 2
        plot_arrow(ax, rotated_vertices[0][0] + 0.15 * np.sin(theta), rotated_vertices[0][1] - 0.15 * np.cos(theta),
                   rotated_vertices[1][0] - rotated_vertices[0][0], rotated_vertices[1][1] - rotated_vertices[0][1])

        # [ PLOTAGEM DO GRÁFICO COM O MATPLOTLIB ]

        plt.axis('off')  # esconder os eixos
        plt.show()



# =-=-=-=-=-=-=-= [ MÓDULO PARA PLOTAR O GRÁFICO DAS DEFORMASÕES ANGULARES EXTREMAS  ] =-=-=-=-=-=-=-= #

    def pltang(self):

        # [ FUNÇÃO QUE GERA OS VETORES ]

        def plot_arrow(ax, x, y, dx, dy):
                ax.arrow(x, y, dx, dy, head_width=0.05, head_length=0.1, fc='k', ec='k')

        # [ CAPTURA O ÂNGULO TETA_1 GERADO ]

        angle1 = float(self.lineEdit_tetaangmin_3.text())
        theta1 = np.radians(angle1)  # Conversão para radianos

        # [ CRIAÇÃO DAS COORDENADAS DOS PONTOS DO QUADRADO]

        vertices = np.array([[-0.5, -0.5], [0.5, -0.5], [0.5, 0.5], [-0.5, 0.5], [-0.5, -0.5]])

        # [ MATRIZ DE ROTAÇÃO E ROTAÇÃO DO QUADRADO ]

        Rot = np.array([[np.cos(theta1), np.sin(theta1)], [-np.sin(theta1), np.cos(theta1)]])
        rotated_vertices = np.dot(vertices, Rot)

        # [ PLOTAGEM DO QUADRADO ]

        fig, ax = plt.subplots()

        # [ PLOTAGEM DOS EIXOS X E Y TRACEJADOS ]

        ax.plot([-1.8, 1.8], [0, 0], linestyle='--', color='salmon', zorder=0)
        ax.plot([0, 0], [-1.8, 1.8], linestyle='--', color='salmon', zorder=0)

        # [ PLOTAGEM DO TENSOR DE TENSÃO NO GRÁFICO E NOME DO SOFTWARE]

        epsilon_xxplt = float(self.lineEdit_epsilonxx.text())
        epsilon_yyplt = float(self.lineEdit_epsilonyy.text())
        epsilon_zzplt = float(self.lineEdit_epsilonzz.text())
        epsilon_xyplt = float(self.lineEdit_epsilonxy.text())

        ax.plot([-1.8, -1.8], [-1.75, -1.25], linestyle='solid', color='black', zorder=4)
        ax.plot([-0.7, -0.7], [-1.75, -1.25], linestyle='solid', color='black', zorder=4)
        ax.plot([-1.8, -1.75], [-1.25, -1.25], linestyle='solid', color='black', zorder=4)
        ax.plot([-1.8, -1.75], [-1.75, -1.75], linestyle='solid', color='black', zorder=4)
        ax.plot([-0.7, -0.75], [-1.25, -1.25], linestyle='solid', color='black', zorder=4)
        ax.plot([-0.7, -0.75], [-1.75, -1.75], linestyle='solid', color='black', zorder=4)
        ax.plot([-1.85, -1.915], [-1.48, -1.48], linestyle='solid', color='black', zorder=4)
        ax.plot([-1.85, -1.915], [-1.52, -1.52], linestyle='solid', color='black', zorder=4)
        plt.text(-2.1, -1.5, "[ Ɛ ]", ha='center', va='center', color='black', weight='bold', zorder=4)
        plt.text(-1.6, -1.35, "{}".format(round(epsilon_xxplt, 2)), ha='center', va='center', color='black', fontsize=7,
                 zorder=4)  # epsilonxx
        plt.text(-1.250, -1.35, "{}".format(round(epsilon_xyplt, 2)), ha='center', va='center', color='black', fontsize=7,
                 zorder=4)  # epsilonxy
        plt.text(-0.9, -1.35, "0", ha='center', va='center', color='black', fontsize=7, zorder=4)  # sigmaxz
        plt.text(-1.6, -1.52, "{}".format(round(epsilon_xyplt, 2)), ha='center', va='center', color='black', fontsize=7,
                 zorder=4)  # epsilonyx
        plt.text(-1.250, -1.52, "{}".format(round(epsilon_yyplt, 2)), ha='center', va='center', color='black', fontsize=7,
                 zorder=4)  # epsilonyy
        plt.text(-0.9, -1.52, "0", ha='center', va='center', color='black', fontsize=7, zorder=4)  # sigmayz
        plt.text(-1.6, -1.65, "0", ha='center', va='center', color='black', fontsize=7, zorder=4)  # sigmazx
        plt.text(-1.250, -1.65, "0", ha='center', va='center', color='black', fontsize=7, zorder=4)  # sigmazy
        plt.text(-0.9, -1.65, "{}".format(round(epsilon_zzplt, 2)), ha='center', va='center', color='black', fontsize=7,
                 zorder=4)  # epsilonzz
        plt.text(-1.65, -1.11, "* Tensor de deformação de origem ", ha='center', va='center', color='black', fontsize=7,
                 zorder=4)
        plt.text(-1.137, 1.83, "PlaneStr2 © - (Versão 1.0)  ", ha='center', va='center', color='black', fontsize=10,
                 zorder=4)

        # [ DEFINIÇÃO DOS LIMITES DOS EIXOS ]

        ax.set_xlim(-2, 2)
        ax.set_ylim(-2, 2)

        # [ DESENHO E PREENCHIMENTO DO QUADRADO ]

        ax.fill(rotated_vertices[:, 0], rotated_vertices[:, 1], color='red', zorder=1)

        # [ APLICAÇÃO DOS VETORES NO PONTO MÉDIO DE CADA UMA DAS FACES DO QUADRADO ]

        epsilon_medplt = float(self.lineEdit_epsilonmedio.text())

        # FACES LATERAIS -----------------------------------------------------------------------------------------------

        if epsilon_medplt < 0:
                left_midpoint = (vertices[0] + vertices[3]) / 2
                right_midpoint = (vertices[1] + vertices[2]) / 2
                midpoints = [left_midpoint, right_midpoint]
                for midpoint in midpoints:
                        rotated_midpoint = np.dot(midpoint, Rot)
                        dx = rotated_midpoint[0]
                        dy = rotated_midpoint[1]
                        plot_arrow(ax, rotated_midpoint[0] + 1.2 * dx, rotated_midpoint[1] + 1.2 * dy, -dx, -dy)

        else:
                left_midpoint = (vertices[0] + vertices[3]) / 2
                right_midpoint = (vertices[1] + vertices[2]) / 2
                midpoints = [left_midpoint, right_midpoint]
                for midpoint in midpoints:
                        rotated_midpoint = np.dot(midpoint, Rot)
                        dx = rotated_midpoint[0]
                        dy = rotated_midpoint[1]
                        plot_arrow(ax, rotated_midpoint[0], rotated_midpoint[1], dx, dy)

        # FACES SUPERIORES E INFERIORES --------------------------------------------------------------------------------

        if epsilon_medplt < 0:
                top_midpoint = (vertices[0] + vertices[1]) / 2
                bottom_midpoint = (vertices[2] + vertices[3]) / 2
                midpoints = [top_midpoint, bottom_midpoint]
                for midpoint in midpoints:
                        rotated_midpoint = np.dot(midpoint, Rot)
                        dx = rotated_midpoint[0]
                        dy = rotated_midpoint[1]
                        plot_arrow(ax, rotated_midpoint[0] + 1.2 * dx, rotated_midpoint[1] + 1.2 * dy, -dx, -dy)

        else:
                top_midpoint = (vertices[0] + vertices[1]) / 2
                bottom_midpoint = (vertices[2] + vertices[3]) / 2
                midpoints = [top_midpoint, bottom_midpoint]
                for midpoint in midpoints:
                        rotated_midpoint = np.dot(midpoint, Rot)
                        dx = rotated_midpoint[0]
                        dy = rotated_midpoint[1]
                        plot_arrow(ax, rotated_midpoint[0], rotated_midpoint[1], dx, dy)

        # [ LEGENDAS GERAIS ]

        angmaxplt = float(self.lineEdit_angmax.text())
        angminplt = float(self.lineEdit_angmin.text())

        plt.text(1, -1.6, "Ɛméd = {}".format(round(epsilon_medplt, 2)), ha='center', va='center', color='black',
                 weight='bold', zorder=4)  # VALOR DO EPSILON MÉDIO
        plt.text(1, -1.8, "Ang máx = {}".format(round(angmaxplt, 2)), ha='center', va='center', color='black',
                 weight='bold', zorder=4)  # VALOR DO EPSILON MÉDIO
        plt.text(1, -2, "Ang mín = {}".format(round(angminplt , 2)), ha='center', va='center', color='black',
                 weight='bold', zorder=4)  # VALOR DO EPSILON MÉDIO
        plt.text(1.65, -0.2, "eixo x", ha='center', va='center', color='salmon', weight='bold', zorder=4)  # EIXO X
        plt.text(-0.13, 1.65, "eixo y", ha='center', va='center', color='salmon', weight='bold', zorder=4,
                 rotation=90)  # EIXO Y
        plt.text(0, 2.3, "[ ESTADO PARA O QUAL AS DEFORMAÇÕES ANGULARES SÃO MÁXIMAS ]", ha='center', va='center',
                 color='black', weight='bold', zorder=4)  # TÍTULO

        # [ SEGMENTO DE CIRCUNFERÊNCIA ANG MAX  ]

        arc = Arc([0, 0], 2.3, 2.3, theta1=0, theta2=angle1, edgecolor='indianred', linewidth=1.5, zorder=3)
        ax.add_patch(arc)
        plt.plot([], [], label="θ ang máx = {} graus".format(round(angle1+90, 2)), color='darkred', linestyle='solid')
        plt.legend()

        # [ SEGMENTO DE CIRCUNFERÊNCIA ANG MIN ]

        arc = Arc([0, 0], 2.6, 2.6, theta1=0, theta2=(angle1 + 90), edgecolor='darkred', linewidth=1.5, zorder=3)
        ax.add_patch(arc)
        plt.plot([], [], label="θ ang mín = {} graus".format(round((angle1), 2)), color='indianred', linestyle='solid')
        plt.legend()

        # [ PLOTAGEM DOS VETORES DE CISALHAMENTO ]

        # CIS MÍNIMO 1
        plot_arrow(ax, rotated_vertices[0][0] - 0.1 * np.cos(theta1), rotated_vertices[0][1] - 0.1 * np.sin(theta1),
                   rotated_vertices[3][0] - rotated_vertices[0][0], rotated_vertices[3][1] - rotated_vertices[0][1])

        # CIS MÁXIMO 1
        plot_arrow(ax, rotated_vertices[2][0] - 0.15 * np.sin(theta1), rotated_vertices[2][1] + 0.15 * np.cos(theta1),
                   rotated_vertices[3][0] - rotated_vertices[2][0], rotated_vertices[3][1] - rotated_vertices[2][1])

        # CIS MÍNIMO 2
        plot_arrow(ax, rotated_vertices[2][0] + 0.1 * np.cos(theta1), rotated_vertices[2][1] + 0.1 * np.sin(theta1),
                   rotated_vertices[1][0] - rotated_vertices[2][0], rotated_vertices[1][1] - rotated_vertices[2][1])

        # CIS MÁXIMO 2
        plot_arrow(ax, rotated_vertices[0][0] + 0.15 * np.sin(theta1), rotated_vertices[0][1] - 0.15 * np.cos(theta1),
                   rotated_vertices[1][0] - rotated_vertices[0][0], rotated_vertices[1][1] - rotated_vertices[0][1])

        # [ PLOTAGEM DO GRÁFICO COM O MATPLOTLIB ]

        plt.axis('off')  # esconder os eixos
        plt.show()

# =-=-=-=-=-=-=-= [ EXECUÇÃO DA CLASSE RESPONSÁVEL PELA INTERFACE GRÁFICA ] =-=-=-=-=-=-=-= #

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
