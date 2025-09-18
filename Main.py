# jupyter_qtconsole.py
import sys
import os
import json
import threading
import time
import base64
import re
from pathlib import Path
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from Ui import Ui_MainWindow  # Your auto-generated UI
from KernelManager import JupyterClient
from MenuManager import Menu
from HighLighter import PythonHighlighter
from HistoryManager import History
from ScreenManager import Screen
from EventManager import Event
from StyleSheet import styleSheet

class ShiftEnterFilter(QObject):
    runRequested = Signal()  # signal emitted when Shift+Enter is pressed

    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            if event.key() in (Qt.Key_Return, Qt.Key_Enter) and (
                event.modifiers() & Qt.ShiftModifier
            ):
                self.runRequested.emit()  # tell MainWindow to run code
                return True  # consume event
        return super().eventFilter(obj, event)


class MainWindow(QMainWindow, Ui_MainWindow, History, Menu, Screen):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(styleSheet)
        self.setupUi(self)
        self.client = None
        self.currentFile = None
        self.baseFontSize = 12

        # try to start client and show errors if any
        try:
            self.client = JupyterClient()
        except Exception as exc:
            QMessageBox.critical(
                self, "Kernel start failed", f"Could not start kernel:\n{exc}"
            )
            raise

        self.eventManager = Event(self)
        # connect signals from client
        self.client.output.connect(self.appendOutput)
        self.client.image.connect(self.appendImage)
        self.client.error.connect(self.appendError)
        self.client.status.connect(self.onStatus)

        # set fonts
        mono = QFont("Courier", self.baseFontSize)
        self.outputEdit.setFont(mono)
        self.inputEdit.setFont(mono)
        # attach filter to inputEdit
        self._filter = ShiftEnterFilter(self)
        self._filter.runRequested.connect(
            self.eventManager.onRunRequested
        )  # handle execution
        self.inputEdit.installEventFilter(self._filter)

        # Use hasattr checks because UI may have slightly different names
        self.actionnew.triggered.connect(self.newFile)
        self.actionopen.triggered.connect(self.openFile)
        self.actionsave_2.triggered.connect(self.saveFile)
        self.actionsaveAs.triggered.connect(self.saveAsFile)
        self.actionconvertToHtml.triggered.connect(self.convertToHtml)
        self.actionconvert_to_pdf.triggered.connect(self.convertToPdf)
        self.actionincrease.triggered.connect(lambda: self.changeFontSize(2))
        self.actiondecrease.triggered.connect(lambda: self.changeFontSize(-2))
        self.actionrestart.triggered.connect(self.client.restartKernel)
        self.actioninterrupt.triggered.connect(self.client.interuptKernel)
        self.actionshutdown.triggered.connect(self.client.shutdown)

        # Add optional extra actions (Open vs actionOpen duplicates)
        self.actionOpen.triggered.connect(self.openFile)

        self.highlighter = PythonHighlighter(self.inputEdit.document())
        # Shift+Enter
        self._filter = ShiftEnterFilter(self)
        self._filter.runRequested.connect(self.eventManager.onRunRequested)
        self.inputEdit.installEventFilter(self._filter)
        self.inputEdit.setFocus()
        # Update statusbar
        self.statusbar.showMessage("Kernel started")

        # ensure clean shutdown when window closes
        self._closing = False


def main():
    app = QApplication(sys.argv)
    try:
        win = MainWindow()
    except Exception as e:
        QMessageBox.critical(None, "Startup error", str(e))
        return 1
    # win.setMaximumSize()
    win.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
