import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from MainWindowUI import Ui_MainWindow
from ShowOrderUI import Ui_OrderInfoWindow
from Tools import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.kfc = None
        self.bk = None
        self.mcdonald = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.order.clicked.connect(self.order)
        self.ui.query.clicked.connect(self.query)
        self.init_merchant()

    def init_merchant(self):
        self.mcdonald = Lunch()
        self.bk = Lunch()
        self.kfc = Lunch()

    def order(self):
        index = self.ui.merchant.currentIndex()
        food = self.ui.food.text()
        if index == 0:
            self.mcdonald.order(food)
        elif index == 1:
            self.bk.order(food)
        elif index == 2:
            self.kfc.order(food)

    def query(self):
        index = self.ui.merchant.currentIndex()
        out = str()
        if index == 0:
            foodlist = self.mcdonald.result()
        elif index == 1:
            foodlist = self.bk.result()
        elif index == 2:
            foodlist = self.kfc.result()
        if not foodlist:
            out = "No food has been ordered."
        else:
            for i in foodlist:
                out += str(i) + " "
        popwindow = PopUpWindow()
        popwindow.modify(out)
        popwindow.show()
        popwindow.exec()

        print(out)


class PopUpWindow(QMainWindow):
    def __init__(self):
        super(PopUpWindow, self).__init__()
        self.ui = Ui_OrderInfoWindow()
        self.ui.setupUi(self)

    def modify(self, out):
        self.ui.data.setText(out)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
