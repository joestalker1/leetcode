class Solution:
    def show_path(self, tickets, res):
        buf = list(map(lambda x: tickets[x][1], res))
        buf.insert(0, tickets[res[0]][0])
        return buf

    def findItinerary(self, tickets):
        if not tickets:
            return []
        m = {}
        for i in range(len(tickets)):
            dep = tickets[i][0]
            if dep not in m:
                m[dep] = []
            m[dep].append(i)

        for _, indices in m.items():
            indices.sort(key=lambda i: tickets[i][1])

        def dfs(used_tickets, dep, seen=set(), path=[]):
            if used_tickets > len(tickets):
                return path[:]

            if dep not in m:
                return

            len_of_path = len(path)
            for j in m[dep]:
                if j in seen:
                    continue
                seen.add(j)
                path.append(j)
                found = dfs(used_tickets + 1, tickets[j][1], seen, path)
                if found:
                    return found
                seen.remove(j)
                path[len_of_path:] = []

        path = dfs(1, 'JFK')
        return self.show_path(tickets, path)


sol = Solution()
print(sol.findItinerary(
    [["ADL", "EZE"], ["AUA", "AXA"], ["ADL", "TIA"], ["TIA", "ADL"], ["AXA", "CNS"], ["CNS", "ADL"], ["CBR", "ANU"],
     ["JFK", "AUA"], ["JFK", "ADL"], ["JFK", "CNS"], ["BNE", "ANU"], ["AUA", "BNE"], ["ANU", "BNE"], ["ANU", "AXA"],
     ["CBR", "OOL"], ["EZE", "CNS"], ["CNS", "ADL"], ["BNE", "CNS"], ["ANU", "AXA"], ["OOL", "CNS"], ["AUA", "EZE"],
     ["ANU", "AUA"], ["CBR", "BNE"], ["BNE", "AXA"], ["CNS", "BNE"], ["TIA", "CNS"], ["TIA", "BNE"], ["AUA", "AXA"],
     ["TIA", "EZE"], ["CNS", "AXA"], ["EZE", "OOL"], ["ADL", "AXA"], ["ADL", "EZE"], ["BNE", "AXA"], ["AXA", "TIA"],
     ["OOL", "AUA"], ["EZE", "AXA"], ["OOL", "JFK"], ["ADL", "AUA"], ["TIA", "OOL"], ["TIA", "CNS"], ["ANU", "AUA"],
     ["AXA", "OOL"], ["JFK", "BNE"], ["AUA", "ANU"], ["AUA", "BNE"], ["CNS", "CBR"], ["AXA", "ADL"], ["TIA", "EZE"],
     ["CNS", "CBR"], ["ADL", "BNE"], ["AUA", "CBR"], ["EZE", "CNS"], ["EZE", "CNS"], ["OOL", "TIA"], ["OOL", "EZE"],
     ["EZE", "ADL"], ["EZE", "JFK"], ["EZE", "AUA"], ["CNS", "EZE"], ["OOL", "CNS"], ["AXA", "BNE"], ["AXA", "ADL"],
     ["BNE", "CNS"], ["BNE", "OOL"], ["AUA", "TIA"], ["CBR", "OOL"], ["ANU", "TIA"], ["TIA", "OOL"], ["JFK", "EZE"],
     ["OOL", "AXA"], ["AXA", "ANU"], ["TIA", "ANU"], ["OOL", "CBR"], ["AXA", "JFK"], ["ADL", "OOL"], ["AXA", "CBR"],
     ["ADL", "CBR"], ["CNS", "EZE"], ["CBR", "ANU"], ["BNE", "CNS"], ["AXA", "OOL"], ["CNS", "AUA"], ["CNS", "JFK"],
     ["CBR", "TIA"], ["OOL", "TIA"], ["EZE", "JFK"], ["CNS", "CBR"], ["EZE", "BNE"], ["BNE", "EZE"], ["TIA", "CBR"],
     ["CBR", "TIA"], ["BNE", "ADL"], ["ANU", "AUA"], ["CBR", "AXA"], ["AXA", "AUA"], ["BNE", "DRW"], ["JFK", "BNE"],
     ["CNS", "AUA"], ["ADL", "ANU"], ["AUA", "TIA"], ["JFK", "BNE"], ["BNE", "JFK"], ["AUA", "ADL"], ["EZE", "AXA"],
     ["BNE", "OOL"], ["AXA", "ANU"], ["ANU", "EZE"], ["OOL", "TIA"]]))

