# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QtConsoleQFBUiY.ui'
##
## Created by: Qt User Interface Compiler version 5.15.14
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionsave = QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionopen = QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionsave_2 = QAction(MainWindow)
        self.actionsave_2.setObjectName("actionsave_2")
        self.actionnew = QAction(MainWindow)
        self.actionnew.setObjectName("actionnew")
        self.actionsaveAs = QAction(MainWindow)
        self.actionsaveAs.setObjectName("actionsaveAs")
        self.actionconvertToHtml = QAction(MainWindow)
        self.actionconvertToHtml.setObjectName("actionconvertToHtml")
        self.actionconvert_to_pdf = QAction(MainWindow)
        self.actionconvert_to_pdf.setObjectName("actionconvert_to_pdf")
        self.actionincrease = QAction(MainWindow)
        self.actionincrease.setObjectName("actionincrease")
        self.actiondecrease = QAction(MainWindow)
        self.actiondecrease.setObjectName("actiondecrease")
        self.actionrestart = QAction(MainWindow)
        self.actionrestart.setObjectName("actionrestart")
        self.actioninterrupt = QAction(MainWindow)
        self.actioninterrupt.setObjectName("actioninterrupt")
        self.actionshutdown = QAction(MainWindow)
        self.actionshutdown.setObjectName("actionshutdown")
        self.actionexit = QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 2, 2)
        self.outputEdit = QTextBrowser(self.frame_2)
        self.outputEdit.setObjectName("outputEdit")

        self.verticalLayout_3.addWidget(self.outputEdit)

        self.horizontalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.widget)
        self.frame.setObjectName("frame")
        self.frame.setMaximumSize(QSize(600, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(2, 0, 0, 2)
        self.shellEdit = QTextEdit(self.frame)
        self.shellEdit.setObjectName("shellEdit")

        self.horizontalLayout_3.addWidget(self.shellEdit)

        self.horizontalLayout.addWidget(self.frame)

        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 250))
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.widget_2)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 3, 0, 0)
        self.inputEdit = QTextEdit(self.frame_3)
        self.inputEdit.setObjectName("inputEdit")

        self.horizontalLayout_2.addWidget(self.inputEdit)

        self.verticalLayout_2.addWidget(self.frame_3)

        self.verticalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 30))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuFile.setMinimumSize(QSize(12, 0))
        self.menuFile.setMaximumSize(QSize(167777, 16777215))
        self.menuSaveAs = QMenu(self.menubar)
        self.menuSaveAs.setObjectName("menuSaveAs")
        self.menusize = QMenu(self.menubar)
        self.menusize.setObjectName("menusize")
        self.menuexit = QMenu(self.menubar)
        self.menuexit.setObjectName("menuexit")
        self.menuconvert = QMenu(self.menubar)
        self.menuconvert.setObjectName("menuconvert")
        self.menuKernel = QMenu(self.menubar)
        self.menuKernel.setObjectName("menuKernel")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuKernel.menuAction())
        self.menubar.addAction(self.menuSaveAs.menuAction())
        self.menubar.addAction(self.menuconvert.menuAction())
        self.menubar.addAction(self.menusize.menuAction())
        self.menubar.addAction(self.menuexit.menuAction())
        self.menuFile.addAction(self.actionnew)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionopen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionsave_2)
        self.menuFile.addSeparator()
        self.menuSaveAs.addAction(self.actionsave)
        self.menuSaveAs.addSeparator()
        self.menuSaveAs.addAction(self.actionsaveAs)
        self.menuSaveAs.addSeparator()
        self.menusize.addAction(self.actionincrease)
        self.menusize.addSeparator()
        self.menusize.addAction(self.actiondecrease)
        self.menusize.addSeparator()
        self.menuexit.addAction(self.actionexit)
        self.menuexit.addSeparator()
        self.menuconvert.addAction(self.actionconvertToHtml)
        self.menuconvert.addSeparator()
        self.menuconvert.addAction(self.actionconvert_to_pdf)
        self.menuconvert.addSeparator()
        self.menuKernel.addAction(self.actionrestart)
        self.menuKernel.addSeparator()
        self.menuKernel.addAction(self.actioninterrupt)
        self.menuKernel.addSeparator()
        self.menuKernel.addAction(self.actionshutdown)
        self.menuKernel.addSeparator()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", "Open", None))
        self.actionsave.setText(QCoreApplication.translate("MainWindow", "save", None))
        self.actionopen.setText(QCoreApplication.translate("MainWindow", "open", None))
        self.actionsave_2.setText(
            QCoreApplication.translate("MainWindow", "save", None)
        )
        self.actionnew.setText(QCoreApplication.translate("MainWindow", "new", None))
        self.actionsaveAs.setText(
            QCoreApplication.translate("MainWindow", "saveAs", None)
        )
        self.actionconvertToHtml.setText(
            QCoreApplication.translate("MainWindow", "convert to html", None)
        )
        self.actionconvert_to_pdf.setText(
            QCoreApplication.translate("MainWindow", "convert to pdf", None)
        )
        self.actionincrease.setText(
            QCoreApplication.translate("MainWindow", "increase", None)
        )
        self.actiondecrease.setText(
            QCoreApplication.translate("MainWindow", "decrease", None)
        )
        self.actionrestart.setText(
            QCoreApplication.translate("MainWindow", "restart", None)
        )
        self.actioninterrupt.setText(
            QCoreApplication.translate("MainWindow", "interrupt", None)
        )
        self.actionshutdown.setText(
            QCoreApplication.translate("MainWindow", "shutdown", None)
        )
        self.actionexit.setText(QCoreApplication.translate("MainWindow", "exit", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", "File", None))
        self.menuSaveAs.setTitle(QCoreApplication.translate("MainWindow", "Save", None))
        self.menusize.setTitle(QCoreApplication.translate("MainWindow", "Size", None))
        self.menuexit.setTitle(QCoreApplication.translate("MainWindow", "Exit", None))
        self.menuconvert.setTitle(
            QCoreApplication.translate("MainWindow", "Convert", None)
        )
        self.menuKernel.setTitle(
            QCoreApplication.translate("MainWindow", "Kernel", None)
        )

    # retranslateUi
