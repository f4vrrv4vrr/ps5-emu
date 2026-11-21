"""Main application window for the ps5-emu host."""
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel,
)

from ps5emu_core.host import EmulatorHost


class MainWindow(QMainWindow):
    def __init__(self, host: EmulatorHost) -> None:
        super().__init__()
        self.host = host
        self.setWindowTitle("ps5-emu — Playstation 5 Emulator (dev build)")
        self.resize(1280, 720)

        central = QWidget()
        layout = QVBoxLayout(central)

        self.status = QLabel("idle")
        self.btn_boot = QPushButton("Boot ELF")
        self.btn_boot.clicked.connect(self._on_boot)

        layout.addWidget(self.status)
        layout.addWidget(self.btn_boot)
        self.setCentralWidget(central)

    def _on_boot(self) -> None:
        self.status.setText("booting…")
        self.host.load_guest("samples/hello_ps5.elf")
        self.status.setText("running")