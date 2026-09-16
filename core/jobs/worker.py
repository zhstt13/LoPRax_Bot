from __future__ import annotations

from pathlib import Path

from core.jobs.manager import JobStatus, job_manager
from core.downloader.direct import download_direct
from core.downloader.ytdlp import probe_url


async def run_download_job(job_id: str):
    job = job_manager.get(job_id)
    if not job:
        return None

    job_manager.update(job_id, status=JobStatus.PROCESSING, progress=0)

    try:
        output_dir = Path("downloads") / job_id
        output_dir.mkdir(parents=True, exist_ok=True)

        if job.source_url.startswith(("http://", "https://")):
            info = await probe_url(job.source_url)
            job_manager.update(job_id, progress=20)

            job_manager.update(
                job_id,
                status=JobStatus.COMPLETED,
                progress=100,
                result={"info": info},
            )
        else:
            raise ValueError("invalid url")

    except Exception as exc:
        job_manager.update(
            job_id,
            status=JobStatus.FAILED,
            error=str(exc),
        )

    return job_manager.get(job_id)
