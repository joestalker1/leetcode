from collections import deque


class Solution:
    def kSimilarity(self, A, B):
        def neighbours(S):
            for i in range(len(S)):
                if S[i] != B[i]:
                    break
            arr = list(S)
            for j in range(i + 1, len(S)):
                if S[j] == B[i]:
                    arr[j], arr[i] = arr[i], arr[j]
                    yield "".join(arr)
                    arr[j], arr[i] = arr[i], arr[j]

        seen = {A: 0}
        q = deque([A])
        while q:
            s = q.popleft()
            if s == B:
                return seen[s]
            for nei in neighbours(s):
                if nei not in seen:
                    seen[nei] = seen[s] + 1
                    q.append(nei)



sol = Solution()
print(sol.kSimilarity("fffeaacbdbdafcfbbafb", "abcbdfafffefabdbbafc"))
print(sol.kSimilarity("aabbccddee", "dcacbedbae"))  # 5
print(sol.kSimilarity("bccaba", "abacbc"))  # 3
print(sol.kSimilarity(A="abc", B="bca"))  # 2
print(sol.kSimilarity(A="aabc", B="abca"))  # 2
print(sol.kSimilarity(A="ab", B="ba"))  # 1
