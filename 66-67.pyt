import sys
from PyQt5.QtWidgets import QApplication , QMainWindow ,QLabel
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Sigma")
    self.setGeometry(700,300,500,500)
    self.setWindowIcon(QIcon("Baby.jpg"))
    label = QLabel("Hello",self)
    label.setFont(QFont("Arial",30))
    label.setGeometry(0,0,500,100)
    label.setStyleSheet("color: blue;"
                        "background-color: black;"
                        "font-weight: bold")
    label.setAlignment(Qt.AlignHCenter|Qt.AlignTop) #Align the font to the center horizontally
def main():
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec_())
if __name__ == "__main__":
  main()