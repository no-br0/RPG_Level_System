from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont
import sys

class Console(QWidget):
    def __init__(self, parent=None, width=500, height=500):
        super().__init__(parent)
        
        self.text_x = 20
        self.text_y = height - 10
        self.move_y = -20
        
        self.text_bbox = []
        
        self.canvas = QLabel(self)
        self.canvas.setScaledContents(True)
        self.canvas.setStyleSheet('background-color: #1f1f1f; border: 5px solid #303030;')
        self.canvas.move(10, 10)
        
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.canvas)
    
    def move_text(self):
        for i in self.text_bbox:
            self.canvas.move(i, 0, self.move_y)
    
    def clear_console(self):
        self.canvas.clear()
        self.text_bbox.clear()
        print('Console Cleared')
    
    def add_text(self, text):
        self.move_text()
        text = ("> " + text)
        
        font = QFont('Times', 12, QFont.Bold)
        painter = QPainter(self.canvas.pixmap())
        painter.setFont(font)
        painter.setPen(QColor('lightgreen'))
        painter.drawText(self.text_x, self.text_y, text)
        painter.end()
        self.text_bbox.append(self.canvas.pixmap().rect())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    console = Console(None, 600, 400)
    console.add_text("Hello World")
    console.show()
    sys.exit(app.exec_())