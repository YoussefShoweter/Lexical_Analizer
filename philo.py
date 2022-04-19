# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'philo.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import re
from PyQt5 import QtCore, QtGui, QtWidgets,QtWebEngineWidgets
import copy
from New import get_tokens_list
import  New
from animated import tiny_transitions, G

class Ui_philo(object):
    def setupUi(self, philo):
        philo.setObjectName("philo")
        philo.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(philo)
        self.centralwidget.setObjectName("centralwidget")

        self.nextSateButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextSateButton.setGeometry(QtCore.QRect(30, 760, 100, 32))
        self.nextSateButton.setObjectName("nextSateButton")

        self.textEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(420, 400, 350, 131))
        self.textEdit.setObjectName("textEdit")

        self.regexButton = QtWidgets.QPushButton(self.centralwidget)
        self.regexButton.setGeometry(QtCore.QRect(570, 560, 141, 51))
        self.regexButton.setObjectName("regexButton")

        self.regexLabel = QtWidgets.QLabel(self.centralwidget)
        self.regexLabel.setGeometry(QtCore.QRect(500, 370, 288, 16))
        self.regexLabel.setObjectName("regexLabel")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 350, 391, 400))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        philo.setCentralWidget(self.centralwidget)

        self.retranslateUi(philo)
        QtCore.QMetaObject.connectSlotsByName(philo)
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webEngineView.setGeometry(QtCore.QRect(20, 10, 760, 330))
        self.webEngineView.setObjectName("webEngineView")

    def retranslateUi(self, philo):
        _translate = QtCore.QCoreApplication.translate
        philo.setWindowTitle(_translate("philo", "Tiny Compiler"))
        self.nextSateButton.setText(_translate("philo", "Next State"))
        self.regexButton.setText(_translate("philo", "Check Regex"))
        self.regexButton.clicked.connect(self.onClickTokenize)
        self.regexLabel.setText(_translate("philo", "Regex Label"))






        # self.label.setText(_translate("MainWindow", "            Insert your code here:"))

        self.textEdit.setPlaceholderText( "Input your Code here")
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("philo", "Token"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("philo", "Type"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("philo", "From"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("philo", "To"))

        self.tableWidget.setColumnWidth(0, 90)
        self.tableWidget.setColumnWidth(1, 90)
        self.tableWidget.setColumnWidth(2, 115)
        self.tableWidget.setColumnWidth(3, 115)
        self.nextSateButton.setText("Next state ")


        self.nextSateButton.clicked.connect(self.OnClickNextState)


    def onClickTokenize(self):
        input_code = str(self.textEdit.toPlainText())
        self.regexLabel.setText(New.check(input_code))
        self.G = copy.deepcopy(G)
        self.tokens = self.get_tokens_tabledata(input_code)
        print(self.tokens)
        G.save_graph("animated.html")
        self.webEngineView.load(QtCore.QUrl.fromLocalFile("\\animated.html"))
        self.webEngineView.show()
        self.tableWidget.setRowCount(len(self.tokens))
        self.n = 0
        print(self.n)

#
#
    def OnClickNextState(self):
        if self.n < len(self.tokens):
            token = self.tokens[self.n]
            self.tableWidget.setItem(self.n, 0, QtWidgets.QTableWidgetItem(token["token"]))
            self.tableWidget.setItem(self.n, 1, QtWidgets.QTableWidgetItem(token["type"]))
            self.tableWidget.setItem(self.n, 2, QtWidgets.QTableWidgetItem(token["current"]))
            self.tableWidget.setItem(self.n, 3, QtWidgets.QTableWidgetItem(token["next"]))
            self.G.nodes[int(token["current"]) - 1]["color"] = 'red'
            self.G.nodes[int(token["next"]) - 1]["color"] = {"background": 'indigo', "border": 'purple'}
            self.G.save_graph("animated.html")
            self.redisplayDFA()
        else:
            self.G.nodes[int(self.tokens[-1]["next"]) - 1]["color"] = {"background": 'lime', "border": 'pink'}
            self.G.save_graph("animated.html")
            self.redisplayDFA()

        self.n = self.n + 1

    # def get_tokens_tabledata(self, input_code):
    #     tokens_list = get_tokens_list(input_code)
    #     print(tokens_list)
    #
    #     current = '1'
    #     for token in tokens_list:
    #         token["current"] = current
    #         if token["type"] not in tiny_transitions[current]:
    #             next = '12'
    #             self.G.add_edge(int(current), 12)
    #         else:
    #             next = tiny_transitions[current][token["type"]]
    #             token["next"] = next
    #             current = next
    #     return tokens_list
    def get_tokens_tabledata(self, input_code):
        tokens_list = get_tokens_list(input_code)
        if tokens_list is None:
            return None
        else:
            current = '1'
            for token in tokens_list:
                token["current"] = current
                if token["type"] not in tiny_transitions[current]:
                    next = '11'
                    self.G.add_edge(int(current), 11)
                else:
                    next = tiny_transitions[current][token["type"]]
                token["next"] = next
                current = next
            return tokens_list

    def redisplayDFA(self):
        self.webEngineView.close()
        self.webEngineView.load(QtCore.QUrl.fromLocalFile("\\animated.html"))
        self.webEngineView.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    philo = QtWidgets.QMainWindow()
    ui = Ui_philo()
    ui.setupUi(philo)
    philo.show()
    sys.exit(app.exec_())
