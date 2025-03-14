# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(747, 558)
        Dialog.setStyleSheet(u"#body {\n"
"            font-family: Arial, sans-serif;\n"
"            background-color: #f4f7f8;\n"
"            color: #333;\n"
"            padding: 20px;\n"
"\n"
"        }\n"
"#h1 {\n"
"            color: #444;\n"
"			font-size: 22px;\n"
"			font-weight: 700;\n"
"\n"
"        }\n"
"\n"
"QLabel {\n"
"			font-weight: bold;\n"
"			margin-bottom: 2px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"			padding: 3px;\n"
"            margin-bottom: 5px;\n"
"            margin-top: 2px;\n"
"            border: 1px solid #ccc;\n"
"            border-radius: 4px;\n"
"}\n"
"QPushButton {\n"
"            background-color: #007bff;\n"
"            color: white;\n"
"            border: none;\n"
"            border-radius: 4px;\n"
"            cursor: pointer;\n"
"        }\n"
"\n"
"QPushButton:hover {\n"
"            background-color: #0056b3;\n"
"        }")
        self.body = QWidget(Dialog)
        self.body.setObjectName(u"body")
        self.body.setGeometry(QRect(80, 60, 561, 461))
        self.add = QPushButton(self.body)
        self.add.setObjectName(u"add")
        self.add.setGeometry(QRect(40, 220, 101, 24))
        self.layoutWidget = QWidget(self.body)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 90, 491, 122))
        self.form = QVBoxLayout(self.layoutWidget)
        self.form.setObjectName(u"form")
        self.form.setContentsMargins(0, 0, 0, 0)
        self.new_title = QLabel(self.layoutWidget)
        self.new_title.setObjectName(u"new_title")

        self.form.addWidget(self.new_title)

        self.title = QLineEdit(self.layoutWidget)
        self.title.setObjectName(u"title")

        self.form.addWidget(self.title)

        self.new_answers = QLabel(self.layoutWidget)
        self.new_answers.setObjectName(u"new_answers")

        self.form.addWidget(self.new_answers)

        self.answer = QLineEdit(self.layoutWidget)
        self.answer.setObjectName(u"answer")

        self.form.addWidget(self.answer)

        self.layoutWidget1 = QWidget(self.body)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(40, 280, 494, 51))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.settings = QLabel(self.layoutWidget1)
        self.settings.setObjectName(u"settings")

        self.verticalLayout_3.addWidget(self.settings)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.victorina = QCheckBox(self.layoutWidget1)
        self.victorina.setObjectName(u"victorina")

        self.horizontalLayout.addWidget(self.victorina)

        self.multichoise = QCheckBox(self.layoutWidget1)
        self.multichoise.setObjectName(u"multichoise")

        self.horizontalLayout.addWidget(self.multichoise)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.submit = QPushButton(self.body)
        self.submit.setObjectName(u"submit")
        self.submit.setGeometry(QRect(40, 370, 75, 24))
        self.back = QPushButton(self.body)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(40, 410, 75, 24))
        self.h1 = QLabel(self.body)
        self.h1.setObjectName(u"h1")
        self.h1.setGeometry(QRect(40, 30, 261, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.add.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043e\u0442\u0432\u0435\u0442", None))
        self.new_title.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.title.setText("")
        self.new_answers.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u0432\u0435\u0442\u044b", None))
        self.settings.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 (\u043f\u043e\u043a\u0430 \u043d\u0435 \u0440\u0430\u0431\u043e\u0442\u0430\u044e\u0442):", None))
        self.victorina.setText(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0436\u0438\u043c \u0432\u0438\u043a\u0442\u043e\u0440\u0438\u043d\u044b", None))
        self.multichoise.setText(QCoreApplication.translate("Dialog", u"\u041d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0432\u0430\u0440\u0438\u0430\u043d\u0442\u043e\u0432 \u043e\u0442\u0432\u0435\u0442\u0430", None))
        self.submit.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.back.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.h1.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0437\u0434\u0430\u0435\u043c \u043d\u043e\u0432\u044b\u0439 \u043e\u043f\u0440\u043e\u0441", None))
    # retranslateUi

