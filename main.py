import sys
import random
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel


class YellowEllipse(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 400)

        self.label = QLabel(self)
        self.label.move(0, 0)
        self.label.resize(400, 350)

        self.button = QPushButton(self)
        self.button.move(150, 350)
        self.button.resize(100, 30)
        self.button.setText("Рисование")
        self.button.clicked.connect(self.drawing)

    def drawing(self):
        qp = QPainter(self)
        qp.drawEllipse(10, 10)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = YellowEllipse()
    window.show()
    sys.exit(app.exec())
