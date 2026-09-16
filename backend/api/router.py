from fastapi import APIRouter, BackgroundTasks

from backend.api.download import create_download
from backend.api.jobs import get_job_status
from core.jobs.worker import run_download_job

router = APIRouter()


@router.post("/download")
async def download(url: str, background_tasks: BackgroundTasks):
    job = create_download(url)
    background_tasks.add_task(run_download_job, job.id)
    return {
        "job_id": job.id,
        "status": job.status,
    }


@router.get("/jobs/{job_id}")
async def job_status(job_id: str):
    job = get_job_status(job_id)
    return job
