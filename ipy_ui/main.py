# Front imports
from PyQt5.QtWidgets import QApplication, QMainWindow

# PostgreSQL Connector.
from packages.connector import WorkerSQL
from PyQt5.QtWidgets import QWidget
from ui.pages.front import (
    UI_MainWindow,
    findErrorWindow,
    successWindow,
    errorWindow,
    UI_LoginPage,
    UI_RegistrPage,
)

# Back pages classes / functions
from functions.back import (
    StatisticPage,
    SubscribersPage,
    CreateTicketPage,
    TicketsInfoPage,
    InfoPage,
    FindPage,
)

# Filter ascii
from string import ascii_letters

# Current time
from datetime import datetime

# Powershell execute
from subprocess import (
    Popen,
    PIPE,
)

from os import path

# Another imports
import logging
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = UI_MainWindow()
        self.ui.setupUi(self)
        self.StatisticPage = self.ui.pushButton
        self.InfoPage = self.ui.pushButton_2
        self.SubscribersPage = self.ui.pushButton_3
        self.CreateTicketPage = self.ui.pushButton_6
        self.TicketsInfoPage = self.ui.pushButton_4
        self.HomeSearch = self.ui.search_btn

        self.menu_buttons_dict = {
            self.StatisticPage: StatisticPage,
            self.InfoPage: InfoPage,
            self.SubscribersPage: SubscribersPage,
            self.CreateTicketPage: CreateTicketPage,
            self.TicketsInfoPage: TicketsInfoPage,
            self.HomeSearch: FindPage,
        }
        # Список игнорируемых букв
        self.ignored_letters = list(ascii_letters)

        # Домашняя страница при запуске
        self.show_home_window()

        # Присоединение сигналов
        self.ui.search_btn.clicked.connect(self.search_data)
        self.ui.tabWidget.tabCloseRequested.connect(self.close_tab)

        self.StatisticPage.clicked.connect(self.show_selected_window)
        self.InfoPage.clicked.connect(self.show_selected_window)
        self.SubscribersPage.clicked.connect(self.show_selected_window)
        self.CreateTicketPage.clicked.connect(self.show_selected_window)
        self.TicketsInfoPage.clicked.connect(self.show_selected_window)

    def show_home_window(self):
        result = self.open_tab_flag(self.StatisticPage.text())

        self.set_btn_checked(self.StatisticPage)

        if result[0]:
            self.ui.tabWidget.setCurrentIndex(result[1])

        else:
            tab_title = self.StatisticPage.text()
            current_index = self.ui.tabWidget.addTab(StatisticPage(), tab_title)

            self.ui.tabWidget.setVisible(current_index)
            self.ui.tabWidget.setVisible(True)

    def set_btn_checked(self, btn):
        for button in self.menu_buttons_dict.keys():
            if button != btn:
                button.setChecked(False)

            else:
                button.setChecked(True)

    def show_selected_window(self):
        button = self.sender()
        result = self.open_tab_flag(button.text())

        self.set_btn_checked(button)

        if result[0]:
            self.ui.tabWidget.setCurrentIndex(result[1])

        else:
            tab_title = button.text()
            current_index = self.ui.tabWidget.addTab(self.menu_buttons_dict[button](), tab_title)

            self.ui.tabWidget.setCurrentIndex(current_index)
            self.ui.tabWidget.setVisible(True)

    def show_fast_search(self, good_string):
        current_index = self.ui.tabWidget.addTab(FindPage(good_string), 'Поиск')

        self.ui.tabWidget.setCurrentIndex(current_index)
        self.ui.tabWidget.setVisible(True)

    def close_tab(self, index):
        self.ui.tabWidget.removeTab(index)

        if self.ui.tabWidget.count() == 0:
            self.ui.toolBox.setCurrentIndex(0)

            self.show_home_window()

    def open_tab_flag(self, btn_text):
        open_tab_count = self.ui.tabWidget.count()

        for i in range(open_tab_count):
            tab_title = self.ui.tabWidget.tabText(i)
            if tab_title == btn_text:

                return True, i

            else:
                continue

        return False,

    # Фильтр вводимой фразы в поисковую строку
    def search_data(self):
        bad_request = list()
        good_string = ''
        check_phrase = self.ui.lineEdit.text().strip()

        if len(check_phrase) < 35:
            for data in check_phrase:
                code = ord(data)
                if 1039 < code or (code == 1025 or code == 1105 or code == 32
                                   or code == 34 or code == 45 or code == 1103):
                    good_string += data
                else:
                    bad_request.append(data)

            if good_string == '' or good_string == ' ' \
                    or good_string == '  ' or good_string == '   ':
                logging.info('\n[!] [SEARCH] Request ignored : [{0}]'.format(bad_request))

                findErrorWindow(message=bad_request, text='Запрос пуст или содержит запрещённые символы.')

                bad_request.clear()

            if len(bad_request) > 0:
                logging.info('\n[!] [SEARCH] Filtered message : {0}'.format(bad_request))

                findErrorWindow(message=bad_request, text='Запрос пуст или содержит запрещённые символы.')

            # Фильтрация ошибочных запросов с содержанием пробелов или недопустимых символов
            elif len(good_string) != 0 and len(bad_request) == 0 and good_string != ' ' and good_string != '  ' \
                    and good_string != '   ' and good_string != '    ' and good_string != '     ' \
                    and good_string != '      ' and good_string != '      ' and good_string != '       ':

                # Ограничение открытых вкладок
                if int(self.ui.tabWidget.count()) > 5:
                    logging.info('\n[!] [COUNT] User limit max > 5')

                    findErrorWindow(message=int(self.ui.tabWidget.count()),
                                    text='Превышен лимит открытых вкладок, закройте некоторые\n'
                                         'и повторите запрос заново.')
                else:
                    self.show_fast_search(good_string)

            bad_request.clear()


