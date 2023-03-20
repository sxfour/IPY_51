from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):

    def __init__(self):
        self.label = None
        self.label_0 = None
        self.label_1 = None
        self.verticalLayout = None

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 200)

        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label_0 = QtWidgets.QLabel(Form)
        self.label_0.setEnabled(True)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)

        self.label_0.setFont(font)
        self.label_0.setObjectName("label_0")
        self.label_0.setAlignment(QtCore.Qt.AlignLeft)

        self.verticalLayout.addWidget(self.label_0)

        self.label_1 = QtWidgets.QLabel(Form)
        self.label_1.setEnabled(False)

        font = QtGui.QFont()
        font.setPointSize(12)

        self.label_1.setFont(font)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")

        self.verticalLayout.addWidget(self.label_1)

        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(False)

        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)

        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight)
        self.label.setObjectName("label")

        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate

        Form.setWindowTitle(_translate("Form", "Form"))

        self.label_0.setText(_translate("Form", "Поиск абонентов происходит по ключевым словам.\n"
                                                "Для поиска введите ключевое слово в строку.\n"
                                                "Например : ООО \"Артик-энерго\"\n"
                                                "\n"
                                                "Успешный ответ будет содержать все связанные таблицы и данные с этой "
                                                "организацией.\n"
                                                "Если нужно вывести все ИП или ООО, формируем запрос точно так же.\n"
                                                "Например: ИП\n\n\n"
                                                "В вкладке 'База данных' -> 'Абоненты', находится список всех "
                                                "действующих абонетов.\n\n\n"
                                                "Для редактирования абонента/абонентов, следует:\n\n"
                                                "\t1. Нажать кнопку 'Разрешить редактирование' в окне 'Абоненты'.\n"
                                                "\t2. Выбрать ячейку (двойным щелчком) которую нужно изменить, "
                                                "отредактировать.\n"
                                                "\t3. После редактирования нажать 'Сохранить изменения', далее\n "
                                                "\t'Разрешить редактирование', чтобы выйти из режима редактирования.\n"))

        # self.label_1.setText(_translate("Form", "Пустая страница"))

        self.label.setText(_translate("Form", "dev by sxfour"))
