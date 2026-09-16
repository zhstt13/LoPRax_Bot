from __future__ import annotations

import asyncio

from core.jobs.manager import job_manager
from core.jobs.worker import run_download_job


def create_download(url: str):
    job = job_manager.create(url)
    asyncio.create_task(run_download_job(job.id))
    return job
