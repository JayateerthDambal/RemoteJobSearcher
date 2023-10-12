from weworkremotely import get_wwr_jobs as get_wework_jobs


def get_remote_jobs(input):
    jobs = []
    jobs += get_wework_jobs(input)

    return jobs
