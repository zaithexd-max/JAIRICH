import sys
from PyQt5.QtWidgets import QApplication , QMainWindow ,QLabel,QWidget,QVBoxLayout,QHBoxLayout,QGridLayout
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("PyQt5")
    self.initUI() #Initialize the initUI
    self.setGeometry(500,300,500,500)
  def initUI(self):
    central_widget = QWidget() #Creating a Widget to hold our label and then send it into the code down here
    self.setCentralWidget(central_widget) # Add to main window
    label1 = QLabel("#1",self)
    label2 = QLabel("#2",self)
    label3 = QLabel("#3",self)
    label4 = QLabel("#4",self)
    label5 = QLabel("#5",self)
    #label = QLabel(text, parent)
    label1.setStyleSheet("background-color: red")
    label2.setStyleSheet("background-color: yellow")
    label3.setStyleSheet("background-color: green")
    label4.setStyleSheet("background-color: blue")
    label5.setStyleSheet("background-color: purple")
  #Add a css to our project
    Grid = QGridLayout() #Assign a layout manager to a variable
    Grid.addWidget(label1,0,0) 
    Grid.addWidget(label2,0,1)
    Grid.addWidget(label3,1,0)
    Grid.addWidget(label4,1,1)
    Grid.addWidget(label5,1,2)
    #Send the code into the layout manager
    #Grid.addWidget(widget,row,column)
    central_widget.setLayout(Grid)
def main():
  app = QApplication(sys.argv)
  #QApplication is the main application object in PyQt5. Every PyQt5 GUI program must have exactly one QApplication instance.
  window = MainWindow()
  #MainWindow() is your custom class that inherits from QMainWindow. now we put it into the variable
  window.show()
  #This function show the window
  sys.exit(app.exec_())
  #This function ensures that your Python program exits cleanly and passes this return code back to the operating system.
if __name__ == "__main__":
  main()