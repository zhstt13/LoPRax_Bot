from __future__ import annotations

from pathlib import Path
from urllib.parse import urlparse

import aiohttp


async def download_direct(url: str, output_dir: Path, file_name: str | None = None) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)

    if not file_name:
        file_name = Path(urlparse(url).path).name or "download.bin"

    destination = output_dir / file_name

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            with destination.open("wb") as file:
                async for chunk in response.content.iter_chunked(1024 * 64):
                    file.write(chunk)

    return destination
