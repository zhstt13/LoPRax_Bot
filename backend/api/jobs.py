from core.jobs.manager import JobManager

job_manager = JobManager()


def get_job_status(job_id: str):
    return job_manager.get(job_id)
