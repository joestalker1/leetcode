def largest_subset_jobs(jobs):
    # sort by earliest end time
    # assume the ealiest job has fewer not-overlapped jobs.
    sorted_jobs = sorted(jobs, key=lambda j: j[1])
    results = []

    for job in sorted_jobs:
        if not results:
            results.append(job)

        if job[0] >= results[-1][1]:
            results.append(job)

    return results


print(largest_subset_jobs([(0, 6),
                           (1, 4),
                           (3, 5),
                           (3, 8),
                           (4, 7),
                           (5, 9),
                           (6, 10),
                           (8, 11)]))
