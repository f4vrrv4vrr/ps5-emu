# Contributing to ps5-emu

Thanks for helping out with the ps5-emu (Playstation 5 Emulator) project!

## Ground rules
- We only accept code that helps **emulation research and homebrew
  development**. Do not submit code geared at piracy, running
  unlicensed retail dumps, or DRM circumvention.
- Keep pull requests scoped. One concern per PR.
- Plugins live under `extensions/` and must use the `ps5x_` filename prefix
  so `PluginRegistry.discover()` picks them up.

## Dev setup
```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python scripts\run_dev.py
```

## Style
- Python 3.10+, `from __future__ import annotations` at the top.
- No emoji in code or commits.
- Tests live under `tests/` and must pass before merge.

## Legal
Reverse-engineering work here is for interoperability research. Do not
distribute copyrighted firmware or PUP files inside this repository.