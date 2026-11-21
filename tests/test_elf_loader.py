from pathlib import Path

import pytest

from ps5emu_core.services.elf_loader import ElfLoader


def test_rejects_non_elf(tmp_path: Path) -> None:
    bogus = tmp_path / "bad.bin"
    bogus.write_bytes(b"not-elf-file")
    with pytest.raises(ValueError):
        ElfLoader(bogus).parse()