class RegistrPage(QWidget):

    def __init__(self):
        super(RegistrPage, self).__init__()
        self.ui = UI_RegistrPage()
        self.ui.setupUi(self)

        self.mac = LoginWindow.macLocal()

        self.ui.lineEdit_2.setEnabled(False)
        self.ui.label_2.setText("MAC устройства: {0}".format(self.mac))

        self.ui.pushButton.clicked.connect(self.sendMessageSMTP)

    def sendMessageSMTP(self):
        message = str(self.ui.lineEdit.text().strip())
        time = datetime.now()

        try:
            bad_request = list()
            good_string = ''

            if len(message) < 30:
                for data in message:
                    code = ord(data)
                    if 1039 < code or (code == 1025 or code == 1105 or code == 32
                                       or code == 34 or code == 45 or code == 1103):
                        good_string += data
                    else:
                        bad_request.append(data)

                if good_string == '' or good_string == ' ' \
                        or good_string == '  ' or good_string == '   ':
                    findErrorWindow(message=bad_request, text='Запрос пуст или содержит запрещённые символы.')

                    bad_request.clear()

                if len(bad_request) > 0:
                    findErrorWindow(message=bad_request, text='Запрос пуст или содержит запрещённые символы.')

                # Фильтрация ошибочных запросов с содержанием пробелов или недопустимых символов
                elif len(good_string) != 0 and len(bad_request) == 0 and good_string != ' ' and good_string != '  ' \
                        and good_string != '   ' and good_string != '    ' and good_string != '     ' \
                        and good_string != '      ' and good_string != '      ' and good_string != '       ':

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
                    msg['Subject'] = 'ИПУ Регистрация [ {0} ] # [ {1} ] '.format('Регистрация нового пользователя',
                                                                                 time)

                    msg.attach(MIMEText('Требуется регистрация, логин : {0}\nMAC : {1}'
                                        .format(message, self.mac), 'plain'))

                    # Для работы с почтой mail.ru указываем 25 порт.
                    server = SMTP('smtp.mail.ru', 25, timeout=1)

                    server.starttls()
                    server.login(from_addr, ind_value)

                    text = msg.as_string()

                    server.sendmail(from_addr, to_addr, text)
                    server.quit()

                    successWindow('Сообщение успешно отправлено.')

                    self.ui.lineEdit.clear()
                    # self.ui.lineEdit_2.clear()

            else:
                errorWindow(message, 'Превышен лимит символов.')

        except Exception as ex:
            # Окно с ошибкой и информацией от искл.
            errorWindow(message=ex, text='Сообщение не отправлено.')

            # Запись в лог
            logging.error('[!] [EXCEPTION] Error SMTP, more info : {0}'.format(ex), exc_info=True)


