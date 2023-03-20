from packages.connector import WorkerSQL
from ui.pages.error import errorWindow
from PyQt5.QtWidgets import QWidget
from ui.pages.home_1 import Ui_Form
from logging import error


class Home_1(QWidget, object):

    def __init__(self):
        super(Home_1, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.settings = 'packages/postgresql/database.ini'
        self.section = 'postgresql'

        self.setWindow()

    def setWindow(self):
        try:
            data = self.checkPostgreSQL()[0]
            self.ui.label_1.setText('Версия : {0}\n Дата запроса : {1}'.format(data[0], data[1]))
        except Exception as ex:
            self.ui.label_1.setText('— Простите, а что, совсем никого нет дома?\n'
                                    '— Совсем никого.\n'
                                    '— Что-то здесь не так.\nКто-то там все-таки есть!\n'
                                    'Кто-то же должен был сказать «совсем никого»!')

            # Запись в лог
            error('[!] [EXCEPTION] Error, more info : {0}'.format(ex), exc_info=True)

            # Окно с ошибкой и информацией от искл
            errorWindow(message=ex, text='Соединение сброшено, обратитесь к администратору.')

    # Запрос к PostgreSQL
    def checkPostgreSQL(self):
        return WorkerSQL("SELECT version(), CURRENT_DATE;", self.settings, self.section).connectPostgreSQL()
