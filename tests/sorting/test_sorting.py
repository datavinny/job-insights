from src.sorting import sort_by

jobs = []


def test_sort_by_criteria():
    sort_by(jobs, "date_posted")
    sort_by(jobs, "max_salary")
    sort_by(jobs, "min_salary")
    # if sort_by(jobs, "invalid"):
    #     XFAIL(Expected Fail)
