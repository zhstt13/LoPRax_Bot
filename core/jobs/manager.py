from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from uuid import uuid4


class JobStatus(str, Enum):
    CREATED = "created"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class DownloadJob:
    source_url: str
    id: str = field(default_factory=lambda: str(uuid4()))
    status: JobStatus = JobStatus.CREATED
    progress: int = 0
    result: dict | None = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    error: str | None = None


class JobManager:
    def __init__(self) -> None:
        self._jobs: dict[str, DownloadJob] = {}

    def create(self, source_url: str) -> DownloadJob:
        job = DownloadJob(source_url=source_url)
        self._jobs[job.id] = job
        return job

    def get(self, job_id: str) -> DownloadJob | None:
        return self._jobs.get(job_id)

    def update(self, job_id: str, **changes) -> DownloadJob | None:
        job = self._jobs.get(job_id)
        if not job:
            return None
        for key, value in changes.items():
            if hasattr(job, key):
                setattr(job, key, value)
        return job


job_manager = JobManager()
