from PyQt5.QtWidgets import QWidget
from ui.pages.home_5 import Ui_Form


class Home_5(QWidget):

    def __init__(self):
        super(Home_5, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
