from PyQt5.QtWidgets import QWidget
from ui.pages.home_3 import Ui_Form


def callback(result):
    print(result)


class Home_3(QWidget, object):

    def __init__(self):
        super(Home_3, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.label.setText('Пустота, да и только...')
