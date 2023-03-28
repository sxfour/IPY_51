# Front User Interface.
from ui.pages.all_pages_front import (
    UI_StatisticPage,
    UI_SubscribersPage,
    UI_CreateTicketPage,
    UI_TicketsInfoPage,
    UI_FindPage,
    UI_InfoPage,
    successWindow,
    errorWindow,
)

# MainWindow classes.
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtWidgets

# Random integer.
from random import randint

# Logs on stack.
from logging import (
    error,
    info,
)

# CSV save on file.
from csv import writer

# View local dirs.
from os import path

# Time.
from datetime import datetime
from time import strptime

# PostgreSQL Connector.
from packages.connector import WorkerSQL


class StatisticPage(QWidget, object):

    def __init__(self):
        super(StatisticPage, self).__init__()
        self.ui = UI_StatisticPage()
        self.ui.setupUi(self)

        self.message = 'нет подключения'
        self.settings = 'packages/postgresql/database.ini'
        self.section = 'postgresql'

        self.time = datetime.now().strftime('%d.%m.%Y')
        self.time_ = strptime(self.time, '%d.%m.%Y')

        self.setWindow()

    def checkDateDatabase(self):
        try:
            # Получения даты сервера.
            currentDateServer = str(self.checkPostgreSQL("SELECT version(), CURRENT_DATE;")[0][1])

            # Применениe формата для сравнения дат.
            formatTimeServer = datetime.strptime(currentDateServer, '%Y-%m-%d')
            formatTimeServer_ = strptime(formatTimeServer.strftime('%d.%m.%Y'), '%d.%m.%Y')

            # Проверка совпадения текущих системных дат клиент-сервер.
            if self.time == formatTimeServer.strftime('%d.%m.%Y'):
                # Запрос к PostgreSQL.
                data = self.checkPostgreSQL("SELECT * FROM ipy_names;")

                random_el = randint(0, len(data))
                timecheck_data = strptime(''.join(data[random_el][8]).replace('.', '/'), '%d/%m/%Y')

                # Сравнение дат таблиц базы и сервера, клиентское приложение не используется.
                if timecheck_data < formatTimeServer_:
                    # Запрос к PostgreSQL с заменой дат на сегодня.
                    # Библиотека для связи с PostgreSQL не работает в многопоточном режиме, поэтому создана отдельная
                    # функция для внесения изменений в дату (смотреть в бэк PostgreSQL)
                    self.editTablePostgreSQL("UPDATE ipy_names SET crnt_date = '{0}'".format(formatTimeServer.strftime('%d.%m.%Y')), callback_data=data)

                    successWindow(message='Обновление дат выполнено.\nСервер : {0} Клиент : {1}'.format(currentDateServer, self.time))

                elif timecheck_data == formatTimeServer_:
                    info('\n[!] [TIME] Datetime (OK) : Server : {0}, Client : {1}'.format(currentDateServer, self.time))

                    # for subs in data:
                    #     # Если столбец не содержит дату, пропускаем.
                    #     if subs[8] is None:
                    #         # error('[!] [DATE] Datetime : Date : {0}, Org : {1}'.format(subs[8], subs[5]), exc_info=True)
                    #         pass
                    #     else:
                    #         timecheck = strptime(''.join(subs[8]).replace('.', '/'), '%d/%m/%Y')
                    #         try:
                    #             if timecheck < self.time_:
                    #                 print('\x1b[31;3mПросрочено\033[0m', subs[8], subs[5])
                    #
                    #             elif timecheck >= self.time_:
                    #                 print('\033[32;3mНе просрочено\033[0m', subs[8], subs[5])
                    #
                    #         except ValueError as err:
                    #             print('\x1b[31;3mДата указана неправильно! %s\033[0m' % err)
                    #
                    # print(self.time, self.time_, formatTimeServer.strftime('%d.%m.%Y'))

            else:
                # Запись в лог.
                error('[!] [TIME] Error, more info : Client time = {0}, Server time = {1}'.
                      format(self.time, formatTimeServer.strftime('%d.%m.%Y')), exc_info=True)

                # Окно с ошибкой и информацией от искл.
                errorWindow(message='client date = {0}'.format(self.time), text='Системные даты не совпадают..')

                exit()

            successWindow(message='Соединение установлено.')
            return data

        except Exception as ex:
            # Запись в лог.
            error('[!] [EXCEPTION] Error, more info : {0}'.format(ex), exc_info=True)

            # Окно с ошибкой и информацией от искл.
            errorWindow(message=ex, text='Соединение сброшено, обратитесь к администратору.')

            # Выход из программы.
            exit()

    def setWindow(self):
        # Exp при неудачном соединение.
        try:
            data = self.checkDateDatabase()
            example = randint(0, len(data))

            # Пример ответа.
            self.ui.label_ex.setText('\nПример ответа сервера :\n— договор : {0}, марка : {1}'
                                     '\n— заводской № : {2}, пломба : {3}'
                                     '\n— госпроверка : {4}, наименование : {5}'
                                     '\n— адрес : {6}, площадь : {7} кв.м'
                                     '\n— текущая дата : {8}, статус на текущую дату : {9}'
                                     '\n— показания за декабрь : {10}, показания за январь : {11}'
                                     '\n— за месяц : {12} Гкал, {13} м3'
                                     '\n— всего : {14} Гкал, {15} м3'
                                     '\n— примечание : {16}'
                                     .format(data[example][0], data[example][1], data[example][2], data[example][3],
                                             data[example][4], data[example][5], data[example][6], data[example][7],
                                             data[example][8], data[example][9], data[example][10], data[example][11],
                                             data[example][12], data[example][13], data[example][14], data[example][15],
                                             data[example][16]))

            # Счётчик абонентов.
            status_good, status_check, status_bad = 0, 0, 0
            for num in range(len(data)):
                if data[num][9] == 'в работе':
                    status_good += 1
                elif data[num][9] == 'поверка':
                    status_check += 1
                else:
                    status_bad += 1

            self.ui.label_count_0.setText(' Всего записей : {0} '.format(len(data)))
            self.ui.label_count_1.setText(' В работе : {0} '.format(status_good))
            self.ui.label_count_2.setText(' Поверка : {0} '.format(status_check))
            self.ui.label_count_3.setText(' Плохие : {0} '.format(status_bad))

        except Exception as ex:
            self.ui.label_count_0.setText(' Всего записей : {0} '.format(self.message))
            self.ui.label_count_1.setText(' В работе : {0} '.format(self.message))
            self.ui.label_count_2.setText(' Поверка : {0} '.format(self.message))
            self.ui.label_count_3.setText(' Плохие : {0} '.format(self.message))
            self.ui.label.setText('\n— Уф… Нет, лучше назад… Уф… Нет, лучше вперед…\n'
                                  'Ой-ёй-ёй! Спасите-помогите! Ни вперед, ни назад!\n'
                                  '— Ты что, застрял?!\n— Нет, я просто отдыхаю!')

            # Запись в лог.
            error('[!] [EXCEPTION] Error, more info : {0}'.format(ex), exc_info=True)

            # Окно с ошибкой и информацией от искл.
            errorWindow(message=ex, text='Соединение сброшено, обратитесь к администратору.')

    # Запрос к PostgreSQL.
    def checkPostgreSQL(self, request):
        return WorkerSQL(request, self.settings, self.section).connectPostgreSQL()

    def editTablePostgreSQL(self, request, callback_data):
        return WorkerSQL(request, self.settings, self.section).editTableWithoutThreads(callback_data=callback_data)


