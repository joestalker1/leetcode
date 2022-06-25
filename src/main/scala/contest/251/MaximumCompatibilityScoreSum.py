class Solution:
    def maxCompatibilitySum(self, students, mentors) -> int:
        scores = [[0] * len(students) for _ in range(len(students))]
        for i in range(len(students)):
            for j in range(len(mentors)):
                cur_score = 0
                for k in range(len(mentors[j])):
                    cur_score += (1 if mentors[j][k] == students[i][k] else 0)
                if scores[i][j] < cur_score:
                    scores[i][j] = cur_score

        def find_max_score(scores,i, seen):
            if i == len(students):
                return 0
            max_score = 0
            for j in range(len(mentors)):
                if j in seen:
                    continue
                seen.add(j)
                max_score = max(max_score, scores[i][j] + find_max_score(scores,i+1, seen))
                seen.discard(j)
            return max_score

        seen = set()
        return find_max_score(scores, 0, seen)

sol = Solution()
print(sol.maxCompatibilitySum(students = [[1,1,0],[1,0,1],[0,0,1]], mentors = [[1,0,0],[0,0,1],[1,1,0]]))#8