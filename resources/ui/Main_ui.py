# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QTabWidget, QWidget)
from . import main_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(730, 453)
        MainWindow.setStyleSheet(u"#MainWindow ,#centralwidget{\n"
"	background-color: rgb(53, 53, 53);\n"
"\n"
"}\n"
"#MainWindow #tabWidget::tab-bar {\n"
"	border: 30px solid rgb(0, 0, 255);\n"
"	color: rgb(189, 189, 189);\n"
"\n"
"}\n"
"\n"
"#MainWindow  QTabBar{\n"
"	background-color: rgb(53, 53, 53);\n"
"	\n"
"}\n"
"#MainWindow  QTabBar::tab { \n"
"	border-top-left-radius:12;\n"
"	border-top-right-radius:12;\n"
"  	padding: 10px;\n"
"	color :rgb(189, 189, 189);\n"
"	\n"
" }\n"
"\n"
"#MainWindow  QTabBar::tab:selected {\n"
"	background-color: rgb(0, 142, 246);\n"
"	text-decoration: none;\n"
"\n"
" }\n"
"\n"
"#MainWindow  #tabWidget::pane{\n"
"	border-top:2px solid rgb(0, 142, 246) ;\n"
"\n"
"}\n"
"\n"
"#mainTab QPushButton{\n"
"	background-color: rgb(43, 45, 53);\n"
"	color: rgb(189, 189, 189);\n"
"    border: 1px solid rgb(189, 189, 189);\n"
"    border-radius: 12px; \n"
"    padding: 20px; \n"
"\n"
"}\n"
"\n"
"#mainTab QPushButton::hover{\n"
"	background-color: rgb(0, 142, 246);\n"
"	color: rgb(189, 189, 189);\n"
"    border: 1px solid rg"
                        "b(189, 189, 189);\n"
"    border-radius: 12px; \n"
"    padding: 20px; \n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabletTracking(False)
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setIconSize(QSize(30, 30))
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideMiddle)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.titleTab = QWidget()
        self.titleTab.setObjectName(u"titleTab")
        self.titleTab.setStyleSheet(u"")
        self.tabWidget.addTab(self.titleTab, "")
        self.mainTab = QWidget()
        self.mainTab.setObjectName(u"mainTab")
        self.gridLayout_2 = QGridLayout(self.mainTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.liveButton = QPushButton(self.mainTab)
        self.liveButton.setObjectName(u"liveButton")
        icon = QIcon()
        icon.addFile(u":/icons/Icons/circle-dot-regular.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.liveButton.setIcon(icon)
        self.liveButton.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.liveButton)

        self.recordsButton = QPushButton(self.mainTab)
        self.recordsButton.setObjectName(u"recordsButton")
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/film-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.recordsButton.setIcon(icon1)
        self.recordsButton.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.recordsButton)

        self.dataBaseButton = QPushButton(self.mainTab)
        self.dataBaseButton.setObjectName(u"dataBaseButton")
        icon2 = QIcon()
        icon2.addFile(u":/icons/Icons/database-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dataBaseButton.setIcon(icon2)
        self.dataBaseButton.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.dataBaseButton)

        self.settingbutton = QPushButton(self.mainTab)
        self.settingbutton.setObjectName(u"settingbutton")
        icon3 = QIcon()
        icon3.addFile(u":/icons/Icons/gear-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingbutton.setIcon(icon3)
        self.settingbutton.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.settingbutton)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        icon4 = QIcon()
        icon4.addFile(u":/icons/Icons/house-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.mainTab, icon4, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.titleTab), QCoreApplication.translate("MainWindow", u"Access Controler", None))
        self.liveButton.setText(QCoreApplication.translate("MainWindow", u"  Live", None))
        self.recordsButton.setText(QCoreApplication.translate("MainWindow", u"Records", None))
        self.dataBaseButton.setText(QCoreApplication.translate("MainWindow", u"  Data Base", None))
        self.settingbutton.setText(QCoreApplication.translate("MainWindow", u"parametre ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mainTab), QCoreApplication.translate("MainWindow", u"Main", None))
    # retranslateUi

