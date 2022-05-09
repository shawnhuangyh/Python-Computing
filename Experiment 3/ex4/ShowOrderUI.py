# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ShowOrderUI.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_OrderInfoWindow(object):
    def setupUi(self, OrderInfoWindow):
        if not OrderInfoWindow.objectName():
            OrderInfoWindow.setObjectName(u"OrderInfoWindow")
        OrderInfoWindow.resize(300, 300)
        self.centralwidget = QWidget(OrderInfoWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.orderinfo = QLabel(self.centralwidget)
        self.orderinfo.setObjectName(u"orderinfo")
        self.orderinfo.setGeometry(QRect(70, 10, 151, 41))
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.orderinfo.setFont(font)
        self.orderinfo.setAlignment(Qt.AlignCenter)
        self.data = QLabel(self.centralwidget)
        self.data.setObjectName(u"data")
        self.data.setGeometry(QRect(10, 60, 281, 191))
        self.data.setAlignment(Qt.AlignCenter)
        OrderInfoWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(OrderInfoWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 300, 24))
        OrderInfoWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(OrderInfoWindow)
        self.statusbar.setObjectName(u"statusbar")
        OrderInfoWindow.setStatusBar(self.statusbar)

        self.retranslateUi(OrderInfoWindow)

        QMetaObject.connectSlotsByName(OrderInfoWindow)
    # setupUi

    def retranslateUi(self, OrderInfoWindow):
        OrderInfoWindow.setWindowTitle(QCoreApplication.translate("OrderInfoWindow", u"MainWindow", None))
        self.orderinfo.setText(QCoreApplication.translate("OrderInfoWindow", u"Order Info", None))
        self.data.setText("")
    # retranslateUi

