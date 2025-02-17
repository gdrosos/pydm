# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pydm.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from qtpy import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(677, 465)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 677, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHistory = QtWidgets.QMenu(self.menubar)
        self.menuHistory.setObjectName("menuHistory")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuCustomActions = QtWidgets.QMenu(self.menubar)
        self.menuCustomActions.setObjectName("menuCustomActions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.navbar = QtWidgets.QToolBar(MainWindow)
        self.navbar.setMovable(False)
        self.navbar.setFloatable(False)
        self.navbar.setObjectName("navbar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.navbar)
        self.actionEdit_in_Designer = QtWidgets.QAction(MainWindow)
        self.actionEdit_in_Designer.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionEdit_in_Designer.setObjectName("actionEdit_in_Designer")
        self.actionAbout_PyDM = QtWidgets.QAction(MainWindow)
        self.actionAbout_PyDM.setEnabled(True)
        self.actionAbout_PyDM.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionAbout_PyDM.setObjectName("actionAbout_PyDM")
        self.actionReload_Display = QtWidgets.QAction(MainWindow)
        self.actionReload_Display.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionReload_Display.setObjectName("actionReload_Display")
        self.actionIncrease_Font_Size = QtWidgets.QAction(MainWindow)
        self.actionIncrease_Font_Size.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionIncrease_Font_Size.setObjectName("actionIncrease_Font_Size")
        self.actionDecrease_Font_Size = QtWidgets.QAction(MainWindow)
        self.actionDecrease_Font_Size.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionDecrease_Font_Size.setObjectName("actionDecrease_Font_Size")
        self.actionShow_File_Path_in_Title_Bar = QtWidgets.QAction(MainWindow)
        self.actionShow_File_Path_in_Title_Bar.setCheckable(True)
        self.actionShow_File_Path_in_Title_Bar.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionShow_File_Path_in_Title_Bar.setObjectName("actionShow_File_Path_in_Title_Bar")
        self.actionBack = QtWidgets.QAction(MainWindow)
        self.actionBack.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionBack.setObjectName("actionBack")
        self.actionForward = QtWidgets.QAction(MainWindow)
        self.actionForward.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionForward.setObjectName("actionForward")
        self.actionHome = QtWidgets.QAction(MainWindow)
        self.actionHome.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionHome.setObjectName("actionHome")
        self.actionShow_Navigation_Bar = QtWidgets.QAction(MainWindow)
        self.actionShow_Navigation_Bar.setCheckable(True)
        self.actionShow_Navigation_Bar.setChecked(True)
        self.actionShow_Navigation_Bar.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionShow_Navigation_Bar.setObjectName("actionShow_Navigation_Bar")
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionShow_Menu_Bar = QtWidgets.QAction(MainWindow)
        self.actionShow_Menu_Bar.setCheckable(True)
        self.actionShow_Menu_Bar.setChecked(True)
        self.actionShow_Menu_Bar.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionShow_Menu_Bar.setObjectName("actionShow_Menu_Bar")
        self.actionShow_Status_Bar = QtWidgets.QAction(MainWindow)
        self.actionShow_Status_Bar.setCheckable(True)
        self.actionShow_Status_Bar.setChecked(True)
        self.actionShow_Status_Bar.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionShow_Status_Bar.setObjectName("actionShow_Status_Bar")
        self.actionShow_Connections = QtWidgets.QAction(MainWindow)
        self.actionShow_Connections.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionShow_Connections.setObjectName("actionShow_Connections")
        self.actionShow_Help = QtWidgets.QAction(MainWindow)
        self.actionShow_Help.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionShow_Help.setObjectName("actionShow_Help")
        self.actionLoadTool = QtWidgets.QAction(MainWindow)
        self.actionLoadTool.setObjectName("actionLoadTool")
        self.actionEnter_Fullscreen = QtWidgets.QAction(MainWindow)
        self.actionEnter_Fullscreen.setObjectName("actionEnter_Fullscreen")
        self.actionDefault_Font_Size = QtWidgets.QAction(MainWindow)
        self.actionDefault_Font_Size.setObjectName("actionDefault_Font_Size")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setEnabled(True)
        self.actionQuit.setObjectName("actionQuit")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName('actionSave')
        self.actionSave.setVisible(False)
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName('actionSave_As')
        self.actionSave_As.setVisible(False)
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName('actionLoad')
        self.actionLoad.setVisible(False)
        self.actionChange_Stylesheet = QtWidgets.QAction(MainWindow)
        self.actionChange_Stylesheet.setObjectName("actionChange_Stylesheet")
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionChange_Stylesheet)
        self.menuFile.addAction(self.actionEdit_in_Designer)
        self.menuFile.addAction(self.actionReload_Display)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionAbout_PyDM)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionQuit)
        self.menuView.addAction(self.actionEnter_Fullscreen)
        self.menuView.addAction(self.actionIncrease_Font_Size)
        self.menuView.addAction(self.actionDecrease_Font_Size)
        self.menuView.addAction(self.actionDefault_Font_Size)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionShow_File_Path_in_Title_Bar)
        self.menuView.addAction(self.actionShow_Navigation_Bar)
        self.menuView.addAction(self.actionShow_Menu_Bar)
        self.menuView.addAction(self.actionShow_Status_Bar)
        self.menuView.addAction(self.actionShow_Connections)
        self.menuView.addAction(self.actionShow_Help)
        self.menuHistory.addAction(self.actionBack)
        self.menuHistory.addAction(self.actionForward)
        self.menuHistory.addAction(self.actionHome)
        self.menuTools.addAction(self.actionLoadTool)
        self.menuTools.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHistory.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuCustomActions.menuAction())
        self.navbar.addAction(self.actionBack)
        self.navbar.addAction(self.actionForward)
        self.navbar.addSeparator()
        self.navbar.addAction(self.actionHome)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyDM Main Window"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHistory.setTitle(_translate("MainWindow", "History"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuCustomActions.setTitle(_translate("MainWindow", "Actions"))
        self.navbar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionEdit_in_Designer.setText(_translate("MainWindow", "Edit in Designer"))
        self.actionAbout_PyDM.setText(_translate("MainWindow", "About PyDM"))
        self.actionReload_Display.setText(_translate("MainWindow", "Reload Display"))
        self.actionReload_Display.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionIncrease_Font_Size.setText(_translate("MainWindow", "Increase Font Size"))
        self.actionIncrease_Font_Size.setShortcut(_translate("MainWindow", "Ctrl+="))
        self.actionDecrease_Font_Size.setText(_translate("MainWindow", "Decrease Font Size"))
        self.actionDecrease_Font_Size.setShortcut(_translate("MainWindow", "Ctrl+-"))
        self.actionShow_File_Path_in_Title_Bar.setText(_translate("MainWindow", "Show File Path in Title Bar"))
        self.actionBack.setText(_translate("MainWindow", "Back"))
        self.actionBack.setShortcut(_translate("MainWindow", "Ctrl+Left"))
        self.actionForward.setText(_translate("MainWindow", "Forward"))
        self.actionForward.setShortcut(_translate("MainWindow", "Ctrl+Right"))
        self.actionHome.setText(_translate("MainWindow", "Home"))
        self.actionHome.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionShow_Navigation_Bar.setText(_translate("MainWindow", "Show Navigation Bar"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File..."))
        self.actionOpen_File.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionShow_Menu_Bar.setText(_translate("MainWindow", "Show Menu Bar"))
        self.actionShow_Menu_Bar.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.actionShow_Status_Bar.setText(_translate("MainWindow", "Show Status Bar"))
        self.actionShow_Connections.setText(_translate("MainWindow", "Show Connections..."))
        self.actionShow_Help.setText(_translate("MainWindow", "View Help for this Display"))
        self.actionLoadTool.setText(_translate("MainWindow", "Load..."))
        self.actionEnter_Fullscreen.setText(_translate("MainWindow", "Enter Fullscreen"))
        self.actionEnter_Fullscreen.setShortcut(_translate("MainWindow", "F11"))
        self.actionDefault_Font_Size.setText(_translate("MainWindow", "Default Font Size"))
        self.actionDefault_Font_Size.setShortcut(_translate("MainWindow", "Ctrl+0"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As..."))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionChange_Stylesheet.setText(_translate("MainWindow", "Change Stylesheet"))
