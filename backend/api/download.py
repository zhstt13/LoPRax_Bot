from core.jobs.manager import JobManager
from core.parser import parse_input

job_manager = JobManager()


def create_download(url: str):
    parsed = parse_input(url)
    job = job_manager.create(parsed)
    return job
