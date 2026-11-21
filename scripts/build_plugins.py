"""Zip-archive all bundled extensions into dist/plugins/."""
from __future__ import annotations

import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "extensions"
OUT = ROOT / "dist" / "plugins"


def build() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for module in SRC.glob("ps5x_*.py"):
        target = OUT / f"{module.stem}-0.1.0.zip"
        with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as zf:
            zf.write(module, module.name)
        print(f"packed {target}")


if __name__ == "__main__":
    build()