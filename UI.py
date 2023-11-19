import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout, QMessageBox
import Functions



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

    self.mensaje1_encriptado = QLineEdit()
    self.mensaje1_encriptado.setReadOnly(True)

    self.mensaje2_encriptado = QLineEdit()
    self.mensaje2_encriptado.setReadOnly(True)

    layout = QGridLayout()
    layout.addWidget(self.mensaje, 0, 0, 1, 2)
    layout.addWidget(self.p, 1, 0)
    layout.addWidget(self.q, 1, 1)
    layout.addWidget(self.e, 2, 0)
    layout.addWidget(self.encriptar, 3, 0)
    layout.addWidget(self.mensaje1_encriptado, 4, 0, 1, 2)
    layout.addWidget(self.mensaje2_encriptado, 4, 0, 2, 2)

    self.setFixedSize(500, 300)

    self.setLayout(layout)

  def funcion_Prince(self):
    try:
        p = int(round(float(self.p.text())))
        q = int(round(float(self.q.text())))
        e = int(round(float(self.e.text())))
        phi = ((p-1)*(q-1))
    except ValueError:
        QMessageBox.warning(self, "Error", "Por favor, ingresa números válidos para p, q y e.")
        return
    
    mensaje = self.mensaje.text()

    if not self.es_primo(p):
      QMessageBox.warning(self, "Error", "El número p no es primo.")
      return

    if not self.es_primo(q):
      QMessageBox.warning(self, "Error", "El número q no es primo.")
      return
    
    if not p*q>2525:
      QMessageBox.warning(self, "Error", "p*q debe ser mayor a 2525.")
      return
    
    
    if e <= 1:
      QMessageBox.warning(self, "Error", "El número e debe ser mayor a 1.")
      return
    
    if Functions.euclides(e,phi) != 1:
      QMessageBox.warning(self, "Error", "El mcd (e,phi) debe ser igual a 1.")
      return
      
    
    

    mensaje1_encriptado = Functions.encryption(Functions.mensaje(mensaje, e, p*q)) 
    mensaje2_encriptado = Functions.mensaje(mensaje, e, p*q)

    self.mensaje1_encriptado.setText(mensaje1_encriptado)
    self.mensaje2_encriptado.setText(mensaje2_encriptado)




class DesencriptadorRSA(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Desencriptador RSA")

        # Elementos existentes
        self.mensaje_encriptado = QLineEdit()
        self.mensaje_encriptado.setPlaceholderText("Ingresa el mensaje encriptado")
        self.e = QLineEdit()
        self.e.setPlaceholderText("Ingresa el entero e")
        self.n = QLineEdit()
        self.n.setPlaceholderText("Ingresa el número n")
        self.desencriptar = QPushButton("Desencriptar")
        self.desencriptar.clicked.connect(self.funcion_desencriptar)
        self.mensaje_desencriptado = QLineEdit()
        self.mensaje_desencriptado.setReadOnly(True)

        # Nuevo elemento para mostrar la clave privada
        self.clave_privada = QLineEdit()
        self.clave_privada.setReadOnly(True)
        self.clave_privada.setPlaceholderText("Clave privada")

        # Añadiendo elementos al layout
        layout = QGridLayout()
        layout.addWidget(self.mensaje_encriptado, 0, 0, 1, 2)
        layout.addWidget(self.e, 1, 0)
        layout.addWidget(self.n, 1, 1)
        layout.addWidget(self.desencriptar, 2, 0)
        layout.addWidget(self.mensaje_desencriptado, 3, 0, 1, 2)
        layout.addWidget(self.clave_privada, 4, 0, 1, 2)  # Añade la clave privada al layout

        self.setLayout(layout)
        self.setFixedSize(500, 300)

    def funcion_desencriptar(self):
        try:
            e = int(self.e.text())
            n = int(self.n.text())
            if not n > 2525:
                QMessageBox.warning(self, "Error", "n debe ser mayor a 2525")
                return
              
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingresa números válidos para e y n.")
            return

        # Calcula y muestra la clave privada
        clave_priv = Functions.privateKey(e, n)
        self.clave_privada.setText(str(clave_priv))

        # Desencriptación del mensaje
        mensaje_encriptado = self.mensaje_encriptado.text()
        mensaje_desencriptado = Functions.mensajeC(mensaje_encriptado, e, n)
        self.mensaje_desencriptado.setText(mensaje_desencriptado)
