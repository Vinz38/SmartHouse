from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class HyperlinkLabel(QLabel): #? Гипер ссылки
    def __init__(self, parent=None):
        super().__init__()
        self.setStyleSheet('font-size: 20px')
        self.setOpenExternalLinks(True)
        self.setParent(parent)
    

class theoryWindow(QWidget):
    def __init__(self, *args, **qwargs):
        super().__init__(*args, **qwargs)
        self.parent_window = args[0] #? Добавляем первое во второе
        self.initUI()

    def initUI(self):
        self.main_line = QVBoxLayout()
        self.main_group = QGroupBox()


        self.button_theory1 = QPushButton("Датчик движения") #! ДАТЧИКИ; САМАЯ ЛЕВАЯ ЛИНИЯ(main_layout_group2);
        self.button_theory1.setFixedSize(150, 35)
        self.button_theory1.setFont(QFont("Times", 12))
        self.button_theory2 = QPushButton("Датчик вибрации")
        self.button_theory2.setFixedSize(150, 35)
        self.button_theory2.setFont(QFont("Times", 12))
        self.button_theory3 = QPushButton("Датчик дыма")
        self.button_theory3.setFixedSize(150, 35)
        self.button_theory3.setFont(QFont("Times", 12))
        self.button_theory4 = QPushButton("Климатические д.")
        self.button_theory4.setFixedSize(150, 35)
        self.button_theory4.setFont(QFont("Times", 12))
        self.button_theory5 = QPushButton("Д. освещенности")
        self.button_theory5.setFixedSize(150, 35)
        self.button_theory5.setFont(QFont("Times", 12))
        self.button_theory6 = QPushButton("Датчик открытия")
        self.button_theory6.setFixedSize(150, 35)
        self.button_theory6.setFont(QFont("Times", 12))
        self.button_theory7 = QPushButton("Датчик протечки")
        self.button_theory7.setFixedSize(150, 35)
        self.button_theory7.setFont(QFont("Times", 12))
        self.button_theory8 = QPushButton("Датчик утечки газа")
        self.button_theory8.setFixedSize(150, 35)
        self.button_theory8.setFont(QFont("Times", 12))


        self.button_smartspeaker = QPushButton("«Алиса»") #! Умная колонка, умная розетка, умная лампочка; (ne_layout1, ne_layout2, ne_layout3)
        self.button_smartspeaker.setFixedSize(150, 35)
        self.button_smartspeaker.setFont(QFont("Times", 12))
        self.button_smartpowersocer = QPushButton("Умные розетки")
        self.button_smartpowersocer.setFixedSize(150, 35)
        self.button_smartpowersocer.setFont(QFont("Times", 12))
        self.button_smartlamp = QPushButton("Умные лампочки")
        self.button_smartlamp.setFixedSize(150, 35)
        self.button_smartlamp.setFont(QFont("Times", 12))
        
        
        self.button_back = QPushButton("Назад") #! НАЗАД; СРЕДНЯЯ ЛИНИЯ(main_layout_group3) 
        self.button_back.setFixedSize(150, 35)
        self.button_back.setFont(QFont("Times", 12))


        self.akt_b = QPushButton("Актуальность \nУмного дома") #! Актуальность; САМАЯ ПРАВАЯ ЛИНИЯ(main_layout_group1)
        self.akt_b.setFixedSize(160, 45)
        self.akt_b.setFont(QFont("Times", 12))


        ismarth = QLabel(self) #! ВСТАВКА КАРТИНОК     
        ismarthpix = QPixmap('ismarthouse.png')
        ismarth.setPixmap(ismarthpix) 
        ismarth.setFixedSize(220, 220)


        main_layout_group = QHBoxLayout()
        main_layout_group1 = QVBoxLayout()
        main_layout_group2 = QVBoxLayout()
        main_layout_group3 = QVBoxLayout()
        main_layout_group.addLayout(main_layout_group2)
        main_layout_group.addLayout(main_layout_group1)
        main_layout_group3.addLayout(main_layout_group)

        ne_layout1 = QHBoxLayout()
        ne_layout2 = QHBoxLayout()
        ne_layout3 = QHBoxLayout()
        main_layout_group2.addLayout(ne_layout1)
        main_layout_group2.addLayout(ne_layout2)
        main_layout_group2.addLayout(ne_layout3)

        ne_layout1.addWidget(self.button_theory1, alignment = Qt.AlignLeft) #? ne_layout1 1111111
        ne_layout2.addWidget(self.button_theory2, alignment = Qt.AlignLeft) #? ne_layout2 2222222
        ne_layout3.addWidget(self.button_theory3, alignment = Qt.AlignLeft) #? ne_layout3 3333333
        main_layout_group2.addWidget(self.button_theory4, alignment = Qt.AlignLeft) #! main_layout_group2 222222222
        main_layout_group2.addWidget(self.button_theory5, alignment = Qt.AlignLeft)
        main_layout_group2.addWidget(self.button_theory6, alignment = Qt.AlignLeft)
        main_layout_group2.addWidget(self.button_theory7, alignment = Qt.AlignLeft)
        main_layout_group2.addWidget(self.button_theory8, alignment = Qt.AlignLeft)


        ne_layout1.addWidget(self.button_smartspeaker, alignment = Qt.AlignRight) #? ne_layout1 1111111
        ne_layout2.addWidget(self.button_smartpowersocer, alignment = Qt.AlignRight) #? ne_layout2 22222222
        ne_layout3.addWidget(self.button_smartlamp, alignment = Qt.AlignRight) #? ne_layout3 33333333


        main_layout_group3.addWidget(self.button_back, alignment = Qt.AlignCenter) #! main_layout_group3 333333333333

        self.main_group.setLayout(main_layout_group3)
        self.main_group.setTitle("Информация о устройствах")
        self.main_group.setFixedSize(800, 500)
    
        main_layout_group1.addWidget(ismarth, alignment= Qt.AlignCenter)
        main_layout_group1.addWidget(self.akt_b, alignment= Qt.AlignCenter)
        self.akt_b.clicked.connect(self.akt)
        self.setLayout(self.main_line)
        ne_main_line = QHBoxLayout()
        self.main_line.addLayout(ne_main_line)
        ne_main_line.addWidget(self.main_group, alignment = Qt.AlignLeft)

        self.button_back.clicked.connect(self.back) #! Кнопка НАЗАД

        self.button_theory1.clicked.connect(self.button_theory_expansion1) #! Подключение функций к кнопкам датчиков.
        self.button_theory2.clicked.connect(self.button_theory_expansion2)
        self.button_theory3.clicked.connect(self.button_theory_expansion3)
        self.button_theory4.clicked.connect(self.button_theory_expansion4)
        self.button_theory5.clicked.connect(self.button_theory_expansion5)
        self.button_theory6.clicked.connect(self.button_theory_expansion6)
        self.button_theory7.clicked.connect(self.button_theory_expansion7)
        self.button_theory8.clicked.connect(self.button_theory_expansion8)

        self.button_smartspeaker.clicked.connect(self.ssis) #! Подключение к кнопкам: умная колонка, умная розетка, умная лампочка.  
        self.button_smartlamp.clicked.connect(self.slis)
        self.button_smartpowersocer.clicked.connect(self.spsis)

    def back(self):
        self.hide()
        self.parent_window.main_group1.show() #? Показываем группу первого окна
    
    def ssis(self):
        linkTemplate = '<a href={0}>{1}</a>'
        self.main_group.hide()
        self.g_ss = QGroupBox()
        self.g_ss.setTitle("Умная колонка")
        self.g_ss.setFixedSize(800, 500)
        ss_l = QVBoxLayout()
        ss_label = QLabel('''Умные колонки Яндекса с виртуальным ассистентом №1.Алиса включает музыку, рассказывает
о погоде, вызывает такси, заказывает продукты, помогает управлять умным домом и умеет 
ещё много всего''')

        ss_label.setFont(QFont("Times", 14))
        ss_label2 = HyperlinkLabel(self)
        ss_label2.setText(linkTemplate.format('www.dns-shop.ru/product/127c5bcb7f0aed20', 'Яндекс.Станция Мини'))
        ss_label3 = HyperlinkLabel(self)
        ss_label3.setText(linkTemplate.format('www.dns-shop.ru/product/6022f0d258bfed20', 'Яндекс.Станция 2'))
        ss_label4 = HyperlinkLabel(self)
        ss_label4.setText(linkTemplate.format('www.dns-shop.ru/product/e498e4397a02ed20', 'Яндекс.Станция Миди'))
        

        ssa = QLabel(self)
        ssapix = QPixmap('am.png')
        ssa.setPixmap(ssapix) 
        ssa.setFixedSize(190, 190)

        ssa1 = QLabel(self)
        ssapix1 = QPixmap('a2.png')
        ssa1.setPixmap(ssapix1) 
        ssa1.setFixedSize(190, 190)

        ssa2 = QLabel(self)
        ssapix2 = QPixmap('amid.png')
        ssa2.setPixmap(ssapix2) 
        ssa2.setFixedSize(190, 190)


        self.b_ss = QPushButton("Назад")
        self.b_ss.clicked.connect(self.back_ss)

        ss_l.addWidget(ss_label, alignment = Qt.AlignLeft)

        sslH = QHBoxLayout()
        sslH1 = QVBoxLayout()
        sslH2 = QVBoxLayout() 
        sslH3 = QVBoxLayout()    
        sslH.addLayout(sslH1)
        sslH.addLayout(sslH2)
        sslH.addLayout(sslH3)
        ss_l.addLayout(sslH)
        sslH1.addWidget(ssa, alignment = Qt.AlignLeft)
        sslH2.addWidget(ssa1, alignment = Qt.AlignLeft)
        sslH3.addWidget(ssa2, alignment = Qt.AlignLeft)
        sslH1.addWidget(ss_label2, alignment = Qt.AlignLeft)
        sslH2.addWidget(ss_label3, alignment = Qt.AlignLeft)
        sslH3.addWidget(ss_label4, alignment = Qt.AlignLeft)

        ss_l.addWidget(self.b_ss, alignment = Qt.AlignCenter)
        self.g_ss.setLayout(ss_l)
        self.main_line.addWidget(self.g_ss, alignment = Qt.AlignLeft)
        self.g_ss.show()
    def back_ss(self):
        self.g_ss.hide()
        self.main_group.show()

    
    def slis(self):
        linkTemplate = '<a href={0}>{1}</a>'
        self.main_group.hide()
        self.g_sl = QGroupBox()
        self.g_sl.setTitle("Умная лампочка")
        self.g_sl.setFixedSize(800, 500)
        sl_l = QVBoxLayout()
        sl_label = QLabel('''Умная лампочка — это устройство, которое позволяет управлять светом с помощью смартфона, 
голосовых команд или пульта дистанционного управления. Они могут менять цвет, яркость и 
тон света в зависимости от настроек, а также управляться через Wi-Fi или Bluetooth.Умные лам-
-почки используют технологию светодиодов (LED), которая позволяет им потреблять меньше 
энергии, чем обычные лампочки.''')
        
        sl = QLabel(self)
        slpixmap = QPixmap('sl.png')
        sl.setPixmap(slpixmap)

        sl_label.setFont(QFont("Times", 14))
        sl_label2 = HyperlinkLabel(self)
        sl_label2.setText(linkTemplate.format('www.dns-shop.ru/product/f63b1f144841ed20', 'Умная светодиодная лампа Яндекс'))
        self.b_sl = QPushButton("Назад")
        self.b_sl.clicked.connect(self.back_sl)
        sl_l.addWidget(sl_label, alignment = Qt.AlignLeft)
        sl_l.addWidget(sl, alignment = Qt.AlignCenter)
        sl_l.addWidget(sl_label2, alignment = Qt.AlignCenter)
        sl_l.addWidget(self.b_sl, alignment = Qt.AlignCenter)
        self.g_sl.setLayout(sl_l)
        self.main_line.addWidget(self.g_sl, alignment = Qt.AlignLeft)
        self.g_sl.show()
    def back_sl(self):
        self.g_sl.hide()
        self.main_group.show()


    def spsis(self):
        linkTemplate = '<a href={0}>{1}</a>'
        self.main_group.hide()
        self.g_sps = QGroupBox()
        self.g_sps.setTitle("Умная розетка")
        self.g_sps.setFixedSize(800, 500)
        sps_l = QVBoxLayout()
        sps_label = QLabel('''Умная розетка — это электромагнитное реле с возможностью дистанционного управления 
по Wi-Fi или Bluetooth. Для этого в розетке установлены микропроцессор и модуль беспро- 
-водной связи. В зависимости от модели и производителя розетки могут управляться как 
с помощью фирменного программного обеспечения, так и в рамках универсальных 
протоколов — то есть, через различные системы умного дома Apple, Google, «Яндекс».''')
        
        sc = QLabel(self)
        scpixmap = QPixmap('sc.png')
        sc.setPixmap(scpixmap)
        
        sps_label.setFont(QFont("Times", 14))
        sps_label2 = HyperlinkLabel(self)
        sps_label2.setText(linkTemplate.format('www.dns-shop.ru/product/c779d910ea66ed20', 'Умная розетка Яндекс'))
        self.b_sps = QPushButton("Назад")
        self.b_sps.clicked.connect(self.back_sps)
        sps_l.addWidget(sps_label, alignment = Qt.AlignLeft)
        sps_l.addWidget(sc, alignment = Qt.AlignCenter)
        sps_l.addWidget(sps_label2, alignment = Qt.AlignCenter)
        sps_l.addWidget(self.b_sps, alignment = Qt.AlignCenter)
        self.g_sps.setLayout(sps_l)
        self.main_line.addWidget(self.g_sps, alignment = Qt.AlignLeft)
        self.g_sps.show()
    def back_sps(self):
        self.g_sps.hide()
        self.main_group.show()


    def akt(self):
        self.main_group.hide()
        self.g_akt = QGroupBox()
        self.g_akt.setTitle("Актуальность")
        self.g_akt.setFixedSize(800, 500)
        akt_l = QVBoxLayout()
        akt_label = QLabel('''Актуальность умного дома обусловлена рядом преимуществ, среди которых:
        1.Экономия времени и ресурсов. Система автоматизирует множество рутинных задач, 
        пользователь меньше времени тратит на управление домашними процессами. 
        Например, термостаты автоматически регулируют температуру в зависимости 
        от времени суток и присутствия человека, а управление освещением может 
        автоматически выключать свет там, где никто не находится, 
        или включать его при обнаружении движения. 
        2. Экологичность. Интеллектуальное управление помогает сократить 
        потребление энергии за счёт автоматического регулирования освещения, отопления, 
        бытовых приборов. За счёт этого повышается энергоэффективность жилья, 
        что помогает уменьшить углеродный след и негативное воздействие на окружающую среду. 
        3. Безопасность. 12 Система видеонаблюдения может анализировать поведение людей,
        находящихся на территории, и на основе искусственного интеллекта 
        определять потенциальные угрозы. 
        Если будет замечено подозрительное поведение, 
        она автоматически отправит владельцу уведомление, включит сирену. 
        4. Персонализированное окружение. 
        Слаженная работа домашней инфраструктуры создаёт персонализированное 
        окружение для каждого обитателя.''')
        akt_label.setFont(QFont("Times", 12))
        self.b_akt = QPushButton("Назад")
        self.b_akt.clicked.connect(self.back_akt)
        akt_l.addWidget(akt_label, alignment = Qt.AlignLeft)
        akt_l.addWidget(self.b_akt, alignment = Qt.AlignCenter)
        self.g_akt.setLayout(akt_l)
        self.main_line.addWidget(self.g_akt, alignment = Qt.AlignLeft)
        self.g_akt.show()
    def back_akt(self):
        self.g_akt.hide()
        self.main_group.show()


    def button_theory_expansion1(self):
        linkTemplate = '<a href={0}>{1}</a>' #? Тоже для гиперссылки
        self.main_group.hide()
        self.g_button_theory1 = QGroupBox()
        self.g_button_theory1.setFixedSize(800, 500)
        self.g_button_theory1.setTitle("Датчик движения")
        layout_button_theory1 = QVBoxLayout()
        label_button_theory1_2 = QLabel('''Датчики движения испускают пучок инфракрасных лучей и улавливают их отражения от окру-
-жающих предметов. При последовательном прерывании нескольких лучей происходит сраба-
-тывание датчика. Независимо от способа крепления — на потолок или на стену, датчики дви-
-жения контролируют определенный сектор в 90–180° и имеют определенный диапазон рас-
-стояний срабатывания — обычно 5–10 м, максимум до 20 м.''')
        
        dl = QLabel(self)
        dlpixmap = QPixmap('dl.png')
        dl.setPixmap(dlpixmap)

        label_button_theory1_2.setFont(QFont("Times", 14))
        label_button_theory1_2_1 = HyperlinkLabel(self) #? Эта и следующая тоже для гипер ссылок
        label_button_theory1_2_1.setText(linkTemplate.format('www.dns-shop.ru/product/8b41a9c1ce9aed20', 'Датчик движения')) #! ссылка; что будет написано
        label_button_theory1_2_1.setFont(QFont("Times", 10))
        self.back__button_theory1 = QPushButton("Назад")
        layout_button_theory1.addWidget(label_button_theory1_2, alignment = Qt.AlignLeft)
        layout_button_theory1.addWidget(dl, alignment = Qt.AlignCenter)
        layout_button_theory1.addWidget(label_button_theory1_2_1, alignment = Qt.AlignCenter)
        layout_button_theory1.addWidget(self.back__button_theory1, alignment = Qt.AlignCenter)
        self.g_button_theory1.setLayout(layout_button_theory1)
        self.back__button_theory1.clicked.connect(self.back_theory1)
        self.main_line.addWidget(self.g_button_theory1, alignment = Qt.AlignLeft)
        self.g_button_theory1.show()

    def back_theory1(self):
        self.g_button_theory1.hide()
        self.main_group.show()


    def button_theory_expansion2(self):
        linkTemplate = '<a href={0}>{1}</a>'
        self.main_group.hide()
        self.g_button_theory2 = QGroupBox()
        self.g_button_theory2.setFixedSize(800, 500)
        self.g_button_theory2.setTitle("Датчик вибрации")
        layout_button_theory2 = QVBoxLayout()
        label_button_theory2_2 = QLabel('''Датчик вибрации (удара) содержит акселерометры — электронные компоненты, реагирующие
на изменение ускорения. В зависимости от количества акселерометров в датчике, они могут 
различать воздействия: вибрации, удары и наклоны. ''')
        
        drv = QLabel(self)
        drvpixmap = QPixmap('drv.png')
        drv.setPixmap(drvpixmap)

        label_button_theory2_2.setFont(QFont("Times", 14))
        label_button_theory2_2_1 = HyperlinkLabel(self)
        label_button_theory2_2_1.setText(linkTemplate.format('www.dns-shop.ru/product/55d4b0a3426e3332', 'Датчик вибрации'))
        label_button_theory2_2_1.setFont(QFont("Times", 10))
        self.back__button_theory2 = QPushButton("Назад")
        layout_button_theory2.addWidget(label_button_theory2_2, alignment = Qt.AlignLeft)
        layout_button_theory2.addWidget(drv, alignment = Qt.AlignCenter)
        layout_button_theory2.addWidget(label_button_theory2_2_1, alignment = Qt.AlignCenter)
        layout_button_theory2.addWidget(self.back__button_theory2, alignment = Qt.AlignCenter)
        self.g_button_theory2.setLayout(layout_button_theory2)
        self.back__button_theory2.clicked.connect(self.back_theory2)
        self.main_line.addWidget(self.g_button_theory2, alignment = Qt.AlignLeft)
        self.g_button_theory2.show()

    def back_theory2(self):
        self.g_button_theory2.hide()
        self.main_group.show()


    def button_theory_expansion3(self):
        linkTemplate = '<a href={0}>{1}</a>'
        self.main_group.hide()
        self.g_button_theory3 = QGroupBox()
        self.g_button_theory3.setFixedSize(800, 500)
        self.g_button_theory3.setTitle("Датчики дыма")
        layout_button_theory3 = QVBoxLayout()
        label_button_theory3_2 = QLabel('''Датчик дыма содержит пару светодиод+фотодатчик и реагирует на изменение прозрачности воз-
-духа. Поэтому возможны ложные срабатывания датчика на пыль и на пар — имейте это в виду 
при выборе места установки. Датчики дыма используются в качестве элемента пожарной 
сигнализации. Их срабатывание, кроме стандартного оповещения пользователю, может давать 
командуна запуск модулей пожаротушения и звонок в пожарную службу. Датчики дыма 
часто оснащены локальной звуковой и световой сигнализацией для скорейшего привлечения 
внимания к произошедшему.''')
        
        dd = QLabel(self)
        ddpixmap = QPixmap('dd.png')
        dd.setPixmap(ddpixmap)

        label_button_theory3_2.setFont(QFont("Times", 14))
        label_button_theory3_2_1 = HyperlinkLabel(self)
        label_button_theory3_2_1.setText(linkTemplate.format('www.dns-shop.ru/product/f143cba028f1ed20', 'Датчик дыма'))
        label_button_theory3_2_1.setFont(QFont("Times", 10))
        self.back__button_theory3 = QPushButton("Назад")
        layout_button_theory3.addWidget(label_button_theory3_2, alignment = Qt.AlignLeft)
        layout_button_theory3.addWidget(dd, alignment = Qt.AlignCenter)
        layout_button_theory3.addWidget(label_button_theory3_2_1, alignment = Qt.AlignCenter)
        layout_button_theory3.addWidget(self.back__button_theory3, alignment = Qt.AlignCenter)
        self.g_button_theory3.setLayout(layout_button_theory3)
        self.back__button_theory3.clicked.connect(self.back_theory3)
        self.main_line.addWidget(self.g_button_theory3, alignment = Qt.AlignLeft)
        self.g_button_theory3.show()

    def back_theory3(self):
        self.g_button_theory3.hide()
        self.main_group.show()
    

    def button_theory_expansion4(self):
        linkTemplate = '<a href={0}>{1}</a>'
        self.main_group.hide()
        self.g_button_theory4 = QGroupBox()
        self.g_button_theory4.setFixedSize(800, 500)
        self.g_button_theory4.setTitle("Климатические датчики")
        layout_button_theory4 = QVBoxLayout()
        label_button_theory4_2 = QLabel('''Климатический датчик (термогигрометр) передает информацию о температуре и влаж-
-ности в месте установки. При этом отдельные датчики температуры или влажности 
встречаются редко. С помощью термогигрометров ведется контроль климатических условий в 
разных частях дома.Такие датчики помогают экономить электроэнергию и повышать комфорт-
-ность жилища, поддерживая нужную температуру и влажность там, где это нужно 
и когда это нужно. ''')
        label_button_theory4_2.setFont(QFont("Times", 14))
        label_button_theory4_2_1 = HyperlinkLabel(self)
        label_button_theory4_2_1.setText(linkTemplate.format('www.dns-shop.ru/product/db780eae64ef3332', 'Климатические датчики'))
        label_button_theory4_2_1.setFont(QFont("Times", 10))

        dv = QLabel(self)
        dvpixmap = QPixmap('dv.png')
        dv.setPixmap(dvpixmap)

        self.back__button_theory4 = QPushButton("Назад")
        layout_button_theory4.addWidget(label_button_theory4_2, alignment = Qt.AlignLeft)
        layout_button_theory4.addWidget(dv, alignment = Qt.AlignCenter)
        layout_button_theory4.addWidget(label_button_theory4_2_1, alignment = Qt.AlignCenter)
        layout_button_theory4.addWidget(self.back__button_theory4, alignment = Qt.AlignCenter)
        self.g_button_theory4.setLayout(layout_button_theory4)
        self.back__button_theory4.clicked.connect(self.back_theory4)
        self.main_line.addWidget(self.g_button_theory4, alignment = Qt.AlignLeft)
        self.g_button_theory4.show()

    def back_theory4(self):
        self.g_button_theory4.hide()
        self.main_group.show()


    def button_theory_expansion5(self):
        linkTemplate = '<a href={0}>{1}</a>'
        self.main_group.hide()
        self.g_button_theory5 = QGroupBox()
        self.g_button_theory5.setFixedSize(800, 500)
        self.g_button_theory5.setTitle("Датчик освещенности")
        layout_button_theory5 = QVBoxLayout()
        label_button_theory5_2 = QLabel('''Датчик измеряет уровень освещенности в месте установки и обычно используется 
для управления светильниками. Через систему умного дома, датчик может управлять 
диммером,поддерживая в комнате постоянный уровень освещенности независимо от 
яркости внешнего освещения.Такие датчики позволяют экономить электроэнергию, 
включая/выключая освещение в зависимости от времени суток. Датчики освещенности 
часто используются совместно с датчиками движения, при этом сигнал на включение 
ламп при возникновении движения в контролируемой зоне подается только в темное 
время суток. Некоторые датчики движения уже содержат в себе и датчик освещения.''')
        label_button_theory5_2.setFont(QFont("Times", 14))
        label_button_theory5_2_1 = HyperlinkLabel(self)
        label_button_theory5_2_1.setText(linkTemplate.format('www.dns-shop.ru/product/8b41a9c1ce9aed20', 'Датчик освещенности'))
        label_button_theory5_2_1.setFont(QFont("Times", 10))

        dl1 = QLabel(self)
        dlpixmap1 = QPixmap('dl.png')
        dl1.setPixmap(dlpixmap1)

        self.back__button_theory5 = QPushButton("Назад")
        layout_button_theory5.addWidget(label_button_theory5_2, alignment = Qt.AlignLeft)
        layout_button_theory5.addWidget(dl1, alignment = Qt.AlignCenter)
        layout_button_theory5.addWidget(label_button_theory5_2_1, alignment = Qt.AlignCenter)
        layout_button_theory5.addWidget(self.back__button_theory5, alignment = Qt.AlignCenter)
        self.g_button_theory5.setLayout(layout_button_theory5)
        self.back__button_theory5.clicked.connect(self.back_theory5)
        self.main_line.addWidget(self.g_button_theory5, alignment = Qt.AlignLeft)
        self.g_button_theory5.show()

    def back_theory5(self):
        self.g_button_theory5.hide()
        self.main_group.show()


    def button_theory_expansion6(self):
        linkTemplate = '<a href={0}>{1}</a>'
        self.main_group.hide()
        self.g_button_theory6 = QGroupBox()
        self.g_button_theory6.setFixedSize(800, 500)
        self.g_button_theory6.setTitle("Датчик открытия")
        layout_button_theory6 = QVBoxLayout()
        label_button_theory6_2 = QLabel('''Датчик открытия состоит из двух частей, плотно прилегающих друг к другу. При разнесении их
на некоторое расстояние, датчик срабатывает, передавая сигнал в центр управления.
Обычно датчики открытия используются в системах сигнализации, контролируя открытие 
дверей и окон. Также нередко использование датчика открытия окна для блокировки 
включения кондиционера.''')
        label_button_theory6_2.setFont(QFont("Times", 14))
        label_button_theory6_2_1 = HyperlinkLabel(self)
        label_button_theory6_2_1.setText(linkTemplate.format('www.dns-shop.ru/product/c460f1bace99ed20', 'Датчик открытия'))
        label_button_theory6_2_1.setFont(QFont("Times", 10))

        dp = QLabel(self)
        dppixmap = QPixmap('dp.png')
        dp.setPixmap(dppixmap)

        self.back__button_theory6 = QPushButton("Назад")
        layout_button_theory6.addWidget(label_button_theory6_2, alignment = Qt.AlignLeft)
        layout_button_theory6.addWidget(dp, alignment = Qt.AlignCenter)
        layout_button_theory6.addWidget(label_button_theory6_2_1, alignment = Qt.AlignCenter)
        layout_button_theory6.addWidget(self.back__button_theory6, alignment = Qt.AlignCenter)
        self.g_button_theory6.setLayout(layout_button_theory6)
        self.back__button_theory6.clicked.connect(self.back_theory6)
        self.main_line.addWidget(self.g_button_theory6, alignment = Qt.AlignLeft)
        self.g_button_theory6.show()

    def back_theory6(self):
        self.g_button_theory6.hide()
        self.main_group.show()
    

    def button_theory_expansion7(self):
        linkTemplate = '<a href={0}>{1}</a>'
        self.main_group.hide()
        self.g_button_theory7 = QGroupBox()
        self.g_button_theory7.setFixedSize(800, 500)
        self.g_button_theory7.setTitle("Датчик протечки")
        layout_button_theory7 = QVBoxLayout()
        label_button_theory7_2 = QLabel('''Датчик протечки содержит пару оголенных контактов в нижней части. При попадании воды 
внутрь датчика, между контактами начинает протекать ток, вызывая срабатывание. Совместное 
использование с умными розетками позволит при срабатывании датчика отключить стиральную 
машину или выключить насосную станцию, прекратив подачу воды. Более надежный вариант 
прекращения подачи воды при сработке датчика протечки — использование крана с электро-
-приводом. При установке его на ввод воды в квартиру и подключении к единой системе умного 
дома, датчик протечки предотвратит затопление независимо от того, где и как вода попала 
на пол.''')
        label_button_theory7_2.setFont(QFont("Times", 14))
        label_button_theory7_2_1 = HyperlinkLabel(self)
        label_button_theory7_2_1.setText(linkTemplate.format('www.dns-shop.ru/product/21c54733ce9aed20', 'Датчик протечки'))
        label_button_theory7_2_1.setFont(QFont("Times", 10))

        dpr = QLabel(self)
        dprpixmap = QPixmap('dpr.png')
        dpr.setPixmap(dprpixmap)

        self.back__button_theory7 = QPushButton("Назад")
        layout_button_theory7.addWidget(label_button_theory7_2, alignment = Qt.AlignLeft)
        layout_button_theory7.addWidget(dpr, alignment = Qt.AlignCenter)
        layout_button_theory7.addWidget(label_button_theory7_2_1, alignment = Qt.AlignCenter)
        layout_button_theory7.addWidget(self.back__button_theory7, alignment = Qt.AlignCenter)
        self.g_button_theory7.setLayout(layout_button_theory7)
        self.back__button_theory7.clicked.connect(self.back_theory7)
        self.main_line.addWidget(self.g_button_theory7, alignment = Qt.AlignLeft)
        self.g_button_theory7.show()

    def back_theory7(self):
        self.g_button_theory7.hide()
        self.main_group.show()
    

    def button_theory_expansion8(self):
        linkTemplate = '<a href={0}>{1}</a>'
        self.main_group.hide()
        self.g_button_theory8 = QGroupBox()
        self.g_button_theory8.setFixedSize(800, 500)
        self.g_button_theory8.setTitle("Датчик утечки газа")
        layout_button_theory8 = QVBoxLayout()
        label_button_theory8_2 = QLabel('''Датчик реагирует на наличие в воздухе опасных газов — горючих (метана, пропана) или угар-
-ного газа.В зависимости от конфигурации системы умного дома, может производиться перекры-
-тие газовой трубы, включение вытяжки или звонок в аврийную службу. Такие датчики часто 
снабжаются сиренами и световой сигнализацией — это позволяет ускорить обнаружение
утечки газа.''')
        label_button_theory8_2.setFont(QFont("Times", 14))
        label_button_theory8_2_1 = HyperlinkLabel(self)
        label_button_theory8_2_1.setText(linkTemplate.format('www.dns-shop.ru/product/bcaeb4c555afed20', 'Датчик утечки газа'))
        label_button_theory8_2_1.setFont(QFont("Times", 10))

        du = QLabel(self)
        dupixmap = QPixmap('du.png')
        du.setPixmap(dupixmap)

        self.back__button_theory8 = QPushButton("Назад")
        layout_button_theory8.addWidget(label_button_theory8_2, alignment = Qt.AlignLeft)
        layout_button_theory8.addWidget(du, alignment = Qt.AlignCenter)
        layout_button_theory8.addWidget(label_button_theory8_2_1, alignment = Qt.AlignCenter)
        layout_button_theory8.addWidget(self.back__button_theory8, alignment = Qt.AlignCenter)
        self.g_button_theory8.setLayout(layout_button_theory8)
        self.back__button_theory8.clicked.connect(self.back_theory8)
        self.main_line.addWidget(self.g_button_theory8, alignment = Qt.AlignLeft)
        self.g_button_theory8.show()

    def back_theory8(self):
        self.g_button_theory8.hide()
        self.main_group.show()