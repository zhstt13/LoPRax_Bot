from __future__ import annotations

from pathlib import Path

from core.jobs.manager import JobStatus, job_manager
from core.models import ParsedInput
from core.downloader.ytdlp import probe_url


async def run_download_job(job_id: str):
    job = job_manager.get(job_id)
    if not job:
        return None

    job_manager.update(job_id, status=JobStatus.PROCESSING, progress=0)

    try:
        output_dir = Path("downloads") / job_id
        output_dir.mkdir(parents=True, exist_ok=True)

        parsed = ParsedInput(source_url=job.source_url)
        info = await probe_url(parsed)

        job_manager.update(
            job_id,
            status=JobStatus.COMPLETED,
            progress=100,
            result={
                "type": "probe",
                "output_dir": str(output_dir),
                "info": info,
            },
        )

    except Exception as exc:
        job_manager.update(
            job_id,
            status=JobStatus.FAILED,
            error=str(exc),
        )

    return job_manager.get(job_id)