print(sol.findItinerary(
    [["EZE", "TIA"], ["EZE", "HBA"], ["AXA", "TIA"], ["JFK", "AXA"], ["ANU", "JFK"], ["ADL", "ANU"], ["TIA", "AUA"],
     ["ANU", "AUA"], ["ADL", "EZE"], ["ADL", "EZE"], ["EZE", "ADL"], ["AXA", "EZE"], ["AUA", "AXA"], ["JFK", "AXA"],
     ["AXA", "AUA"], ["AUA", "ADL"], ["ANU", "EZE"], ["TIA", "ADL"], ["EZE", "ANU"], ["AUA", "ANU"]]))

# ["JFK","AXA","AUA","ADL","ANU","AUA","ANU","EZE","ADL","EZE","ANU","JFK","AXA","EZE","TIA","AUA","AXA","TIA","ADL","EZE","HBA"]

# print(sol.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))

#   print(sol.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
# ["JFK","ATL","JFK","SFO","ATL","SFO"]
# print(sol.findItinerary(
#     [["AXA", "EZE"], ["EZE", "AUA"], ["ADL", "JFK"], ["ADL", "TIA"], ["AUA", "AXA"], ["EZE", "TIA"], ["EZE", "TIA"],
#      ["AXA", "EZE"], ["EZE", "ADL"], ["ANU", "EZE"], ["TIA", "EZE"], ["JFK", "ADL"], ["AUA", "JFK"], ["JFK", "EZE"],
#      ["EZE", "ANU"], ["ADL", "AUA"], ["ANU", "AXA"], ["AXA", "ADL"], ["AUA", "JFK"], ["EZE", "ADL"], ["ANU", "TIA"],
#      ["AUA", "JFK"], ["TIA", "JFK"], ["EZE", "AUA"], ["AXA", "EZE"], ["AUA", "ANU"], ["ADL", "AXA"], ["EZE", "ADL"],
#      ["AUA", "ANU"], ["AXA", "EZE"], ["TIA", "AUA"], ["AXA", "EZE"], ["AUA", "SYD"], ["ADL", "JFK"], ["EZE", "AUA"],
#      ["ADL", "ANU"], ["AUA", "TIA"], ["ADL", "EZE"], ["TIA", "JFK"], ["AXA", "ANU"], ["JFK", "AXA"], ["JFK", "ADL"],
#      ["ADL", "EZE"], ["AXA", "TIA"], ["JFK", "AUA"], ["ADL", "EZE"], ["JFK", "ADL"], ["ADL", "AXA"], ["TIA", "AUA"],
#      ["AXA", "JFK"], ["ADL", "AUA"], ["TIA", "JFK"], ["JFK", "ADL"], ["JFK", "ADL"], ["ANU", "AXA"], ["TIA", "AXA"],
#      ["EZE", "JFK"], ["EZE", "AXA"], ["ADL", "TIA"], ["JFK", "AUA"], ["TIA", "EZE"], ["EZE", "ADL"], ["JFK", "ANU"],
#      ["TIA", "AUA"], ["EZE", "ADL"], ["ADL", "JFK"], ["ANU", "AXA"], ["AUA", "AXA"], ["ANU", "EZE"], ["ADL", "AXA"],
#      ["ANU", "AXA"], ["TIA", "ADL"], ["JFK", "ADL"], ["JFK", "TIA"], ["AUA", "ADL"], ["AUA", "TIA"], ["TIA", "JFK"],
#      ["EZE", "JFK"], ["AUA", "ADL"], ["ADL", "AUA"], ["EZE", "ANU"], ["ADL", "ANU"], ["AUA", "AXA"], ["AXA", "TIA"],
#      ["AXA", "TIA"], ["ADL", "AXA"], ["EZE", "AXA"], ["AXA", "JFK"], ["JFK", "AUA"], ["ANU", "ADL"], ["AXA", "TIA"],
#      ["ANU", "AUA"], ["JFK", "EZE"], ["AXA", "ADL"], ["TIA", "EZE"], ["JFK", "AXA"], ["AXA", "ADL"], ["EZE", "AUA"],
#      ["AXA", "ANU"], ["ADL", "EZE"], ["AUA", "EZE"]]))
# print(sol.findItinerary([["JFK","AAA"],["AAA","JFK"],["JFK","BBB"],["JFK","CCC"],["CCC","JFK"]]))
# ["JFK","AAA","JFK","CCC","JFK","BBB"]
print(sol.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
# print(sol.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
# print(sol.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
