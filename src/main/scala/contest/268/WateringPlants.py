class Solution:
    def wateringPlants(self, plants, capacity: int) -> int:
        if not plants:
            return 0
        cur_water = capacity
        steps = 0
        for i in range(len(plants)):
            if cur_water < plants[i]:
                # need go to fill the can
                steps += i+ 1 + i
                cur_water = capacity - plants[i]
            else:
                cur_water -= plants[i]
                steps += 1
        return steps
        #[3,2,4,2,1],6, 17



sol = Solution()
print(sol.wateringPlants([3,2,4,2,1],6))#17