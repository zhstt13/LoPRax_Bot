from fastapi import APIRouter

from backend.api.download import create_download
from backend.api.jobs import get_job_status

router = APIRouter()


@router.post("/download")
async def download(url: str):
    return create_download(url)


@router.get("/jobs/{job_id}")
async def job_status(job_id: str):
    return get_job_status(job_id)
