"""Shared contracts implemented by extension modules."""
from __future__ import annotations

from pathlib import Path
from typing import Protocol, runtime_checkable


@runtime_checkable
class HleModule(Protocol):
    """High-level emulation (HLE) module contract for PS5 syscall shims."""

    PLUGIN_NAME: str
    SUPPORTED_SYSCALLS: tuple[int, ...]

    def on_host_boot(self, host: object) -> None: ...
    def on_guest_loaded(self, elf_path: Path) -> None: ...
    def on_frame(self, frame_index: int) -> None: ...


@runtime_checkable
class GpuBackend(Protocol):
    NAME: str

    def init(self, width: int, height: int) -> None: ...
    def present(self, framebuffer: bytes) -> None: ...
    def shutdown(self) -> None: ...