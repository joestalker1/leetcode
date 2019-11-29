class Solution(object):
    def bulbSwitch2(self, n):
        if n <= 0:
            return 0
        if n == 1 or n == 2:
            return 1
        bulbs = [1] * (n + 1)  # after 1 all bulbs are on
        bulbs[0] = 0
        for i in range(2, n + 1):
            j = 1

            for j in range(1, n + 1):
                if i == 2 and j % i == 0:
                    bulbs[j] = 0
                elif j % i == 0:
                    bulbs[j] = 1 - bulbs[j]
            #print('{} - {}'.format(i, bulbs))
        return sum(bulbs)

    def bulbSwitch(self, n):
        if n <= 0:
            return 0
        if n == 1 or n == 2:
            return 1
        bulbs = [1] * (n + 1) # after 1 all bulbs are on
        bulbs[0] = 0
        for i in range(2, n + 1):
            j = i
            while j <= n:
                bulbs[j] = 1 - bulbs[j]
                j += i
            print('{} - {}'.format(i, bulbs))
        return sum(bulbs)


sol = Solution()
print(sol.bulbSwitch(20))
#print(sol.bulbSwitch2(9999))
#print(sol.bulbSwitch(3))





