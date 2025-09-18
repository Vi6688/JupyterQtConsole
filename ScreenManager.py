from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
import re
import html
import base64

# put this near top-level (once)
PY_KEYWORDS = [
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
KEYWORD_RE = re.compile(r"\b(" + "|".join(re.escape(k) for k in PY_KEYWORDS) + r")\b")
STRING_RE = re.compile(r"(\".*?(?<!\\)\"|\'.*?(?<!\\)\')", re.DOTALL)
NUMBER_RE = re.compile(r"\b\d+(\.\d+)?\b")
URL_RE = re.compile(r"(https?://[^\s<>]+)")
import uuid
from PySide6.QtCore import QUrl, Qt
from PySide6.QtGui import QImage, QTextImageFormat, QTextCursor, QTextDocument

class Screen:
    def __init__(self):
        pass

    def appendError(self, text: str):
        # mark errors with prefix
        self.appendOutput("[error] " + text, outputType="error")

    def appendImage(self, bytes_png: bytes):
        """Insert PNG into QTextBrowser with rounded white background card."""
        try:
            # Load image
            img = QImage.fromData(bytes_png, "PNG")
            if img.isNull():
                raise ValueError("Invalid PNG")

            # Flatten transparency onto white
            result = QImage(img.size(), QImage.Format_RGB32)
            result.fill(QColor("white"))
            painter = QPainter(result)
            painter.drawImage(0, 0, img)
            painter.end()

            # Re-encode to PNG for embedding
            ba = QByteArray()
            buffer = QBuffer(ba)
            buffer.open(QIODevice.WriteOnly)
            result.save(buffer, "PNG")
            buffer.close()
            b64 = base64.b64encode(ba.data()).decode("ascii")

            # Insert into QTextBrowser with rounded white card
            html_img = f"""
            <div style="
                margin:12px 0;
                padding:8px;
                background:#ffffff;
                border:1px solid #dddddd;
                border-radius:12px;   /* Rounded corners */
                text-align:center;
                box-shadow:0 2px 8px rgba(0,0,0,0.3); /* subtle shadow */
            ">
                <img src="data:image/png;base64,{b64}" style="max-width:95%; border-radius:8px;" />
            </div>
            <div style="height:10px;"></div>
            """

            cursor = self.outputEdit.textCursor()
            cursor.movePosition(QTextCursor.End)
            cursor.insertHtml(html_img)
            self.outputEdit.ensureCursorVisible()
        except Exception as e:
            self.appendOutput(f"[image decode fail] {e}", outputType="error")


    def onStatus(self, state: str):
        self.statusbar.showMessage(f"Kernel status: {state}")

    def appendOutput(self, text: str, outputType="stdout"):
        """
        Ultra-modern, vibrant output for QTextBrowser.
        Matches dark blue accent theme.
        outputType: "stdout", "error", "input"
        """
        cursor = self.outputEdit.textCursor()
        cursor.movePosition(QTextCursor.End)

        # --- Styles tuned for vibrant dark theme ---
        styles = {
            "stdout": (
                "color:#f0f0f0; background:rgba(255,255,255,0.03); "
                "padding:2px 6px; border-radius:6px;"
            ),
            "error": (
                "color:#ff6b6b; font-weight:700; "
                "background:rgba(255,107,107,0.18); padding:2px 6px; "
                "border-radius:6px; border:1px solid rgba(255,107,107,0.3);"
            ),
            "input": (
                "color:#61afef; font-weight:700; "
                "background:rgba(97,175,239,0.15); padding:2px 6px; "
                "border-radius:6px; border:1px solid rgba(97,175,239,0.3);"
            ),
        }
        base_style = styles.get(outputType, styles["stdout"])
        font_css = (
            "font-family:'JetBrains Mono','Fira Code','Courier New',monospace;"
            "font-size:14px; line-height:1.55;"
        )
        count = 0
        for raw_line in text.splitlines() or [""]:
            line = raw_line

            # --- Extract string literals ---
            strings = []

            def _store_string(m):
                idx = len(strings)
                strings.append(m.group(0))
                return f"\x00STR{idx}\x00"

            no_strings = STRING_RE.sub(_store_string, line)

            # --- Escape HTML ---
            escaped = html.escape(no_strings)

            # --- Highlight keywords & numbers ---
            def _kw_num_repl(m):
                g = m.group(0)
                if KEYWORD_RE.match(g):
                    return f'<span style="color:#c792ea; font-weight:600;">{g}</span>'
                else:
                    return f'<span style="color:#ffcb6b; font-weight:600;">{g}</span>'

            combined_re = re.compile(
                r"\b("
                + "|".join(re.escape(k) for k in PY_KEYWORDS)
                + r")\b|\b\d+(\.\d+)?\b"
            )
            highlighted = combined_re.sub(_kw_num_repl, escaped)

            # --- Restore strings (vibrant green) ---
            def _restore_placeholder(m):
                idx = int(m.group(1))
                s = strings[idx]
                return f'<span style="color:#98c379;">{html.escape(s)}</span>'  

            highlighted = re.sub(r"\x00STR(\d+)\x00", _restore_placeholder, highlighted)

            # --- URLs clickable (cyan) ---
            def _url_repl(m):
                url = m.group(0)
                return (
                    f'<a href="{url}" '
                    f'style="color:#56b6c2; text-decoration:underline; font-weight:600;">'
                    f'{html.escape(url)}</a>'
                )

            highlighted = URL_RE.sub(_url_repl, highlighted)

            # --- Format per output type ---
            if outputType == "input":
                if not count:
                    cursor.insertHtml("<br>")
                prompt_html = (
                    '<span style="color:#e5c07b; font-weight:800; margin-right:6px;">&gt;&gt;&gt;</span>'
                )
                final_html = f'{prompt_html}<span style="{base_style} {font_css}">{highlighted}</span>'
            else:
                final_html = f'<span style="{base_style} {font_css}">{highlighted}</span>'
            count += 1
            cursor.insertHtml(final_html + "\n<br>")
        # --- Smooth auto-scroll ---
        self.outputEdit.moveCursor(QTextCursor.End)
        self.outputEdit.ensureCursorVisible()
