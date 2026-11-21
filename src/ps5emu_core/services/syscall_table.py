"""Syscall ID → HLE handler dispatch table."""
from __future__ import annotations

from collections.abc import Callable

Handler = Callable[[int, int, int, int, int, int], int]


class SyscallTable:
    def __init__(self) -> None:
        self._table: dict[int, Handler] = {}

    def register(self, number: int, handler: Handler) -> None:
        if number in self._table:
            raise KeyError(f"syscall {number} already registered")
        self._table[number] = handler

    def dispatch(self, number: int, *args: int) -> int:
        handler = self._table.get(number)
        if handler is None:
            return -38  # ENOSYS equivalent
        return handler(*args)

    def __len__(self) -> int:
        return len(self._table)