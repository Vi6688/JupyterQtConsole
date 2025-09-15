from PySide6.QtGui import (
    QTextCursor,
    QFont,
    QColor,
    QTextCharFormat,
    QSyntaxHighlighter,
)

class PythonHighlighter(QSyntaxHighlighter):
    KEYWORDS = [
        "False",
        "class",
        "finally",
        "is",
        "return",
        "None",
        "continue",
        "for",
        "lambda",
        "try",
        "True",
        "def",
        "from",
        "nonlocal",
        "while",
        "and",
        "del",
        "global",
        "not",
        "with",
        "as",
        "elif",
        "if",
        "or",
        "yield",
        "assert",
        "else",
        "import",
        "pass",
        "break",
        "except",
        "in",
        "raise",
    ]

    def __init__(self, document):
        super().__init__(document)
        self.keywordFormat = QTextCharFormat()
        self.keywordFormat.setForeground(QColor("teal"))
        self.keywordFormat.setFontWeight(QFont.Bold)

        self.stringFormat = QTextCharFormat()
        self.stringFormat.setForeground(QColor("darkGreen"))

        self.commentFormat = QTextCharFormat()
        self.commentFormat.setForeground(QColor("darkGray"))
        self.commentFormat.setFontItalic(True)

    def highlightBlock(self, text):
        import re

        # Highlight keywords
        for word in PythonHighlighter.KEYWORDS:
            for match in re.finditer(r"\b" + word + r"\b", text):
                self.setFormat(match.start(), len(word), self.keywordFormat)
        # Strings
        for match in re.finditer(r'(\'[^\']*\'|"[^"]*")', text):
            self.setFormat(match.start(), len(match.group()), self.stringFormat)
        # Comments
        comment_index = text.find("#")
        if comment_index != -1:
            self.setFormat(comment_index, len(text) - comment_index, self.commentFormat)
