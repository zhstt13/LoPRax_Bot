from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class DownloadArtifact:
    path: Path
    file_name: str
    send_type: str
    caption: str


@dataclass(slots=True)
class ParsedInput:
    source_url: str
    custom_file_name: str | None = None
    username: str | None = None
    password: str | None = None
