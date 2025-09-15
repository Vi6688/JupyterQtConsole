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


class Screen:
    def __init__(self):
        pass

    def appendError(self, text: str):
        # mark errors with prefix
        self.appendOutput("[error] " + text, outputType="error")


    def appendImage(self, bytes_png: bytes):
        """Insert image into QTextBrowser with white background."""
        try:
            b64 = base64.b64encode(bytes_png).decode("ascii")
            html_img = f"""
            <div style="background-color:white; padding:4px; border-radius:4px; display:inline-block;">
                <img src="data:image/png;base64,{b64}" />
            </div><br/>
            """
            self.outputEdit.moveCursor(QTextCursor.End)
            self.outputEdit.insertHtml(html_img)
            self.outputEdit.moveCursor(QTextCursor.End)
        except Exception as e:
            self.appendOutput(f"[image decode fail] {e}")

    def onStatus(self, state: str):
        self.statusbar.showMessage(f"Kernel status: {state}")

    def appendOutput(self, text: str, outputType="stdout"):
        """
        Modern vibrant output for QTextBrowser.
        outputType: "stdout", "error", "input"
        """
        cursor = self.outputEdit.textCursor()
        cursor.movePosition(QTextCursor.End)

        # --- Styles for dark theme ---
        styles = {
            "stdout": "color:#f5f5f5; background:transparent; padding:0 2px;",
            "error": (
                "color:#ff6c6b; font-weight:700; "
                "background:rgba(255,108,107,0.15); padding:2px 6px; border-radius:5px;"
            ),
            "input": (
                "color:#61afef; font-weight:700; "
                "background:rgba(97,175,239,0.12); padding:2px 6px; border-radius:5px;"
            ),
        }
        base_style = styles.get(outputType, styles["stdout"])
        font_css = (
            "font-family:'JetBrains Mono','Fira Code','Courier New',monospace; font-size:14px; line-height:1.5;"
        )

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

            # --- Restore strings with green ---
            def _restore_placeholder(m):
                idx = int(m.group(1))
                s = strings[idx]
                return f'<span style="color:#98c379;">{html.escape(s)}</span>'

            highlighted = re.sub(r"\x00STR(\d+)\x00", _restore_placeholder, highlighted)

            # --- URLs clickable ---
            def _url_repl(m):
                url = m.group(0)
                return f'<a href="{url}" style="color:#56b6c2; text-decoration:underline;">{html.escape(url)}</a>'

            highlighted = URL_RE.sub(_url_repl, highlighted)

            # --- Input prompt styling ---
            if outputType == "input":
                prompt_html = (
                    '<span style="color:#e5c07b; font-weight:800; margin-right:6px;">&gt;&gt;&gt;</span>'
                )
                final_html = f'{prompt_html}<span style="{base_style} {font_css}">{highlighted}</span>'
            elif outputType == "error":
                final_html = f'<span style="{base_style} {font_css}">{highlighted}</span>'
            else:
                # subtle background glow for stdout
                final_html = f'<span style="background:rgba(255,255,255,0.02); {base_style} {font_css}">{highlighted}</span>'

            cursor.insertHtml(final_html + "<br>\n")

        # --- Scroll to bottom ---
        self.outputEdit.moveCursor(QTextCursor.End)
        self.outputEdit.ensureCursorVisible()
