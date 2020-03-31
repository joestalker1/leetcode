from collections import defaultdict
import bisect

class Solution:
    def highFive(self, items):
        if not items:
            return 0
        id_to_scores = defaultdict(list)
        for id, score in items:
            if len(id_to_scores[id]) < 5:
                id_to_scores[id].append(score)
                id_to_scores[id].sort()
            else:
                min_score = id_to_scores[id]
                if min_score < score:
                    i = bisect.bisect_left(id_to_scores[id], score)
                    id_to_scores[id].insert(i, score)
                    id_to_scores.pop(0)
        res = []
        for id, scores in id_to_scores.items():
            avg = sum(scores) // 5
            res.append([id, avg])
        res.sort(key=lambda x: x[0])
        return res
