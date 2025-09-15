# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designertLXWJA.ui'
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
        # --- Modern UI stylesheet ---
        MainWindow.setStyleSheet(
            """
    QMainWindow {
        background: #1e1e1e;
    }

    /* --- Menubar --- */
    QMenuBar {
        background-color: #2d2d2d;
        border-bottom: 1px solid #3c3c3c;
        font-family: 'Segoe UI', 'Ubuntu', sans-serif;
        font-size: 13px;
        padding: 2px;  /* smaller height */
        color: #cccccc;
    }
    QMenuBar::item {
        background: #2d2d2d;
        padding: 4px 10px;
        margin: 2px;
        border-radius: 4px;
        border: 1px solid #3c3c3c;  /* border for buttons */
    }
    QMenuBar::item:selected {
        background: #0078d7;
        color: white;
        border: 1px solid #005a9e;  /* highlight border */
    }

    /* --- Menus --- */
    QMenu {
        background-color: #2d2d2d;
        border: 1px solid #3c3c3c;
        border-radius: 8px;
        padding: 6px;
        font-size: 13px;
        color: #cccccc;
    }
    QMenu::item {
        padding: 6px 20px;
        border-radius: 4px;
    }
    QMenu::item:selected {
        background-color: #0078d7;
        color: white;
    }

    /* --- Text editors (input, shell, output) --- */
    QTextEdit, QTextBrowser {
        background: #252526;
        border: 1px solid #3c3c3c;
        border-radius: 8px;
        padding: 8px;
        font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
        font-size: 13px;
        color: #f5f5f5;
        selection-background-color: #0078d7;
        selection-color: white;
    }

    /* --- Frames --- */
    QFrame {
        border: 1px solid #3c3c3c;
        border-radius: 6px;
        background: transparent;
    }

    /* --- Status bar --- */
    QStatusBar {
        background: #2d2d2d;
        border-top: 1px solid #3c3c3c;
        font-size: 12px;
        padding: 4px;
        color: #bbbbbb;
    }

    /* --- Scrollbars --- */
    QScrollBar:vertical {
        border: 1px solid #3c3c3c;
        background: #2a2a2a;
        width: 10px;
        margin: 0px;
        border-radius: 5px;
    }
    QScrollBar::handle:vertical {
        background: #555555;
        border-radius: 5px;
        min-height: 20px;
    }
    QScrollBar::handle:vertical:hover {
        background: #777777;
    }
    QScrollBar:horizontal {
        border: 1px solid #3c3c3c;
        background: #2a2a2a;
        height: 10px;
        margin: 0px;
        border-radius: 5px;
    }
    QScrollBar::handle:horizontal {
        background: #555555;
        border-radius: 5px;
        min-width: 20px;
    }
    QScrollBar::handle:horizontal:hover {
        background: #777777;
    }

    /* --- Tool buttons (if added later) --- */
    QToolButton {
        background: #2d2d2d;
        border: 1px solid #3c3c3c;
        padding: 6px;
        margin: 2px;
        border-radius: 6px;
        color: #cccccc;
    }
    QToolButton:hover {
        background: #0078d7;
        color: white;
        border: 1px solid #005a9e;
    }
"""
        )

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
        self.widget_2.setMaximumSize(QSize(16777215, 170))
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
        self.menuSaveAs = QMenu(self.menubar)
        self.menuSaveAs.setObjectName("menuSaveAs")
        self.menusize = QMenu(self.menubar)
        self.menusize.setObjectName("menusize")
        self.menuexit = QMenu(self.menubar)
        self.menuexit.setObjectName("menuexit")
        self.menuconvert = QMenu(self.menubar)
        self.menuconvert.setObjectName("menuconvert")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSaveAs.menuAction())
        self.menubar.addAction(self.menuconvert.menuAction())
        self.menubar.addAction(self.menusize.menuAction())
        self.menubar.addAction(self.menuexit.menuAction())
        self.menuFile.addAction(self.actionnew)
        self.menuFile.addAction(self.actionopen)
        self.menuFile.addAction(self.actionsave_2)
        self.menuSaveAs.addAction(self.actionsave)
        self.menuSaveAs.addAction(self.actionsaveAs)
        self.menusize.addAction(self.actionincrease)
        self.menusize.addAction(self.actiondecrease)
        self.menuconvert.addAction(self.actionconvertToHtml)
        self.menuconvert.addAction(self.actionconvert_to_pdf)

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
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", "File", None))
        self.menuSaveAs.setTitle(QCoreApplication.translate("MainWindow", "Save", None))
        self.menusize.setTitle(QCoreApplication.translate("MainWindow", "Size", None))
        self.menuexit.setTitle(QCoreApplication.translate("MainWindow", "Exit", None))
        self.menuconvert.setTitle(
            QCoreApplication.translate("MainWindow", "Convert", None)
        )

    # retranslateUi
