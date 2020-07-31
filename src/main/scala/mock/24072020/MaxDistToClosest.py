class Solution:
    def maxDistToClosest(self, seats):
        persons = [i for i in range(len(seats)) if seats[i] == 1]
        n = len(seats)
        max_dist = max(len(seats) - persons[-1] - 1, persons[0])
        for i in range(1, len(persons)):
            dist = persons[i] - persons[i - 1] - 1
            if dist % 2 == 1:
                dist = (dist + 1) // 2
            else:
                dist = dist // 2
            max_dist = max(max_dist, dist)
        return max_dist


sol = Solution()
print(sol.maxDistToClosest([0,0,1,0,1,1]))#2




