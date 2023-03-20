from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon


def errorWindow(message, text):
    error = QMessageBox()
    error.setWindowIcon(QIcon('ui/ico_main/oops.png'))
    error.setWindowTitle('Ошибка')
    error.setText(text)
    error.setIcon(QMessageBox.Warning)
    error.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
    error.setDefaultButton(QMessageBox.Ok)
    error.setDetailedText('Details : {0}'.format(message))

    buttonCancel = error.button(QMessageBox.Cancel)

    buttonCancel.setText('Отмена')

    error.exec_()


def successWindow(message):
    success = QMessageBox()
    success.setWindowIcon(QIcon('ui/ico_main/ico.png'))
    success.setWindowTitle('ИПУ Тестирование')
    success.setText(message)
    success.setIcon(QMessageBox.Information)
    success.setStandardButtons(QMessageBox.Ok)

    success.exec_()
