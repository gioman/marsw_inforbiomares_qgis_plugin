# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditorMetadadosMarswInforbiomares/snimarQtInterfaceView/templates/dialogs//chooseFreeKeywordDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialogDate(object):
    def setupUi(self, dialogDate):
        dialogDate.setObjectName("dialogDate")
        dialogDate.resize(430, 250)
        dialogDate.setMinimumSize(QtCore.QSize(430, 250))
        dialogDate.setMaximumSize(QtCore.QSize(430, 250))
        dialogDate.setSizeGripEnabled(True)
        dialogDate.setModal(False)
        self.btn_cancelar = QtWidgets.QPushButton(dialogDate)
        self.btn_cancelar.setGeometry(QtCore.QRect(180, 210, 96, 30))
        self.btn_cancelar.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_cancelar.setAutoDefault(False)
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.btn_adicionar = QtWidgets.QPushButton(dialogDate)
        self.btn_adicionar.setGeometry(QtCore.QRect(280, 210, 96, 30))
        self.btn_adicionar.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_adicionar.setAutoDefault(False)
        self.btn_adicionar.setObjectName("btn_adicionar")
        self.formLayoutWidget = QtWidgets.QWidget(dialogDate)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 411, 202))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(60)
        self.formLayout.setVerticalSpacing(5)
        self.formLayout.setObjectName("formLayout")
        self.widget = QtWidgets.QWidget(self.formLayoutWidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.info_label_line_keyword = QtWidgets.QPushButton(self.widget)
        self.info_label_line_keyword.setMaximumSize(QtCore.QSize(20, 20))
        self.info_label_line_keyword.setFlat(True)
        self.info_label_line_keyword.setObjectName("info_label_line_keyword")
        self.horizontalLayout.addWidget(self.info_label_line_keyword)
        self.label_line_keyword = QtWidgets.QLabel(self.widget)
        self.label_line_keyword.setObjectName("label_line_keyword")
        self.horizontalLayout.addWidget(self.label_line_keyword)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.widget)
        self.line_keyword = gui.QgsFilterLineEdit(self.formLayoutWidget)
        self.line_keyword.setMinimumSize(QtCore.QSize(58, 30))
        self.line_keyword.setProperty("qgisRelation", "")
        self.line_keyword.setObjectName("line_keyword")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_keyword)
        self.widget1 = QtWidgets.QWidget(self.formLayoutWidget)
        self.widget1.setObjectName("widget1")
        self.horizontalLayout1 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout1.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout1.setSpacing(0)
        self.horizontalLayout1.setObjectName("horizontalLayout1")
        self.info_label_combo_type = QtWidgets.QPushButton(self.widget1)
        self.info_label_combo_type.setMaximumSize(QtCore.QSize(20, 20))
        self.info_label_combo_type.setFlat(True)
        self.info_label_combo_type.setObjectName("info_label_combo_type")
        self.horizontalLayout1.addWidget(self.info_label_combo_type)
        self.label_combo_type = QtWidgets.QLabel(self.widget1)
        self.label_combo_type.setObjectName("label_combo_type")
        self.horizontalLayout1.addWidget(self.label_combo_type)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.widget1)
        self.combo_type = QtWidgets.QComboBox(self.formLayoutWidget)
        self.combo_type.setMinimumSize(QtCore.QSize(0, 30))
        self.combo_type.setObjectName("combo_type")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.combo_type)
        self.widget2 = QtWidgets.QWidget(self.formLayoutWidget)
        self.widget2.setObjectName("widget2")
        self.horizontalLayout2 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout2.setSpacing(0)
        self.horizontalLayout2.setObjectName("horizontalLayout2")
        self.info_label_line_thesaurus = QtWidgets.QPushButton(self.widget2)
        self.info_label_line_thesaurus.setMaximumSize(QtCore.QSize(20, 20))
        self.info_label_line_thesaurus.setFlat(True)
        self.info_label_line_thesaurus.setObjectName("info_label_line_thesaurus")
        self.horizontalLayout2.addWidget(self.info_label_line_thesaurus)
        self.label_line_thesaurus = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_line_thesaurus.setFont(font)
        self.label_line_thesaurus.setObjectName("label_line_thesaurus")
        self.horizontalLayout2.addWidget(self.label_line_thesaurus)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.widget2)
        self.line_thesaurus = gui.QgsFilterLineEdit(self.formLayoutWidget)
        self.line_thesaurus.setMinimumSize(QtCore.QSize(58, 30))
        self.line_thesaurus.setProperty("qgisRelation", "")
        self.line_thesaurus.setObjectName("line_thesaurus")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.line_thesaurus)
        self.widget3 = QtWidgets.QWidget(self.formLayoutWidget)
        self.widget3.setObjectName("widget3")
        self.horizontalLayout3 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout3.setSpacing(0)
        self.horizontalLayout3.setObjectName("horizontalLayout3")
        self.info_label_date_date_2 = QtWidgets.QPushButton(self.widget3)
        self.info_label_date_date_2.setMaximumSize(QtCore.QSize(20, 20))
        self.info_label_date_date_2.setFlat(True)
        self.info_label_date_date_2.setObjectName("info_label_date_date_2")
        self.horizontalLayout3.addWidget(self.info_label_date_date_2)
        self.label_date_date_2 = QtWidgets.QLabel(self.widget3)
        self.label_date_date_2.setObjectName("label_date_date_2")
        self.horizontalLayout3.addWidget(self.label_date_date_2)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.widget3)
        self.widget4 = QtWidgets.QWidget(self.formLayoutWidget)
        self.widget4.setObjectName("widget4")
        self.horizontalLayout4 = QtWidgets.QHBoxLayout(self.widget4)
        self.horizontalLayout4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout4.setSpacing(0)
        self.horizontalLayout4.setObjectName("horizontalLayout4")
        self.info_label_combo_dataType = QtWidgets.QPushButton(self.widget4)
        self.info_label_combo_dataType.setMaximumSize(QtCore.QSize(20, 20))
        self.info_label_combo_dataType.setFlat(True)
        self.info_label_combo_dataType.setObjectName("info_label_combo_dataType")
        self.horizontalLayout4.addWidget(self.info_label_combo_dataType)
        self.label_combo_dataType = QtWidgets.QLabel(self.widget4)
        self.label_combo_dataType.setObjectName("label_combo_dataType")
        self.horizontalLayout4.addWidget(self.label_combo_dataType)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.widget4)
        self.combo_dataType = QtWidgets.QComboBox(self.formLayoutWidget)
        self.combo_dataType.setMinimumSize(QtCore.QSize(0, 30))
        self.combo_dataType.setObjectName("combo_dataType")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.combo_dataType)
        self.widget_2 = QtWidgets.QWidget(self.formLayoutWidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.date_date_2 = QtWidgets.QDateEdit(self.widget_2)
        self.date_date_2.setMinimumSize(QtCore.QSize(98, 30))
        self.date_date_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.date_date_2.setDate(QtCore.QDate(2015, 6, 14))
        self.date_date_2.setTime(QtCore.QTime(0, 0, 0))
        self.date_date_2.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.date_date_2.setCalendarPopup(True)
        self.date_date_2.setObjectName("date_date_2")
        self.horizontalLayout_2.addWidget(self.date_date_2)
        self.btn_clear_date_date_2 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_clear_date_date_2.sizePolicy().hasHeightForWidth())
        self.btn_clear_date_date_2.setSizePolicy(sizePolicy)
        self.btn_clear_date_date_2.setMinimumSize(QtCore.QSize(40, 30))
        self.btn_clear_date_date_2.setMaximumSize(QtCore.QSize(40, 30))
        self.btn_clear_date_date_2.setText("")
        self.btn_clear_date_date_2.setObjectName("btn_clear_date_date_2")
        self.horizontalLayout_2.addWidget(self.btn_clear_date_date_2)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.widget_2)

        self.retranslateUi(dialogDate)
        QtCore.QMetaObject.connectSlotsByName(dialogDate)

    def retranslateUi(self, dialogDate):
        _translate = QtCore.QCoreApplication.translate
        dialogDate.setWindowTitle(_translate("dialogDate", "Escolha Palavra-Chave Livre"))
        self.btn_cancelar.setText(_translate("dialogDate", "Cancelar"))
        self.btn_adicionar.setText(_translate("dialogDate", "Adicionar"))
        self.label_line_keyword.setText(_translate("dialogDate", "Palavra-Chave:"))
        self.line_keyword.setPlaceholderText(_translate("dialogDate", "palavra"))
        self.label_combo_type.setText(_translate("dialogDate", "Tipo:"))
        self.label_line_thesaurus.setText(_translate("dialogDate", "Thesaurus:"))
        self.line_thesaurus.setPlaceholderText(_translate("dialogDate", "Thesaurus"))
        self.label_date_date_2.setText(_translate("dialogDate", "Data"))
        self.label_combo_dataType.setText(_translate("dialogDate", "Tipo de Data"))
        self.date_date_2.setDisplayFormat(_translate("dialogDate", "dd/MM/yy"))
from qgis import gui