class InfoPage(QWidget, object):

    def __init__(self):
        super(InfoPage, self).__init__()
        self.ui = UI_InfoPage()
        self.ui.setupUi(self)

        self.settings = 'packages/postgresql/database.ini'
        self.section = 'postgresql'

        self.setWindow()

    def setWindow(self):
        try:
            data = self.checkPostgreSQL("SELECT version(), CURRENT_DATE;")[0]
            self.ui.label_1.setText('Версия : {0}\n Дата запроса : {1}'.format(data[0], data[1]))
        except Exception as ex:
            self.ui.label_1.setText('— Простите, а что, совсем никого нет дома?\n'
                                    '— Совсем никого.\n'
                                    '— Что-то здесь не так.\nКто-то там все-таки есть!\n'
                                    'Кто-то же должен был сказать «совсем никого»!')

            # Запись в лог.
            error('[!] [EXCEPTION] Error, more info : {0}'.format(ex), exc_info=True)

            # Окно с ошибкой и информацией от искл.
            errorWindow(message=ex, text='Соединение сброшено, обратитесь к администратору.')

    # Запрос к PostgreSQL.
    def checkPostgreSQL(self, request):
        return WorkerSQL(request, self.settings, self.section).connectPostgreSQL()


class SubscribersPage(QWidget, object):

    def __init__(self):
        super(SubscribersPage, self).__init__()
        self.ui = UI_SubscribersPage()
        self.ui.setupUi(self)

        self.settings = 'packages/postgresql/database.ini'
        self.section = 'postgresql'

        # self.createTableBox()

        # При выборе элемента из списка в combo box, активируется.
        self.ui.comboBox.activated.connect(self.selectTable)
        self.ui.pushButton.clicked.connect(self.editTable)
        self.ui.pushButton_2.clicked.connect(self.saveTable)
        self.ui.pushButton_3.clicked.connect(self.saveTableEdits)

    def createTableBox(self, data):
        try:
            counter = 0
            self.ui.tableWidget.setRowCount(len(data))
            for rows in data:
                self.ui.comboBox.addItem('{0}, {1}'.format(rows[5], rows[6]))
                for double_counter in range(len(data[0])):
                    self.ui.tableWidget.setItem(counter, double_counter,
                                                QtWidgets.QTableWidgetItem(rows[double_counter]))
                counter += 1

            # Уменьшить сетку до размера данных таблицы.
            self.ui.tableWidget.resizeRowsToContents()
        except Exception as ex:
            self.ui.label.setText('Подключение отсутствует')

            # Невидимость, при отсутствие соединения.
            self.ui.pushButton_2.setVisible(False)
            self.ui.pushButton_3.setVisible(False)
            self.ui.pushButton.setVisible(False)
            self.ui.comboBox.setVisible(False)
            self.ui.comboBox.setVisible(False)

            # Запись в лог.
            error('[!] [EXCEPTION] Error create table box, more info : {0}'.format(ex), exc_info=True)

            # Окно с ошибкой и информацией от искл.
            errorWindow(message=ex, text='Соединение сброшено, обратитесь к администратору.')

    def selectTable(self):
        try:
            counter = 0
            index = self.ui.comboBox.currentIndex()
            if not index:
                # Запрос к PostgreSQL с сортировкой по имени.
                data = self.checkPostgreSQL("SELECT * FROM ipy_names ORDER BY name_user;")

                self.createTableBox(data)

                # Очистка таблицы и создание новой.
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

                # Очистка таблицы и создание новой.
                self.ui.tableWidget.setRowCount(len(data))

                for rows in data:
                    for double_counter in range(len(data[0])):
                        self.ui.tableWidget.setItem(counter, double_counter,
                                                    QtWidgets.QTableWidgetItem(rows[double_counter]))
                    counter += 1
                self.ui.tableWidget.resizeRowsToContents()
        except Exception as ex:
            # Запись в лог.
            error('[!] [EXCEPTION] Error select table, more info : {0}'.format(ex), exc_info=True)

            # Окно с ошибкой и информацией от искл.
            errorWindow(message=ex, text='Соединение сброшено, обратитесь к администратору.')

    # Кнопка редактирование таблицы.
    def editTable(self, checked):
        if checked:
            self.ui.label.setText('Список абонентов (режим редактирования)')

            # Connect функции курсора.
            self.ui.tableWidget.selectionModel().selectionChanged.connect(self.findTablePosition)

            # Цвет текста.
            self.ui.label.setEnabled(True)
            self.ui.label.setStyleSheet("background-color: rgba(255, 191, 0, 155);")
        else:
            # Текст строки.
            self.ui.label.setText('Список абонентов (режим просмотра)')

            # Disconnect функции курсора.
            self.ui.tableWidget.selectionModel().selectionChanged.disconnect()

            # Цвет текста.
            self.ui.label.setEnabled(False)
            self.ui.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

    # Поиск курсора по таблице и сохранение изменений.
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

    # Кнопка сохранение таблицы в csv.
    def saveTable(self):
        data = self.checkPostgreSQL("SELECT * FROM ipy_names;")
        filename = 'csv/ИПУ(все абоненты).csv'
        try:
            with open(filename, mode='w', encoding='cp1251') as file:
                csv_writer = writer(file, delimiter=';', lineterminator='\n')

                for row in data:
                    csv_writer.writerow(row)

                successWindow(message='Файл сохранён в директорию : \n{0}'.format(path.dirname(path.abspath(filename))))
        except Exception as ex:
            # Запись в лог.
            error('[!] [EXCEPTION] Error save table, more info : {0}'.format(ex), exc_info=True)

            # Окно с ошибкой и информацией от искл.
            errorWindow(message=ex, text='Сохранение файла невозможно, проверьте директорию.')

    # Кнопка сохранение изменений в таблице.
    def saveTableEdits(self):
        print('Сохранить изменения')

    # Запрос к PostgreSQL.
    def checkPostgreSQL(self, request):
        return WorkerSQL(request, self.settings, self.section).connectPostgreSQL()


