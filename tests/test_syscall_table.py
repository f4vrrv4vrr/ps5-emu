from ps5emu_core.services.syscall_table import SyscallTable


def test_dispatch_unknown_returns_enosys() -> None:
    table = SyscallTable()
    assert table.dispatch(999) == -38


def test_register_and_dispatch() -> None:
    table = SyscallTable()
    table.register(0x10, lambda a, b, c, d, e, f: a + b)
    assert table.dispatch(0x10, 2, 3, 0, 0, 0, 0) == 5