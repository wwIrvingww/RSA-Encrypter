import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

# Importa las clases para Encriptar y Desencriptar
from UI import *



class PantallaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("RSA Encriptador/Desencriptador")

        self.btnEncriptar = QPushButton("Encriptar", self)
        self.btnEncriptar.clicked.connect(self.abrirEncriptador)

        self.btnDesencriptar = QPushButton("Desencriptar", self)
        self.btnDesencriptar.clicked.connect(self.abrirDesencriptador)

        layout = QVBoxLayout()
        layout.addWidget(self.btnEncriptar)
        layout.addWidget(self.btnDesencriptar)

        self.setLayout(layout)
        self.setFixedSize(300, 200)

    def abrirEncriptador(self):
        self.encriptador = EncriptadorRSA()
        self.encriptador.show()

    def abrirDesencriptador(self):
        self.desencriptador = DesencriptadorRSA()
        self.desencriptador.show()
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    principal = PantallaPrincipal()
    principal.show()
    sys.exit(app.exec_())
