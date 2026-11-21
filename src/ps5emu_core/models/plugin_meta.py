"""Metadata for a discovered extension module."""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class PluginMeta:
    name: str
    version: str
    author: str
    path: Path
    syscalls: tuple[int, ...] = field(default_factory=tuple)

    def short(self) -> str:
        return f"{self.name} {self.version} by {self.author} ({len(self.syscalls)} syscalls)"