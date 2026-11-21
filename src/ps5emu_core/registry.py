"""Plugin registry — discovers extension modules under a directory."""
from __future__ import annotations

import importlib.util
import logging
from pathlib import Path
from types import ModuleType

log = logging.getLogger(__name__)


class PluginRegistry:
    """Scans `plugin_dir` for `ps5x_*.py` modules and exposes lifecycle hooks."""

    HOOKS = ("on_host_boot", "on_guest_loaded", "on_frame", "on_host_shutdown")

    def __init__(self, plugin_dir: Path) -> None:
        self.plugin_dir = Path(plugin_dir)
        self.plugins: list[ModuleType] = []

    def discover(self) -> None:
        if not self.plugin_dir.exists():
            log.warning("plugin dir missing: %s", self.plugin_dir)
            return
        for entry in sorted(self.plugin_dir.glob("ps5x_*.py")):
            spec = importlib.util.spec_from_file_location(entry.stem, entry)
            if spec is None or spec.loader is None:
                continue
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if getattr(module, "PLUGIN_NAME", None):
                log.info("registered plugin: %s", module.PLUGIN_NAME)
                self.plugins.append(module)

    def call_hook(self, hook: str, *args: object) -> None:
        assert hook in self.HOOKS, f"unknown hook {hook}"
        for plugin in self.plugins:
            fn = getattr(plugin, hook, None)
            if callable(fn):
                try:
                    fn(*args)
                except Exception:  # noqa: BLE001
                    log.exception("plugin %s failed in hook %s", plugin.__name__, hook)