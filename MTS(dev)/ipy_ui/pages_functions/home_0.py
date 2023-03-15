from ui.pages.error import errorWindow, successWindow
from packages.connector import WorkerSQL
from PyQt5.QtWidgets import QWidget
from ui.pages.home_0 import Ui_Form
from random import randint
from logging import error


class Home(QWidget):

    def __init__(self):
        super(Home, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.message = 'нет подключения'
        self.settings = 'packages/postgresql/database.ini'
        self.section = 'postgresql'

        self.setWindow()

    def setWindow(self):
        # Exp при неудачном соединение
        try:
            data = self.checkPostgreSQL()
            example = randint(0, len(data))

            # Пример ответа
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

            # Счётчик абонентов
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

            successWindow()

        except Exception as ex:
            self.ui.label_count_0.setText(' Всего записей : {0} '.format(self.message))
            self.ui.label_count_1.setText(' В работе : {0} '.format(self.message))
            self.ui.label_count_2.setText(' Поверка : {0} '.format(self.message))
            self.ui.label_count_3.setText(' Плохие : {0} '.format(self.message))
            self.ui.label.setText('\n— Уф… Нет, лучше назад… Уф… Нет, лучше вперед…\n'
                                  'Ой-ёй-ёй! Спасите-помогите! Ни вперед, ни назад!\n'
                                  '— Ты что, застрял?!\n— Нет, я просто отдыхаю!')

            # Запись в лог
            error('[!] [EXCEPTION] Error, more info : {0}'.format(ex), exc_info=True)

            # Окно с ошибкой и информацией от искл
            errorWindow(message=ex)

    # Запрос к PostgreSQL
    def checkPostgreSQL(self):
        return WorkerSQL("SELECT * FROM ipy_names;", self.settings, self.section).connectPostgreSQL()
