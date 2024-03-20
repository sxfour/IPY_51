# -*- coding: utf-8 -*-

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

from ui.pages.front import (
    UI_StatisticPage,
    UI_SubscribersPage,
    UI_CreateTicketPage,
    UI_ConnectDatabasePage,
    UI_CreatePage,
    UI_FindPage,
    UI_InfoPage,
    successWindow,
    errorWindow,
)
from PyQt5.QtWidgets import QWidget
from PyQt5 import (
    QtWidgets,
    QtGui,
)
from random import randint
from logging import (
    error,
    info,
)
from packages.connector import WorkerSQL
from datetime import datetime
from time import strptime
from csv import writer
from os import path

from functions.back import (
    StatisticPage,
    SubscribersPage,
    CreateTicketPage,
    CreateDatabasePage,
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
)

import sys
