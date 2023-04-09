import sys
#from PyQt6.QtCore import *
#from PyQt6.QtGui import *
#from PyQt6.QtWidgets import *
from PySide6 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        
        self.button_is_checked = True
        
        self.setWindowTitle("My App")
        
        self.button = QtWidgets.QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.button_clicked)
        self.button.toggled.connect(self.button_toggled)
        self.button.released.connect(self.button_released)
        self.button.setChecked(self.button_is_checked)
        
        #self.setFixedSize(QtCore.QSize(400,300))
        
        self.setCentralWidget(self.button)
        
    def button_clicked(self):
        print("Clicked")
        
    def button_toggled(self, checked):
        self.button_is_checked = checked
        print(f'Toggled: {self.button_is_checked}')
        
    def button_released(self):
        self.button_is_checked = self.button.isChecked()
        
        print(f'Released: {self.button_is_checked}')
    
    
    
def main():
    app = QtWidgets.QApplication(sys.argv)
    window= Window()
    window.show()
    app.exec()
    
if __name__ == '__main__':
    main()