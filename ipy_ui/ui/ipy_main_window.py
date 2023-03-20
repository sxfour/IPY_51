from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 400)

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

        self.pushButton_7 = QtWidgets.QPushButton(self.page_3)

        font = QtGui.QFont()
        font.setPointSize(10)

        self.pushButton_7.setFont(font)
        self.pushButton_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setObjectName("pushButton_7")

        self.verticalLayout_3.addWidget(self.pushButton_7)

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

        self.pushButton_4.setText(_translate("MainWindow", "Поиск"))

        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "База данных"))

        self.pushButton_6.setText(_translate("MainWindow", "Создать тикет"))

        self.pushButton_7.setText(_translate("MainWindow", "Обращения"))

        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "Помощь"))

        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Для поиска введите название организации или ИП"))


from static import resource_rc
