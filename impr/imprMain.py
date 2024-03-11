from uuid import (
    UUID,
    uuid3,
    NAMESPACE_DNS,
    getnode,
)
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
)
from packages.connector import WorkerSQL
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QKeyEvent
from string import ascii_letters
from datetime import datetime
from ui.pages.front import (
    findErrorWindow,
    successWindow,
    errorWindow,
    UI_LoginPage,
    UI_RegistrPage,
    UI_MainWindow,
)
from functions.back import (
    StatisticPage,
    SubscribersPage,
    CreateTicketPage,
    CreateUserPage,
    InfoPage,
    FindPage,
)
from logging import (
    basicConfig,
    info,
    error,
    INFO,
)

from json import (
    dump,
    load,
)

from os import (
    remove,
    path,
)

import sys