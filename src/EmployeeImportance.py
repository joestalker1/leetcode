
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id):
        imp = {}
        for emp in employees:
            if id == emp.id:
                imp[id] = emp.importance
                for sub in emp.subordinate:
                    if sub in imp and imp[sub] < 0:
                            imp[sub] = -imp[sub]
                    else:
                        imp[sub] = 0
            elif emp.id in imp:
                imp[emp.id] = emp.importance
                for sub in emp.subordinate:
                    if sub in imp and imp[sub] < 0:
                            imp[sub] = -imp[sub]
                    else:
                        imp[sub] = 0
            else:
                imp[emp.id] = -emp.importance
        return sum(imp.values())

