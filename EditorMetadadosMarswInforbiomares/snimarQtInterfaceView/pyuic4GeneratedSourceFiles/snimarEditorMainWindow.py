# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditorMetadadosMarswInforbiomares/snimarQtInterfaceView/templates/snimarEditorMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        mainwindow.setObjectName("mainwindow")
        mainwindow.resize(800, 600)
        mainwindow.setMinimumSize(QtCore.QSize(800, 600))
        mainwindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        mainwindow.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Portugal))
        mainwindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.centralwidget = QtWidgets.QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.filelist = QtWidgets.QWidget()
        self.filelist.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.filelist.setObjectName("filelist")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.filelist)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.filetable = QtWidgets.QTableView(self.filelist)
        self.filetable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.filetable.setAlternatingRowColors(True)
        self.filetable.setGridStyle(QtCore.Qt.SolidLine)
        self.filetable.setSortingEnabled(True)
        self.filetable.setCornerButtonEnabled(False)
        self.filetable.setObjectName("filetable")
        self.filetable.horizontalHeader().setCascadingSectionResizes(True)
        self.filetable.horizontalHeader().setMinimumSectionSize(10)
        self.gridLayout_2.addWidget(self.filetable, 0, 0, 1, 5)
        self.btn_conform_all = QtWidgets.QPushButton(self.filelist)
        self.btn_conform_all.setMaximumSize(QtCore.QSize(110, 16777215))
        self.btn_conform_all.setObjectName("btn_conform_all")
        self.gridLayout_2.addWidget(self.btn_conform_all, 2, 3, 1, 1)
        self.thesaurus_version_wrapper = QtWidgets.QWidget(self.filelist)
        self.thesaurus_version_wrapper.setMaximumSize(QtCore.QSize(280, 16777215))
        self.thesaurus_version_wrapper.setObjectName("thesaurus_version_wrapper")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.thesaurus_version_wrapper)
        self.gridLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setVerticalSpacing(4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.thesaurus_title_label = QtWidgets.QLabel(self.thesaurus_version_wrapper)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.thesaurus_title_label.setFont(font)
        self.thesaurus_title_label.setObjectName("thesaurus_title_label")
        self.gridLayout_3.addWidget(self.thesaurus_title_label, 0, 0, 1, 2)
        self.thesaurus_update = QtWidgets.QPushButton(self.thesaurus_version_wrapper)
        self.thesaurus_update.setEnabled(True)
        self.thesaurus_update.setCheckable(False)
        self.thesaurus_update.setFlat(False)
        self.thesaurus_update.setObjectName("thesaurus_update")
        self.gridLayout_3.addWidget(self.thesaurus_update, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.thesaurus_version_wrapper, 2, 0, 1, 1)
        self.btn_delete_all = QtWidgets.QPushButton(self.filelist)
        self.btn_delete_all.setMaximumSize(QtCore.QSize(110, 16777215))
        self.btn_delete_all.setObjectName("btn_delete_all")
        self.gridLayout_2.addWidget(self.btn_delete_all, 2, 4, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.filelist)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 2, 2, 1, 1)
        self.widget = QtWidgets.QWidget(self.filelist)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2.addWidget(self.widget, 2, 1, 1, 1, QtCore.Qt.AlignBottom)
        self.tabWidget.addTab(self.filelist, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.filetable_2 = QtWidgets.QTableView(self.frame)
        self.filetable_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.filetable_2.setAlternatingRowColors(True)
        self.filetable_2.setGridStyle(QtCore.Qt.SolidLine)
        self.filetable_2.setSortingEnabled(True)
        self.filetable_2.setCornerButtonEnabled(False)
        self.filetable_2.setObjectName("filetable_2")
        self.filetable_2.horizontalHeader().setCascadingSectionResizes(True)
        self.filetable_2.horizontalHeader().setMinimumSectionSize(10)
        self.verticalLayout_5.addWidget(self.filetable_2)
        self.setServer = QtWidgets.QPushButton(self.frame)
        self.setServer.setObjectName("setServer")
        self.verticalLayout_5.addWidget(self.setServer)
        self.verticalLayout_4.addWidget(self.frame)
        self.tabWidget.addTab(self.tab, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        mainwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.menubar.setObjectName("menubar")
        self.filemenu = QtWidgets.QMenu(self.menubar)
        self.filemenu.setObjectName("filemenu")
        self.menu_new = QtWidgets.QMenu(self.filemenu)
        self.menu_new.setObjectName("menu_new")
        mainwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainwindow)
        self.statusbar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.statusbar.setObjectName("statusbar")
        mainwindow.setStatusBar(self.statusbar)
        self.new_dataset = QtWidgets.QAction(mainwindow)
        self.new_dataset.setObjectName("new_dataset")
        self.menu_save = QtWidgets.QAction(mainwindow)
        self.menu_save.setObjectName("menu_save")
        self.menu_saveas = QtWidgets.QAction(mainwindow)
        self.menu_saveas.setObjectName("menu_saveas")
        self.menu_close = QtWidgets.QAction(mainwindow)
        self.menu_close.setObjectName("menu_close")
        self.menu_open = QtWidgets.QAction(mainwindow)
        self.menu_open.setObjectName("menu_open")
        self.menu_add_dir = QtWidgets.QAction(mainwindow)
        self.menu_add_dir.setObjectName("menu_add_dir")
        self.new_serie = QtWidgets.QAction(mainwindow)
        self.new_serie.setObjectName("new_serie")
        self.new_service = QtWidgets.QAction(mainwindow)
        self.new_service.setObjectName("new_service")
        self.menu_save_all = QtWidgets.QAction(mainwindow)
        self.menu_save_all.setObjectName("menu_save_all")
        self.menu_codelists = QtWidgets.QAction(mainwindow)
        self.menu_codelists.setObjectName("menu_codelists")
        self.menu_resave = QtWidgets.QAction(mainwindow)
        self.menu_resave.setObjectName("menu_resave")
        self.menu_geonetwork = QtWidgets.QAction(mainwindow)
        self.menu_geonetwork.setObjectName("menu_geonetwork")
        self.save_Geonetwork = QtWidgets.QAction(mainwindow)
        self.save_Geonetwork.setObjectName("save_Geonetwork")
        self.menu_new.addAction(self.new_dataset)
        self.menu_new.addAction(self.new_serie)
        self.menu_new.addAction(self.new_service)
        self.filemenu.addAction(self.menu_new.menuAction())
        self.filemenu.addAction(self.menu_open)
        self.filemenu.addAction(self.menu_geonetwork)
        self.filemenu.addAction(self.menu_add_dir)
        self.filemenu.addSeparator()
        self.filemenu.addAction(self.menu_save)
        self.filemenu.addAction(self.menu_saveas)
        self.filemenu.addAction(self.save_Geonetwork)
        self.filemenu.addAction(self.menu_save_all)
        self.filemenu.addSeparator()
        self.filemenu.addAction(self.menu_close)
        self.filemenu.addAction(self.menu_codelists)
        self.filemenu.addAction(self.menu_resave)
        self.filemenu.addSeparator()
        self.menubar.addAction(self.filemenu.menuAction())

        self.retranslateUi(mainwindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

    def retranslateUi(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("mainwindow", "MainWindow"))
        self.btn_conform_all.setText(_translate("mainwindow", "Verificar\n"
" Conformidade\n"
" (Todos)"))
        self.thesaurus_title_label.setText(_translate("mainwindow", "Thesaurus SNIMar"))
        self.thesaurus_update.setToolTip(_translate("mainwindow", "Atualizar a lista de palavras do Thesaurus SNIMar"))
        self.thesaurus_update.setText(_translate("mainwindow", "Actualizar"))
        self.btn_delete_all.setText(_translate("mainwindow", "Apagar\n"
" Lista de\n"
" Ficheiros"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.filelist), _translate("mainwindow", "Lista de Ficheiros"))
        self.setServer.setText(_translate("mainwindow", "Carregar Lista"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("mainwindow", "Lista GeonetWork"))
        self.filemenu.setTitle(_translate("mainwindow", "Ficheiro"))
        self.menu_new.setTitle(_translate("mainwindow", "Novo"))
        self.new_dataset.setText(_translate("mainwindow", "Conjunto de Dados Geograficos"))
        self.menu_save.setText(_translate("mainwindow", "Guardar"))
        self.menu_saveas.setText(_translate("mainwindow", "Guardar como"))
        self.menu_close.setText(_translate("mainwindow", "Fechar"))
        self.menu_open.setText(_translate("mainwindow", "Abrir"))
        self.menu_add_dir.setText(_translate("mainwindow", "Abrir Pasta"))
        self.new_serie.setText(_translate("mainwindow", "Série"))
        self.new_service.setText(_translate("mainwindow", "Serviço"))
        self.menu_save_all.setText(_translate("mainwindow", "Guardar Todos"))
        self.menu_codelists.setText(_translate("mainwindow", "Atualizar Codelists"))
        self.menu_resave.setText(_translate("mainwindow", "Atualizar Metadados"))
        self.menu_geonetwork.setText(_translate("mainwindow", "Abrir URL"))
        self.save_Geonetwork.setText(_translate("mainwindow", "Gravar Geonetwork"))
