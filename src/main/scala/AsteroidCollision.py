class Solution(object):
    def asteroidCollision(self, asteroids):
        if not asteroids:
            return []
        res = [asteroids[0]]
        i = 1
        while i < len(asteroids):
            while res and asteroids[i] < 0 < res[-1]:
                if res[-1] < -asteroids[i]:#
                    res.pop()
                    continue
                elif res[-1] == -asteroids[i]: # =
                    res.pop()
                break
            else:
                res.append(asteroids[i])
            i += 1
        return res

sol = Solution()
print(sol.asteroidCollision([-2,-1,1,2]))#[-2,-1,1,2]
print(sol.asteroidCollision([-2,2,1,-2]))#[-2]
print(sol.asteroidCollision([-2,2,-1,-2]))#[-2]
print(sol.asteroidCollision([-2,-2,1,-2]))#[-2,-2,-2]
print(sol.asteroidCollision([10, 2, -5]))#[10]
print(sol.asteroidCollision([8, -8]))#[]
print(sol.asteroidCollision([5, 10, -5]))#[5,10]