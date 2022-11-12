from collections import Counter

class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        if not s or not answers:
            return 0
        freq = Counter(answers)
        n = len(s) // 2 + 1
        dp = [[set() for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i].add(int(s[2 * i]))
        for l in range(1, n):
            for start in range(n - l):
                end = start + l
                cur = set()
                for i in range(2 * start + 1, 2 * end, 2):
                    if s[i] == '+':
                        for a in dp[start][i // 2]:
                            for b in dp[i // 2 + 1][end]:
                                if a + b <= 1000:
                                    cur.add(a + b)
                    else:
                        for a in dp[start][i // 2]:
                            for b in dp[i // 2 + 1][end]:
                                cur.add(a * b)
                dp[start][end] = cur
        points = 0
        right_ans = eval(s)
        for i in dp[0][-1]:
            if i in freq:
                if i == right_ans:
                    points += freq[i] * 5
                else:
                    points += freq[i] * 2
        return points
