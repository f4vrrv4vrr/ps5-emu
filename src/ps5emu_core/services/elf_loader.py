"""Minimal ELF64 loader used by the guest bootstrap."""
from __future__ import annotations

import struct
from dataclasses import dataclass
from pathlib import Path

ELF_MAGIC = b"\x7fELF"
PT_LOAD = 1


@dataclass
class LoadSegment:
    vaddr: int
    filesz: int
    memsz: int
    offset: int
    flags: int


class ElfLoader:
    def __init__(self, path: Path) -> None:
        self.path = Path(path)
        self.segments: list[LoadSegment] = []
        self.entry: int = 0

    def parse(self) -> "ElfLoader":
        data = self.path.read_bytes()
        if data[:4] != ELF_MAGIC:
            raise ValueError(f"not an ELF file: {self.path}")
        if data[4] != 2:
            raise ValueError("only ELF64 supported")
        e_entry, e_phoff = struct.unpack_from("<QQ", data, 0x18)
        e_phentsize, e_phnum = struct.unpack_from("<HH", data, 0x36)
        self.entry = e_entry
        for i in range(e_phnum):
            base = e_phoff + i * e_phentsize
            p_type, p_flags, p_offset, p_vaddr, _p_paddr, p_filesz, p_memsz, _ = \
                struct.unpack_from("<IIQQQQQQ", data, base)
            if p_type == PT_LOAD:
                self.segments.append(LoadSegment(p_vaddr, p_filesz, p_memsz, p_offset, p_flags))
        return self

    def summary(self) -> str:
        return f"entry=0x{self.entry:x} segments={len(self.segments)}"