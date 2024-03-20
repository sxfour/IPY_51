# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import (
    QIcon, QBrush, QColor
)


# Основная форма.
class UI_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 470)

        # Иконка основного окна
        MainWindow.setWindowIcon(QtGui.QIcon('ui/ico_main/ico.png'))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(0)
        self.splitter.setObjectName("splitter")

        self.menu_widget = QtWidgets.QWidget(self.splitter)
        self.menu_widget.setMinimumSize(QtCore.QSize(140, 150))

        font = QtGui.QFont()
        font.setPointSize(10)

        self.menu_widget.setFont(font)
        self.menu_widget.setStyleSheet("")
        self.menu_widget.setObjectName("menu_widget")

        self.gridLayout = QtWidgets.QGridLayout(self.menu_widget)
        self.gridLayout.setContentsMargins(4, 5, 4, 5)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")

        self.toolBox = QtWidgets.QToolBox(self.menu_widget)
        self.toolBox.setEnabled(True)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        self.toolBox.setFont(font)
        self.toolBox.setStyleSheet("#toolBox::tab {\n"
                                   "    padding-left:5px;\n"
                                   "    text-align:left;\n"
                                   "    border-radius: 5px;\n"
                                   "}\n"
                                   "\n"
                                   "#toolBox::tab:hover {\n"
                                   "    background-color: rgb(152, 207, 255);\n"
                                   "    font-size: 15px;\n"
                                   "}\n"
                                   "#toolBox::tab:selected {\n"
                                   "    background-color: rgb(152, 207, 255);\n"
                                   "    font-size: 15px;\n"
                                   "}\n"
                                   "\n"
                                   "#toolBox QPushButton {\n"
                                   "    padding:5px 0px 5px 20px;\n"
                                   "    text-align:left;\n"
                                   "    border-radius: 5px;\n"
                                   "}\n"
                                   "\n"
                                   "#toolBox QPushButton:hover {\n"
                                   "    background-color: #85C1E9;\n"
                                   "}\n"
                                   "\n"
                                   "#toolBox QPushButton:checked {\n"
                                   "    background-color: rgb(176, 221, 255);\n"
                                   "}")
        self.toolBox.setObjectName("toolBox")

        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 132, 347))

        font = QtGui.QFont()
        font.setPointSize(8)

        self.page.setFont(font)
        self.page.setStyleSheet("")
        self.page.setObjectName("page")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")

        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setEnabled(True)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)

        self.pushButton.setFont(font)
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("")
        self.pushButton.setCheckable(True)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QtWidgets.QPushButton(self.page)

        font = QtGui.QFont()
        font.setPointSize(10)

        self.pushButton_2.setFont(font)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setObjectName("pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        spacerItem = QtWidgets.QSpacerItem(20, 410, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.verticalLayout.addItem(spacerItem)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/menu.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.toolBox.addItem(self.page, icon, "")

        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 132, 347))
        self.page_2.setObjectName("page_2")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.page_2)

        font = QtGui.QFont()
        font.setPointSize(10)

        self.pushButton_3.setFont(font)
        self.pushButton_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setObjectName("pushButton_3")

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QtWidgets.QPushButton(self.page_2)

        font = QtGui.QFont()
        font.setPointSize(10)

        self.pushButton_4.setFont(font)
        self.pushButton_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setObjectName("pushButton_3")

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.pushButtonAddConnection = QtWidgets.QPushButton(self.page_2)

        font = QtGui.QFont()
        font.setPointSize(10)

        self.pushButtonAddConnection.setFont(font)
        self.pushButtonAddConnection.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonAddConnection.setCheckable(True)
        self.pushButtonAddConnection.setObjectName("pushButtonAddConnection")

        self.verticalLayout_2.addWidget(self.pushButtonAddConnection)

        spacerItem1 = QtWidgets.QSpacerItem(20, 380, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(spacerItem1)

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/database.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.toolBox.addItem(self.page_2, icon1, "")

        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 132, 347))
        self.page_3.setObjectName("page_3")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.pushButton_6 = QtWidgets.QPushButton(self.page_3)

        font = QtGui.QFont()
        font.setPointSize(10)

        self.pushButton_6.setFont(font)
        self.pushButton_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setObjectName("pushButton_6")

        self.verticalLayout_3.addWidget(self.pushButton_6)

        # self.pushButton_7 = QtWidgets.QPushButton(self.page_3)
        #
        # font = QtGui.QFont()
        # font.setPointSize(10)
        #
        # self.pushButton_7.setFont(font)
        # self.pushButton_7.setFocusPolicy(QtCore.Qt.NoFocus)
        # self.pushButton_7.setCheckable(True)
        # self.pushButton_7.setObjectName("pushButton_7")
        #
        # self.verticalLayout_3.addWidget(self.pushButton_7)

        spacerItem2 = QtWidgets.QSpacerItem(20, 410, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(spacerItem2)

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/help.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.toolBox.addItem(self.page_3, icon2, "")

        self.gridLayout.addWidget(self.toolBox, 0, 0, 1, 1)

        self.main_widget = QtWidgets.QWidget(self.splitter)
        self.main_widget.setObjectName("main_widget")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.main_widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.tabWidget = QtWidgets.QTabWidget(self.main_widget)
        self.tabWidget.setStyleSheet("#tabWidget {\n"
                                     "    background-color: #ffff;\n"
                                     "}\n"
                                     "\n"
                                     "QTabBar::close-button {\n"
                                     "    margin-left: 1px;\n"
                                     "    image: url(:/icons/icons/exit.ico)\n"
                                     "}\n"
                                     "\n"
                                     "QTabBar::close-button:hover {\n"
                                     "    border-radius: 6px;\n"
                                     "    background-color: rgb(151, 205, 255);\n"
                                     "    image: url(:/icons/icons/exit.ico);\n"
                                     "}")
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName("tabWidget")

        self.gridLayout_2.addWidget(self.tabWidget, 2, 0, 1, 1)

        self.search_widget = QtWidgets.QWidget(self.main_widget)
        self.search_widget.setStyleSheet("#search_widget {\n"
                                         "    background-color: rgb(220, 220, 220);\n"
                                         "}\n"
                                         "#pushButton_8 {\n"
                                         "    padding:5px 5px;\n"
                                         "    border-radius: 5px;\n"
                                         "}\n"
                                         "\n"
                                         "#pushButton_8 {\n"
                                         "    padding-left: 10px;\n"
                                         "}")
        self.search_widget.setObjectName("search_widget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.search_widget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButton_8 = QtWidgets.QPushButton(self.search_widget)
        self.pushButton_8.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_8.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_8.setStyleSheet("#pushButton_8:hover {\n"
                                        "    background-color: #85C1E9;\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_8:pressed {\n"
                                        "    background-color: rgb(176, 221, 255);\n"
                                        "}")
        self.pushButton_8.setText("")

        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/left_arrow.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/right_arrow.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)

        self.pushButton_8.setIcon(icon3)
        self.pushButton_8.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setObjectName("pushButton_8")

        self.horizontalLayout.addWidget(self.pushButton_8)

        spacerItem3 = QtWidgets.QSpacerItem(128, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout.addItem(spacerItem3)

        self.search_frame = QtWidgets.QFrame(self.search_widget)
        self.search_frame.setMinimumSize(QtCore.QSize(550, 30))
        self.search_frame.setMaximumSize(QtCore.QSize(850, 30))

        font = QtGui.QFont()
        font.setPointSize(10)

        self.search_frame.setFont(font)
        self.search_frame.setStyleSheet("#search_frame {\n"
                                        "    border:  2px solid rgb(220, 220, 220);;\n"
                                        "    border-radius: 10px;\n"
                                        "    background-color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "\n"
                                        "#search_btn {\n"
                                        "    padding:5px 5px;\n"
                                        "    border-radius: 15px;\n"
                                        "}\n"
                                        "\n"
                                        "#search_btn:pressed {\n"
                                        "    padding-left: 10px;\n"
                                        "}")
        self.search_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.search_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.search_frame.setObjectName("search_frame")

        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.search_frame)
        self.horizontalLayout_10.setContentsMargins(15, 0, 5, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")

        self.lineEdit = QtWidgets.QLineEdit(self.search_frame)

        font = QtGui.QFont()
        font.setPointSize(10)

        self.lineEdit.setFont(font)
        self.lineEdit.setFrame(False)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")

        self.horizontalLayout_10.addWidget(self.lineEdit)

        self.search_btn = QtWidgets.QPushButton(self.search_frame)
        self.search_btn.setStyleSheet("#search_btn:hover {\n"
                                      "    background-color: #85C1E9;\n"
                                      "    border-radius: 4px;\n"
                                      "}\n"
                                      "\n"
                                      "#search_btn:pressed {\n"
                                      "    background-color: rgb(176, 221, 255);\n"
                                      "    border-radius: 4px;\n"
                                      "}")
        self.search_btn.setText("")

        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/find_user.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.search_btn.setIcon(icon4)
        self.search_btn.setIconSize(QtCore.QSize(20, 20))
        self.search_btn.setObjectName("search_btn")

        self.horizontalLayout_10.addWidget(self.search_btn)

        self.horizontalLayout.addWidget(self.search_frame)

        spacerItem4 = QtWidgets.QSpacerItem(127, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout.addItem(spacerItem4)

        self.gridLayout_2.addWidget(self.search_widget, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(6)

        self.tabWidget.setCurrentIndex(-1)

        self.pushButton_8.toggled['bool'].connect(self.menu_widget.setHidden)  # type: ignore

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "ИПУ Тестирование"))

        self.pushButton.setText(_translate("MainWindow", "Статистика"))

        self.pushButton_2.setText(_translate("MainWindow", "Информация"))

        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Меню"))

        self.pushButton_3.setText(_translate("MainWindow", "Абоненты"))

        self.pushButton_4.setText(_translate("MainWindow", "Создать"))

        self.pushButtonAddConnection.setText(_translate("MainWindow", "Подключение"))

        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "База данных"))

        self.pushButton_6.setText(_translate("MainWindow", "Создать тикет"))

        # self.pushButton_7.setText(_translate("MainWindow", "Обращения"))

        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "Помощь"))

        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Для поиска введите название организации или ИП"))


