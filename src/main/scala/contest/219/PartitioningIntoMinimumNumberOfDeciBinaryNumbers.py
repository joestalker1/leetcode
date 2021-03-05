class Solution:
    def minPartitions(self, n: str):
        return int(max(n))

sol = Solution()
print(sol.minPartitions("27346209830709182346"))#9
print(sol.minPartitions("82734"))#8
print(sol.minPartitions('32'))#3
