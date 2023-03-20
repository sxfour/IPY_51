from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.ipy_main_window import Ui_MainWindow
from pages_functions.home_1 import Home_1
from pages_functions.home_2 import Home_2
from pages_functions.home_3 import Home_3, callback
from pages_functions.home_5 import Home_5
from pages_functions.home_6 import Home_6
from pages_functions.home_0 import Home
from string import ascii_letters

import logging
import sys


class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.home_btn = self.ui.pushButton
        self.home_btn_0 = self.ui.pushButton_2
        self.home_btn_1 = self.ui.pushButton_3
        self.home_btn_2 = self.ui.pushButton_4
        self.home_btn_4 = self.ui.pushButton_6
        self.home_btn_5 = self.ui.pushButton_7
        self.home_search = self.ui.search_btn

        self.menu_buttons_dict = {
            self.home_btn: Home,
            self.home_btn_0: Home_1,
            self.home_btn_1: Home_2,
            self.home_btn_2: Home_3,
            self.home_btn_4: Home_5,
            self.home_btn_5: Home_6,
            self.home_search: Home_3,
        }

        # Список игнорируемых букв
        self.ignored_letters = list(ascii_letters)

        # Домашняя страница при запуске
        self.show_home_window()

        # Присоединение сигналов
        self.ui.search_btn.clicked.connect(self.search_data)
        self.ui.tabWidget.tabCloseRequested.connect(self.close_tab)

        self.home_btn.clicked.connect(self.show_selected_window)
        self.home_btn_0.clicked.connect(self.show_selected_window)
        self.home_btn_1.clicked.connect(self.show_selected_window)
        self.home_btn_2.clicked.connect(self.show_selected_window)
        self.home_btn_4.clicked.connect(self.show_selected_window)
        self.home_btn_5.clicked.connect(self.show_selected_window)

    def show_home_window(self):
        result = self.open_tab_flag(self.home_btn.text())

        self.set_btn_checked(self.home_btn)

        if result[0]:
            self.ui.tabWidget.setCurrentIndex(result[1])
        else:
            tab_title = self.home_btn.text()
            current_index = self.ui.tabWidget.addTab(Home(), tab_title)

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
            print('1')
            self.ui.tabWidget.setCurrentIndex(result[1])
        else:
            tab_title = button.text()
            current_index = self.ui.tabWidget.addTab(self.menu_buttons_dict[button](),
                                                     tab_title)

            self.ui.tabWidget.setCurrentIndex(current_index)
            self.ui.tabWidget.setVisible(True)

    def show_fast_search(self, good_string):
        tab_title = 'Поиск'
        button = self.sender()
        current_index = self.ui.tabWidget.addTab(self.menu_buttons_dict[button](),
                                                 tab_title)

        self.ui.tabWidget.setCurrentIndex(current_index)

        callback(result=good_string)

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

    # Фильтр вводимой фразы пользователем
    def search_data(self):
        bad_request = list()
        good_string = ''
        check_phrase = self.ui.lineEdit.text().strip()
        if len(check_phrase) < 35:
            for data in check_phrase:
                code = ord(data)
                if 1039 < code or (code == 1025 or code == 1105
                                   or code == 32 or code == 34
                                   or code == 45 or code == 1103):
                    good_string += data
                else:
                    bad_request.append(data)
            if good_string == '' or good_string == ' ' \
                    or good_string == '  ' or good_string == '   ':
                logging.info('\n[!] [SEARCH] Request ignored : [{0}]'.format(good_string))
            else:
                self.show_fast_search(good_string)

                logging.info('\n[+] [SEARCH] Request good : [{0}]'.format(good_string))

            logging.info('\n[!] [SEARCH] Filtered message : {0}'.format(bad_request))
        else:
            logging.info('\n[!] [SEARCH] Request ignored : [{0}]'.format(check_phrase))


if __name__ == '__main__':
    # Логирование всех exceptions
    logging.basicConfig(level=logging.INFO, filename='logs/stack.log',
                        filemode='w', format='%(asctime)s %(levelname)s %(message)s')

    # Запуск основного UI
    app = QApplication(sys.argv)
    window = MyWindow()

    window.show()

    sys.exit(app.exec_())
