class Solution:
    # rows are applicants
    # colums are jobs
    def search(self, u, graph, job_to_ap, seen):
        for v in range(len(job_to_ap)):
            # if job is processed or not interested,skip it
            if v in seen or not graph[u][v]:
                continue
            seen.add(v)
            # if job is assigned to, let search new job for job applicant
            if not job_to_ap[v] or self.search(job_to_ap[v], graph, job_to_ap, seen):
                job_to_ap[v] = u
                return True
        return False

    def matching(self, graph):
        n = len(graph)
        # job number
        m = len(graph[0])
        job_to_ap = [False] * m
        matched = 0
        for u in range(n):
            seen = set()
            if self.search(u, graph, job_to_ap, seen):
                matched += 1
        return matched


sol = Solution()
bpGraph =[[0, 1, 1, 0, 0, 0],
          [1, 0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0],
          [0, 0, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1]]

print(sol.matching(bpGraph))

