class Solution:
    def getCollisionTimes(self, cars):
        n = len(cars)
        ans = [-1.0] * n
        #left in the stack that current car can collide
        st = []
        for i in range(len(cars) - 1, -1, -1):
            p,v = cars[i]
            while st:
                j = st[-1]
                p2,v2 = cars[j]
                #pop if car has higher speed
                #or car in st[-1] bumped into previous car earlier than current car collides st[-1]
                if cars[j][1] >= v or (p2 - p) / (v-v2) >= ans[j] and ans[j] >= 0:
                    st.pop()
                else:
                    break
            #we poped out all cars we can't collide, so calculate crash time)
            if st:
                j = st[-1]
                p2,v2 = cars[j]
                ans[i] = (p2 - p) / (v-v2)
            st.append(i)
        return ans


sol = Solution()
print(sol.getCollisionTimes([[3,4],[5,4],[6,3],[9,1]]))# [2.00000,1.00000,1.50000,-1.00000]

