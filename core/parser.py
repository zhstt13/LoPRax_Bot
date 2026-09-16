from __future__ import annotations

from urllib.parse import urlparse

from .models import ParsedInput


def parse_user_input(text: str, username: str | None = None) -> ParsedInput:
    """Parse user input into a downloader-independent request model."""
    value = text.strip()
    custom_file_name = None

    if "|" in value:
        value, custom_file_name = [part.strip() for part in value.split("|", 1)]

    parsed = urlparse(value)
    if not parsed.scheme or not parsed.netloc:
        raise ValueError("Invalid URL")

    return ParsedInput(
        source_url=value,
        custom_file_name=custom_file_name,
        username=username,
        password=None,
    )
