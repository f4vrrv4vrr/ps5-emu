# Writing a ps5-emu extension

Extensions are plain Python modules that expose a `PLUGIN_NAME` string and any
subset of the lifecycle hooks defined in `ps5emu_core.contracts.HleModule`.

## Hook order
1. `on_host_boot(host)` — host is fully wired, no guest yet.
2. `on_guest_loaded(elf_path)` — a guest ELF was just mapped.
3. `on_frame(frame_index)` — called once per emulated frame.
4. `on_host_shutdown(host)` — last chance to flush state.

## Example skeleton
```python
PLUGIN_NAME = "my-shim"
PLUGIN_VERSION = "0.1.0"
SUPPORTED_SYSCALLS = (0x900,)

def on_host_boot(host): ...
def on_guest_loaded(elf_path): ...
def on_frame(frame_index): ...
```

Drop it in `~/.ps5emu/plugins/ps5x_myshim.py` and restart the host.