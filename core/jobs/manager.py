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
    id: str = field(default_factory=lambda: str(uuid4()))
    status: JobStatus = JobStatus.CREATED
    progress: int = 0
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    error: str | None = None


class JobManager:
    def __init__(self) -> None:
        self._jobs: dict[str, DownloadJob] = {}

    def create(self) -> DownloadJob:
        job = DownloadJob()
        self._jobs[job.id] = job
        return job

    def get(self, job_id: str) -> DownloadJob | None:
        return self._jobs.get(job_id)

    def update_status(self, job_id: str, status: JobStatus) -> None:
        job = self._jobs[job_id]
        job.status = status
