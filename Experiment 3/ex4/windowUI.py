# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windowUI.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(350, 250)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 30, 259, 132))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.merchant = QLineEdit(self.widget)
        self.merchant.setObjectName(u"merchant")

        self.gridLayout.addWidget(self.merchant, 0, 1, 1, 1)

        self.merchant_prompt = QLabel(self.widget)
        self.merchant_prompt.setObjectName(u"merchant_prompt")
        font = QFont()
        font.setBold(True)
        self.merchant_prompt.setFont(font)

        self.gridLayout.addWidget(self.merchant_prompt, 0, 0, 1, 1)

        self.food_prompt = QLabel(self.widget)
        self.food_prompt.setObjectName(u"food_prompt")
        self.food_prompt.setFont(font)

        self.gridLayout.addWidget(self.food_prompt, 1, 0, 1, 1)

        self.food = QLineEdit(self.widget)
        self.food.setObjectName(u"food")

        self.gridLayout.addWidget(self.food, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.order = QPushButton(self.widget)
        self.order.setObjectName(u"order")

        self.verticalLayout.addWidget(self.order)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 350, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.merchant_prompt.setText(QCoreApplication.translate("MainWindow", u"Select a merchant:", None))
        self.food_prompt.setText(QCoreApplication.translate("MainWindow", u"Select your food:", None))
        self.order.setText(QCoreApplication.translate("MainWindow", u"Order", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Query previous order", None))
    # retranslateUi

