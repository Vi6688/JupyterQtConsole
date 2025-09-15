import os, json, time
from PySide6.QtCore import Qt
from PySide6.QtGui import QTextCursor, QKeySequence
from PySide6.QtWidgets import QTextEdit, QMessageBox
import re
from PySide6.QtWidgets import QCompleter
from PySide6.QtCore import Qt


class Event:
    HISTORY_FILE = os.path.expanduser("~/.my_repl_history.json")

    def __init__(self, parent):
        self.parent = parent  # main window
        self.inputEdit = parent.inputEdit
        self.outputEdit = parent.outputEdit
        self.client = parent.client
        self.statusbar = parent.statusbar

        self.history = []
        self.historyIndex = 0
        self._closing = False
        self._multilineBuffer = []  # store lines for multiline input

        self.loadHistory()
        self.history_search_prefix = None
        self._in_history_navigation = False
        # ensure historyIndex starts at len(self.history)
        self.historyIndex = len(self.history)
        # Override key press
        self.inputEdit.keyPressEvent = self.inputKeyPress

    # ------------------------------
    # Run request
    # ------------------------------
    def onRunRequested(self):
        code = self.inputEdit.toPlainText()
        if not code.strip():
            return

        # Detect multiline (e.g. "for", "if", "def" without proper end)
        if self.isMultilineIncomplete(code):
            self._multilineBuffer.append(code)
            self.parent.appendOutput("... " + code, outputType="input")
            self.inputEdit.clear()
            return

        if self._multilineBuffer:
            self._multilineBuffer.append(code)
            code = "\n".join(self._multilineBuffer)
            self._multilineBuffer.clear()

        self.appendHistory(code)
        self.inputEdit.clear()
        self.parent.appendOutput(code, outputType="input")
        self.client.execute(code)

    def isMultilineIncomplete(self, code: str) -> bool:
        """Detect if the input should continue (like Python REPL)."""
        stripped = code.strip()
        return (
            stripped.endswith(":")
            or stripped.endswith("\\")
            or stripped in {"def", "for", "if", "while", "class", "try"}
        )

    # ------------------------------
    # History management
    # ------------------------------

    def appendHistory(self, code: str):
        code = code.rstrip()  # remove trailing spaces
        if code:
            # Remove previous duplicate if exists
            if code in self.history:
                self.history.remove(code)
            self.history.append(code)
            self.history_search_prefix = None
            self.historyIndex = len(self.history)
            self.saveHistory()

    def loadHistory(self):
        if os.path.exists(self.HISTORY_FILE):
            try:
                with open(self.HISTORY_FILE, "r") as f:
                    raw_history = json.load(f)
                    # Remove duplicates while keeping last occurrence and strip trailing spaces
                    seen = set()
                    self.history = []
                    for item in reversed(raw_history):
                        item = item.rstrip()  # remove trailing spaces
                        if item not in seen:
                            seen.add(item)
                            self.history.append(item)
                    self.history.reverse()  # restore original order
                    self.historyIndex = len(self.history)
            except Exception:
                self.history = []

    def saveHistory(self):
        try:
            with open(self.HISTORY_FILE, "w") as f:
                json.dump(self.history[-500:], f)  # keep last 500 commands
        except Exception:
            pass

    # ------------------------------
    # Key handling
    # ------------------------------
    def inputKeyPress(self, event):
        key = event.key()
        mods = event.modifiers()
        if key == Qt.Key_Backspace:
            cursor = self.inputEdit.textCursor()
            cursor.movePosition(QTextCursor.StartOfLine, QTextCursor.KeepAnchor)
            current_line = cursor.selectedText()

            if current_line.endswith("    "):  # 4 spaces
                for _ in range(4):
                    QTextEdit.keyPressEvent(self.inputEdit, event)
                return
    
        if key in (Qt.Key_Return, Qt.Key_Enter) and (mods & Qt.ShiftModifier):
            self.onRunRequested()
        # --- ENTER / RETURN ---
        elif key in (Qt.Key_Return, Qt.Key_Enter):
            cursor = self.inputEdit.textCursor()
            cursor.movePosition(QTextCursor.StartOfLine, QTextCursor.KeepAnchor)
            current_line = cursor.selectedText()

            # Let QTextEdit handle the newline
            QTextEdit.keyPressEvent(self.inputEdit, event)

            # Count leading spaces
            indent = len(current_line) - len(current_line.lstrip(" "))

            # If line ends with ':' → add one indent level (4 spaces)
            if current_line.strip().endswith(":"):
                indent += 4

            # Insert indentation
            self.inputEdit.insertPlainText(" " * indent)
            return

                # --- UP history navigation ---
        elif key == Qt.Key_Up:
            current_text = self.inputEdit.toPlainText()
            stripped = current_text.strip()
            # If starting fresh search
            if not self._in_history_navigation:
                self.history_search_prefix = stripped
                self.historyIndex = len(self.history)  # reset search start
                self._in_history_navigation = True

            # search backwards
            for i in range(self.historyIndex - 1, -1, -1):
                if self.history[i].startswith(self.history_search_prefix):
                    self.historyIndex = i
                    self.inputEdit.setPlainText(self.history[i])
                    self.inputEdit.moveCursor(QTextCursor.End)
                    return
            return

        # --- DOWN history navigation ---
        elif key == Qt.Key_Down:
            current_text = self.inputEdit.toPlainText()
            stripped = current_text.strip()

            # If empty input, regular cycling
            if not stripped and not self._in_history_navigation:
                self.history_search_prefix = None
                if self.history:
                    self.historyIndex = min(len(self.history), self.historyIndex + 1)
                    if self.historyIndex < len(self.history):
                        self.inputEdit.setPlainText(self.history[self.historyIndex])
                    else:
                        self.inputEdit.clear()
                return

            # If starting fresh search
            if not self._in_history_navigation:
                self.history_search_prefix = stripped
                self.historyIndex = -1
                self._in_history_navigation = True

            # search forwards
            for i in range(self.historyIndex + 1, len(self.history)):
                if self.history[i].startswith(self.history_search_prefix):
                    self.historyIndex = i
                    self.inputEdit.setPlainText(self.history[i])
                    self.inputEdit.moveCursor(QTextCursor.End)
                    return
            self.inputEdit.clear()
            self._in_history_navigation = False
            return

        # --- TAB completion from history ---
        elif key == Qt.Key_Tab:
            event.accept()
            # self.onTabPressed()
        else:
            # For all other keys, reset history navigation
            self._in_history_navigation = False
            self.history_search_prefix = None
            self.historyIndex = len(self.history)
            QTextEdit.keyPressEvent(self.inputEdit, event)

    def onTabPressed(self):
        text = self.inputEdit.toPlainText()
        cursor = self.inputEdit.textCursor()
        pos = cursor.position()

        # Get word before cursor
        import re

        prefix_match = re.search(r"(\w+(\.\w*)?)$", text[:pos])
        prefix = prefix_match.group(1) if prefix_match else ""

        completions = []

        # Attribute completion
        if "." in prefix:
            try:
                obj_name, attr_prefix = prefix.rsplit(".", 1)
                ns = self.client.locals if hasattr(self.client, "locals") else {}
                obj = eval(obj_name, ns, ns)
                completions = [
                    f"{obj_name}.{a}" for a in dir(obj) if a.startswith(attr_prefix)
                ]
            except Exception:
                completions = []
        else:
            # History-based completion
            completions = [h for h in self.history if h.startswith(prefix)]

        if not completions:
            return

        # Create completer
        completer = QCompleter(completions, self.inputEdit)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setWidget(self.inputEdit)

        # Function to insert selected completion
        def insertCompletion(selected):
            cursor = self.inputEdit.textCursor()
            # select current prefix
            start_pos = pos - len(prefix)
            cursor.setPosition(start_pos)
            cursor.setPosition(pos, QTextCursor.KeepAnchor)
            cursor.removeSelectedText()
            cursor.insertText(selected)
            self.inputEdit.setTextCursor(cursor)
            completer.popup().hide()

        completer.activated.connect(insertCompletion)
        completer.complete()

    def saveInputToFile(self):
        try:
            code = self.inputEdit.toPlainText()
            if code.strip():
                path = os.path.expanduser("~/last_input.py")
                with open(path, "w") as f:
                    f.write(code)
                self.statusbar.showMessage(f"Saved input to {path}", 3000)
        except Exception as e:
            QMessageBox.warning(self.parent, "Save Failed", str(e))
