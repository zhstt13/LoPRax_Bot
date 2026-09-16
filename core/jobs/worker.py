from __future__ import annotations

from core.jobs.manager import JobStatus, job_manager


async def run_download_job(job_id: str):
    job = job_manager.get(job_id)
    if not job:
        return None

    job_manager.update(job_id, status=JobStatus.PROCESSING, progress=0)

    try:
        # Downloader integration will be connected here.
        # This worker intentionally stays independent from Telegram/API.
        job_manager.update(
            job_id,
            status=JobStatus.COMPLETED,
            progress=100,
            result={"message": "worker completed"},
        )
    except Exception as exc:
        job_manager.update(
            job_id,
            status=JobStatus.FAILED,
            error=str(exc),
        )

    return job_manager.get(job_id)
