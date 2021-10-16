
# const int INF = 1e9;
#     vector<int> d(n+1, INF);
#     d[0] = -INF;
#
#     for (int i = 0; i < n; i++) {
#         int j = upper_bound(d.begin(), d.end(), a[i]) - d.begin();
#         if (d[j-1] < a[i] && a[i] < d[j])
#             d[j] = a[i];
#     }
#
#     int ans = 0;
#     for (int i = 0; i <= n; i++) {
#         if (d[i] < INF)
#             ans = i;
#     }
#     return ans;

import math
import bisect

class Solution:
    def removeStudents(self, H, N):
        if not H or len(H) == 0:
            return 0
        dp = [math.inf] * (N+1)
        dp[0] = -math.inf
        for i in range(N):
            j = bisect.bisect_left(dp, H[i])
            if dp[j-1] < H[i] and H[i] < dp[j]:
                dp[j] = H[i]
        j = 0
        for i in range(N + 1):
            if dp[i] < math.inf:
                j = i
        return N - j





sol = Solution()
#print(sol.removeStudents([4,3,2,1], 4))#3
print(sol.removeStudents( [9, 1, 2, 3, 1, 5], 6))#2


