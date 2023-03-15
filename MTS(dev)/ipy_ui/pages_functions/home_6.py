from PyQt5.QtWidgets import QWidget
from ui.pages.home_6 import Ui_Form


class Home_6(QWidget):

    def __init__(self):
        super(Home_6, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
