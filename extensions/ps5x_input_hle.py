"""HLE module: maps guest DualSense HID reads to host input."""
PLUGIN_NAME = "input-hle"
PLUGIN_VERSION = "0.4.0"
SUPPORTED_SYSCALLS = (0x611, 0x612, 0x613)

_btn_state = 0


def on_host_boot(host) -> None:  # noqa: ANN001
    print(f"[{PLUGIN_NAME}] attached to host")


def on_guest_loaded(elf_path) -> None:  # noqa: ANN001
    print(f"[{PLUGIN_NAME}] guest loaded: {elf_path}")


def on_frame(frame_index: int) -> None:
    global _btn_state
    # rotate a dummy button press every 60 frames so pong demos react
    _btn_state = (frame_index // 60) % 4