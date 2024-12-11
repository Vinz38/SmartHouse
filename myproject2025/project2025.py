from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from project2025_second_win import * 
from project2025_third_win import *

class FirstWindow(QWidget):
    def __init__(self, *args, **qwargs):
        #! *args, **qwargs - все аргументы, которые умеет принимать QWidget   
        super().__init__(*args, **qwargs)
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon('ava.jpeg'))
        self.main_line = QVBoxLayout()
        self.setLayout(self.main_line)
        self.main_group1 = QGroupBox()
        Vline = QVBoxLayout()
        main_label = QLabel("Умный дом")
        main_label.setFont(QFont("Times", 25))
        Vline.addWidget(main_label, alignment = Qt.AlignCenter)
        self.d_button = QPushButton("Больше о умном доме")
        self.d_button.setFont(QFont("Times", 13))
        self.d_button.setFixedSize(220, 75)
        self.t_button = QPushButton("Информация о устройствах \nдля умного дома")
        self.t_button.setFont(QFont("Times", 13))
        self.t_button.setFixedSize(220, 75)
        Vline.addWidget(self.d_button, alignment = Qt.AlignCenter)
        Vline.addWidget(self.t_button, alignment = Qt.AlignCenter)
        self.main_group1.setLayout(Vline)
        self.main_line.addWidget(self.main_group1, alignment = Qt.AlignCenter)
        self.main_group1.setFixedSize(800, 500)
        self.t_button.clicked.connect(self.ssw)
        self.d_button.clicked.connect(self.sss)
        self.setFont(QFont("calibri", 13))        

    def ssw(self):
        self.new_window = theoryWindow(self) #? Первое сохраняем во втором
        self.new_window.setFont(QFont("calibri", 15))
        self.new_window.setFixedSize(800, 500)
        self.new_window.show()
        self.main_group1.hide()
    
    def sss(self):
        self.new_window1 = PatternWindow(self)
        self.new_window1.setFont(QFont("calibri", 15))
        self.new_window1.setFixedSize(800, 500)
        self.new_window1.show()
        self.main_group1.hide()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


def main():
    app = QApplication([])
    window = FirstWindow()
    window.setFixedSize(800, 500)
    window.setWindowTitle("Умный дом") 
    window.center()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()




#!button.setGeometry(200, 150, 100, 40)