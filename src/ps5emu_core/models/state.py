"""Runtime state models for the guest VM."""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class GuestThread:
    tid: int
    rip: int
    rsp: int
    name: str = ""


@dataclass
class VmState:
    entry: int = 0
    image: Path | None = None
    threads: list[GuestThread] = field(default_factory=list)
    heap_top: int = 0x8000_0000
    stack_top: int = 0x7fff_0000

    def spawn_thread(self, tid: int, rip: int, name: str = "") -> GuestThread:
        thread = GuestThread(tid=tid, rip=rip, rsp=self.stack_top - 0x10 * tid, name=name)
        self.threads.append(thread)
        return thread