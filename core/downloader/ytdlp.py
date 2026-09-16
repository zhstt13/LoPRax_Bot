from __future__ import annotations

import asyncio
import json
from pathlib import Path

from core.models import DownloadArtifact, ParsedInput


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
    return json.loads(stdout)


async def download_ytdlp(
    parsed_input: ParsedInput,
    output_dir: Path,
) -> DownloadArtifact:
    output_dir.mkdir(parents=True, exist_ok=True)

    command = [
        "yt-dlp",
        "-o",
        str(output_dir / "%(title)s.%(ext)s"),
        parsed_input.source_url,
    ]

    await run_ytdlp(command)

    files = list(output_dir.iterdir())
    if not files:
        raise RuntimeError("download completed without output file")

    file_path = files[0]

    return DownloadArtifact(
        path=file_path,
        file_name=file_path.name,
        send_type="document",
        caption=file_path.name,
    )
