"""Entry point for the ps5-emu desktop shell."""
import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication

from ps5emu_core.host import EmulatorHost
from ps5emu_core.registry import PluginRegistry
from ps5emu_infra.telemetry import init_telemetry
from ps5emu_infra.settings import load_settings


def main(argv: list[str] | None = None) -> int:
    argv = argv or sys.argv
    settings = load_settings(Path.home() / ".ps5emu" / "settings.toml")
    init_telemetry(settings.telemetry_endpoint, enabled=settings.telemetry_enabled)

    registry = PluginRegistry(plugin_dir=settings.plugin_dir)
    registry.discover()

    host = EmulatorHost(registry=registry, settings=settings)
    host.boot()

    app = QApplication(argv)
    from ps5emu_app.shell.main_window import MainWindow

    window = MainWindow(host=host)
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())