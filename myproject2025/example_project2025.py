'''from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
#? from second_win import * - импорт окна из другого файла

class FirstWindow(QWidget):
    def __init__(self, *args, **qwargs):
        #! *args, **qwargs - все аргументы, которые умеет принимать QWidget   
        super().__init__(*args, **qwargs)
        self.initUI()
    def initUI(self):
        main_line_f = QVBoxLayout()
        info_label1 = QLabel('Добро подаловать, это приложение, тест Руфье')
        info_label2 = QLabel('Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровья.\n' 'Проба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности сердца при физической нагрузке.\n' 'У испытуемого, находящегося в положении лежа на спине в течение 5 мин, определяют частоту пульса за 15 секунд;\n' 'затем в течение 45 секунд испытуемый выполняет 30 приседаний.\n' 'После окончания нагрузки испытуемый ложится, и у него вновь подсчитывается число пульсаций за первые 15 секунд,\n' 'а потом — за последние 15 секунд первой минуты периода восстановления.\n' 'Важно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головокружение, шум в\n' 'ушах, сильная одышка и др.), то тест необходимо прервать и обратиться к врачу.')
        self.setLayout(main_line_f)
        self.button1 = QPushButton('Продолжить')
        main_line_f.addWidget(info_label1, alignment = Qt.AlignCenter)
        main_line_f.addWidget(info_label2, alignment = Qt.AlignCenter)
        main_line_f.addWidget(self.button1, alignment = Qt.AlignCenter)
        self.button1.clicked.connect(self.ssw)
    def ssw(self):
        self.hide()
        self.new_window = SecondWindow()
        self.setFont(QFont("calibri", 15))
        self.new_window.show()

app = QApplication([])
window = FirstWindow()
window.show()
app.exec_()
''' #! 1 window

'''class SecondWindow(QWidget):
    def __init__(self, *args, **qwargs): 
        super().__init__(*args, **qwargs)
        self.initUI()
    def initUI(self):
        self.main_layout = QHBoxLayout()
        self.left_layout = QVBoxLayout()
        self.right_layout = QVBoxLayout()
        self.main_layout.addLayout(self.left_layout)
        self.main_layout.addLayout(self.right_layout)
        self.setLayout(self.main_layout)

        self.label_name = QLabel("Введите ФИО:")
        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText("Игнатый Игнат Игнатович")

        self.label_age = QLabel("Сколько вам полных лет:")
        self.input_age = QLineEdit()
        self.input_age.setValidator(QIntValidator())
        self.input_age.setPlaceholderText("15 лет")

        self.label_instr1 = QLabel("test1")
        self.button_t1 = QPushButton("Начать первый тест")
        self.input_res3 = QLineEdit()
        self.input_res3.setValidator(QIntValidator())
        self.input_name.setPlaceholderText("Результаты теста")

        self.label_instr2 = QLabel("test2")
        self.button_t2 = QPushButton("Начать второй тест")

        self.label_instr3 = QLabel("test3")
        self.button_t3 = QPushButton("Начать финальный тест")

        self.input_res1 = QLineEdit()
        self.input_res1.setValidator(QIntValidator())
        self.input_res1.setPlaceholderText("")
        self.input_res2 = QLineEdit()
        self.input_res2.setValidator(QIntValidator())
        self.input_res2.setPlaceholderText("")

        self.label_timer = QLabel("00:00")
        self.right_layout.addWidget(self.label_timer, alignment=Qt.AlignRight)

        self.button_resf = QPushButton("Отправить результаты")

        self.left_layout.addWidget(self.label_name, alignment=Qt.AlignLeft)
        self.left_layout.addWidget(self.input_name, alignment=Qt.AlignLeft)

        self.left_layout.addWidget(self.label_age, alignment=Qt.AlignLeft)
        self.left_layout.addWidget(self.input_age, alignment=Qt.AlignLeft)
        
        self.left_layout.addWidget(self.label_instr1, alignment=Qt.AlignLeft)
        self.left_layout.addWidget(self.button_t1, alignment=Qt.AlignLeft)
        self.left_layout.addWidget(self.input_res3, alignment=Qt.AlignLeft)

        self.left_layout.addWidget(self.label_instr2, alignment=Qt.AlignLeft)
        self.left_layout.addWidget(self.button_t2, alignment=Qt.AlignLeft)

        self.left_layout.addWidget(self.label_instr3, alignment=Qt.AlignLeft)
        self.left_layout.addWidget(self.button_t3, alignment=Qt.AlignLeft)

        self.left_layout.addWidget(self.input_res1, alignment=Qt.AlignLeft)
        self.left_layout.addWidget(self.input_res2, alignment=Qt.AlignLeft)

        self.left_layout.addWidget(self.button_resf, alignment=Qt.AlignLeft)
        self.button_resf.clicked.connect(self.cui)
    def ssw(self):
        self.hide()
        self.new_window = final_window()
        self.info_inside_final_window()
        self.setFont(QFont("calibri", 15))
        self.new_window.show()
    def cui(self):
        if self.input_name.text() == '':
            self.show_error("Введите ФИО")
            return 'ошибка'
        elif self.input_age.text() == '':
            self.show_error("Введите возвраст")
            return 'ошибка'
        self.ssw()
    def show_error(self, text):
        error = QMessageBox()
        error.setWindowTitle("Ошибка")
        error.setText(text)
        error.exec_()
    def info_inside_final_window(self):
        self.new_window.nadpis1.setText("Информация о пользователе: <br> <b><i><u>" + self.input_name.text())
        index = (4*(int(self.input_res1.text())+int(self.input_res2.text())+int(self.input_res3.text()))-200)/10
        self.new_window.nadpis2.setText("Ваш ИР: " + str(index))
        age = int(self.input_age.text())
        result = self.new_window.calc_result(age, index)
        self.new_window.nadpis3.setText("ваша работоспособность сердца: "+ result)''' #!2 window