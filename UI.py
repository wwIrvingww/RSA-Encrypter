import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout



class EncriptadorRSA(QWidget):

  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    self.setWindowTitle("Encriptador RSA")

    self.mensaje = QLineEdit()
    self.mensaje.setPlaceholderText("Ingresa el mensaje")
    self.p = QLineEdit()
    self.p.setPlaceholderText("Ingresa el número primo p")
    self.q = QLineEdit()
    self.q.setPlaceholderText("Ingresa el número primo q")
    self.e = QLineEdit()
    self.e.setPlaceholderText("Ingresa el entero e")

    self.encriptar = QPushButton("Encriptar")
    self.encriptar.clicked.connect(self.funcion_Prince)

    self.mensaje_encriptado = QLineEdit()
    self.mensaje_encriptado.setReadOnly(True)

    layout = QGridLayout()
    layout.addWidget(self.mensaje, 0, 0, 1, 2)
    layout.addWidget(self.p, 1, 0)
    layout.addWidget(self.q, 1, 1)
    layout.addWidget(self.e, 2, 0)
    layout.addWidget(self.encriptar, 3, 0)
    layout.addWidget(self.mensaje_encriptado, 4, 0, 1, 2)

    self.setLayout(layout)

  def funcion_Prince(self):
      pass



if __name__ == "__main__":
  app = QApplication(sys.argv)
  encriptador = EncriptadorRSA()
  encriptador.show()
  sys.exit(app.exec_())
