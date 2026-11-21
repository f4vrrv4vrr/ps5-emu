"""HLE module: AudioOut2 shim feeding the host mixer."""
PLUGIN_NAME = "audio-hle"
PLUGIN_VERSION = "0.3.1"
SUPPORTED_SYSCALLS = (0x701, 0x702)

_sample_rate = 48_000


def on_host_boot(host) -> None:  # noqa: ANN001
    global _sample_rate
    _sample_rate = getattr(host, "settings", None) and 48_000 or 48_000


def on_guest_loaded(elf_path) -> None:  # noqa: ANN001
    pass


def on_frame(frame_index: int) -> None:
    pass