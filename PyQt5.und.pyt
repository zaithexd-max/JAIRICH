import sys #Provides access to system-specific parameters and functions
from PyQt5.QtWidgets import QApplication , QMainWindow 
class MainWindow(QMainWindow):#We are creating a custom window class that inherits from QMainWindow means that our class gets all the functionality of QMainWindow automatically:
  def __init__(self): #This is the constructor method.Called automatically when we create an instance of MainWindow.
    super().__init__() #This line think of it as “Do everything a normal QMainWindow does first, then I’ll add my customizations.”
    self.setWindowTitle("PyQt5")#Sets the title of the window that appears on the top bar.
def main():
  app = QApplication(sys.argv)#Creates the application object. Must have 1 QApplication per app
  window = MainWindow()#Creates an instance of our custom MainWindow class.(Turn it into variable for much more easier to type)
  window.show()#Makes the window visible on the screen.

  sys.exit(app.exec_())
  #app.exec_() starts the event loop.
    #Handles all user interaction (mouse clicks, keyboard input, window resizing, redrawing).
    #Blocks further code execution until the app is closed.
  #sys.exit() ensures that Python exits cleanly with the return code from exec_() (usually 0 for normal exit).
if __name__ == "__main__":
  main()