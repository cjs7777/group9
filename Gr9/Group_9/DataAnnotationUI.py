from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1035, 755)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1031, 988))
        self.tabWidget.setStyleSheet("QTabBar::tab{width:120}\n"
"QTabBar::tab{height:40}\n"
"QTabBar::tab{ background-color: gray }")
        self.tabWidget.setIconSize(QtCore.QSize(25, 25))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(390, 60, 211, 51))
        self.textBrowser.setStyleSheet("QTextBrowser{border-width:0;border-style:outset}")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_2.setGeometry(QtCore.QRect(110, 170, 171, 41))
        self.textBrowser_2.setStyleSheet("QTextBrowser{border-width:0;border-style:outset}")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_3.setGeometry(QtCore.QRect(110, 300, 171, 41))
        self.textBrowser_3.setStyleSheet("QTextBrowser{border-width:0;border-style:outset}")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(330, 170, 361, 41))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_2.setGeometry(QtCore.QRect(330, 300, 361, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(440, 420, 111, 51))
        self.pushButton.setStyleSheet("QPushButton{ font-family:\'Microsoft YaHei\';font-size:23px;color:#666666;}")
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_4.setGeometry(QtCore.QRect(360, 30, 261, 51))
        self.textBrowser_4.setStyleSheet("QTextBrowser{border-width:0;border-style:outset}")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.listWidget = QtWidgets.QListWidget(self.tab_3)
        self.listWidget.setGeometry(QtCore.QRect(140, 130, 231, 371))
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(self.tab_3)
        self.listWidget_2.setGeometry(QtCore.QRect(610, 130, 301, 371))
        self.listWidget_2.setObjectName("listWidget_2")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_5.setGeometry(QtCore.QRect(160, 80, 171, 41))
        self.textBrowser_5.setStyleSheet("QTextBrowser{border-width:0;border-style:outset}")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 530, 101, 41))
        self.pushButton_2.setStyleSheet("QPushButton{ font-family:\'Microsoft YaHei\';font-size:18px;color:#666666;}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 530, 101, 41))
        self.pushButton_3.setStyleSheet("QPushButton{ font-family:\'Microsoft YaHei\';font-size:18px;color:#666666;}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_4.setGeometry(QtCore.QRect(610, 530, 101, 41))
        self.pushButton_4.setStyleSheet("QPushButton{ font-family:\'Microsoft YaHei\';font-size:18px;color:#666666;}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_5.setGeometry(QtCore.QRect(800, 530, 101, 41))
        self.pushButton_5.setStyleSheet("QPushButton{ font-family:\'Microsoft YaHei\';font-size:18px;color:#666666;}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_6.setGeometry(QtCore.QRect(450, 30, 201, 51))
        self.textBrowser_6.setStyleSheet("QTextBrowser{border-width:0;border-style:outset}")
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_7.setGeometry(QtCore.QRect(30, 20, 101, 31))
        self.textBrowser_7.setStyleSheet("QTextBrowser{border-width:0;border-style:outset}")
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_3.setGeometry(QtCore.QRect(150, 20, 251, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_8.setGeometry(QtCore.QRect(10, 60, 131, 31))
        self.textBrowser_8.setStyleSheet("QTextBrowser{border-width:0;border-style:outset}")
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.textEdit_4 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_4.setGeometry(QtCore.QRect(150, 60, 251, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.listWidget_3 = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_3.setGeometry(QtCore.QRect(0, 110, 761, 431))
        self.listWidget_3.setObjectName("listWidget_3")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        self.listWidget_4 = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_4.setGeometry(QtCore.QRect(760, 110, 271, 601))
        self.listWidget_4.setObjectName("listWidget_4")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser_9.setGeometry(QtCore.QRect(410, 40, 211, 51))
        self.textBrowser_9.setStyleSheet("QTextBrowser{border-width:0;border-style:outset}")
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.textEdit_5 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_5.setGeometry(QtCore.QRect(330, 120, 421, 41))
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_6 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_6.setGeometry(QtCore.QRect(330, 210, 231, 41))
        self.textEdit_6.setObjectName("textEdit_6")
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser_10.setGeometry(QtCore.QRect(120, 120, 171, 41))
        self.textBrowser_10.setStyleSheet("QTextBrowser{border-width:0;border-style:outset}")
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser_11.setGeometry(QtCore.QRect(120, 210, 171, 41))
        self.textBrowser_11.setStyleSheet("QTextBrowser{border-width:0;border-style:outset}")
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.label = QtWidgets.QLabel(self.tab_4)
        self.label.setGeometry(QtCore.QRect(360, 310, 191, 131))
        self.label.setObjectName("label")
        self.textBrowser_12 = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser_12.setGeometry(QtCore.QRect(120, 470, 171, 41))
        self.textBrowser_12.setStyleSheet("QTextBrowser{border-width:0;border-style:outset}")
        self.textBrowser_12.setObjectName("textBrowser_12")
        self.textEdit_7 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_7.setGeometry(QtCore.QRect(320, 470, 431, 41))
        self.textEdit_7.setObjectName("textEdit_7")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_6.setGeometry(QtCore.QRect(300, 550, 111, 51))
        self.pushButton_6.setStyleSheet("QPushButton{ font-family:\'Microsoft YaHei\';font-size:23px;color:#666666;}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_7.setGeometry(QtCore.QRect(550, 550, 111, 51))
        self.pushButton_7.setStyleSheet("QPushButton{ font-family:\'Microsoft YaHei\';font-size:23px;color:#666666;}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.textBrowser_13 = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser_13.setGeometry(QtCore.QRect(120, 360, 171, 41))
        self.textBrowser_13.setStyleSheet("QTextBrowser{border-width:0;border-style:outset}")
        self.textBrowser_13.setObjectName("textBrowser_13")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\">数据爬取</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">请输入网址：</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">保存路径：</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "爬虫"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\">自定义标签类</span></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">已有标签类</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "新增标签类"))
        self.pushButton_3.setText(_translate("MainWindow", "删除标签类"))
        self.pushButton_4.setText(_translate("MainWindow", "新增标签"))
        self.pushButton_5.setText(_translate("MainWindow", "删除标签"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "标签"))
        self.textBrowser_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\">数据标注</span></p></body></html>"))
        self.textBrowser_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">当前路径</span></p></body></html>"))
        self.textBrowser_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">当前标签类</span></p></body></html>"))
        __sortingEnabled = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        item = self.listWidget_3.item(0)
        item.setText(_translate("MainWindow", "评论"))
        self.listWidget_3.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_4.isSortingEnabled()
        self.listWidget_4.setSortingEnabled(False)
        item = self.listWidget_4.item(0)
        item.setText(_translate("MainWindow", "标签"))
        self.listWidget_4.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "标注"))
        self.textBrowser_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\">数据分析</span></p></body></html>"))
        self.textBrowser_10.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">当前路径</span></p></body></html>"))
        self.textBrowser_11.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">选择标签类</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "暂无图片"))
        self.textBrowser_12.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">导出路径</span></p></body></html>"))
        self.pushButton_6.setText(_translate("MainWindow", "查看结果"))
        self.pushButton_7.setText(_translate("MainWindow", "导出数据"))
        self.textBrowser_13.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">选择标签类</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "分析"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "帮助"))

