from ui.pages.front import (
    UI_StatisticPage,
    UI_SubscribersPage,
    UI_CreateTicketPage,
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
