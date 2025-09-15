from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from fpdf import FPDF

_HAS_FPDF = True

class Menu:
    def __init__(self):
        pass

    def newFile(self):
        self.inputEdit.clear()
        self.outputEdit.clear()
        self.currentFile = None
        self.statusbar.showMessage("New file")

    def openFile(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "Text Files (*.txt);;All Files (*)"
        )
        if path:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    self.inputEdit.setPlainText(f.read())
                self.currentFile = path
                self.statusbar.showMessage(f"Opened {path}")
            except Exception as e:
                QMessageBox.warning(self, "Open failed", f"Could not open file:\n{e}")

    def saveFile(self):
        if self.currentFile:
            try:
                with open(self.currentFile, "w", encoding="utf-8") as f:
                    f.write(self.inputEdit.toPlainText())
                self.statusbar.showMessage(f"Saved {self.currentFile}")
            except Exception as e:
                QMessageBox.warning(self, "Save failed", f"Could not save file:\n{e}")
        else:
            self.saveAsFile()

    def saveAsFile(self):
        path, _ = QFileDialog.getSaveFileName(
            self, "Save File As", "", "Text Files (*.txt);;All Files (*)"
        )
        if path:
            try:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(self.inputEdit.toPlainText())
                self.currentFile = path
                self.statusbar.showMessage(f"Saved {path}")
            except Exception as e:
                QMessageBox.warning(self, "Save failed", f"Could not save file:\n{e}")

    def convertToHtml(self):
        path, _ = QFileDialog.getSaveFileName(
            self, "Export to HTML", "", "HTML Files (*.html)"
        )
        if path:
            try:
                html = (
                    f"<html><body><pre>{self.outputEdit.toHtml()}</pre></body></html>"
                )
                with open(path, "w", encoding="utf-8") as f:
                    f.write(html)
                self.statusbar.showMessage(f"Exported HTML to {path}")
            except Exception as e:
                QMessageBox.warning(
                    self, "Export failed", f"Could not export to HTML:\n{e}"
                )

    def convertToPdf(self):
        if not _HAS_FPDF:
            QMessageBox.information(
                self,
                "Missing dependency",
                "Install 'fpdf' (pip install fpdf) to export PDF.",
            )
            return
        path, _ = QFileDialog.getSaveFileName(
            self, "Export to PDF", "", "PDF Files (*.pdf)"
        )
        if path:
            try:
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Courier", size=10)
                for line in self.outputEdit.toPlainText().splitlines():
                    pdf.multi_cell(0, 5, line)
                pdf.output(path)
                self.statusbar.showMessage(f"Exported PDF to {path}")
            except Exception as e:
                QMessageBox.warning(
                    self, "Export failed", f"Could not export to PDF:\n{e}"
                )

    def changeFontSize(self, delta):
        self.baseFontSize = max(8, self.baseFontSize + delta)
        font = QFont("Courier", self.baseFontSize)
        self.outputEdit.setFont(font)
        self.inputEdit.setFont(font)
        self.statusbar.showMessage(f"Font size: {self.baseFontSize}")