class FindPage(QWidget, object):

    def __init__(self, good_string: str):
        super(FindPage, self).__init__()
        self.ui = UI_FindPage()
        self.ui.setupUi(self)

        self.data = None
        self.good_string = good_string
        self.settings = 'packages/postgresql/database.ini'
        self.section = 'postgresql'

        self.findUser()

        # При выборе элемента из списка в combo box, активируется.
        self.ui.pushButton.clicked.connect(self.editTable)
        self.ui.pushButton_2.clicked.connect(self.saveTable)
        self.ui.pushButton_3.clicked.connect(self.saveTableEdits)

    def findUser(self):
        # Фильтрация ошибочного запроса с содержанием пробелов.
        if self.good_string == ' ' or self.good_string == '  ' or self.good_string == '   ' \
                or self.good_string == '    ' or self.good_string == '    ' or self.good_string == '     ' \
                or self.good_string == '      ' or self.good_string == '       ' or self.good_string == '        ':

            # Невидимость, при отсутствие соединения.
            self.ui.pushButton_2.setVisible(False)
            self.ui.pushButton_3.setVisible(False)
            self.ui.pushButton.setVisible(False)

        else:
            try:
                counter = 0
                data = self.checkPostgreSQL(
                    'SELECT * FROM ipy_names WHERE name_user LIKE \'{0}%\''.format(self.good_string))
                self.data = str(len(data))

                self.ui.label.setText('Поиск по абонентам, найдено совпадений '
                                      ': {0} (режим просмотра)'.format(len(data)))
                self.ui.tableWidget.setRowCount(len(data))
                for rows in data:
                    for double_counter in range(len(data[0])):
                        self.ui.tableWidget.setItem(counter, double_counter,
                                                    QtWidgets.QTableWidgetItem(rows[double_counter]))
                    counter += 1
                self.ui.tableWidget.resizeRowsToContents()
            except Exception as ex:
                self.ui.label.setText('Подключение отсутствует')

                # Невидимость, при отсутствие соединения.
                self.ui.pushButton_2.setVisible(False)
                self.ui.pushButton_3.setVisible(False)
                self.ui.pushButton.setVisible(False)

                # Запись в лог.
                error('[!] [EXCEPTION] Error find name from database, more info : {0}'.format(ex), exc_info=True)

                # Окно с ошибкой и информацией от искл.
                errorWindow(message=ex, text='Соединение сброшено, обратитесь к администратору.')

    # Кнопка редактирование таблицы.
    def editTable(self, checked):
        if checked:
            self.ui.label.setText('Поиск по абонентам, найдено совпадений : '
                                  '{0} (режим редактирования)'.format(self.data))

            # Connect функции курсора.
            self.ui.tableWidget.selectionModel().selectionChanged.connect(self.findTablePosition)

            # Цвет текста.
            self.ui.label.setEnabled(True)
            self.ui.label.setStyleSheet("background-color: rgba(255, 191, 0, 155);")
        else:
            # Текст строки.
            self.ui.label.setText('Поиск по абонентам, найдено совпадений : {0} (режим просмотра)'.format(self.data))

            # Цвет текста.
            self.ui.label.setEnabled(False)
            self.ui.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

            # Disconnect функции курсора.
            self.ui.tableWidget.selectionModel().selectionChanged.disconnect()

    # Поиск курсора по таблице и сохранение изменений.
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

    # Кнопка сохранение таблицы в csv.
    def saveTable(self):
        # Фильтрация ошибочного запроса с содержанием пробелов.
        if self.good_string == ' ' or self.good_string == '  ' or self.good_string == '   ' \
                or self.good_string == '    ' or self.good_string == '    ' or self.good_string == '     ' \
                or self.good_string == '      ' or self.good_string == '       ' or self.good_string == '        ':
            pass
        else:
            data = self.checkPostgreSQL(
                'SELECT * FROM ipy_names WHERE name_user LIKE \'{0}%\''.format(self.good_string))
            filename = 'csv/ИПУ(ключевой поиск).csv'
            try:
                with open(filename, mode='w', encoding='cp1251') as file:
                    csv_writer = writer(file, delimiter=';', lineterminator='\n')

                    for row in data:
                        csv_writer.writerow(row)

                    # Окно с сообщением.
                    successWindow(message='Файл сохранён в директорию : \n'
                                          '{0}'.format(path.dirname(path.abspath(filename))))
            except Exception as ex:
                # Запись в лог.
                error('[!] [EXCEPTION] Error save table, more info : {0}'.format(ex), exc_info=True)

                # Окно с ошибкой и информацией от искл.
                errorWindow(message=ex, text='Сохранение файла невозможно, проверьте директорию.')

    # Кнопка сохранение изменений в таблице.
    def saveTableEdits(self):
        print('Сохранить изменения')

    def checkPostgreSQL(self, request):
        return WorkerSQL(request, self.settings, self.section).connectPostgreSQL()


class CreateTicketPage(QWidget, object):

    def __init__(self):
        super(CreateTicketPage, self).__init__()
        self.ui = UI_CreateTicketPage()
        self.ui.setupUi(self)


class TicketsInfoPage(QWidget, object):

    def __init__(self):
        super(TicketsInfoPage, self).__init__()
        self.ui = UI_TicketsInfoPage()
        self.ui.setupUi(self)
