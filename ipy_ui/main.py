# Front imports
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.pages.all_pages_front import (
    UI_MainWindow,
    findErrorWindow,
)

# Back pages classes / functions
from functions.all_pages_back import (
    StatisticPage,
    SubscribersPage,
    CreateTicketPage,
    TicketsInfoPage,
    InfoPage,
    FindPage,
)

# Filter ascii
from string import ascii_letters

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
        self.TicketsInfoPage = self.ui.pushButton_7
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
                    and good_string != '   ' and good_string != '    ' and good_string != '     '\
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


if __name__ == '__main__':
    # Логирование всех exceptions
    logging.basicConfig(level=logging.INFO, filename='logs/stack.log',
                        filemode='w', format='%(asctime)s %(levelname)s %(message)s')

    # Запуск основного UI
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec_())
