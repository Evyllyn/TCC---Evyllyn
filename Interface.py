import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt, QPoint


class DrawingArea(QWidget):
    def __init__(self):
        super().__init__()
        self.nodes = []  # Lista para armazenar as coordenadas dos nós
        self.lines = []  # Lista para armazenar as linhas desenhadas
        self.drawing_line = False  # Flag para verificar se estamos desenhando uma linha

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.drawing_line:
                # Desenhando uma linha
                self.lines.append((self.last_point, event.pos()))
                self.drawing_line = False
            else:
                # Desenhando um nó
                self.nodes.append(event.pos())
            self.update()

    def mouseMoveEvent(self, event):
        if self.drawing_line:
            self.current_point = event.pos()
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(Qt.blue, 3)
        painter.setPen(pen)

        # Desenhar nós
        for node in self.nodes:
            painter.drawPoint(node)

        # Desenhar linhas
        for line in self.lines:
            painter.drawLine(line[0], line[1])

        # Desenhar linha enquanto arrasta
        if self.drawing_line and hasattr(self, 'current_point'):
            painter.drawLine(self.last_point, self.current_point)

    def start_drawing_line(self):
        self.drawing_line = True
        self.last_point = self.nodes[-1] if self.nodes else QPoint(0, 0)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Desenho de Nós e Linhas")
        self.setGeometry(100, 100, 800, 600)

        # Layout principal
        layout = QVBoxLayout()

        # Área de desenho
        self.drawing_area = DrawingArea()
        layout.addWidget(self.drawing_area)

        # Botões de controle
        button_layout = QHBoxLayout()

        self.node_button = QPushButton("Nó")
        self.node_button.clicked.connect(self.select_node)
        button_layout.addWidget(self.node_button)

        self.line_button = QPushButton("Linha")
        self.line_button.clicked.connect(self.select_line)
        button_layout.addWidget(self.line_button)

        layout.addLayout(button_layout)

        # Widget central
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def select_node(self):
        # Lógica para selecionar a função de desenhar nós
        self.drawing_area.drawing_line = False

    def select_line(self):
        # Lógica para selecionar a função de desenhar linhas
        if self.drawing_area.nodes:
            self.drawing_area.start_drawing_line()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
