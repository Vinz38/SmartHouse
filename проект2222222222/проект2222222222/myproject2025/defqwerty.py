
#!button.setGeometry(200, 150, 100, 40)



class HyperlinkLabel(QLabel): #? Гипер ссылки
    def __init__(self, parent=None):
        super().__init__()
        self.setStyleSheet('font-size: 20px')
        self.setOpenExternalLinks(True)
        self.setParent(parent)
    
    linkTemplate = '<a href={0}>{1}</a>' #? Тоже для гиперссылки
    label_button_theory1_2_1 = HyperlinkLabel(self) #? Эта и следующая тоже для гипер ссылок
    label_button_theory1_2_1.setText(linkTemplate.format('www.dns-shop.ru/product/8b41a9c1ce9aed20', 'Датчик движения')) #! ссылка; что будет написано


label = QLabel(self)
pixmap = QPixmap('image.png')
label.setPixmap(pixmap) #! ВСТАВКА КАРТИНОК