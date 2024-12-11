from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class PatternWindow(QWidget):
    def __init__(self, *args, **qwargs):
        super().__init__(*args, **qwargs)
        self.parent_window = args[0]
        self.initUI()
    def initUI(self):
        self.main_line = QVBoxLayout()
        self.main_group = QGroupBox()
        self.button_theory1 = QPushButton("Из чего состоит умный дом")
        self.button_theory1.setFont(QFont("Times", 12))
        self.button_theory1.setFixedSize(325, 45)
        self.button_theory2 = QPushButton("Как добавлять устройства") 
        self.button_theory2.setFont(QFont("Times", 12))
        self.button_theory2.setFixedSize(325, 45)
        self.button_theory5 = QPushButton("Как добавлять СТОРОННИЕ устройства") 
        self.button_theory5.setFont(QFont("Times", 12))
        self.button_theory5.setFixedSize(325, 45)
        self.button_theory3 = QPushButton("Как создавать сценарии")
        self.button_theory3.setFont(QFont("Times", 12))
        self.button_theory3.setFixedSize(325, 45)
        self.button_theory4 = QPushButton("Коротко: как настроить умный дом Яндекса")
        self.button_theory4.setFont(QFont("Times", 12))
        self.button_theory4.setFixedSize(325, 45)
        self.button_back = QPushButton("Назад")


        pusto1 = QHBoxLayout()
        pusto4 = QHBoxLayout()
        a1 = QLabel(" ")
        a4 = QLabel(" ")
        pusto1.addWidget(a1, alignment = Qt.AlignCenter)
        pusto4.addWidget(a4, alignment = Qt.AlignCenter)
    

        main_layout_group1 = QHBoxLayout()
        main_layout_group2 = QHBoxLayout()
        main_layout_group3 = QVBoxLayout()

        main_layout_group3.addLayout(pusto1)
        main_layout_group3.addLayout(main_layout_group1)
        main_layout_group3.addLayout(pusto4)
        main_layout_group3.addLayout(main_layout_group2)
        main_layout_group1.addWidget(self.button_theory1, alignment = Qt.AlignLeft)
        main_layout_group1.addWidget(self.button_theory2, alignment = Qt.AlignLeft)
        main_layout_group2.addWidget(self.button_theory5, alignment = Qt.AlignLeft)
        main_layout_group2.addWidget(self.button_theory3, alignment = Qt.AlignLeft)
        main_layout_group3.addWidget(self.button_theory4, alignment = Qt.AlignCenter)
        main_layout_group3.addWidget(self.button_back, alignment = Qt.AlignCenter)
        self.main_group.setLayout(main_layout_group3)
        self.main_group.setTitle("Как настроить умный дом")
        self.main_group.setFixedSize(800, 500)
        self.setLayout(self.main_line)
        ne_main_line = QHBoxLayout()
        self.main_line.addLayout(ne_main_line)
        ne_main_line.addWidget(self.main_group, alignment = Qt.AlignLeft)
        self.button_back.clicked.connect(self.back)
        self.button_theory1.clicked.connect(self.withis)
        self.button_theory2.clicked.connect(self.kdis)
        self.button_theory3.clicked.connect(self.msis)
        self.button_theory4.clicked.connect(self.muis)
        self.button_theory5.clicked.connect(self.rdis)
    def back(self):
        self.hide()
        self.parent_window.main_group1.show()


    def withis(self):
        self.main_group.hide()
        self.wi = QGroupBox()
        self.wi.setTitle("Из чего состоит умный дом")
        self.wi.setFixedSize(800, 500)
        wi_l = QVBoxLayout()
        wi_lab1 = QLabel('''В любой системе умного дома три основные составляющие:
        1. Умные устройства — управляются дистанционно и участвуют в сценариях.
        2. Сервер — обрабатывает запросы пользователя, передает их устройствам, «помнит» сценарии.
        3. Интерфейс — умная колонка или приложение на смартфоне, которые передают команды пользователя на сервер.''')
        wi_lab1.setFont(QFont("Times", 10))
        wi_lab2 = QLabel("В случае с автономными системами вроде Home Assistant все эти компоненты, включая сервер, \nнаходятся внутри дома. Более простым в использовании системам от Яндекса, Apple или Google почти для всего \nтребуется постоянное подключение к интернету:\nвашими лампочками и датчиками управляет внешний дата-центр. Это немного замедляет реакцию на команды, \nзато большинство «сложных» этапов настройки умного дома корпорация уже выполнила за вас.")
        wi_lab2.setFont(QFont("Times", 10))
        wi_lab3 = QLabel('''Вот что входит в самый простой набор для умного дома Яндекса:
        1. Приложение «Дом с Алисой» на смартфоне или страница «Устройства» в браузере на компьютере.
        2. Умная лампочка, розетка или другое устройство из списка совместимых.''')
        wi_lab3.setFont(QFont("Times", 10))
        wi_l.addWidget(wi_lab1, alignment = Qt.AlignLeft) 
        wi_l.addWidget(wi_lab2, alignment = Qt.AlignLeft)
        wi_l.addWidget(wi_lab3, alignment = Qt.AlignLeft)
        self.wi_back = QPushButton("Назад")
        wi_l.addWidget(self.wi_back, alignment = Qt.AlignCenter)
        self.main_line.addWidget(self.wi, alignment = Qt.AlignLeft)
        self.wi_back.clicked.connect(self.back_wi)
        self.wi.setLayout(wi_l)
        self.wi.show()
    def back_wi(self):
        self.wi.hide()
        self.main_group.show()


    def kdis(self):
        self.main_group.hide()
        self.kd = QGroupBox()
        self.kd.setTitle("Как добавлять устройства")
        self.kd.setFixedSize(800, 500)
        kd_l = QVBoxLayout()
        kd_lab1 = QLabel('''Все умные устройства, которые вы собираетесь использовать, нужно добавлять через «Дом с Алисой». 
Они бывают трех видов:
        1. Устройства Яндекса подключаются напрямую в приложении. 
        Нужно нажать «+» в правом верхнем углу и следовать инструкциям.
        2. Гаджеты сторонних фирм вроде Xiaomi нужно сначала активировать, 
        а потом связать аккаунты производителя устройства и Яндекса.
        3. Сторонние датчики, лампочки и выключатели с протоколом Zigbee привязываются к устройству-хабу, 
        а не к аккаунту напрямую. Если хабом выступает Станция Миди, Станция Дуо или Станция Дуо Макс, 
        то процесс примерно такой же, как с устройствами от Яндекса.''')
        kd_lab1.setFont(QFont("Times", 10))
        kd_lab2 = QLabel('''Умные устройства Яндекса подключаются проще всего — к аккаунту Яндекса через домашнюю сеть Wi-Fi. 
Также их проще всего выбрать: точно не нужно переживать о совместимости. 
Вот, например, как подключить лампочку Яндекса:
        1. Откройте приложение и нажмите «+».
        2. Выберите «Устройства Яндекса» и соответствующую категорию.
        3. Следуйте инструкции на экране: устройство нужно перевести в режим сопряжения, пощелкав выключателем 
        или зажав специальную кнопку на корпусе.
        4. Выберите сеть Wi-Fi. Большинство устройств совместимы только со старым медленным стандартом 2,4 ГГц 
        — это даже к лучшему, потому что так они не помешают ноутбукам и смартфонам в «быстрой» сети 5 ГГц.
        5. Дождитесь обнаружения устройства, иногда это занимает много времени. Когда все будет готово, 
        придумайте для лампочки уникальное запоминающееся имя, задайте для нее комнату и конкретный дом. 
        Называя приборы, лучше не давать им те же имена, что и у комнат, чтобы система не путалась.''')
        kd_lab2.setFont(QFont("Times", 10))
        kd_l.addWidget(kd_lab1, alignment = Qt.AlignLeft) 
        kd_l.addWidget(kd_lab2, alignment = Qt.AlignLeft) 
        self.kd_backend = QPushButton("Назад")
        self.main_line.addWidget(self.kd, alignment = Qt.AlignLeft)
        self.kd_backend.clicked.connect(self.kd_back)
        kd_l.addWidget(self.kd_backend, alignment = Qt.AlignCenter)
        self.kd.setLayout(kd_l)
        self.kd.show()
    def kd_back(self):
        self.kd.hide()
        self.main_group.show()
    
    def rdis(self):
        self.main_group.hide()
        self.rd = QGroupBox()
        self.rd.setTitle("Как добавлять СТОРОННИЕ устройства")
        self.rd.setFixedSize(800, 500)
        rd_l = QVBoxLayout()
        rd_lab1 = QLabel('''Сторонние устройства требуют немного больше времени. Сначала их нужно добавить в отдельное приложение 
от производителя, а потом объединить аккаунты с Яндексом. Все устройства одной фирмы добавляются разом, 
повторно подключать их по одному не нужно.''')
        rd_lab2 = QLabel('''У такого подхода есть плюс: Яндексу все равно, для какого региона произведены ваши устройства. Например, 
робот-пылесос куплен на «Алиэкспрессе» и предназначен для Китая, а увлажнитель — для России. В приложении 
Mi Home они одновременно не отображаются — чтобы добавить и пользоваться ими, приходится переключаться 
между разными регионами в настройках приложения. Но после синхронизации в «Доме с Алисой» они доступны.''')
        rd_lab3 = QLabel('''Вот как добавить стороннее устройство на примере увлажнителя Xiaomi:
        1. Скачайте фирменное приложение — в данном случае Mi Home.
        2. Создайте аккаунт или войдите в существующий. Запомните данные для входа, они скоро понадобятся снова.
        3. Подключите устройство к розетке и включите его.
        4. Нажмите «+» в верхнем правом углу и нажмите на кнопку «Добавить устройство».
        5. Если устройство само перешло в режим подключения, оно отобразится наверху экрана. Если нет — промотайте вниз, 
        найдите нужную модель и следуйте инструкции.
        6. Когда устройство добавлено, назовите его как-нибудь или не меняйте ничего: в «Доме с Алисой» все равно придется заново задать 
        название и расположение устройства.
        7. Добавьте все гаджеты одного бренда и закройте приложение.
        8. Откройте «Дом с Алисой», нажмите «+» и выберите «Устройство умного дома». Листайте вниз, пока не увидите 
        логотип нужного производителя.
        9. Нажмите на логотип — откроется окно для объединения аккаунтов. Введите логин и пароль, которые использовали в пункте 2, 
        проставьте галочки на все запросы разрешений.
        10. Готово — все устройства Xiaomi добавлены в умный дом Яндекса. Осталось только распределить их по комнатам, 
        дать новые названия и добавить в группы или сценарии.''')
        rd_lab1.setFont(QFont("Times", 10))
        rd_lab2.setFont(QFont("Times", 10))
        rd_lab3.setFont(QFont("Times", 10))
        rd_l.addWidget(rd_lab1, alignment = Qt.AlignLeft)
        rd_l.addWidget(rd_lab2, alignment = Qt.AlignLeft)
        rd_l.addWidget(rd_lab3, alignment = Qt.AlignLeft)
        self.rd_backend = QPushButton("Назад")
        self.main_line.addWidget(self.rd, alignment = Qt.AlignLeft)
        self.rd_backend.clicked.connect(self.rd_back)
        rd_l.addWidget(self.rd_backend, alignment = Qt.AlignCenter)
        self.rd.setLayout(rd_l)
        self.rd.show()
    def rd_back(self):
        self.rd.hide()
        self.main_group.show()

    def msis(self):
        self.main_group.hide()
        self.ms = QGroupBox()
        self.ms.setTitle("Как создавать сценарии")
        self.ms.setFixedSize(800, 500)
        ms_l = QVBoxLayout()
        ms_lab1 = QLabel('''Управлять каждой отдельной лампочкой или розеткой голосом удобно. 
Но суть умного дома в том, чтобы устройства работали сообща и даже контролировали друг друга. 
Для этого нужны 
сценарии — заранее созданные программы, которые состоят из двух частей:
        1. Условие — заданное время, срабатывание датчика или определенная голосовая команда.
        2. Результат — включение или выключение устройств, проигрывание музыки, изменение настроек освещения и т.д.
Например: уходя из дома, я прощаюсь с колонкой в прихожей «Алиса, я ушел». 
После этого она выключает весь свет в квартире кроме гирлянды на окне кухни. 
Гирляндой управляет умная розетка — она запрограммирована включаться в момент заката солнца 
и выключаться в два часа ночи, когда все уже точно спят.''')
        ms_lab1.setFont(QFont("Times", 10))
        ms_lab2 = QLabel('''Как создать сценарий:
        1. Нажмите на «+» в главном меню и выберите «Сценарии».
        2. Задайте уникальное название и заполните пункты «Если» и «Тогда».
        3. Условия стоит указывать максимально подробно, чтобы избежать ложных срабатываний. 
        Например, для включения света по датчику отметьте не только обнаружение движения, 
        но и минимальную освещенность помещения, чтобы лампы не загорались днем.
        4. В ответ на условие может происходить сколько угодно событий: 
        часть лампочек включатся, часть — выключатся, еще некоторые сменят цвет или яркость. 
        Одновременно робот-пылесос начнет уборку, а колонки во всей квартире 
        начнут хором исполнять «Богемскую рапсодию» и заведут будильник на пять утра следующего дня. 
        Именно такая комбинация кажется бесполезной, но хорошо иллюстрирует возможности.''')
        ms_lab2.setFont(QFont("Times", 10))
        self.ms_backend = QPushButton("Назад")
        self.main_line.addWidget(self.ms, alignment = Qt.AlignLeft)
        self.ms_backend.clicked.connect(self.ms_back)
        ms_l.addWidget(ms_lab1, alignment = Qt.AlignLeft)
        ms_l.addWidget(ms_lab2, alignment = Qt.AlignLeft)
        ms_l.addWidget(self.ms_backend, alignment = Qt.AlignCenter)
        self.ms.setLayout(ms_l)
        self.ms.show()
    def ms_back(self):
        self.ms.hide()
        self.main_group.show()

    def muis(self):
        self.main_group.hide()
        self.mu = QGroupBox()
        self.mu.setTitle("Коротко: как настроить умный дом Яндекса")
        self.mu.setFixedSize(800, 500)
        mu_l = QVBoxLayout()
        mu_lab1 = QLabel('''        1. Начните с простого: использовать умные лампочки и розетки можно даже без колонки с Алисой — со смартфона или компьютера.
        2. Самое очевидное применение умного дома — освещение. 
        Выключать все лампы одной командой удобно, и не придется переживать на работе, что забыли где-то что-то погасить.
        3. Для более продвинутой системы запаситесь датчиками. 
        Датчики движения и освещения помогут полностью автоматизировать освещение, 
        а умный термометр-гигрометр будет включать увлажнитель воздуха и кондиционер по мере необходимости.
        4. Умный дом повышает безопасность: датчик протечки и накладки на вентили перекроют воду в случае аварии, 
        а умный замок пришлет уведомление, если вы ушли из дома, забыв его закрыть. 
        Если пользуетесь утюгом — можно включать его в умную розетку, 
        чтобы дистанционно выключить в случае чего.
        5. Умный дом Яндекса сильно зависит от подключения к интернету. 
        Если забудете оплатить ежемесячный тариф или засбоит роутер — многие устройства перестанут работать. 
        Новые модели вроде Станции Миди управляют устройствами Zigbee и без интернета, 
        но этот протокол поддерживают далеко не все умные гаджеты.''')
        mu_lab1.setFont(QFont("Times", 10))
        self.mu_backend = QPushButton("Назад")
        self.main_line.addWidget(self.mu, alignment = Qt.AlignLeft)
        self.mu_backend.clicked.connect(self.mu_back)
        mu_l.addWidget(mu_lab1, alignment = Qt.AlignLeft)
        mu_l.addWidget(self.mu_backend, alignment = Qt.AlignCenter)
        self.mu.setLayout(mu_l)
        self.mu.show()
    def mu_back(self):
        self.mu.hide()
        self.main_group.show()

