from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(400, 200)

        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")

        self.label_count_0 = QtWidgets.QLabel(Form)

        font = QtGui.QFont()
        font.setPointSize(10)

        self.label_count_0.setFont(font)
        self.label_count_0.setStyleSheet("#label_count_0:hover {\n"
                                         "    background-color: rgba(220, 220, 220, 255);\n"
                                         "}")
        self.label_count_0.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_count_0.setObjectName("label_count_0")

        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_count_0)

        self.label_count_1 = QtWidgets.QLabel(Form)

        font = QtGui.QFont()
        font.setPointSize(10)

        self.label_count_1.setFont(font)
        self.label_count_1.setStyleSheet("#label_count_1:hover {\n"
                                         "    \n"
                                         "    background-color: rgba(0, 170, 0, 100);\n"
                                         "}\n"
                                         "")
        self.label_count_1.setObjectName("label_count_1")

        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_count_1)

        self.label_count_2 = QtWidgets.QLabel(Form)
        self.label_count_2.setEnabled(True)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)

        self.label_count_2.setFont(font)
        self.label_count_2.setStyleSheet("#label_count_2:hover {\n"
                                         "    background-color: rgb(0, 80, 255, 100);\n"
                                         "}\n"
                                         "")
        self.label_count_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_count_2.setObjectName("label_count_2")

        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_count_2)

        self.label_count_3 = QtWidgets.QLabel(Form)
        self.label_count_3.setEnabled(True)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)

        self.label_count_3.setFont(font)
        self.label_count_3.setStyleSheet("#label_count_3:hover {\n"
                                         "    background-color: rgb(255, 0, 0, 100);\n"
                                         "}\n"
                                         "")
        self.label_count_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_count_3.setObjectName("label_count_3")

        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_count_3)

        font = QtGui.QFont()
        font.setPointSize(10)

        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(False)

        font = QtGui.QFont()
        font.setPointSize(12)

        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.label)

        self.label_ex = QtWidgets.QLabel(Form)
        self.label_ex.setEnabled(False)

        font = QtGui.QFont()
        font.setPointSize(12)

        self.label_ex.setFont(font)
        self.label_ex.setAlignment(QtCore.Qt.AlignLeft)
        self.label_ex.setObjectName("label_ex")

        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.label_ex)

        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate

        Form.setWindowTitle(_translate("Form", "Form"))
