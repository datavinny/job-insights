from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them
    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    job_list = read(path)
    unique_job_types = []
    for job in job_list:
        if job["job_type"] not in unique_job_types:
            unique_job_types.append(job["job_type"])
    return unique_job_types


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    filtred_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtred_jobs.append(job)
    return filtred_jobs


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    job_list = read(path)
    unique_industries = []
    for job in job_list:
        if job["industry"] and job["industry"] not in unique_industries:
            unique_industries.append(job["industry"])
    return unique_industries


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    filtred_jobs = []
    for job in jobs:
        if job["industry"] == industry:
            filtred_jobs.append(job)
    return filtred_jobs


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    job_list = read(path)
    max_salary = 0
    for job in job_list:
        if bool(job["max_salary"]) and \
           job["max_salary"].isdigit() and \
           int(job["max_salary"]) > max_salary:
            max_salary = int(job["max_salary"])
    return max_salary


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    job_list = read(path)
    min_salary = 999999999999999999999
    for job in job_list:
        if bool(job["min_salary"]) and \
           job["min_salary"].isdigit() and \
           int(job["min_salary"]) < min_salary:
            min_salary = int(job["min_salary"])
    return min_salary


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError('one of the params is missing')
    elif not (type(job["min_salary"]) is int) or \
            not (type(job["max_salary"]) is int) or not (type(salary) is int):
        raise ValueError('One of the values is not a valid integer')
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError('min_salary cannot be greather than max_salary')
    if job["min_salary"] <= salary <= job["max_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    filtred_jobs = []
    for job in jobs:
        if type(job["min_salary"]) is int and \
           type(job["max_salary"]) is int and \
           type(salary) is int and \
           job["max_salary"] > job["min_salary"]:
            if matches_salary_range(job, salary):
                filtred_jobs.append(job)
    return filtred_jobs
