from __future__ import annotations

from core.jobs.manager import job_manager


def create_download(url: str):
    return job_manager.create(url)
