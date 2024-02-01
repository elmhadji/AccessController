# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Camera.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Camera(object):
    def setupUi(self, Camera):
        if not Camera.objectName():
            Camera.setObjectName(u"Camera")
        Camera.resize(729, 481)
        self.gridLayout = QGridLayout(Camera)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.cameraTitleLabel_01 = QLabel(Camera)
        self.cameraTitleLabel_01.setObjectName(u"cameraTitleLabel_01")
        self.cameraTitleLabel_01.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.cameraTitleLabel_01)

        self.cameraLabel_01 = QLabel(Camera)
        self.cameraLabel_01.setObjectName(u"cameraLabel_01")
        self.cameraLabel_01.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.cameraLabel_01)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 4)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.cameraTitleLabel_02 = QLabel(Camera)
        self.cameraTitleLabel_02.setObjectName(u"cameraTitleLabel_02")
        self.cameraTitleLabel_02.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.cameraTitleLabel_02)

        self.cameraLabel_02 = QLabel(Camera)
        self.cameraLabel_02.setObjectName(u"cameraLabel_02")
        self.cameraLabel_02.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.cameraLabel_02)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 4)

        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.retranslateUi(Camera)

        QMetaObject.connectSlotsByName(Camera)
    # setupUi

    def retranslateUi(self, Camera):
        Camera.setWindowTitle(QCoreApplication.translate("Camera", u"Form", None))
        self.cameraTitleLabel_01.setText(QCoreApplication.translate("Camera", u"Camera 01", None))
        self.cameraLabel_01.setText(QCoreApplication.translate("Camera", u"TextLabel", None))
        self.cameraTitleLabel_02.setText(QCoreApplication.translate("Camera", u"Camera 02", None))
        self.cameraLabel_02.setText(QCoreApplication.translate("Camera", u"TextLabel", None))
    # retranslateUi

