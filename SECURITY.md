# Security Policy

ps5-emu executes guest ELF images. Treat any binary from an untrusted source
as a potential host-injection vector.

## Reporting a vulnerability
Please email `security@ps5emu.dev` (GPG key on the project page) with the
subject line `[ps5-emu SECURITY]`. Do **not** open a public issue.

We acknowledge within 72 hours and aim to ship a patch within 14 days for
critical issues in `ps5emu_core` or `ps5emu_infra`.

## Scope
- `src/ps5emu_core/**` — syscall table, ELF loader, plugin registry
- `src/ps5emu_infra/**` — settings and telemetry
- `extensions/**` — bundled HLE shims

Out of scope: user-supplied plugins in `~/.ps5emu/plugins`.