import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout, QMessageBox



class EncriptadorRSA(QWidget):

  def __init__(self):
    super().__init__()
    self.initUI()
  
  def es_primo(self, num):
    
    if num <= 1:
      return False

    for i in range(2, int(num ** 0.5) + 1):
      if num % i == 0:
        return False

    return True


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
    p = int(self.p.text())
    q = int(self.q.text())
    e = int(self.e.text())
    
    mensaje = self.mensaje.text()

    if not self.es_primo(p):
      QMessageBox.warning(self, "Error", "El número p no es primo.")
      return

    if not self.es_primo(q):
      QMessageBox.warning(self, "Error", "El número q no es primo.")
      return
    
    if e < 26:
      QMessageBox.warning(self, "Error", "El número e debe ser igual o mayor a 26.")
      return
    

    mensaje_encriptado =mensaje # encriptar(mensaje, p, q, e) ACÁ IRIRÍA LO DE PRINCE

    self.mensaje_encriptado.setText(mensaje_encriptado)




if __name__ == "__main__":
  app = QApplication(sys.argv)
  encriptador = EncriptadorRSA()
  encriptador.show()
  sys.exit(app.exec_())
