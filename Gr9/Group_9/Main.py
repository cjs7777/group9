# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QTableWidgetItem, QApplication, QMainWindow, QHeaderView

#导入程序运行必须模块
import sys
#导入designer工具生成的模块
from DataAnnotationUI import Ui_MainWindow
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow

from Spider import *
from File import FileIO

class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)

        # 添加登录按钮信号和槽。注意display函数不加小括号()
        self.pushButton.clicked.connect(self.display)
        # 添加退出按钮信号和槽。调用close函数
        self.pushButton.clicked.connect(self.close)

    def display(self):
        # 获取界面输入
        stock = self.textEdit.toPlainText()
        filePath = self.textEdit_2.toPlainText()

        stock = "SH603517"
        filePath = r".\data.csv"
        print(stock)
        print(filePath)

        crawler = Crawler(stock)  # 创建爬虫
        siteData = ['StockComment', 'https://xueqiu.com/query/v1/symbol/search/status?', 10, 10]  # 网页参数
        sites = []  # 通过提供的参数生成的Wedsite对象
        sites.append(Website(siteData[0], siteData[1], siteData[2], siteData[3]))
        contents = crawler.parse(sites[0])
        if contents == None:
            return
        # print(type(contents))
        fileio = FileIO()
        fileio.writeFile(filePath, contents)

if __name__ == "__main__":
    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    # 初始化
    myWin = MyMainForm()
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())

