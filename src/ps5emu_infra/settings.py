"""Settings loader for the ps5-emu host."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # py<3.11
    import tomli as tomllib  # type: ignore


@dataclass
class Settings:
    plugin_dir: Path
    telemetry_enabled: bool = False
    telemetry_endpoint: str = ""
    log_level: str = "INFO"
    gpu_backend: str = "vulkan"


def load_settings(path: Path) -> Settings:
    plugin_dir = Path.home() / ".ps5emu" / "plugins"
    if not path.exists():
        return Settings(plugin_dir=plugin_dir)
    with path.open("rb") as fh:
        raw = tomllib.load(fh)
    core = raw.get("core", {})
    return Settings(
        plugin_dir=Path(core.get("plugin_dir", plugin_dir)).expanduser(),
        telemetry_enabled=bool(core.get("telemetry_enabled", False)),
        telemetry_endpoint=str(core.get("telemetry_endpoint", "")),
        log_level=str(core.get("log_level", "INFO")),
        gpu_backend=str(core.get("gpu_backend", "vulkan")),
    )