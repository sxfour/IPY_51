from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(932, 417)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)

        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(Form)

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
        self.comboBox.setMinimumSize(QtCore.QSize(250, 20))
        self.comboBox.setMaximumSize(QtCore.QSize(250, 30))

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
        self.pushButton.setMinimumSize(QtCore.QSize(180, 20))
        self.pushButton.setMaximumSize(QtCore.QSize(180, 30))

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
        self.pushButton_2.setMinimumSize(QtCore.QSize(180, 20))
        self.pushButton_2.setMaximumSize(QtCore.QSize(180, 30))
        self.pushButton_2.setObjectName("pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)

        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(180, 20))
        self.pushButton_3.setMaximumSize(QtCore.QSize(180, 30))
        self.pushButton_3.setObjectName("pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 0, 6, 1, 1)

        self.verticalLayout.addWidget(self.widget)

        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(17)
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

        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(Form)

        self.comboBox.setCurrentIndex(0)

        self.tableWidget.horizontalHeader().resizeSection(0, 70)
        self.tableWidget.horizontalHeader().resizeSection(1, 90)
        self.tableWidget.horizontalHeader().resizeSection(3, 70)
        self.tableWidget.horizontalHeader().resizeSection(5, 200)
        self.tableWidget.horizontalHeader().resizeSection(6, 140)
        self.tableWidget.horizontalHeader().resizeSection(9, 120)
        self.tableWidget.horizontalHeader().resizeSection(10, 144)
        self.tableWidget.horizontalHeader().resizeSection(11, 140)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate

        Form.setWindowTitle(_translate("Form", "Form"))

        self.label.setText(_translate("Form", "Список абонентов (режим просмотра)"))

        self.comboBox.setItemText(0, _translate("Form", "Показать всех абонентов"))

        self.pushButton.setText(_translate("Form", "Разрешить редактирование"))

        self.pushButton_2.setText(_translate("Form", "Сохранить таблицу в csv"))

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
