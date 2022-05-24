
from PyQt5 import QtCore, QtGui, QtWidgets,QtWebEngineWidgets
import copy
from New import Obtain_Tokens_from_text0
import  New
from animated import Token_transitions, G

#REPEAT x:=m;x:=3;UNTIL z=9

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
        self.textEdit.setGeometry(QtCore.QRect(420, 530, 350, 131))
        self.textEdit.setObjectName("textEdit")

        self.regexButton = QtWidgets.QPushButton(self.centralwidget)
        self.regexButton.setGeometry(QtCore.QRect(530, 690, 141, 51))
        self.regexButton.setObjectName("regexButton")

        self.legend1 = QtWidgets.QLabel(self.centralwidget)
        self.legend1.setGeometry(QtCore.QRect(450, 350, 288, 16))
        self.legend1.setObjectName("legend1")

        self.legend2 = QtWidgets.QLabel(self.centralwidget)
        self.legend2.setGeometry(QtCore.QRect(450, 370, 288, 16))
        self.legend2.setObjectName("legend2")

        self.legend3 = QtWidgets.QLabel(self.centralwidget)
        self.legend3.setGeometry(QtCore.QRect(450, 390, 288, 16))
        self.legend3.setObjectName("legend3")

        self.legend4 = QtWidgets.QLabel(self.centralwidget)
        self.legend4.setGeometry(QtCore.QRect(450, 410, 288, 16))
        self.legend4.setObjectName("legend4")

        self.legend5 = QtWidgets.QLabel(self.centralwidget)
        self.legend5.setGeometry(QtCore.QRect(450, 430, 288, 16))
        self.legend5.setObjectName("legend5")


        self.legend6 = QtWidgets.QLabel(self.centralwidget)
        self.legend6.setGeometry(QtCore.QRect(450, 450, 288, 16))
        self.legend6.setObjectName("legend6")

        self.legend7 = QtWidgets.QLabel(self.centralwidget)
        self.legend7.setGeometry(QtCore.QRect(450, 470, 288, 16))
        self.legend7.setObjectName("legend7")

        self.regexLabel = QtWidgets.QLabel(self.centralwidget)
        self.regexLabel.setGeometry(QtCore.QRect(430, 500, 360, 25))
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

        # font = QtGui.QFont()
        # font.setPointSize(0)
        # font.setBold(True)
        # font.setWeight(75)
        # self.regexLabel.setStyleSheet("font")
        self.legend1.setStyleSheet("background-color: orange;")
        self.legend2.setStyleSheet("background-color: red;")
        self.legend3.setStyleSheet("background-color: lightblue;")
        self.legend4.setStyleSheet("background-color:lightgreen; ")
        self.legend5.setStyleSheet("background-color: yellow;")
        self.legend6.setStyleSheet("background-color: grey;")
        self.legend7.setStyleSheet("background-color: black;"
                                   "color:white")




        self.regexButton.setStyleSheet("background-color: lightblue;"
                                       "border-style: outset;"
                                        "border-width: 1px;"
                                        "border-radius: 15px;"
                                        "border-color: black;"
                                        "padding: 4px;"
                                       )
        self.nextSateButton.setStyleSheet("background-color: lightblue;"
                                       "border-style: outset;"
                                       "border-width: 1px;"
                                       "border-radius: 15px;"
                                       "border-color: black;"
                                       "padding: 4px;"
                                       )






    def retranslateUi(self, philo):
        _translate = QtCore.QCoreApplication.translate
        philo.setWindowTitle(_translate("philo", "Case 4 Lexical Analyzer"))
        self.nextSateButton.setText(_translate("philo", "Next State"))
        self.regexButton.setText(_translate("philo", "Check Regex"))
        self.regexButton.clicked.connect(self.TransfertoTokens)
        self.regexLabel.setText(_translate("philo", "Regex Label"))
        self.legend1.setText(_translate("philo", "Current state --> Orange"))
        self.legend2.setText(_translate("philo", "Previous states --> Red"))
        self.legend3.setText(_translate("philo", "Undiscovered States"))
        self.legend4.setText(_translate("philo", "Goal state --> Green"))
        self.legend5.setText(_translate("philo", "Final state --> Yellow"))
        self.legend6.setText(_translate("philo", "Stuck State --> Grey"))
        self.legend7.setText(_translate("philo", "Option states --> Black"))









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
        self.nextSateButton.setText("Next Token ")


        self.nextSateButton.clicked.connect(self.NextTokenButton)


    def TransfertoTokens(self):

        input_code = str(self.textEdit.toPlainText())
        if New.check(input_code) =="ACCEPTED  ...Correct Syntax":
            self.regexLabel.setStyleSheet("QLabel{font-size: 11pt;color:green;}")

        else:
            self.regexLabel.setStyleSheet("QLabel{font-size: 11pt;color:red;}" )
            # if New.within(input_code)==False:
            #     self.webEngineView.close()

        self.regexLabel.setText(New.check(input_code))
        self.G = copy.deepcopy(G)
        self.tokens = self.Table_view_Tokens(input_code)
        G.save_graph("animated.html")
        self.webEngineView.load(QtCore.QUrl.fromLocalFile("\\animated.html"))
        self.webEngineView.show()
        self.tableWidget.setRowCount(len(self.tokens))
        self.n = 0
        print(self.n)

#
#
    def NextTokenButton(self):
        if self.n < len(self.tokens):
            token = self.tokens[self.n]
            self.tableWidget.setItem(self.n, 0, QtWidgets.QTableWidgetItem(token["token"]))
            self.tableWidget.setItem(self.n, 1, QtWidgets.QTableWidgetItem(token["type"]))
            self.tableWidget.setItem(self.n, 2, QtWidgets.QTableWidgetItem(token["current"]))
            self.tableWidget.setItem(self.n, 3, QtWidgets.QTableWidgetItem(token["next"]))
            self.G.nodes[int(token["current"]) - 1]["color"] = 'red'
            self.G.nodes[int(token["next"]) - 1]["color"] = {"background": 'orange', "border": 'black'}
            self.G.save_graph("animated.html")
            self.InteractiveDFA()
        else:
            self.G.nodes[int(self.tokens[-1]["next"]) - 1]["color"] = {"background": 'yellow', "border": 'black'}
            self.G.save_graph("animated.html")
            self.InteractiveDFA()

        self.n = self.n + 1


    def Table_view_Tokens(self, input_code):
        tokens_list = Obtain_Tokens_from_text0(input_code)
        if tokens_list is None:
            return None
        else:
            current = '1'
            for token in tokens_list:
                token["current"] = current
                if token["type"] not in Token_transitions[current]:
                    next = '11'
                    self.G.add_edge(int(current), 11)
                else:
                    next = Token_transitions[current][token["type"]]
                token["next"] = next
                current = next
            return tokens_list

    def InteractiveDFA(self):
        self.webEngineView.close()
        self.webEngineView.load(QtCore.QUrl.fromLocalFile("\\animated.html"))

        self.webEngineView.load(QtCore.QUrl.fromLocalFile("\\animated.html"))
        self.webEngineView.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    philo = QtWidgets.QMainWindow()
    # philo.setStyleSheet("background-color:lightblue;")
    philo.setWindowIcon(QtGui.QIcon("1.png"))

    ui = Ui_philo()
    ui.setupUi(philo)
    philo.show()
    sys.exit(app.exec_())