# Окно статистики.
class UI_StatisticPage(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(400, 200)

        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")

        self.label_count_0 = QtWidgets.QLabel(Form)

        font = QtGui.QFont()
        font.setPointSize(10)

        self.label_count_0.setFont(font)
        self.label_count_0.setStyleSheet("#label_count_0:hover {\n"
                                         "    background-color: rgba(220, 220, 220, 255);\n"
                                         "}")
        self.label_count_0.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_count_0.setObjectName("label_count_0")

        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_count_0)

        self.label_count_1 = QtWidgets.QLabel(Form)

        font = QtGui.QFont()
        font.setPointSize(10)

        self.label_count_1.setFont(font)
        self.label_count_1.setStyleSheet("#label_count_1:hover {\n"
                                         "    \n"
                                         "    background-color: rgba(0, 170, 0, 100);\n"
                                         "}\n"
                                         "")
        self.label_count_1.setObjectName("label_count_1")

        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_count_1)

        self.label_count_2 = QtWidgets.QLabel(Form)
        self.label_count_2.setEnabled(True)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)

        self.label_count_2.setFont(font)
        self.label_count_2.setStyleSheet("#label_count_2:hover {\n"
                                         "    background-color: rgb(0, 80, 255, 100);\n"
                                         "}\n"
                                         "")
        self.label_count_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_count_2.setObjectName("label_count_2")

        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_count_2)

        self.label_count_3 = QtWidgets.QLabel(Form)
        self.label_count_3.setEnabled(True)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)

        self.label_count_3.setFont(font)
        self.label_count_3.setStyleSheet("#label_count_3:hover {\n"
                                         "    background-color: rgb(255, 0, 0, 100);\n"
                                         "}\n"
                                         "")
        self.label_count_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_count_3.setObjectName("label_count_3")

        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_count_3)

        font = QtGui.QFont()
        font.setPointSize(10)

        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(False)

        font = QtGui.QFont()
        font.setPointSize(12)

        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.label)

        self.label_ex = QtWidgets.QLabel(Form)
        self.label_ex.setEnabled(False)

        font = QtGui.QFont()
        font.setPointSize(12)

        self.label_ex.setFont(font)
        self.label_ex.setAlignment(QtCore.Qt.AlignLeft)
        self.label_ex.setObjectName("label_ex")

        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.label_ex)

        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate

        Form.setWindowTitle(_translate("Form", "Form"))


