styleSheet = """
    QMainWindow {
        background: #1b1b1b;
    }

    /* --- Menubar --- */
    QMenuBar {
        background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                          stop:0 #2a2a2a, stop:1 #202020);
        border-bottom: 1px solid #3c3c3c;
        font-family: 'Segoe UI', 'Ubuntu', sans-serif;
        font-size: 13px;
        padding: 4px;
        color: #dcdcdc;
    }
    QMenuBar::item {
        padding: 6px 12px;
        margin: 2px;
        border-radius: 6px;
        background: #2d2d2d;          /* default background */
        border: 1px solid #3c3c3c;
    }
    QMenuBar::item:selected {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #00a2ff, stop:1 #0066cc);
        color: white;
        border: 1px solid #005a9e;
        box-shadow: 0px 0px 6px #00a2ff;
    }

    /* --- Menus --- */
    QMenu {
        background-color: #252525;
        border: 1px solid #3c3c3c;
        border-radius: 10px;
        padding: 8px;
        font-size: 13px;
        color: #eeeeee;
    }
    QMenu::item {
        padding: 8px 24px;
        border-radius: 6px;
        background-color: #2d2d2d;   /* default background */
        margin: 2px;
    }
    QMenu::item:selected {
        background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                          stop:0 #00a2ff, stop:1 #0078d7);
        color: white;
    }

    /* --- Text editors --- */
    QTextEdit, QTextBrowser {
        background: #1e1e1e;
        border: 1px solid #3c3c3c;
        border-radius: 10px;
        padding: 10px;
        font-family: 'JetBrains Mono', 'Fira Code', monospace;
        font-size: 13px;
        color: #f5f5f5;
        selection-background-color: #00a2ff;
        selection-color: white;
    }
    QTextEdit:focus, QTextBrowser:focus {
        border: 1px solid #00a2ff;
        box-shadow: 0 0 8px #00a2ff;
    }

    /* --- Frames --- */
    QFrame {
        border: 1px solid #3c3c3c;
        border-radius: 8px;
        background: #1e1e1e;
    }

    /* --- Status bar --- */
    QStatusBar {
        background: #222222;
        border-top: 1px solid #3c3c3c;
        font-size: 12px;
        padding: 6px;
        color: #bbbbbb;
    }

    /* --- Scrollbars --- */
    QScrollBar:vertical {
        border: none;
        background: #2a2a2a;
        width: 12px;
        margin: 2px;
        border-radius: 6px;
    }
    QScrollBar::handle:vertical {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #00a2ff, stop:1 #0078d7);
        border-radius: 6px;
        min-height: 20px;
    }
    QScrollBar::handle:vertical:hover {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #33c4ff, stop:1 #0099ff);
    }

    QScrollBar:horizontal {
        border: none;
        background: #2a2a2a;
        height: 12px;
        margin: 2px;
        border-radius: 6px;
    }
    QScrollBar::handle:horizontal {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #00a2ff, stop:1 #0078d7);
        border-radius: 6px;
        min-width: 20px;
    }
    QScrollBar::handle:horizontal:hover {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #33c4ff, stop:1 #0099ff);
    }

    /* --- Tool buttons --- */
    QToolButton {
        background: #2d2d2d;
        border: 1px solid #3c3c3c;
        padding: 8px 12px;
        margin: 3px;
        border-radius: 8px;
        color: #cccccc;
    }
    QToolButton:hover {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #00a2ff, stop:1 #0078d7);
        color: white;
        border: 1px solid #005a9e;
        box-shadow: 0px 0px 6px #00a2ff;
    }
"""