class LoginWindow(QWidget):

    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui = UI_LoginPage()
        self.ui.setupUi(self)

        self.counterPassword = 0
        self.settings = 'packages/postgresql/database.ini'
        self.section = 'postgresql'
        self.mac = LoginWindow.macLocal()

        self.ui.loginButton.clicked.connect(self.verifyPassword)
        self.ui.commandLinkButton.clicked.connect(self.sendRegform)

    def sendRegform(self):
        WindowReg.show()
        self.close()

    @staticmethod
    def macLocal():
        valid_path = path.dirname(path.abspath("getmac.ps1"))
        fullPath = "{0}\\{1}\\{2}".format(valid_path, "functions\\modules", "getmac.ps1")
        p = Popen(["powershell.exe", fullPath], stdout=PIPE)
        mac_local = str(p.communicate()[0].decode('cp1251').replace("\r\n", "")).upper()

        return mac_local

    def verifyPassword(self):
        try:
            password_local = [self.ui.passwordEdit.text()]
            username_local = self.ui.usernameEdit.text()

            bad_request = list()
            good_string = ''
            check_phrase = self.ui.usernameEdit.text().strip()

            if len(check_phrase) < 10:
                for data in check_phrase:
                    code = ord(data)
                    if 1039 < code or (code == 1025 or code == 1105 or code == 32
                                       or code == 34 or code == 45 or code == 1103):
                        good_string += data
                    else:
                        bad_request.append(data)

                if good_string == '' or good_string == ' ' \
                        or good_string == '  ' or good_string == '   ':
                    logging.info('\n[!] [SEARCH] Request ignored : [{0}]'.format(bad_request))

                    findErrorWindow(message=bad_request, text='Запрос пуст или содержит запрещённые символы.')

                    bad_request.clear()

                if len(bad_request) > 0:
                    logging.info('\n[!] [SEARCH] Filtered message : {0}'.format(bad_request))

                    findErrorWindow(message=bad_request, text='Запрос пуст или содержит запрещённые символы.')

                # Фильтрация ошибочных запросов с содержанием пробелов или недопустимых символов
                elif len(good_string) != 0 and len(bad_request) == 0 and good_string != ' ' and good_string != '  ' \
                        and good_string != '   ' and good_string != '    ' and good_string != '     ' \
                        and good_string != '      ' and good_string != '      ' and good_string != '       ':
                    data = self.checkPostgreSQL("SELECT * FROM login_data WHERE login = '{0}';".format(good_string))

                    valid_username = data[0][0]
                    valid_password = data[0][1]
                    valid_mac = str(data[0][2]).upper()

                    if valid_password is None:
                        if username_local == valid_username and password_local[0] == '' \
                                and self.mac == valid_mac and self.counterPassword < 4:
                            Window.show()
                            self.close()
                        else:
                            # Окно с ошибкой и информацией от искл.
                            errorWindow(message='Without info', text='Данные для входа неверны!')
                    else:
                        if username_local == valid_username and password_local[0] == valid_password \
                                and self.mac == valid_mac and self.counterPassword < 4:
                            Window.show()
                            self.close()
        except Exception as ex:
            # Окно с ошибкой и информацией от искл.
            errorWindow(message='Without info', text='Данные для входа неверны!')

            # Запись в лог
            logging.error('[!] [EXCEPTION] Error login page, more info : {0}'.format(ex), exc_info=True)

    # Запрос к PostgreSQL.
    def checkPostgreSQL(self, request):
        if self.counterPassword > 1:
            self.ui.frame.setEnabled(False)
            self.ui.commandLinkButton.setEnabled(False)

            self.ui.label.setStyleSheet("background-color: rgba(255, 0, 0, 80)")
            self.ui.label.setText('Превышен лимит ввода пароля!')

            self.ui.passwordEdit.clear()
            self.ui.usernameEdit.clear()
        else:
            self.counterPassword += 1

            self.ui.label.setStyleSheet("background-color: rgba(255, 230, 0, 80)")
            self.ui.label.setText('Осталось попыток: {0}'.format(3 - self.counterPassword))

        return WorkerSQL(request, self.settings, self.section).connectPostgreSQL()


if __name__ == '__main__':
    # Логирование всех exceptions
    logging.basicConfig(level=logging.INFO,
                        filename='logs/stack.log',
                        filemode='w', format='%(asctime)s %(levelname)s %(message)s')

    # Запуск UI.
    MainPage = QApplication(sys.argv)

    WindowReg = RegistrPage()
    WindowVerify = LoginWindow()
    Window = MainWindow()

    WindowVerify.show()

    sys.exit(MainPage.exec_())
