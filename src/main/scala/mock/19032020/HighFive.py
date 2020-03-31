from collections import defaultdict

class Solution:
   def highFive(self, items):
        if not items:
            return []
        id_to_score = defaultdict(list)
        for id,score in items:
            if len(id_to_score[id]) > 5:
                min_score = min(id_to_score[id])
                if min_score < score:
                    id_to_score[id].remove(min_score)
                    id_to_score[id].append(score)
            else:
                id_to_score[id].append(score)
        id_to_average = []
        for id in range(1, 1001):
            if id not in id_to_score:
                break
            sums = sum(id_to_score[id]) // 5
            id_to_average.append([id, sums])
        return id_to_average
