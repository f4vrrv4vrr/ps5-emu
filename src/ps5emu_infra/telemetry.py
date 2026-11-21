"""Opt-in anonymous telemetry for crash reports."""
from __future__ import annotations

import logging
import platform

log = logging.getLogger(__name__)
_ENABLED = False
_ENDPOINT = ""


def init_telemetry(endpoint: str, enabled: bool = False) -> None:
    global _ENABLED, _ENDPOINT
    _ENDPOINT = endpoint
    _ENABLED = enabled and bool(endpoint)
    log.info("telemetry %s (endpoint=%r)", "enabled" if _ENABLED else "disabled", _ENDPOINT)


def report_event(name: str, payload: dict | None = None) -> None:
    if not _ENABLED:
        return
    body = {"event": name, "os": platform.platform(), "payload": payload or {}}
    log.debug("telemetry event: %s", body)