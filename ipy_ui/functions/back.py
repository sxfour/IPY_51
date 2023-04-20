# Front User Interface.
from ui.pages.front import (
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
from PyQt5 import (
    QtWidgets,
    QtGui,
)

from subprocess import (
    Popen,
    PIPE,
)

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

        self.good_id, self.bad_id = list(), list()

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
                if timecheck_data < formatTimeServer_ or timecheck_data > formatTimeServer_:
                    # Запрос к PostgreSQL с заменой дат на сегодня.
                    self.editTablePostgreSQL("UPDATE ipy_names SET crnt_date = '{0}'"
                                             .format(formatTimeServer.strftime('%d.%m.%Y')), callback_data=data)

                    # Цикл проверки текущего состояния на дату
                    for subs in data:
                        # Если столбец не содержит дату, пропускаем.
                        if subs[4] is None:
                            pass

                        else:
                            try:
                                # Конвертируем дату госпроверки.
                                govCheckDate = strptime(''.join(subs[4]).replace('.', '/'), '%d/%m/%Y')

                                # Сохранение всех списков с id и передача в callback.
                                if govCheckDate == formatTimeServer_:
                                    self.bad_id.append(subs[17])

                                elif govCheckDate < formatTimeServer_:
                                    self.bad_id.append(subs[17])

                                elif govCheckDate > formatTimeServer_:
                                    self.good_id.append(subs[17])

                                else:
                                    # print('Error', subs[4], formatTimeServer.strftime('%d.%m.%Y'))
                                    pass

                            # Неправильный формат даты и остальные ошибки.
                            except ValueError as err:
                                error('\n[!] [TIME] Table edit error: {0}, {1}, {2}'.format(err, subs[4], subs[5]))

                    # Запись в лог.
                    info('\n[!] [TIME] Datetime refreshed : Server '
                         'table : {0}, Client : {1}'.format(data[random_el][8], self.time))

                    # Окно с сообщением.
                    successWindow(message='Обновление дат выполнено : {0}'
                                  .format(formatTimeServer.strftime('%d.%m.%Y')))

                    # Обновление всех состояний вышедших из строя на тек. дату.
                    self.editGovTablePostgreSQL("UPDATE ipy_names SET status_crnt_date = '{0}'"
                                                .format('вышел из строя'), callback_data=self.bad_id)

                    # Обновление всех состояний в работе на тек. дату.
                    self.editGovTablePostgreSQL("UPDATE ipy_names SET status_crnt_date = '{0}'"
                                                .format('в работе'), callback_data=self.good_id)

                elif timecheck_data == formatTimeServer_:
                    # Запись в лог.
                    info('\n[!] [TIME] Datetime (OK) : Server : {0}, '
                         'Client : {1}'.format(currentDateServer, self.time))
            else:
                # Запись в лог.
                error('[!] [TIME] Error, more info : Client time = {0}, Server time = {1}'.
                      format(self.time, formatTimeServer.strftime('%d.%m.%Y')), exc_info=True)

                # Окно с ошибкой и информацией от искл.
                errorWindow(message='client date = {0}'.format(self.time), text='Системные даты не совпадают..')

                # Выход из программы.
                exit()

            # Окно сообщения.
            successWindow(message='Соединение установлено.')
            return data

        except Exception as ex:
            # Запись в лог.
            error('[!] [EXCEPTION] Error, more info : {0}'.format(ex), exc_info=True)

            # Окно с ошибкой и информацией от искл.
            # errorWindow(message=ex, text='Соединение сброшено, обратитесь к администратору.')

            # Выход из программы.
            # exit()

    def setWindow(self):
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

    # Запрос к PostgreSQL с callback для дат.
    def editTablePostgreSQL(self, request, callback_data):
        return WorkerSQL(request, self.settings, self.section).editTableWithoutThreads(callback_data=callback_data)

    # Запрос к PostgreSQL с callback для статусов.
    def editGovTablePostgreSQL(self, request, callback_data):
        return WorkerSQL(request, self.settings, self.section).editGovWithoutThreads(callback_data=callback_data)


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

        self.time = datetime.now().strftime('%d.%m.%Y')
        self.data_first = list()

        self.settings = 'packages/postgresql/database.ini'
        self.section = 'postgresql'
        self.valid_keys = {
            0: 'treaty', 1: 'brand', 2: 'factory_code', 3: 'seal',
            4: 'state_verificatiom', 5: 'name_user', 6: 'adress', 7: 'area',
            8: 'crnt_date', 9: 'status_crnt_date', 10: 'tsm_december', 11: 'tsm_january',
            12: 'month_gcal', 13: 'month_m3', 14: 'all_gcal', 15: 'all_m3',
            16: 'description',
        }

        # При выборе элемента из списка в combo box, активируется.
        self.ui.comboBox.activated.connect(self.selectTable)
        self.ui.pushButton.clicked.connect(self.editTable)
        self.ui.pushButton_2.clicked.connect(self.saveTable)

        # self.ui.pushButton_3.clicked.connect(self.saveTableEdits)

        self.ui.pushButton_3.setEnabled(False)

    def createTableBox(self, data):
        try:
            counter = 0
            self.ui.tableWidget.setRowCount(len(data))
            for rows in data:
                for double_counter in range(len(data[0])):
                    if type(rows[double_counter]) != int:
                        self.ui.tableWidget.setItem(counter, double_counter,
                                                    QtWidgets.QTableWidgetItem(rows[double_counter]))
                    elif type(rows[double_counter]) == int:
                        self.ui.tableWidget.setItem(counter, double_counter,
                                                    QtWidgets.QTableWidgetItem(str(rows[double_counter])))
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
                if not self.ui.tableWidget.isEnabled():
                    # Запрос к PostgreSQL с сортировкой по имени.
                    data = self.checkPostgreSQL("SELECT * FROM ipy_names ORDER BY name_user;")

                    # Сохраняем ответ в список для передачи его в else при создании combobox.
                    self.data_first.append(data)

                    # Обновляем combobox.
                    self.createTableBox(data)

                    # Очистка таблицы и создание новой.
                    self.ui.tableWidget.setRowCount(len(data))

                    # Редактирование названий колонок на текущий месяц.
                    month = int(datetime.now().month)

                    if month < 12:
                        self.ui.tableWidget.horizontalHeaderItem(10).setText('За {0} месяц'.format(month))
                        self.ui.tableWidget.horizontalHeaderItem(11).setText('За {0} месяц'.format(month + 1))
                    elif month == 12:
                        self.ui.tableWidget.horizontalHeaderItem(10).setText('За {0} месяц'.format(month))
                        self.ui.tableWidget.horizontalHeaderItem(11).setText('За {0} месяц'.format(1))

                    for rows in data:
                        self.ui.comboBox.addItem('{0}, {1}'.format(rows[5], rows[6]))
                        for double_counter in range(len(data[0])):
                            if type(rows[double_counter]) != int:
                                self.ui.tableWidget.setItem(counter, double_counter,
                                                            QtWidgets.QTableWidgetItem(rows[double_counter]))
                                if str(rows[9]).strip() == 'в работе':
                                    self.ui.tableWidget.item(counter, 9).setBackground(
                                        QtGui.QColor(50, 150, 0, 50))
                                elif str(rows[9]).strip() == 'вышел из строя':
                                    self.ui.tableWidget.item(counter, 9).setBackground(
                                        QtGui.QColor(150, 0, 0, 50))
                            elif type(rows[double_counter]) == int:
                                self.ui.tableWidget.setItem(counter, double_counter,
                                                            QtWidgets.QTableWidgetItem(str(rows[double_counter])))
                        counter += 1
                    self.ui.tableWidget.resizeRowsToContents()
                else:
                    errorWindow('None', 'Пожалуйста, выйдите из режима редактирования и повторите запрос.')
            else:
                if not self.ui.tableWidget.isEnabled():
                    counter = 0
                    choice = self.ui.comboBox.currentText()

                    # Обновление списка абонентов.
                    self.createTableBox(self.data_first[0])

                    # Запрос к PostgreSQL.
                    data_ = self.checkPostgreSQL("SELECT * FROM ipy_names WHERE name_user LIKE '{0}%';"
                                                 .format(choice.split(',')[0]))

                    # Очистка таблицы и создание новой.
                    self.ui.tableWidget.setRowCount(len(data_))
                    for rows in data_:
                        for double_counter in range(len(data_[0])):
                            if type(rows[double_counter]) != int:
                                self.ui.tableWidget.setItem(counter, double_counter,
                                                            QtWidgets.QTableWidgetItem(rows[double_counter]))
                                if str(rows[9]).strip() == 'в работе':
                                    self.ui.tableWidget.item(counter, 9).setBackground(QtGui.QColor(50, 150, 0, 50))
                                elif str(rows[9]).strip() == 'вышел из строя':
                                    self.ui.tableWidget.item(counter, 9).setBackground(QtGui.QColor(150, 0, 0, 50))
                            elif type(rows[double_counter]) == int:
                                self.ui.tableWidget.setItem(counter, double_counter,
                                                            QtWidgets.QTableWidgetItem(str(rows[double_counter])))
                        counter += 1
                    self.ui.tableWidget.resizeRowsToContents()
                else:
                    errorWindow('None', 'Пожалуйста, выйдите из режима редактирования и повторите запрос.')
        except Exception as ex:
            # Запись в лог.
            error('[!] [EXCEPTION] Error select table, more info : {0}'.format(ex), exc_info=True)

            # Окно с ошибкой и информацией от искл.
            # errorWindow(message=ex, text='Соединение сброшено, обратитесь к администратору.')

    # Кнопка редактирование таблицы.
    def editTable(self, checked):
        if checked:
            self.ui.label.setText('Список абонентов (режим редактирования)')

            # Очистка курсора.
            self.ui.tableWidget.selectionModel().clearSelection()

            # Connect функции курсора.
            self.ui.tableWidget.cellChanged.connect(self.cellChange)

            # Цвет текста и активация
            self.ui.tableWidget.setEnabled(True)

            self.ui.label.setEnabled(True)
            self.ui.label.setStyleSheet("background-color: rgba(255, 191, 0, 155);")

        else:
            # Текст строки.
            self.ui.label.setText('Список абонентов (режим просмотра)')

            # Очистка курсора.
            self.ui.tableWidget.selectionModel().clearSelection()

            # Disconnect функции курсора.
            self.ui.tableWidget.cellChanged.disconnect()

            # Цвет текста и активация.
            self.ui.tableWidget.setEnabled(False)

            self.ui.label.setEnabled(False)
            self.ui.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

    # Изменение таблицы и формирование запроса к PostgreSQL.
    def cellChange(self):
        current_row = self.ui.tableWidget.currentRow()
        current_column = self.ui.tableWidget.currentColumn()

        if current_column in self.valid_keys:
            id_data = [self.ui.tableWidget.item(current_row, 17).text()]
            text_data = self.ui.tableWidget.item(current_row, current_column).text()

            if len(text_data) < 100:
                self.editGovTablePostgreSQL("UPDATE ipy_names SET {0} = '{1}'"
                                            .format(self.valid_keys.get(current_column),
                                                    text_data), callback_data=id_data)
            else:
                errorWindow('всего символов = {0}, text = {1}'
                            .format(len(text_data), text_data), 'Превышен лимит символов на ячейку.')

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
    # def saveTableEdits(self):
    #     self.ui.tableWidget.selectionModel().clearSelection()

    # Запрос к PostgreSQL.
    def checkPostgreSQL(self, request):
        return WorkerSQL(request, self.settings, self.section).connectPostgreSQL()

    # Запрос к PostgreSQL.
    def editGovTablePostgreSQL(self, request, callback_data):
        return WorkerSQL(request, self.settings, self.section).editGovWithoutThreads(callback_data=callback_data)


class FindPage(QWidget, object):

    def __init__(self, good_string: str):
        super(FindPage, self).__init__()
        self.ui = UI_FindPage()
        self.ui.setupUi(self)

        self.data = None
        self.good_string = good_string
        self.settings = 'packages/postgresql/database.ini'
        self.section = 'postgresql'
        self.valid_keys = {
            0: 'treaty', 1: 'brand', 2: 'factory_code', 3: 'seal',
            4: 'state_verificatiom', 5: 'name_user', 6: 'adress', 7: 'area',
            8: 'crnt_date', 9: 'status_crnt_date', 10: 'tsm_december', 11: 'tsm_january',
            12: 'month_gcal', 13: 'month_m3', 14: 'all_gcal', 15: 'all_m3',
            16: 'description',
        }

        self.findUser()

        # При выборе элемента из списка в combo box, активируется.
        self.ui.pushButton.clicked.connect(self.editTable)
        self.ui.pushButton_2.clicked.connect(self.saveTable)

        # self.ui.pushButton_3.clicked.connect(self.saveTableEdits)

        self.ui.pushButton_3.setEnabled(False)

    def createTableBox(self, data):
        try:
            counter = 0
            self.ui.tableWidget.setRowCount(len(data))
            for rows in data:
                for double_counter in range(len(data[0])):
                    if type(rows[double_counter]) != int:
                        self.ui.tableWidget.setItem(counter, double_counter,
                                                    QtWidgets.QTableWidgetItem(rows[double_counter]))
                    elif type(rows[double_counter]) == int:
                        self.ui.tableWidget.setItem(counter, double_counter,
                                                    QtWidgets.QTableWidgetItem(str(rows[double_counter])))
                counter += 1

            # Уменьшить сетку до размера данных таблицы.
            self.ui.tableWidget.resizeRowsToContents()
        except Exception as ex:
            self.ui.label.setText('Подключение отсутствует')

            # Невидимость, при отсутствие соединения.
            self.ui.pushButton_2.setVisible(False)
            self.ui.pushButton_3.setVisible(False)
            self.ui.pushButton.setVisible(False)

            # Запись в лог.
            error('[!] [EXCEPTION] Error create table box, more info : {0}'.format(ex), exc_info=True)

            # Окно с ошибкой и информацией от искл.
            errorWindow(message=ex, text='Соединение сброшено, обратитесь к администратору.')

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
                data = self.checkPostgreSQL("SELECT * FROM ipy_names WHERE name_user LIKE '{0}%'"
                                            .format(self.good_string))
                self.data = str(len(data))

                self.createTableBox(data)

                self.ui.label.setText('Поиск по абонентам, найдено совпадений '
                                      ': {0} (режим просмотра)'.format(len(data)))
                self.ui.tableWidget.setRowCount(len(data))

                # Редактирование названий колонок на текущий месяц.
                month = int(datetime.now().month)
                if month < 12:
                    self.ui.tableWidget.horizontalHeaderItem(10).setText('Показания за {0} месяц'.format(month))
                    self.ui.tableWidget.horizontalHeaderItem(11).setText('Показания за {0} месяц'.format(month + 1))
                elif month == 12:
                    self.ui.tableWidget.horizontalHeaderItem(10).setText('Показания за {0} месяц'.format(month))
                    self.ui.tableWidget.horizontalHeaderItem(11).setText('Показания за {0} месяц'.format(1))

                for rows in data:
                    for double_counter in range(len(data[0])):
                        if type(rows[double_counter]) != int:
                            self.ui.tableWidget.setItem(counter, double_counter,
                                                        QtWidgets.QTableWidgetItem(rows[double_counter]))
                            if str(rows[9]) == 'в работе':
                                self.ui.tableWidget.item(counter, 9).setBackground(QtGui.QColor(50, 150, 0, 50))
                            elif str(rows[9]) == 'вышел из строя':
                                self.ui.tableWidget.item(counter, 9).setBackground(QtGui.QColor(150, 0, 0, 50))
                        elif type(rows[double_counter]) == int:
                            self.ui.tableWidget.setItem(counter, double_counter,
                                                        QtWidgets.QTableWidgetItem(str(rows[double_counter])))
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

            # Очистка курсора.
            self.ui.tableWidget.selectionModel().clearSelection()

            # Connect функции курсора.
            self.ui.tableWidget.cellChanged.connect(self.cellChange)

            # Цвет текста.
            self.ui.tableWidget.setEnabled(True)

            self.ui.label.setEnabled(True)
            self.ui.label.setStyleSheet("background-color: rgba(255, 191, 0, 155);")

        else:
            # Текст строки.
            self.ui.label.setText('Поиск по абонентам, найдено совпадений : {0} (режим просмотра)'.format(self.data))

            # Очистка курсора.
            self.ui.tableWidget.selectionModel().clearSelection()

            # Disconnect функции курсора.
            self.ui.tableWidget.cellChanged.disconnect()

            # Цвет текста.
            self.ui.tableWidget.setEnabled(False)

            self.ui.label.setEnabled(False)
            self.ui.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

    # Изменение таблицы и формирование запроса к PostgreSQL.
    def cellChange(self):
        current_row = self.ui.tableWidget.currentRow()
        current_column = self.ui.tableWidget.currentColumn()

        if current_column in self.valid_keys:
            id_data = [self.ui.tableWidget.item(current_row, 17).text()]
            text_data = self.ui.tableWidget.item(current_row, current_column).text()

            if len(text_data) < 100:
                self.editGovTablePostgreSQL("UPDATE ipy_names SET {0} = '{1}'"
                                            .format(self.valid_keys.get(current_column),
                                                    text_data), callback_data=id_data)
            else:
                errorWindow('всего символов = {0}, text = {1}'
                            .format(len(text_data), text_data), 'Превышен лимит символов на ячейку.')

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
                    print(path.dirname(path.abspath(filename)))
            except Exception as ex:
                # Запись в лог.
                error('[!] [EXCEPTION] Error save table, more info : {0}'.format(ex), exc_info=True)

                # Окно с ошибкой и информацией от искл.
                errorWindow(message=ex, text='Сохранение файла невозможно, проверьте директорию.')

    # Кнопка сохранение изменений в таблице.
    # def saveTableEdits(self):
    #     self.ui.tableWidget.selectionModel().clearSelection()

    # Запрос к PostgreSQL.
    def checkPostgreSQL(self, request):
        return WorkerSQL(request, self.settings, self.section).connectPostgreSQL()

    # Запрос к PostgreSQL.
    def editGovTablePostgreSQL(self, request, callback_data):
        return WorkerSQL(request, self.settings, self.section).editGovWithoutThreads(callback_data=callback_data)


class CreateTicketPage(QWidget, object):

    def __init__(self):
        super(CreateTicketPage, self).__init__()
        self.ui = UI_CreateTicketPage()
        self.ui.setupUi(self)

        # Соединение с кнопкой отправки сообщения
        self.ui.pushButton.clicked.connect(self.sendMessageSMTP)

    def sendMessageSMTP(self):
        message = str(self.ui.textEdit.toPlainText())
        error_text = str(self.ui.comboBox.currentText())
        time = datetime.now()
        try:
            # Для извлечения IP клиента через PowerShell.
            psExecutor = ["getinfo.ps1", "functions"]
            currentPath = path.dirname(path.abspath(psExecutor[0]))
            fullPath = "{0}\\{1}\\{2}".format(currentPath, psExecutor[1], psExecutor[0])
            p = Popen(["powershell.exe", fullPath], stdout=PIPE)
            result = p.communicate()[0].decode('utf-8')

            if len(message) < 100:
                # Для SMTP.
                from email.mime.multipart import MIMEMultipart
                from email.mime.text import MIMEText
                from smtplib import SMTP

                from_addr = "levashov.teploset@mail.ru"
                to_addr = "mt.seti@yandex.ru"

                # Token for app : 
                ind_value = ""

                msg = MIMEMultipart()

                msg['From'] = from_addr
                msg['To'] = to_addr
                msg['Subject'] = 'ИПУ Обращение [ {0} ] # [ {1} ] '.format(error_text, time)

                msg.attach(MIMEText('{0}\n\n\nGet info : {1}'
                                    .format(message, result), 'plain'))

                # Для работы с почтой mail.ru указываем 25 порт.
                server = SMTP('smtp.mail.ru', 25, timeout=1)

                server.starttls()
                server.login(from_addr, ind_value)

                text = msg.as_string()

                server.sendmail(from_addr, to_addr, text)
                server.quit()

                successWindow('Сообщение успешно отправлено.')

            else:
                errorWindow(message, 'Превышен лимит символов.')

        except Exception as ex:
            # Окно с ошибкой и информацией от искл.
            errorWindow(message=ex, text='Сообщение не отправлено.')

            # Запись в лог
            error('[!] [EXCEPTION] Error SMTP, more info : {0}'.format(ex), exc_info=True)


class TicketsInfoPage(QWidget, object):

    def __init__(self):
        super(TicketsInfoPage, self).__init__()
        self.ui = UI_TicketsInfoPage()
        self.ui.setupUi(self)
