"""EmulatorHost — ties the CPU/GPU backends to the plugin registry."""
from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from ps5emu_core.registry import PluginRegistry
from ps5emu_infra.settings import Settings

log = logging.getLogger(__name__)


@dataclass
class HostState:
    guest_path: Optional[Path] = None
    running: bool = False
    frames: int = 0


class EmulatorHost:
    """Central orchestrator that owns the guest VM lifecycle."""

    def __init__(self, registry: PluginRegistry, settings: Settings) -> None:
        self.registry = registry
        self.settings = settings
        self.state = HostState()

    def boot(self) -> None:
        log.info("booting ps5-emu host, plugins=%d", len(self.registry.plugins))
        # trigger lifecycle hooks on all registered extension modules
        self.registry.call_hook("on_host_boot", self)

    def load_guest(self, path: str | Path) -> None:
        resolved = Path(path).expanduser().resolve()
        log.info("loading guest image: %s", resolved)
        self.state.guest_path = resolved
        self.registry.call_hook("on_guest_loaded", resolved)
        self.state.running = True

    def tick(self, frames: int = 1) -> None:
        for _ in range(frames):
            self.registry.call_hook("on_frame", self.state.frames)
            self.state.frames += 1

    def shutdown(self) -> None:
        self.state.running = False
        self.registry.call_hook("on_host_shutdown", self)