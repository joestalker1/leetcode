class Solution:
    def carPooling(self, trips, capacity):
        if not trips or capacity == 0:
            return False
        start = {}
        end = {}
        max_end = 0
        for people,s,e in trips:
            if s not in start:
                start[s] = []
            start[s].append(people)
            if e not in end:
                end[e] = []
            end[e].append(people)
            max_end = max(e, max_end)
        occupied = 0
        for i in range(max_end + 1):
            if i in end:
                for num in end[i]:
                    occupied -= num
            if i in start:
                for num in start[i]:
                    occupied += num
                    if occupied > capacity:
                        return False
        return True

sol = Solution()
print(sol.carPooling([[9,3,4],[9,1,7],[4,2,4],[7,4,5]], 23))#true
print(sol.carPooling([[8,2,3],[4,1,3],[1,3,6],[8,4,6],[4,4,8]], 12))#false
print(sol.carPooling([[3,2,7],[3,7,9],[8,3,9]], 11))#true
print(sol.carPooling([[7,5,6],[6,7,8],[10,1,6]], 16))#false

print(sol.carPooling([[3,2,8],[4,4,6],[10,8,9]], 11))#true









