from core.jobs.manager import job_manager


def get_job_status(job_id: str):
    return job_manager.get(job_id)
