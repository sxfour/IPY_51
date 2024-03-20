# -*- coding: utf-8 -*-

import mainImports.mainImports as mainConfig


# Главное окно.
class MainWindow(mainConfig.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = mainConfig.UI_MainWindow()
        self.ui.setupUi(self)
        self.StatisticPage = self.ui.pushButton
        self.InfoPage = self.ui.pushButton_2
        self.SubscribersPage = self.ui.pushButton_3
        self.CreateTicketPage = self.ui.pushButton_6
        self.CreateUserPage = self.ui.pushButton_4
        self.HomeSearch = self.ui.search_btn
        self.ConnectDatabasePage = self.ui.pushButtonAddConnection

        self.menu_buttons_dict = {
            self.StatisticPage: mainConfig.StatisticPage,
            self.InfoPage: mainConfig.InfoPage,
            self.SubscribersPage: mainConfig.SubscribersPage,
            self.CreateTicketPage: mainConfig.CreateTicketPage,
            self.CreateUserPage: mainConfig.CreateUserPage,
            self.HomeSearch: mainConfig.FindPage,
            self.ConnectDatabasePage: mainConfig.CreateDatabasePage
        }

        # Список игнорируемых букв
        self.ignored_letters = list(mainConfig.ascii_letters)

        # Домашняя страница при запуске
        self.show_home_window()

        # Присоединение сигналов
        self.ui.search_btn.clicked.connect(self.search_data)
        self.ui.tabWidget.tabCloseRequested.connect(self.close_tab)

        self.StatisticPage.clicked.connect(self.show_selected_window)
        self.InfoPage.clicked.connect(self.show_selected_window)
        self.SubscribersPage.clicked.connect(self.show_selected_window)
        self.CreateTicketPage.clicked.connect(self.show_selected_window)
        self.CreateUserPage.clicked.connect(self.show_selected_window)
        self.ConnectDatabasePage.clicked.connect(self.show_selected_window)

    def __del__(self):
        pass

    def show_home_window(self):
        result = self.open_tab_flag(self.StatisticPage.text())

        self.set_btn_checked(self.StatisticPage)

        if result[0]:
            self.ui.tabWidget.setCurrentIndex(result[1])

        else:
            tab_title = self.StatisticPage.text()
            current_index = self.ui.tabWidget.addTab(mainConfig.StatisticPage(), tab_title)

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
        current_index = self.ui.tabWidget.addTab(mainConfig.FindPage(good_string), 'Поиск')

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
                mainConfig.info('\n[!] [SEARCH] Request ignored : [{0}]'.format(bad_request))

                mainConfig.findErrorWindow(message=bad_request, text='Запрос пуст или содержит запрещённые символы.')

                bad_request.clear()

            if len(bad_request) > 0:
                mainConfig.info('\n[!] [SEARCH] Filtered message : {0}'.format(bad_request))

                mainConfig.findErrorWindow(message=bad_request, text='Запрос пуст или содержит запрещённые символы.')

            # Фильтрация ошибочных запросов с содержанием пробелов или недопустимых символов
            elif len(good_string) != 0 and len(bad_request) == 0 and good_string != ' ' and good_string != '  ' \
                    and good_string != '   ' and good_string != '    ' and good_string != '     ' \
                    and good_string != '      ' and good_string != '      ' and good_string != '       ':

                # Ограничение открытых вкладок
                if int(self.ui.tabWidget.count()) > 5:
                    mainConfig.info('\n[!] [COUNT] User limit max > 5')

                    mainConfig.findErrorWindow(message=int(self.ui.tabWidget.count()),
                                               text='Превышен лимит открытых вкладок, закройте некоторые\n'
                                                    'и повторите запрос заново.')
                else:
                    self.show_fast_search(good_string)

            bad_request.clear()


# Окно регистрации пользователя.
class RegistrPage(mainConfig.QWidget):

    def __init__(self):
        super(RegistrPage, self).__init__()
        self.ui = mainConfig.UI_RegistrPage()
        self.ui.setupUi(self)

        self.ui.lineEdit_2.setEnabled(False)
        self.ui.pushButton.clicked.connect(self.sendMessageSMTP)

    def __del__(self):
        pass

    def sendMessageSMTP(self):
        mac_adress = str(
            ':'.join(['{:02x}'.format((mainConfig.getnode() >> ele) & 0xff) for ele in range(0, 8 * 6, 8)][::-1]))
        message = str(self.ui.lineEdit.text().strip())
        identificator = LoginWindow.uuid_generate(username=message + mac_adress)
        time = mainConfig.datetime.now()

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
                    mainConfig.findErrorWindow(message=bad_request,
                                               text='Запрос пуст или содержит запрещённые символы.')

                    bad_request.clear()

                if len(bad_request) > 0:
                    mainConfig.findErrorWindow(message=bad_request,
                                               text='Запрос пуст или содержит запрещённые символы.')

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

                    # Token for app : Ggcf7gRcSS2Drn4VeReP
                    ind_value = "Ggcf7gRcSS2Drn4VeReP"

                    msg = MIMEMultipart()

                    msg['From'] = from_addr
                    msg['To'] = to_addr
                    msg['Subject'] = 'ИПУ Регистрация [ {0} ] # [ {1} ] '.format('Регистрация нового пользователя',
                                                                                 time)

                    msg.attach(MIMEText('Логин : {0}\nПароль : \nUUID : {1}'
                                        .format(message, identificator), 'plain'))

                    # Для работы с почтой mail.ru указываем 25 порт.
                    server = SMTP('smtp.mail.ru', 25, timeout=1)

                    server.starttls()
                    server.login(from_addr, ind_value)

                    text = msg.as_string()

                    server.sendmail(from_addr, to_addr, text)
                    server.quit()

                    mainConfig.successWindow('Сообщение успешно отправлено.')

                    self.ui.lineEdit.clear()
                    # self.ui.lineEdit_2.clear()

            else:
                mainConfig.errorWindow(message, 'Превышен лимит символов.')

        except Exception as ex:
            # Окно с ошибкой и информацией от искл.
            mainConfig.errorWindow(message=ex, text='Сообщение не отправлено.')

            # Запись в лог
            mainConfig.error('[!] [EXCEPTION] Error SMTP, more info : {0}'.format(ex), exc_info=True)


# Окно входа.
class LoginWindow(mainConfig.QWidget):

    def __init__(self):
        super(LoginWindow, self).__init__()

        self.ui = mainConfig.UI_LoginPage()
        self.ui.setupUi(self)

        self.counterPassword = 0
        self.isPathAutoLogin = False
        self.settings = 'packages/postgresql/database.ini'
        self.section = 'postgresql'

        self.ui.loginButton.clicked.connect(self.verifyUsername)
        self.ui.commandLinkButton.clicked.connect(self.sendRegform)

        self.checkAutoLogin()

    def __del__(self):
        pass

    # Нажатие Enter
    def keyPressEvent(self, event):
        if isinstance(event, mainConfig.QKeyEvent):
            if event.key() == 16777220:
                self.ui.loginButton.click()

    def checkAutoLogin(self):
        try:
            with open('data_json/auto_login.json', 'r', encoding='utf8') as json_file:
                self.ui.usernameEdit.setText(str(mainConfig.load(json_file)['login']))
                self.ui.rememberMe.setChecked(True)
        except FileNotFoundError as ex:
            # Запись в лог
            mainConfig.error('[!] [EXCEPTION] Error checkAutoLogin, more info : {0}'.format(ex), exc_info=True)

    # Показ окна регистрации.
    def sendRegform(self):
        WindowReg.show()
        self.close()

    # Проверка логина.
    def verifyUsername(self):
        try:
            mac_adress = str(':'.join(
                ['{:02x}'.format((mainConfig.getnode() >> ele) & 0xff) for ele in range(0, 8 * 6, 8)][::-1]))
            password_local = [self.ui.passwordEdit.text()]
            username_local = self.ui.usernameEdit.text()
            identificator = str(LoginWindow.uuid_generate(username=username_local + mac_adress))

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
                    mainConfig.info('\n[!] [SEARCH] Request ignored : [{0}]'.format(bad_request))

                    mainConfig.findErrorWindow(message=bad_request,
                                               text='Запрос пуст или содержит запрещённые символы.')

                    bad_request.clear()

                if len(bad_request) > 0:
                    mainConfig.info('\n[!] [SEARCH] Filtered message : {0}'.format(bad_request))

                    mainConfig.findErrorWindow(message=bad_request,
                                               text='Запрос пуст или содержит запрещённые символы.')

                # Фильтрация ошибочных запросов с содержанием пробелов или недопустимых символов
                elif len(good_string) != 0 and len(bad_request) == 0 and good_string != ' ' and good_string != '  ' \
                        and good_string != '   ' and good_string != '    ' and good_string != '     ' \
                        and good_string != '      ' and good_string != '      ' and good_string != '       ':
                    data = self.checkPostgreSQL("SELECT * FROM login_data WHERE login = '{0}';".format(good_string))

                    valid_username = data[0][0]
                    valid_password = data[0][1]
                    valid_uuid = str(data[0][2])

                    if valid_password is None:
                        if username_local == valid_username and password_local[0] == '' \
                                and identificator == valid_uuid and self.counterPassword < 4:
                            Window.show()
                            self.close()
                        else:
                            # Окно с ошибкой и информацией от искл.
                            mainConfig.errorWindow(message='Without info', text='Данные для входа неверны!')
                    else:
                        if username_local == valid_username and password_local[0] == valid_password \
                                and self.mac == valid_uuid and self.counterPassword < 4:
                            Window.show()
                            self.close()

                    # Получаем данные с запомнить и сохраняем в json
                    if self.ui.rememberMe.isChecked():
                        dataToSaveJson = {'login': str(valid_username), 'password': valid_password, 'uuid': valid_uuid}
                        with open('data_json/auto_login.json', 'w') as file:
                            mainConfig.dump(dataToSaveJson, file)
                    elif not self.ui.rememberMe.isChecked():
                        try:
                            mainConfig.remove('data_json/auto_login.json')
                        except FileNotFoundError as ex:
                            # Запись в лог
                            mainConfig.error('[!] [EXCEPTION] Error file path, more info : {0}'.format(ex),
                                             exc_info=True)

        except Exception as ex:
            # Окно с ошибкой и информацией от искл.
            mainConfig.errorWindow(message='Without info', text='Данные для входа неверны!')
            # Запись в лог
            mainConfig.error('[!] [EXCEPTION] Error login page, more info : {0}'.format(ex), exc_info=True)

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

        return mainConfig.WorkerSQL(request, self.settings, self.section).connectPostgreSQL()

    # Декоратор c созданием uuid.
    @staticmethod
    def uuid_generate(username) -> mainConfig.UUID:
        return mainConfig.uuid3(mainConfig.NAMESPACE_DNS, username)


if __name__ == '__main__':
    # Логирование всех искл в файл
    mainConfig.basicConfig(level=mainConfig.INFO,
                           filename='logs/stack.log',
                           filemode='w',
                           format='%(asctime)s %(levelname)s %(message)s',
                           encoding="utf-8")

    # Запуск UI.
    MainPage = mainConfig.QApplication(mainConfig.sys.argv)
    WindowReg = RegistrPage()
    WindowVerify = LoginWindow()
    Window = MainWindow()

    WindowVerify.show()

    mainConfig.sys.exit(MainPage.exec_())
