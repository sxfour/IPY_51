from ui.pages.error import errorWindow, successWindow
from packages.connector import WorkerSQL
from PyQt5.QtWidgets import QWidget
from ui.pages.home_2 import Ui_Form
from PyQt5 import QtWidgets
from logging import error
from csv import writer
from os import path


class Home_2(QWidget, object):

    def __init__(self):
        super(Home_2, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.settings = 'packages/postgresql/database.ini'
        self.section = 'postgresql'

        self.createTableBox()

        # При выборе элемента из списка в combo box, активируется
        self.ui.comboBox.activated.connect(self.selectTable)
        self.ui.pushButton.clicked.connect(self.editTable)
        self.ui.pushButton_2.clicked.connect(self.saveTable)
        self.ui.pushButton_3.clicked.connect(self.saveTableEdits)

    def createTableBox(self):
        try:
            counter = 0
            data = self.checkPostgreSQL("SELECT * FROM ipy_names;")

            self.ui.tableWidget.setRowCount(len(data))
            for rows in data:
                self.ui.comboBox.addItem('{0}, {1}'.format(rows[5], rows[6]))
                for double_counter in range(len(data[0])):
                    self.ui.tableWidget.setItem(counter, double_counter,
                                                QtWidgets.QTableWidgetItem(rows[double_counter]))
                counter += 1
            self.ui.tableWidget.resizeRowsToContents()
        except Exception as ex:
            self.ui.label.setText('Подключение отсутствует')

            # Невидимость, при отсутствие соединения
            self.ui.pushButton_2.setVisible(False)
            self.ui.pushButton_3.setVisible(False)
            self.ui.pushButton.setVisible(False)
            self.ui.comboBox.setVisible(False)
            self.ui.comboBox.setVisible(False)

            error('[!] [EXCEPTION] Error create table box, more info : {0}'.format(ex), exc_info=True)

            errorWindow(message=ex, text='Соединение сброшено, обратитесь к администратору.')

    def selectTable(self):
        try:
            counter = 0
            index = self.ui.comboBox.currentIndex()
            if not index:
                data = self.checkPostgreSQL("SELECT * FROM ipy_names;")
                self.createTableBox()

                # Очистка таблицы и создание новой
                self.ui.tableWidget.setRowCount(len(data))
                for rows in data:
                    self.ui.comboBox.addItem('{0}, {1}'.format(rows[5], rows[6]))
                    for double_counter in range(len(data[0])):
                        self.ui.tableWidget.setItem(counter, double_counter,
                                                    QtWidgets.QTableWidgetItem(rows[double_counter]))
                    counter += 1
                self.ui.tableWidget.resizeRowsToContents()
            else:
                counter = 0
                choice = self.ui.comboBox.currentText()
                data = self.checkPostgreSQL(
                    "SELECT * FROM ipy_names WHERE name_user LIKE '{0}%';".format(choice.split(',')[0]))

                # Очистка таблицы и создание новой
                self.ui.tableWidget.setRowCount(len(data))

                for rows in data:
                    for double_counter in range(len(data[0])):
                        self.ui.tableWidget.setItem(counter, double_counter,
                                                    QtWidgets.QTableWidgetItem(rows[double_counter]))
                    counter += 1
                self.ui.tableWidget.resizeRowsToContents()
        except Exception as ex:

            # Запись в лог
            error('[!] [EXCEPTION] Error select table, more info : {0}'.format(ex), exc_info=True)

            # Окно с ошибкой и информацией от искл
            errorWindow(message=ex, text='Соединение сброшено, обратитесь к администратору.')

    # Кнопка редактирование таблицы
    def editTable(self, checked):
        if checked:
            self.ui.label.setText('Список абонентов (режим редактирования)')

            # Connect функции курсора
            self.ui.tableWidget.selectionModel().selectionChanged.connect(self.findTablePosition)
        else:
            self.ui.label.setText('Список абонентов (режим просмотра)')
            self.ui.tableWidget.selectionModel().selectionChanged.disconnect()

    # Поиск курсора по таблице и сохранение изменений
    def findTablePosition(self, selected, deselected):
        for x in selected.indexes():
            print('Selected Row : {0}, column : {1}, {2}\n'.format(x.row(), x.column(),
                                                                   self.ui.tableWidget.item(
                                                                       self.ui.tableWidget.currentRow(),
                                                                       x.column()).text()))

        for y in deselected.indexes():
            print('Deselected row : {0}, column : {1}, {2}\n'.format(y.row(), y.column(),
                                                                     self.ui.tableWidget.item(
                                                                         self.ui.tableWidget.currentRow(),
                                                                         y.column()).text()))

    # Кнопка сохранение таблицы в csv
    def saveTable(self):
        data = self.checkPostgreSQL("SELECT * FROM ipy_names;")
        filename = 'csv/ИПУ.csv'
        try:
            with open(filename, mode='w', encoding='cp1251') as file:
                csv_writer = writer(file, delimiter=';', lineterminator='\n')

                for row in data:
                    csv_writer.writerow(row)

                successWindow(message='Файл сохранён в директорию : \n{0}'.format(path.dirname(path.abspath(filename))))
        except Exception as ex:
            errorWindow(message=ex, text='Сохранение файла невозможно, проверьте директорию.')

    # Кнопка сохранение изменений в таблице
    def saveTableEdits(self):
        print('Сохранить изменения')

    # Запрос к PostgreSQL
    def checkPostgreSQL(self, request):
        return WorkerSQL(request, self.settings, self.section).connectPostgreSQL()
