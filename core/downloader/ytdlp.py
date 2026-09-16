from __future__ import annotations

import asyncio
from pathlib import Path

from core.models import ParsedInput


async def run_ytdlp(command: list[str], cwd: Path | None = None) -> tuple[str, str]:
    process = await asyncio.create_subprocess_exec(
        *command,
        cwd=str(cwd) if cwd else None,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    if process.returncode != 0:
        raise RuntimeError(stderr.decode().strip() or "yt-dlp failed")
    return stdout.decode().strip(), stderr.decode().strip()


async def probe_url(parsed_input: ParsedInput) -> dict:
    command = ["yt-dlp", "--dump-single-json", parsed_input.source_url]
    stdout, _ = await run_ytdlp(command)
    import json
    return json.loads(stdout)
