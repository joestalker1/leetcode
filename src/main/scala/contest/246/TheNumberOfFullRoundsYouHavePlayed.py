class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:

        def calc_rounds(hour1, min1, hour2, min2):
            assert hour1 <= hour2
            rounds = 0
            d = hour2 - hour1
            if min1 != 0 and d > 0:
                d -= 1
            rounds += d * 4
            if hour1 == hour2:
                q1 = min1 // 15
                if min1 % 15 != 0:
                    q1 += 1
                q2 = min2 // 15
                q = max(0, q2 - q1)
            else:
                q = 0
                if min1 > 0:
                    q = (60 - min1) // 15
                q += min2 // 15

            rounds += q
            return rounds

        hour1, min1 = startTime.split(':')
        hour2, min2 = finishTime.split(':')
        hour1 = int(hour1)
        min1 = int(min1)
        hour2 = int(hour2)
        min2 = int(min2)

        if hour1 > hour2 or hour1 == hour2 and min1 > min2:
            rounds = calc_rounds(hour1, min1, 24, 0) + calc_rounds(0, 0, hour2, min2)
        else:
            rounds = calc_rounds(hour1, min1, hour2, min2)
        return rounds


sol = Solution()
print(sol.numberOfRounds("20:00","06:00") == 40)#40
print(sol.numberOfRounds("14:41", "15:24") == 2)#2
print(sol.numberOfRounds("23:46", "0:01") == 0)#0
print(sol.numberOfRounds("20:00", "06:00")== 40)#40