class Solution:
    def reconstructQueue(self, people):
        if len(people) <= 1:
            return people
        sorted_people = sorted(people,key=lambda x:[-x[0],x[1]])
        res = []
        for h,k in sorted_people:
            res.insert(k,[h,k])
        return res