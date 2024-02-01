# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DataBase.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_DataBase(object):
    def setupUi(self, DataBase):
        if not DataBase.objectName():
            DataBase.setObjectName(u"DataBase")
        DataBase.resize(944, 597)
        DataBase.setStyleSheet(u"#DataBase {\n"
"	\n"
"	background-color: rgb(43, 45, 53);\n"
"}\n"
"\n"
"#DataBase QPushButton{\n"
"	border : 1px solid rgb(189, 189, 189);\n"
"	border-radius: 12px;\n"
"	padding: 15px;\n"
"}\n"
"#DataBase #addButton{\n"
"	background-color: rgb(0, 142, 246);\n"
"}")
        self.gridLayout = QGridLayout(DataBase)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.nameLabel = QLabel(DataBase)
        self.nameLabel.setObjectName(u"nameLabel")
        font = QFont()
        font.setBold(True)
        self.nameLabel.setFont(font)
        self.nameLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.nameLabel)

        self.lineEdit = QLineEdit(DataBase)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(160, 16777215))

        self.horizontalLayout.addWidget(self.lineEdit)

        self.genderLabel = QLabel(DataBase)
        self.genderLabel.setObjectName(u"genderLabel")
        self.genderLabel.setFont(font)
        self.genderLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.genderLabel)

        self.genderComboBox = QComboBox(DataBase)
        self.genderComboBox.addItem("")
        self.genderComboBox.setObjectName(u"genderComboBox")

        self.horizontalLayout.addWidget(self.genderComboBox)

        self.modelingLabel = QLabel(DataBase)
        self.modelingLabel.setObjectName(u"modelingLabel")
        self.modelingLabel.setFont(font)
        self.modelingLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.modelingLabel)

        self.modelingComboBox = QComboBox(DataBase)
        self.modelingComboBox.addItem("")
        self.modelingComboBox.setObjectName(u"modelingComboBox")

        self.horizontalLayout.addWidget(self.modelingComboBox)

        self.resetButton = QPushButton(DataBase)
        self.resetButton.setObjectName(u"resetButton")
        self.resetButton.setFont(font)

        self.horizontalLayout.addWidget(self.resetButton)

        self.searchButton = QPushButton(DataBase)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setFont(font)

        self.horizontalLayout.addWidget(self.searchButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.registerIdButton = QPushButton(DataBase)
        self.registerIdButton.setObjectName(u"registerIdButton")
        self.registerIdButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.registerIdButton)

        self.batchRegisterButton = QPushButton(DataBase)
        self.batchRegisterButton.setObjectName(u"batchRegisterButton")
        self.batchRegisterButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.batchRegisterButton)

        self.modelingButton = QPushButton(DataBase)
        self.modelingButton.setObjectName(u"modelingButton")
        self.modelingButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.modelingButton)

        self.deleteButton = QPushButton(DataBase)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.deleteButton)

        self.checkBox = QCheckBox(DataBase)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_2.addWidget(self.checkBox)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.tableWidget = QTableWidget(DataBase)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(DataBase)

        QMetaObject.connectSlotsByName(DataBase)
    # setupUi

    def retranslateUi(self, DataBase):
        DataBase.setWindowTitle(QCoreApplication.translate("DataBase", u"Form", None))
        self.nameLabel.setText(QCoreApplication.translate("DataBase", u"Name", None))
        self.genderLabel.setText(QCoreApplication.translate("DataBase", u"Gender", None))
        self.genderComboBox.setItemText(0, QCoreApplication.translate("DataBase", u"ALL", None))

        self.modelingLabel.setText(QCoreApplication.translate("DataBase", u"Modeling", None))
        self.modelingComboBox.setItemText(0, QCoreApplication.translate("DataBase", u"ALL", None))

        self.resetButton.setText(QCoreApplication.translate("DataBase", u"Reset", None))
        self.searchButton.setText(QCoreApplication.translate("DataBase", u"Search", None))
        self.registerIdButton.setText(QCoreApplication.translate("DataBase", u"Register ID", None))
        self.batchRegisterButton.setText(QCoreApplication.translate("DataBase", u"Batch Register", None))
        self.modelingButton.setText(QCoreApplication.translate("DataBase", u"Modeling", None))
        self.deleteButton.setText(QCoreApplication.translate("DataBase", u"Delete", None))
        self.checkBox.setText(QCoreApplication.translate("DataBase", u"ALL", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DataBase", u"Selected", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DataBase", u"Faces Library Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("DataBase", u"People Number", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("DataBase", u"Status", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("DataBase", u"Details", None));
    # retranslateUi

