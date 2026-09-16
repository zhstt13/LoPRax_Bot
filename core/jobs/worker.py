from __future__ import annotations

from pathlib import Path

from core.jobs.manager import JobStatus, job_manager
from core.models import ParsedInput
from core.downloader.ytdlp import download_ytdlp


async def run_download_job(job_id: str):
    job = job_manager.get(job_id)
    if not job:
        return None

    job_manager.update(job_id, status=JobStatus.PROCESSING, progress=0)

    try:
        output_dir = Path("downloads") / job_id
        parsed = ParsedInput(source_url=job.source_url)

        artifact = await download_ytdlp(parsed, output_dir)

        job_manager.update(
            job_id,
            status=JobStatus.COMPLETED,
            progress=100,
            result={
                "type": "artifact",
                "path": str(artifact.path),
                "file_name": artifact.file_name,
                "send_type": artifact.send_type,
            },
        )

    except Exception as exc:
        job_manager.update(
            job_id,
            status=JobStatus.FAILED,
            error=str(exc),
        )

    return job_manager.get(job_id)
