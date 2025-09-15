import base64
from PySide6.QtCore import QObject, Signal
from jupyter_client import KernelManager
import threading
import re
ANSI_ESCAPE_RE = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")


def clean_ansi(text: str) -> str:
    """Remove ANSI escape sequences from text."""
    return ANSI_ESCAPE_RE.sub("", text)


class JupyterClient(QObject):
    output = Signal(str)  # text output
    image = Signal(bytes)  # PNG/JPEG image bytes
    error = Signal(str)  # errors
    status = Signal(str)  # 'busy', 'idle', etc
    started = Signal()
    stopped = Signal()
    failed = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.km = None
        self.kc = None
        self._running = False
        self._poll_thread = None
        self._pending = set()

        try:
            self.km = KernelManager()
            self.km.start_kernel()
            self.kc = self.km.client()
            self.kc.start_channels()
        except Exception as e:
            self.failed.emit(f"Failed to start kernel: {e}")
            raise

        self._running = True
        self._poll_thread = threading.Thread(target=self._poll_iopub, daemon=True)
        self._poll_thread.start()
        self.started.emit()

    def execute(self, code: str) -> str:
        if not self.kc:
            raise RuntimeError("Kernel client not started")
        msg_id = self.kc.execute(code)
        self._pending.add(msg_id)
        return msg_id

    def _poll_iopub(self):
        """Background loop reading iopub messages and emitting signals."""
        while self._running:
            try:
                msg = self.kc.get_iopub_msg(timeout=0.5)
            except Exception:
                continue

            try:
                msg_type = msg.get("msg_type", "")
                parent = msg.get("parent_header") or {}
                parent_id = parent.get("msg_id")

                if msg_type == "stream":
                    text = msg.get("content", {}).get("text", "")
                    if text:
                        self.output.emit("".join(text))

                elif msg_type in ("execute_result", "display_data"):
                    data = msg.get("content", {}).get("data", {})

                    # Emit all textual outputs first
                    if "text/plain" in data:
                        self.output.emit(str(data["text/plain"]))
                    if "text/html" in data:
                        self.output.emit(str(data["text/html"]))
                    if "text/markdown" in data:
                        self.output.emit(str(data["text/markdown"]))

                    # Emit images
                    for img_type in ("image/png", "image/jpeg"):
                        if img_type in data:
                            try:
                                raw = base64.b64decode(data[img_type])
                                self.image.emit(raw)
                            except Exception:
                                self.output.emit(f"[failed to decode {img_type}]")

                elif msg_type == "error":
                    tb = msg.get("content", {}).get("traceback", [])
                    tb_clean = [clean_ansi(line) for line in tb]
                    self.error.emit("\n".join(tb_clean))

                elif msg_type == "status":
                    state = msg.get("content", {}).get("execution_state", "")
                    self.status.emit(state)
                    if state == "idle" and parent_id in self._pending:
                        self._pending.discard(parent_id)

            except Exception as e:
                self.error.emit(f"Exception processing iopub message: {e}")

    def shutdown(self):
        self._running = False
        try:
            if self.kc:
                self.kc.stop_channels()
            if self.km:
                self.km.shutdown_kernel(now=True)
        except Exception:
            pass
        if self._poll_thread:
            self._poll_thread.join(timeout=1.0)
        self.stopped.emit()

    def interuptKernel(self):
        try:
            if self.km:
                self.km.interrupt_kernel()
        except Exception as e:
            self.error.emit(f"Interrupt failed: {e}")

    def restartKernel(self):
        try:
            if self.km:
                self.km.restart_kernel(now=True)
        except Exception as e:
            self.error.emit(f"Restart failed: {e}")