# Окно информации.
class UI_InfoPage(object):

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


# Окно абонентов.
class UI_SubscribersPage(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 400)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)

        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(False)

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)

        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.verticalLayout.addWidget(self.label)

        self.widget = QtWidgets.QWidget(Form)

        font = QtGui.QFont()
        font.setPointSize(10)

        self.widget.setFont(font)
        self.widget.setObjectName("widget")

        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")

        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)

        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setMinimumSize(QtCore.QSize(300, 22))
        self.comboBox.setMaximumSize(QtCore.QSize(900, 22))

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        self.comboBox.setFont(font)
        self.comboBox.setEditable(False)
        self.comboBox.setMaxVisibleItems(15)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")

        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)

        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMinimumSize(QtCore.QSize(200, 25))
        self.pushButton.setMaximumSize(QtCore.QSize(200, 25))

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setStyleSheet("")
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(False)
        self.pushButton.setObjectName("pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 5, 1, 1)

        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(200, 25))
        self.pushButton_2.setMaximumSize(QtCore.QSize(200, 25))
        self.pushButton_2.setObjectName("pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)

        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(200, 25))
        self.pushButton_3.setMaximumSize(QtCore.QSize(200, 25))
        self.pushButton_3.setObjectName("pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 0, 6, 1, 1)

        self.verticalLayout.addWidget(self.widget)

        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(18)
        self.tableWidget.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(1, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(2, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(3, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(4, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)
        item.setForeground(QBrush(QColor(27, 200, 0)))

        self.tableWidget.setHorizontalHeaderItem(5, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(6, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(7, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(8, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)
        item.setForeground(QBrush(QColor(0, 85, 255)))

        self.tableWidget.setHorizontalHeaderItem(9, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(10, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(11, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(12, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(13, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(14, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(15, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(16, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(17, item)

        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(Form)

        self.comboBox.setCurrentIndex(0)

        # Размерность ячеек сверху таблицы.
        self.tableWidget.horizontalHeader().resizeSection(0, 30)
        self.tableWidget.horizontalHeader().resizeSection(1, 90)
        self.tableWidget.horizontalHeader().resizeSection(3, 70)
        self.tableWidget.horizontalHeader().resizeSection(5, 200)
        self.tableWidget.horizontalHeader().resizeSection(6, 140)
        self.tableWidget.horizontalHeader().resizeSection(7, 120)
        self.tableWidget.horizontalHeader().resizeSection(8, 85)
        self.tableWidget.horizontalHeader().resizeSection(9, 140)
        self.tableWidget.horizontalHeader().resizeSection(10, 80)
        self.tableWidget.horizontalHeader().resizeSection(11, 85)

        # Выключенное состояние таблицы
        self.tableWidget.setEnabled(False)

        # Размер 0 для невидимости этой колонки в таблице, т.к она не нужна пользователю.
        self.tableWidget.horizontalHeader().resizeSection(17, 0)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate

        Form.setWindowTitle(_translate("Form", "Form"))

        self.label.setText(_translate("Form", "Список абонентов (режим просмотра)"))

        self.comboBox.setItemText(0, _translate("Form", "Показать всех абонентов"))

        self.pushButton.setText(_translate("Form", "Разрешить редактирование"))

        self.pushButton_2.setText(_translate("Form", "Сохранить абонентов в csv"))

        self.pushButton_3.setText(_translate("Form", "Сохранить изменения"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Дог."))

        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Марка"))

        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Заводской №"))

        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Пломба"))

        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Госпроверка"))

        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Наименование"))

        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Адрес"))

        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Площадь, кв.м"))

        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Тек. дата"))

        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Form", "Статус на тек. дату"))

        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Form", "За ?"))

        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("Form", "За ?"))

        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("Form", "За месяц Гкал"))

        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("Form", "За месяц м3"))

        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("Form", "Всего Гкал"))

        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("Form", "Всего м3"))

        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("Form", "Примечание"))

        item = self.tableWidget.horizontalHeaderItem(17)
        item.setText(_translate("Form", "Автоинкремент"))


# Окно поиска.
class UI_FindPage(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 400)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)

        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(False)

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)

        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.verticalLayout.addWidget(self.label)

        self.widget = QtWidgets.QWidget(Form)

        font = QtGui.QFont()
        font.setPointSize(10)

        self.widget.setFont(font)
        self.widget.setObjectName("widget")

        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")

        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)

        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMinimumSize(QtCore.QSize(200, 25))
        self.pushButton.setMaximumSize(QtCore.QSize(200, 25))

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setStyleSheet("")
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(False)
        self.pushButton.setObjectName("pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 5, 1, 1)

        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(270, 25))
        self.pushButton_2.setMaximumSize(QtCore.QSize(270, 25))
        self.pushButton_2.setObjectName("pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)

        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(200, 25))
        self.pushButton_3.setMaximumSize(QtCore.QSize(200, 25))
        self.pushButton_3.setObjectName("pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 0, 6, 1, 1)

        self.verticalLayout.addWidget(self.widget)

        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(18)
        self.tableWidget.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(1, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(2, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(3, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(4, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)
        item.setForeground(QBrush(QColor(27, 200, 0)))

        self.tableWidget.setHorizontalHeaderItem(5, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(6, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(7, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(8, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)
        item.setForeground(QBrush(QColor(0, 85, 255)))

        self.tableWidget.setHorizontalHeaderItem(9, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(10, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(11, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(12, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(13, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(14, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(15, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(16, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(17, item)

        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(Form)

        # Размерность шапки таблицы.
        self.tableWidget.horizontalHeader().resizeSection(0, 70)
        self.tableWidget.horizontalHeader().resizeSection(1, 90)
        self.tableWidget.horizontalHeader().resizeSection(3, 70)
        self.tableWidget.horizontalHeader().resizeSection(5, 200)
        self.tableWidget.horizontalHeader().resizeSection(6, 140)
        self.tableWidget.horizontalHeader().resizeSection(7, 120)
        self.tableWidget.horizontalHeader().resizeSection(9, 140)
        self.tableWidget.horizontalHeader().resizeSection(10, 170)
        self.tableWidget.horizontalHeader().resizeSection(11, 165)

        # Размер 0 для невидимости этой колонки в таблице, т.к она не нужна пользователю.
        self.tableWidget.horizontalHeader().resizeSection(17, 0)

        # Выключенное состояние таблицы
        self.tableWidget.setEnabled(False)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate

        Form.setWindowTitle(_translate("Form", "Form"))

        self.label.setText(_translate("Form", "Поиск по абонентам, найдено совпадений : 0 (режим просмотра}"))

        self.pushButton.setText(_translate("Form", "Разрешить редактирование"))

        self.pushButton_2.setText(_translate("Form", "Сохранить ключевых абонентов в csv"))

        self.pushButton_3.setText(_translate("Form", "Сохранить изменения"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Договор"))

        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Марка"))

        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Заводской №"))

        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Пломба"))

        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Госпроверка"))

        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Наименование"))

        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Адрес"))

        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Площадь, кв.м"))

        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Текущая дата"))

        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Form", "Статус на тек. дату"))

        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Form", "Показания за ?"))

        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("Form", "Показания за ?"))

        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("Form", "За месяц Гкал"))

        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("Form", "За месяц м3"))

        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("Form", "Всего Гкал"))

        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("Form", "Всего м3"))

        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("Form", "Примечание"))

        item = self.tableWidget.horizontalHeaderItem(17)
        item.setText(_translate("Form", "Автоинкремент"))


# Окно создать тикет.
class UI_CreateTicketPage(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 280)

        self.verticalLayout = QtWidgets.QGridLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")

        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setMinimumSize(QtCore.QSize(400, 25))
        self.comboBox.setMaximumSize(QtCore.QSize(500, 25))

        font = QtGui.QFont()
        font.setPointSize(10)

        self.comboBox.setFont(font)
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setEditable(False)
        self.comboBox.setMaxVisibleItems(15)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.verticalLayout.addWidget(self.comboBox)

        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setMinimumSize(QtCore.QSize(400, 100))
        self.textEdit.setMaximumSize(QtCore.QSize(500, 200))

        font = QtGui.QFont()
        font.setPointSize(10)

        self.textEdit.setFont(font)
        self.textEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textEdit.setObjectName("textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setFont(font)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 25))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate

        Form.setWindowTitle(_translate("Form", "Form"))

        self.comboBox.setCurrentText(_translate("Form", "При работе возникают окна с ошибками"))
        self.comboBox.setItemText(0, _translate("Form", "При работе возникают окна с ошибками"))
        self.comboBox.setItemText(1, _translate("Form", "Не могу разобраться с программой"))
        self.comboBox.setItemText(2, _translate("Form", "Нет соединения"))
        self.comboBox.setItemText(3, _translate("Form", "Не могу внести изменения в таблицу"))
        self.comboBox.setItemText(4, _translate("Form", "Показания неверны"))
        self.comboBox.setItemText(5, _translate("Form", "Отсутствуют некоторые элементы управления"))

        self.textEdit.setPlaceholderText(_translate("Form", "Опишите проблему, не более 100 символов"))

        self.pushButton.setText(_translate("Form", "Отправить"))


# Окно создать абонента.
class UI_CreatePage(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 400)
        Form.setMinimumSize(QtCore.QSize(1000, 400))
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)

        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")

        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.labelInfo = QtWidgets.QLabel(Form)
        self.labelInfo.setEnabled(False)

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)

        self.labelInfo.setFont(font)
        self.labelInfo.setStyleSheet("")
        self.labelInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelInfo.setObjectName("label")

        self.verticalLayout_2.addWidget(self.labelInfo)

        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(50, 50))
        self.widget_2.setObjectName("widget_2")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_4.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_4.setMaximumSize(QtCore.QSize(100, 25))

        font = QtGui.QFont()
        font.setPointSize(10)

        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.pushButtonPreffixCheck = QtWidgets.QPushButton(self.widget_2)
        self.pushButtonPreffixCheck.setMinimumSize(QtCore.QSize(200, 25))
        self.pushButtonPreffixCheck.setMaximumSize(QtCore.QSize(200, 25))

        font = QtGui.QFont()
        font.setPointSize(10)


        self.pushButtonPreffixCheck.setFont(font)
        self.pushButtonPreffixCheck.setObjectName("pushButtonPreffixCheck")
        self.pushButtonPreffixCheck.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.pushButtonPreffixCheck)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(spacerItem)

        self.labelInfo2 = QtWidgets.QLabel(self.widget_2)

        font = QtGui.QFont()
        font.setPointSize(10)

        self.labelInfo2.setFont(font)
        self.labelInfo2.setObjectName("labelInfo2")
        self.labelInfo2.setEnabled(True)

        self.horizontalLayout_2.addWidget(self.labelInfo2)

        self.spinBox = QtWidgets.QSpinBox(self.widget_2)
        self.spinBox.setMinimumSize(QtCore.QSize(40, 20))
        self.spinBox.setMaximumSize(QtCore.QSize(40, 20))

        font = QtGui.QFont()
        font.setPointSize(10)

        self.spinBox.setFont(font)
        self.spinBox.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(10)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setEnabled(True)

        self.horizontalLayout_2.addWidget(self.spinBox)

        spacerItem1 = QtWidgets.QSpacerItem(40, 5, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(spacerItem1)

        self.pushButtonEditTable = QtWidgets.QPushButton(self.widget_2)
        self.pushButtonEditTable.setMinimumSize(QtCore.QSize(200, 25))
        self.pushButtonEditTable.setMaximumSize(QtCore.QSize(200, 25))
        self.pushButtonEditTable.setCheckable(True)

        font = QtGui.QFont()
        font.setPointSize(10)

        self.pushButtonEditTable.setFont(font)
        self.pushButtonEditTable.setObjectName("pushButtonEditTable")

        self.horizontalLayout_2.addWidget(self.pushButtonEditTable)

        self.pushButtonAddAbonent = QtWidgets.QPushButton(self.widget_2)
        self.pushButtonAddAbonent.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButtonAddAbonent.setMaximumSize(QtCore.QSize(100, 25))

        font = QtGui.QFont()
        font.setPointSize(10)

        self.pushButtonAddAbonent.setFont(font)
        self.pushButtonAddAbonent.setObjectName("pushButtonAddAbonent")
        self.pushButtonAddAbonent.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.pushButtonAddAbonent)

        self.verticalLayout_2.addWidget(self.widget_2)

        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tableWidget.setAcceptDrops(False)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(17)
        self.tableWidget.setRowCount(1)

        # item = QtWidgets.QTableWidgetItem()
        #
        # self.tableWidget.setVerticalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(1, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(2, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(3, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(4, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(5, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(6, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(7, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(8, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(9, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(10, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(11, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(12, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(13, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(14, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(15, item)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(10)

        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(16, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.setEnabled(False)

        # Размерность ячеек сверху таблицы.
        self.tableWidget.horizontalHeader().resizeSection(0, 30)
        self.tableWidget.horizontalHeader().resizeSection(1, 90)
        self.tableWidget.horizontalHeader().resizeSection(3, 70)
        self.tableWidget.horizontalHeader().resizeSection(5, 200)
        self.tableWidget.horizontalHeader().resizeSection(6, 140)
        self.tableWidget.horizontalHeader().resizeSection(7, 120)
        self.tableWidget.horizontalHeader().resizeSection(8, 85)
        self.tableWidget.horizontalHeader().resizeSection(9, 140)
        self.tableWidget.horizontalHeader().resizeSection(10, 80)
        self.tableWidget.horizontalHeader().resizeSection(11, 85)

        self.verticalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate

        Form.setWindowTitle(_translate("Form", "Form"))

        self.labelInfo.setText(_translate("Form", "Создание абонентов (режим просмотра)"))

        self.pushButton_4.setText(_translate("Form", "Удалить"))

        self.pushButtonPreffixCheck.setText(_translate("Form", "Проверка синтаксиса"))

        self.labelInfo2.setText(_translate("Form", "Введите кол-во добавляемых абонентов:"))

        self.pushButtonEditTable.setText(_translate("Form", "Разрешить редактирование"))

        self.pushButtonAddAbonent.setText(_translate("Form", "Добавить"))

        # item = self.tableWidget.verticalHeaderItem(0)
        # item.setText(_translate("Form", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Дог."))

        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Марка"))

        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Заводской №"))

        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Пломба"))

        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Госпроверка"))

        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Наименование"))

        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Адрес"))

        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Плошадь, кв.м"))

        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Тек. дата"))

        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Form", "Статус на тек.дату"))

        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Form", "Показания за декабрь"))

        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("Form", "Показания за январь"))

        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("Form", "За месяц Гкал"))

        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("Form", "За месяц м3"))

        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("Form", "Всего Гкал"))

        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("Form", "Всего м3"))

        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("Form", "Примечание"))


# Окно настройки подключения к базе данных.
class UI_ConnectDatabasePage(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(750, 340)
        Form.setMinimumSize(QtCore.QSize(750, 340))
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))

        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setObjectName("verticalLayout")

        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")

        self.widget1 = QtWidgets.QWidget(self.widget)
        self.widget1.setGeometry(QtCore.QRect(6, 0, 715, 116))
        self.widget1.setObjectName("widget1")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.labelMain = QtWidgets.QLabel(self.widget1)
        self.labelMain.setEnabled(True)
        self.labelMain.setMaximumSize(QtCore.QSize(16777215, 24))

        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)

        self.labelMain.setFont(font)
        self.labelMain.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.labelMain.setObjectName("labelMain")

        self.verticalLayout_3.addWidget(self.labelMain)

        self.labelInformation = QtWidgets.QLabel(self.widget1)
        self.labelInformation.setMinimumSize(QtCore.QSize(700, 70))
        self.labelInformation.setMaximumSize(QtCore.QSize(700, 70))

        font = QtGui.QFont()
        font.setPointSize(10)

        self.labelInformation.setFont(font)
        self.labelInformation.setStyleSheet("background-color: rgb(255, 255, 0, 105);")
        self.labelInformation.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.labelInformation.setObjectName("labelInformation")

        self.verticalLayout_3.addWidget(self.labelInformation)

        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(6, 122, 715, 138))
        self.widget_2.setMinimumSize(QtCore.QSize(715, 138))
        self.widget_2.setMaximumSize(QtCore.QSize(715, 138))
        self.widget_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_2.setAutoFillBackground(False)
        self.widget_2.setObjectName("widget_2")

        self.lineEditHost = QtWidgets.QLineEdit(self.widget_2)
        self.lineEditHost.setGeometry(QtCore.QRect(71, 7, 250, 20))
        self.lineEditHost.setMinimumSize(QtCore.QSize(250, 20))
        self.lineEditHost.setMaximumSize(QtCore.QSize(100, 20))

        font = QtGui.QFont()
        font.setPointSize(10)

        self.lineEditHost.setFont(font)
        self.lineEditHost.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.lineEditHost.setText("")
        self.lineEditHost.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lineEditHost.setObjectName("lineEditHost")

        self.lineEditPort = QtWidgets.QLineEdit(self.widget_2)
        self.lineEditPort.setGeometry(QtCore.QRect(71, 33, 250, 20))
        self.lineEditPort.setMinimumSize(QtCore.QSize(250, 20))
        self.lineEditPort.setMaximumSize(QtCore.QSize(100, 20))

        font = QtGui.QFont()
        font.setPointSize(10)

        self.lineEditPort.setFont(font)
        self.lineEditPort.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.lineEditPort.setText("")
        self.lineEditPort.setObjectName("lineEditPort")

        self.lineEditDatabase = QtWidgets.QLineEdit(self.widget_2)
        self.lineEditDatabase.setGeometry(QtCore.QRect(71, 59, 250, 20))
        self.lineEditDatabase.setMinimumSize(QtCore.QSize(250, 20))
        self.lineEditDatabase.setMaximumSize(QtCore.QSize(100, 20))

        font = QtGui.QFont()
        font.setPointSize(10)

        self.lineEditDatabase.setFont(font)
        self.lineEditDatabase.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.lineEditDatabase.setObjectName("lineEditDatabase")

        self.lineEditUser = QtWidgets.QLineEdit(self.widget_2)
        self.lineEditUser.setGeometry(QtCore.QRect(71, 85, 250, 20))
        self.lineEditUser.setMinimumSize(QtCore.QSize(250, 20))
        self.lineEditUser.setMaximumSize(QtCore.QSize(100, 20))

        font = QtGui.QFont()
        font.setPointSize(10)

        self.lineEditUser.setFont(font)
        self.lineEditUser.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.lineEditUser.setInputMask("")
        self.lineEditUser.setText("")
        self.lineEditUser.setObjectName("lineEditUser")

        self.lineEditPassword = QtWidgets.QLineEdit(self.widget_2)
        self.lineEditPassword.setGeometry(QtCore.QRect(71, 111, 250, 20))
        self.lineEditPassword.setMinimumSize(QtCore.QSize(250, 20))
        self.lineEditPassword.setMaximumSize(QtCore.QSize(100, 20))

        font = QtGui.QFont()
        font.setPointSize(10)

        self.lineEditPassword.setFont(font)
        self.lineEditPassword.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")

        self.labelHost = QtWidgets.QLabel(self.widget_2)
        self.labelHost.setGeometry(QtCore.QRect(6, 7, 30, 20))
        self.labelHost.setMinimumSize(QtCore.QSize(0, 20))
        self.labelHost.setMaximumSize(QtCore.QSize(16777215, 16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)

        self.labelHost.setFont(font)
        self.labelHost.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelHost.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.labelHost.setObjectName("labelHost")

        self.labelPort = QtWidgets.QLabel(self.widget_2)
        self.labelPort.setGeometry(QtCore.QRect(6, 33, 28, 20))
        self.labelPort.setMinimumSize(QtCore.QSize(0, 20))

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        self.labelPort.setFont(font)
        self.labelPort.setObjectName("labelPort")

        self.labelDatabase = QtWidgets.QLabel(self.widget_2)
        self.labelDatabase.setGeometry(QtCore.QRect(6, 59, 57, 20))
        self.labelDatabase.setMinimumSize(QtCore.QSize(0, 20))

        font = QtGui.QFont()
        font.setPointSize(10)

        self.labelDatabase.setFont(font)
        self.labelDatabase.setObjectName("labelDatabase")

        self.labelUser = QtWidgets.QLabel(self.widget_2)
        self.labelUser.setGeometry(QtCore.QRect(6, 85, 30, 20))
        self.labelUser.setMinimumSize(QtCore.QSize(0, 20))

        font = QtGui.QFont()
        font.setPointSize(10)

        self.labelUser.setFont(font)
        self.labelUser.setObjectName("labelUser")

        self.labelPassword = QtWidgets.QLabel(self.widget_2)
        self.labelPassword.setGeometry(QtCore.QRect(6, 111, 59, 20))
        self.labelPassword.setMinimumSize(QtCore.QSize(0, 20))

        font = QtGui.QFont()
        font.setPointSize(10)

        self.labelPassword.setFont(font)
        self.labelPassword.setObjectName("labelPassword")

        self.textEdit = QtWidgets.QTextEdit(self.widget_2)
        self.textEdit.setGeometry(QtCore.QRect(363, 7, 341, 123))

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        font.setUnderline(False)

        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.textEdit.setReadOnly(True)
        self.textEdit.setOverwriteMode(False)
        self.textEdit.setObjectName("textEdit")

        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(6, 266, 721, 61))
        self.widget_3.setObjectName("widget_3")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButtonTestConn = QtWidgets.QPushButton(self.widget_3)

        font = QtGui.QFont()
        font.setPointSize(10)

        self.pushButtonTestConn.setFont(font)
        self.pushButtonTestConn.setObjectName("pushButtonTestConn")

        self.horizontalLayout.addWidget(self.pushButtonTestConn)

        self.pushButton = QtWidgets.QPushButton(self.widget_3)

        font = QtGui.QFont()
        font.setPointSize(10)

        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButtonSave = QtWidgets.QPushButton(self.widget_3)

        font = QtGui.QFont()
        font.setPointSize(10)

        self.pushButtonSave.setFont(font)
        self.pushButtonSave.setObjectName("pushButtonSave")

        self.horizontalLayout.addWidget(self.pushButtonSave)

        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate

        Form.setWindowTitle(_translate("Form", "Form"))

        self.labelMain.setText(_translate("Form", "Подключение к базе данных (PostgreSQL)"))

        self.labelInformation.setText(
            _translate("Form", "Для подключения к базе данных PostgreSQL заполните все поля.\n"
                               "- После сохранения параметров обязательно проверьте соединение "
                               "с базой данных (Тестировать соединение)\n"
                               "- Для безопасного редактирования выдавайте каждому пользователю отдельные"
                               " права на запись/редактирование\n"
                               "- После сохранения, файл конфигурации будет доступен в корневой директории"))

        self.lineEditHost.setPlaceholderText(_translate("Form", "localhost"))

        self.lineEditPort.setPlaceholderText(_translate("Form", "PostgreSQL default: 5432"))

        self.lineEditDatabase.setPlaceholderText(_translate("Form", "Название базы данных"))

        self.lineEditUser.setPlaceholderText(_translate("Form", "Имя пользователя"))

        self.lineEditPassword.setPlaceholderText(_translate("Form", "Пароль"))

        self.labelHost.setText(_translate("Form", "host:"))

        self.labelPort.setText(_translate("Form", "port:"))

        self.labelDatabase.setText(_translate("Form", "database:"))

        self.labelUser.setText(_translate("Form", "user:"))

        self.labelPassword.setText(_translate("Form", "password:"))

        self.textEdit.setPlaceholderText(_translate("Form", "Логирование тестовго соединения..."))

        self.pushButtonTestConn.setText(_translate("Form", "Тестировать соединение"))

        self.pushButton.setText(_translate("Form", "Поиск в локальной сети"))

        self.pushButtonSave.setText(_translate("Form", "Сохранить"))


# Окно авторизации.
class UI_LoginPage(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(530, 150)
        Form.setMinimumSize(QtCore.QSize(530, 150))
        Form.setMaximumSize(QtCore.QSize(530, 150))
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)

        Form.setWindowIcon(QtGui.QIcon('ui/ico_main/ico.png'))

        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")

        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")

        self.loginButton = QtWidgets.QPushButton(self.frame)
        self.loginButton.setMinimumSize(QtCore.QSize(80, 25))
        self.loginButton.setMaximumSize(QtCore.QSize(80, 25))
        self.loginButton.setAutoDefault(False)

        font = QtGui.QFont()
        font.setPointSize(10)

        self.loginButton.setFont(font)
        self.loginButton.setObjectName("loginButton")

        self.gridLayout.addWidget(self.loginButton, 3, 4, 1, 1)

        self.usernameEdit = QtWidgets.QLineEdit(self.frame)

        font = QtGui.QFont()
        font.setPointSize(10)

        self.usernameEdit.setFont(font)
        self.usernameEdit.setInputMask("")
        self.usernameEdit.setText("")
        self.usernameEdit.setMaxLength(100)
        self.usernameEdit.setFrame(False)
        self.usernameEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.usernameEdit.setObjectName("passwordEdit")
        self.usernameEdit.setFocus()

        self.gridLayout.addWidget(self.usernameEdit, 3, 1, 1, 1)

        self.rememberMe = QtWidgets.QCheckBox(self.frame)

        self.rememberMe.setEnabled(True)
        self.rememberMe.setMinimumSize(QtCore.QSize(83, 20))
        self.rememberMe.setMaximumSize(QtCore.QSize(80, 20))

        font = QtGui.QFont()
        font.setPointSize(9)

        self.rememberMe.setFont(font)
        self.rememberMe.setObjectName("rememberMe")

        self.gridLayout.addWidget(self.rememberMe, 3, 3, 1, 1)

        self.passwordEdit = QtWidgets.QLineEdit(self.frame)

        font = QtGui.QFont()
        font.setPointSize(10)

        self.passwordEdit.setFont(font)
        self.passwordEdit.setText("")
        self.passwordEdit.setMaxLength(100)
        self.passwordEdit.setFrame(False)
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.setObjectName("usernameEdit")
        self.passwordEdit.setEnabled(False)

        self.gridLayout.addWidget(self.passwordEdit, 3, 2, 1, 1)

        self.verticalLayout.addWidget(self.frame)

        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(True)

        font = QtGui.QFont()
        font.setPointSize(9)

        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.verticalLayout.addWidget(self.label)

        self.commandLinkButton = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton.setMinimumSize(QtCore.QSize(300, 38))
        self.commandLinkButton.setMaximumSize(QtCore.QSize(300, 38))

        font = QtGui.QFont()

        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)

        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton.setInputMethodHints(QtCore.Qt.ImhNone)
        self.commandLinkButton.setCheckable(False)
        self.commandLinkButton.setAutoDefault(False)
        self.commandLinkButton.setDefault(False)

        # self.commandLinkButton.setEnabled(False)
        self.commandLinkButton.setObjectName("commandLinkButton")

        self.verticalLayout.addWidget(self.commandLinkButton)

        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate

        Form.setWindowTitle(_translate("Form", "ИПУ Авторизация"))

        self.loginButton.setText(_translate("Form", "Войти"))

        self.usernameEdit.setPlaceholderText(_translate("Form", "Введите логин"))

        self.rememberMe.setText(_translate("Form", "Запомнить"))

        self.commandLinkButton.setText(_translate("Form", "Отправить запрос на регистрацию"))

        self.passwordEdit.setPlaceholderText(_translate("Form", "Введите пароль"))

        self.label.setText(_translate("Form", "*Для входа в приложение используйте данные,"
                                              " которые получили при регистрации"))


# Окно регистрации.
class UI_RegistrPage(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(400, 200)
        Form.setWindowIcon(QtGui.QIcon('ui/ico_main/ico.png'))
        Form.setMinimumSize(QtCore.QSize(400, 200))
        Form.setMaximumSize(QtCore.QSize(400, 200))

        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(25, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(350, 35))
        self.label_2.setMaximumSize(QtCore.QSize(350, 35))

        font = QtGui.QFont()

        font.setPointSize(12)
        font.setUnderline(False)

        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_2.setEnabled(False)

        self.verticalLayout.addWidget(self.label_2)

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setMinimumSize(QtCore.QSize(350, 25))
        self.lineEdit.setMaximumSize(QtCore.QSize(350, 25))

        font = QtGui.QFont()
        font.setPointSize(9)

        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(30)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(350, 25))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(350, 25))

        font = QtGui.QFont()

        font.setPointSize(9)

        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setMaxLength(30)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.pushButton = QtWidgets.QPushButton(Form)

        self.pushButton.setMinimumSize(QtCore.QSize(150, 25))
        self.pushButton.setMaximumSize(QtCore.QSize(150, 25))

        font = QtGui.QFont()
        font.setPointSize(10)

        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate

        Form.setWindowTitle(_translate("Form", "ИПУ Регистрация"))

        self.label_2.setText(_translate("Form", "Форма регистрации"))

        self.lineEdit.setPlaceholderText(_translate("Form", "Введите имя (только кириллица) (не более 30 символов)"))

        self.lineEdit_2.setPlaceholderText(_translate("Form", "Введите пароль (не более 30 символов)"))

        self.pushButton.setText(_translate("Form", "Отправить заявку"))


# Окно ошибки
def errorWindow(message, text):
    error = QMessageBox()
    error.setWindowIcon(QIcon('ui/ico_main/ico.png'))
    error.setWindowTitle('Ошибка')
    error.setText(text)
    error.setIcon(QMessageBox.Warning)
    error.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
    error.setDefaultButton(QMessageBox.Ok)
    error.setDetailedText('Details : {0}'.format(message))

    buttonCancel = error.button(QMessageBox.Cancel)

    buttonCancel.setText('Отмена')

    error.exec_()


# Окно ошибки поисковой строки.
def findErrorWindow(message, text):
    findError = QMessageBox()
    findError.setWindowIcon(QIcon('ui/ico_main/ico.png'))
    findError.setWindowTitle('Ошибка')
    findError.setText(text)
    findError.setIcon(QMessageBox.Critical)
    findError.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
    findError.setDefaultButton(QMessageBox.Ok)
    findError.setDetailedText('Details : {0}'.format(message))

    buttonCancel = findError.button(QMessageBox.Cancel)

    buttonCancel.setText('Отмена')

    findError.exec_()


# Окно успешно.
def successWindow(message):
    success = QMessageBox()
    success.setWindowIcon(QIcon('ui/ico_main/ico.png'))
    success.setWindowTitle('ИПУ Тестирование')
    success.setText(message)
    success.setIcon(QMessageBox.Information)
    success.setStandardButtons(QMessageBox.Ok)

    success.exec_()


# Байтовый тип иконок в формате .py
from static import icons
