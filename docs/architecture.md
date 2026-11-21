# ps5-emu architecture

```
ps5emu_app    → desktop shell (PySide6), bootstrap, main window
ps5emu_core   → EmulatorHost, PluginRegistry, contracts, syscall table, ELF loader
ps5emu_infra  → settings (TOML), telemetry, hosts the plugin directory watcher
extensions    → bundled HLE shims (input, audio, …)
```

The host is a **plugin host**: `PluginRegistry` discovers `ps5x_*.py` files and
invokes lifecycle hooks (`on_host_boot`, `on_guest_loaded`, `on_frame`,
`on_host_shutdown`). Each guest syscall is dispatched through `SyscallTable`,
which is populated by extension modules at boot.

## Not implemented (yet)
- RSX/GFX command buffer translation — see `extensions/ps5x_audio_hle.py` for a
  stub of the pattern we will follow.
- Firmware decryption (out of scope — see SECURITY.md and CONTRIBUTING.md).